# House Price Prediction Using Regression

## Overview

This project implements and compares multiple regression algorithms for predicting house prices. It includes data preprocessing, exploratory data analysis (EDA), feature engineering, model training, hyperparameter tuning, and performance evaluation using standard regression metrics.

## Dataset

The project uses the `Housing.csv` dataset.

**Features**

* Area
* Bedrooms
* Bathrooms
* Stories
* Parking
* Main Road
* Guest Room
* Basement
* Hot Water Heating
* Air Conditioning
* Preferred Area
* Furnishing Status

**Target Variable**

* Price

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook

## Project Workflow

### Data Preprocessing

* Load the dataset
* Check for missing values
* Remove duplicate records
* Encode categorical variables
* Scale numerical features

### Exploratory Data Analysis

* Distribution plots
* Box plots
* Correlation heatmap

### Model Development

The following regression models are implemented:

* Linear Regression
* Ridge Regression
* Lasso Regression
* ElasticNet Regression

### Model Evaluation

Models are evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score
* 5-Fold Cross Validation

Hyperparameter tuning is performed using `GridSearchCV`.

## Project Structure

```text
House-Price-Prediction/
│
├── Housing.csv
├── regression.ipynb
├── README.md
└── requirements.txt
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/House-Price-Prediction.git
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open `regression.ipynb` and run the notebook.

## Dependencies

```
pandas
numpy
matplotlib
seaborn
scikit-learn
jupyter
```

## Results

The notebook compares the performance of multiple regression models using standard evaluation metrics and identifies the model with the best predictive performance.

## Future Improvements

* Implement Decision Tree Regression
* Implement Random Forest Regression
* Experiment with XGBoost
* Apply feature selection techniques
* Deploy the trained model using Flask or Streamlit

## Author

This project was developed as part of a machine learning study on regression techniques for house price prediction.
