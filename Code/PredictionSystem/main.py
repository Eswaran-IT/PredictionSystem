from fastapi import FastAPI, File, UploadFile, HTTPException
from sklearn.model_selection import train_test_split
import pandas as pd
import io
import os
from model import train_model, evaluate_model, save_model, load_model

app = FastAPI()

MODEL_FILENAME = 'model.pkl'
TRAINING_DATA_FILENAME = 'training_data.csv'


# Utility function to save uploaded training data
def save_training_data(dataframe: pd.DataFrame):
    dataframe.to_csv(TRAINING_DATA_FILENAME, index=False)


# Upload endpoint to receive CSV file
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        df = pd.read_csv(io.StringIO(contents.decode("utf-8")))

        # Validate data structure
        required_columns = ['Machine_ID', 'Temperature', 'Run_Time', 'Downtime_Flag']
        if not all(col in df.columns for col in required_columns):
            raise HTTPException(status_code=400, detail=f"Missing required columns. Expected: {required_columns}")

        save_training_data(df)
        return {"filename": file.filename, "rows": len(df), "message": "File uploaded successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File processing error: {str(e)}")


# Train endpoint to train the model on the uploaded dataset
@app.post("/train/")
async def train_model_endpoint():
    try:
        if not os.path.exists(TRAINING_DATA_FILENAME):
            raise HTTPException(status_code=400, detail="Training data not found. Upload the dataset first.")

        df = pd.read_csv(TRAINING_DATA_FILENAME)
        X = df[['Machine_ID', 'Temperature', 'Run_Time']]
        y = df['Downtime_Flag']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = train_model(X_train, y_train)

        save_model(model)

        accuracy, f1 = evaluate_model(model, X_test, y_test)
        return {"accuracy": accuracy, "f1_score": f1, "message": "Model trained successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Training failed: {str(e)}")


@app.post("/predict/")
async def predict_downtime(data: dict):
    try:
        # Required columns for prediction
        required_columns = ['Machine_ID', 'Temperature', 'Run_Time']

        # Convert input JSON to DataFrame
        df = pd.DataFrame([data])

        # Check if required columns are present
        if not all(col in df.columns for col in required_columns):
            raise HTTPException(status_code=400, detail=f"Missing required columns. Expected: {required_columns}")

        # Load the model
        model = load_model()

        # Predict
        predictions = model.predict(df[required_columns])
        confidence = model.predict_proba(df[required_columns]).max(axis=1)

        result = [{"Downtime": "Yes" if pred == 1 else "No", "Confidence": float(conf)} for pred, conf in
                  zip(predictions, confidence)]
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")