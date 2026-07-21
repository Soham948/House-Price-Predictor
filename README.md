# 🏠 House Price Prediction using Machine Learning & Flask

A complete end-to-end Machine Learning project that predicts house prices using the Ames Housing Dataset. The project includes data preprocessing, exploratory data analysis (EDA), feature engineering, model training, model evaluation, and deployment using Flask.

---

## 📌 Project Overview

This project uses Machine Learning algorithms to predict the selling price of houses based on various property features such as:

- Overall Quality
- Overall Condition
- Lot Area
- Ground Living Area
- Garage Area
- Garage Capacity
- Basement Area
- Number of Bedrooms
- Number of Bathrooms
- Year Built

The trained model is deployed as a Flask web application with an interactive user interface where users can enter house details and receive an estimated selling price instantly.

---

## 🚀 Features

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Missing Value Handling
- Feature Engineering
- Feature Scaling using StandardScaler
- Multiple Regression Models
- Model Evaluation using R² Score, MAE and RMSE
- Random Forest Regressor (Best Model)
- Model Serialization using Pickle
- Flask Web Application
- Responsive User Interface
- Real-time House Price Prediction

---

## 🛠 Technologies Used

### Programming Language
- Python

### Libraries
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Pickle
- Flask

### Frontend
- HTML5
- CSS3
- Bootstrap 5

### IDE
- Jupyter Notebook
- Visual Studio Code

---

## 📊 Machine Learning Workflow

1. Import Dataset
2. Data Cleaning
3. Handle Missing Values
4. Exploratory Data Analysis
5. Feature Engineering
6. Encode Categorical Variables
7. Train-Test Split
8. Feature Scaling
9. Model Training
10. Model Evaluation
11. Save Best Model
12. Deploy using Flask

---

## 🤖 Models Implemented

- Linear Regression
- Ridge Regression
- Lasso Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor

**Best Performing Model:** Random Forest Regressor

---

## 📂 Project Structure

```
House-Price-Prediction
│
├── app.py
├── HousePricePrediction.pkl
├── scaler.pkl
├── columns.pkl
├── requirements.txt
├── README.md
│
├── templates
│   ├── index.html
│   └── result.html
│
├── static
│   ├── style.css
│   └── house.jpg
│
├── notebook
│   └── HousePricePrediction.ipynb
│
└── dataset
    └── AmesHousing.csv
```

---

## 💻 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/House-Price-Prediction.git
```

Move into the project folder

```bash
cd House-Price-Prediction
```

Create a virtual environment

```bash
python -m venv myvenv
```

Activate virtual environment

Windows

```bash
myvenv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 📈 Model Performance

The Random Forest Regressor achieved the best performance among all tested regression models after data preprocessing and feature engineering.

Evaluation Metrics:

- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

---

## 🌐 Web Application

The Flask application allows users to:

- Enter house details
- Predict selling price instantly
- View predictions through a clean and responsive interface

---

## 📷 Screenshots

Add screenshots here after deployment.

Example:

- Home Page
- Prediction Result
- Model Evaluation

---

## 🔮 Future Improvements

- Streamlit Deployment
- Docker Support
- CI/CD Pipeline
- Cloud Deployment (AWS/Azure/GCP)
- SHAP Explainability
- REST API
- User Authentication
- Prediction History
- Interactive Dashboard

---

## 👨‍💻 Author

**Soham Rajapurkar**

Bachelor of Technology (Computer Science - Data Science)

Machine Learning | Data Science | Python | Flask | SQL | Power BI

---

## ⭐ If you like this project

Please give this repository a ⭐ on GitHub.
