from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
import joblib

# Function to train the model
def train_model(X_train, y_train):
    model = LogisticRegression(max_iter=2000)
    model.fit(X_train, y_train)
    return model

# Function to evaluate the model
def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)
    return accuracy, f1

# Function to save the model
def save_model(model, filename='model.pkl'):
    joblib.dump(model, filename)

# Function to load the model
def load_model(filename='model.pkl'):
    return joblib.load(filename)

# Function to make predictions with probabilities
def predict_proba(model, X):
    return model.predict_proba(X)

