# 🚀 Predictive Analysis API

## 📑 Table of Contents

1. **📘 Introduction**
2. **✨ Features**
3. **🛠️ Setup**
4. **🔗 Endpoints**
5. **📦 Dependencies**

---

## 📘 1. Introduction

This repository contains a RESTful API developed using **FastAPI** to perform predictive analysis for manufacturing operations. The API includes endpoints for:
- Uploading datasets.
- Training machine learning models.
- Making predictions related to machine downtime or production defects.

---

## ✨ 2. Features

- **📤 Upload Endpoint**: Accepts CSV files containing manufacturing data.
- **🧠 Train Endpoint**: Trains a model based on the uploaded dataset.
- **🔮 Predict Endpoint**: Predicts machine downtime or defects for new input data.

---

## 🛠️ 3. Setup

### 🚀 Getting Started

To get started with the **Predictive Analysis API**, follow these steps:

### 🛠️ 3.1 Clone the GitHub Repository

1. Clone the repository from GitHub:
    ```bash
    git clone https://github.com/Eswaran-IT/PredictionSystem.git
    cd PredictionSystem
    ```

2. **OR** download the repository as a ZIP file and extract it.

---

### 🛠️ 3.2 Set Up the Environment

Ensure you have Python installed on your machine. Then, set up the environment:

1. Navigate to the project directory:
    ```bash
    cd PredictionSystem
    ```

2. Install dependencies using:
    ```bash
    pip install -r requirements.txt
    ```

   ✅ This will install all required Python packages specified in the `requirements.txt` file.

---

### 🛠️ 3.3 Running the FastAPI Application

To run the FastAPI server:

1. Execute the following command:
    ```bash
    uvicorn main:app --reload
    ```

   ✅ This will start the server on: `http://localhost:8000`.

---

### 🔍 3.4 Testing with Postman

#### 🛠️ Import the Postman Collection

1. After cloning the repository, locate the `PredictionSystem.postman_collection.json` file in the project directory.

2. Import the collection into Postman:
   - Open **Postman**.
   - Go to **File > Import**.
     3. Select and upload the file: `PredictionSystem.postman_collection.json` from your cloned/downloaded directory.

   Alternatively, you can import the collection directly from the GitHub repository:
   [PredictionSystem.postman_collection.json](https://github.com/Eswaran-IT/PredictionSystem/blob/main/PredictionSystem.postman_collection.json).

2. **Use the Collection**:
   - The collection contains pre-configured requests for:
     - **Upload Endpoint** (`POST /upload/`)
     - **Train Endpoint** (`POST /train/`)
     - **Predict Endpoint** (`POST /predict/`)
   - Each request has been set up with example inputs and expected outputs for quick testing.

   - Use the imported collection to make requests to the FastAPI server running locally on `http://127.0.0.1:8000/`.
   - Refer to the example requests and responses in the "API Endpoints Overview" section above.


3. **Example Requests and Responses**:
    - Each endpoint has been pre-tested, and the results are available for easy import into Postman.

---

### 3.5 API Endpoints Overview

1. **Upload Endpoint** (`POST /upload/`)
     Upload Endpoint: http://localhost:8000/upload/

    - Description: Upload a CSV file containing manufacturing data (e.g., Machine_ID, Temperature, Run_Time).
    - Request: CSV file
    - Response: 
      ```json
      {"filename": "newdataset.csv", "rows": 100, "message": "File uploaded successfully."}
      ```

3. **Train Endpoint** (`POST /train/`)
    Train Endpoint: http://localhost:8000/train/
   
    - Description: Train a predictive model based on the uploaded dataset.
    - Response:
      ```json
      {"accuracy": 0.95, "f1_score": 0.90, "message": "Model trained successfully."}
      ```

5. **Predict Endpoint** (`POST /predict/`)
    Predict Endpoint: http://localhost:8000/predict/
    - Description: Predict machine downtime or defects for new data.
    - Request Body:
      ```json
      {"Temperature": 80, "Run_Time": 120}
      ```
    - Response:
      ```json
      {"Downtime": "Yes", "Confidence": 0.85}
      ```

---

### 3.6 Technical Stack

- **Python**: The programming language used.
- **FastAPI**: Web framework for building APIs.
- **Postman**: API testing tool for interacting with RESTful APIs.
- **scikit-learn**: For machine learning models.
- **Joblib**: For saving and loading machine learning models.
