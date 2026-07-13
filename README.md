\# House Price Prediction Using Machine Learning
\## Project Overview
This project focuses on predicting house prices using Machine Learning regression algorithms.
The model is trained on a housing dataset containing different features of houses. Multiple regression algorithms are implemented, evaluated, compared, and optimized using cross-validation and hyperparameter tuning.


The best-performing model can be deployed as a REST API using FastAPI to provide real-time house price predictions.

\---

\# Dataset



The project uses `Housing.csv`.



The dataset contains information about houses such as:



\* Area

\* Bedrooms

\* Bathrooms

\* Stories

\* Main Road Access

\* Guest Room Availability

\* Basement Availability

\* Hot Water Heating

\* Air Conditioning

\* Parking

\* Preferred Area

\* Furnishing Status



\### Target Variable



\* Price



The objective is to predict the house price based on these input features.



\---



\# Machine Learning Workflow



The complete workflow followed in this project:



```

Data Collection

&#x20;       |

&#x20;       ↓

Data Exploration (EDA)

&#x20;       |

&#x20;       ↓

Data Preprocessing

&#x20;       |

&#x20;       ↓

Feature Encoding

&#x20;       |

&#x20;       ↓

Train-Test Split

&#x20;       |

&#x20;       ↓

Feature Scaling

&#x20;       |

&#x20;       ↓

Model Training

&#x20;       |

&#x20;       ↓

Model Evaluation

&#x20;       |

&#x20;       ↓

Cross Validation

&#x20;       |

&#x20;       ↓

Hyperparameter Tuning

&#x20;       |

&#x20;       ↓

Best Model Selection

&#x20;       |

&#x20;       ↓

API Deployment

```



\---



\# Machine Learning Models Used



The following regression models were implemented:



\### 1. Linear Regression



A basic regression algorithm used to understand the relationship between input features and house prices.



\### 2. Ridge Regression



A regularized regression model that reduces overfitting by adding L2 regularization.



\### 3. Lasso Regression



A regularized regression technique that performs feature selection using L1 regularization.



\### 4. Elastic Net Regression



A combination of Ridge and Lasso regression that uses both L1 and L2 regularization.



\---



\# Data Preprocessing



The following preprocessing steps were performed:



\* Loading dataset using Pandas

\* Data exploration and visualization

\* Checking missing values

\* Encoding categorical variables

\* Separating features and target variable

\* Splitting data into training and testing sets

\* Feature scaling using Min\_Max



\---



\# Model Evaluation



The models are evaluated using the following metrics:



\## Mean Absolute Error (MAE)



Measures the average absolute difference between actual and predicted values.



\## Mean Squared Error (MSE)



Measures the average squared difference between actual and predicted values.



\## Root Mean Squared Error (RMSE)



Represents prediction error in the same units as the target variable.



\## R² Score



Shows how well the model explains the variation in house prices.



\---



\# Model Optimization



After initial model comparison:



\## Cross Validation



Cross-validation is applied to check model performance on different subsets of data and ensure reliable results.



\## Hyperparameter Tuning



GridSearchCV is used to find the best parameters for each regression model.



This improves model performance and helps select the final optimized model.



\---



\# API Deployment



The trained machine learning model is deployed using \*\*FastAPI\*\*.



The API allows users to send house features and receive predicted house prices.



\## API Workflow



```

User Input

&#x20;    |

&#x20;    ↓

FastAPI Endpoint

&#x20;    |

&#x20;    ↓

Input Validation

&#x20;    |

&#x20;    ↓

Feature Preprocessing

&#x20;    |

&#x20;    ↓

Scaler Transformation

&#x20;    |

&#x20;    ↓

Machine Learning Model

&#x20;    |

&#x20;    ↓

Predicted House Price

```



\---



\# API Features



The API:



\* Loads the trained machine learning model

\* Loads the saved scaler

\* Accepts house details as input

\* Processes input data

\* Returns predicted house price



\---



\# Example API Request



\### Endpoint



```

POST /predict

```



\### Example Input



```json

{

&#x20;   "area": 7420,

&#x20;   "bedrooms": 4,

&#x20;   "bathrooms": 2,

&#x20;   "stories": 3,

&#x20;   "mainroad": "yes",

&#x20;   "guestroom": "no",

&#x20;   "basement": "no",

&#x20;   "hotwaterheating": "no",

&#x20;   "airconditioning": "yes",

&#x20;   "parking": 2,

&#x20;   "prefarea": "yes",

&#x20;   "furnishingstatus": "semi-furnished"

}

```



\### Example Response



```json

{

&#x20;   "predicted\_price": 8500000

}

```



\---



\# Technologies Used



\## Programming Language



\* Python



\## Libraries



\* Pandas

\* NumPy

\* Scikit-learn

\* Matplotlib

\* Seaborn

\* Joblib



\## Development Tools



\* Jupyter Notebook

\* VS Code



\## Deployment



\* FastAPI

\* Uvicorn



\---



\# Project Structure



```

house\_price\_prediction\_app/



│

├── Housing.csv

│

├── regression.ipynb

│

├── app.py

│

├── model.pkl

│

├── scaler.pkl

│

├── requirements.txt

│

└── README.md

```



\---



\# Installation and Setup



\## 1. Clone Repository



```

git clone <repository-url>

```



\## 2. Move Into Project Directory



```

cd house\_price\_prediction\_app

```



\## 3. Create Virtual Environment



```

python -m venv venv

```



\## 4. Activate Virtual Environment



Windows:



```

venv\\Scripts\\activate

```



\## 5. Install Dependencies



```

pip install -r requirements.txt

```



\---



\# Running the Project



\## Run Machine Learning Notebook



```

jupyter notebook

```



Open:



```

regression.ipynb

```



Run all cells.



\---



\# Run FastAPI Application



Start API server:



```

uvicorn app:app --reload

```



API will run at:



```

http://127.0.0.1:8000

```



\---



\# API Documentation



FastAPI provides automatic documentation.



Open:



```

http://127.0.0.1:8000/docs

```



You can test the prediction endpoint directly from Swagger UI.





