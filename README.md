# End-to-End Machine Learning Project: Student Performance Prediction System

A comprehensive machine learning application that predicts student exam performance using various features like gender, ethnicity, parental education level, lunch type, and test preparation course. The system includes data ingestion, transformation, model training with hyperparameter tuning, and a web-based prediction interface built with FastAPI.

## 📋 Project Overview

This project implements a complete machine learning pipeline for predicting student math exam scores based on various demographic and educational features. It demonstrates best practices for data engineering, model selection, hyperparameter optimization, and deployment.

### Key Features

- **Complete ML Pipeline**: Data ingestion → Transformation → Model Training → Predictions
- **Multi-Model Evaluation**: Tests 8 different algorithms (Random Forest, Gradient Boosting, XGBoost, CatBoost, Decision Tree, Linear Regression, KNN, AdaBoost)
- **Hyperparameter Tuning**: GridSearchCV optimization for each model
- **Web Interface**: User-friendly FastAPI web application for making predictions
- **Containerization**: Docker support for easy deployment
- **Error Handling**: Custom exception handling with detailed logging
- **Modular Architecture**: Clean separation of concerns with components and pipelines

---

## 📁 Project Structure

```
ML-Project-1/
├── artifacts/                              # Generated ML artifacts
│   ├── raw.csv                            # Original dataset
│   ├── train.csv                          # Training set (80%)
│   ├── test.csv                           # Test set (20%)
│   ├── model.pkl                          # Trained ML model
│   └── preprocessor.pkl                   # Fitted preprocessor
│
├── catboost_info/                         # CatBoost training logs
│   ├── catboost_training.json
│   ├── learn_error.tsv
│   ├── time_left.tsv
│   └── learn/
│
├── logs/                                  # Application logs
│
├── notebook/                              # Jupyter notebooks
│   ├── 1 . EDA STUDENT PERFORMANCE.ipynb # Exploratory Data Analysis
│   ├── 2. MODEL TRAINING.ipynb            # Model Training & Evaluation
│   └── data/
│       └── stud.csv                       # Source dataset (1000 students)
│
├── src/                                   # Main source code
│   ├── __init__.py
│   ├── exception.py                       # Custom exception handling
│   ├── logger.py                          # Logging configuration
│   ├── utils.py                           # Utility functions (save/load models)
│   ├── components/                        # ML pipeline components
│   │   ├── __init__.py
│   │   ├── data_ingestion.py              # Data loading & splitting
│   │   ├── data_transformation.py         # Feature preprocessing & scaling
│   │   └── model_trainer.py               # Model training & evaluation
│   └── pipeline/                          # ML pipelines
│       ├── __init__.py
│       ├── train_pipeline.py              # Training workflow
│       └── predict_pipeline.py            # Prediction workflow
│
├── templates/                             # HTML templates for web interface
│   ├── index.html                         # Home page
│   └── home.html                          # Prediction form & results
│
├── app.py                                 # FastAPI application (main entry point)
├── setup.py                               # Package configuration
├── requirements.txt                       # Python dependencies
├── dockerfile                             # Docker configuration
├── Procfile                               # Heroku deployment config
└── README.md                              # This file
```

---

## 🔧 Tech Stack

### Core ML & Data Processing
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **scikit-learn**: Machine learning algorithms and preprocessing
- **xgboost**: Gradient boosting framework
- **catboost**: Categorical boosting
- **dill**: Advanced serialization (model persistence)

### Visualization & EDA
- **matplotlib**: Data visualization
- **seaborn**: Statistical data visualization

### Web Framework
- **FastAPI**: Modern, fast web framework
- **Jinja2**: Template engine for HTML rendering
- **uvicorn**: ASGI web server
- **python-multipart**: Form data parsing

### Deployment
- **Docker**: Containerization
- **Heroku**: Cloud deployment (via Procfile)

---

## 🎯 Dataset Information

**Source**: `notebook/data/stud.csv`  
**Samples**: 1,000 student records  
**Target Variable**: `math_score` (0-100)  

### Features Used

**Numerical Features**:
- `reading_score`: Student's reading test score (0-100)
- `writing_score`: Student's writing test score (0-100)

**Categorical Features**:
- `gender`: Male / Female
- `race_ethnicity`: Group A, B, C, D, E
- `parental_level_of_education`: Some high school, high school, some college, associate's degree, bachelor's degree, master's degree
- `lunch`: Free/reduced or standard
- `test_preparation_course`: None or completed

---

## 🤖 Model Selection & Training

### Models Evaluated
The system trains and compares 8 different regression models:

1. **Random Forest** - Ensemble method with multiple trees
2. **Decision Tree** - Single tree with various criteria
3. **Gradient Boosting** - Sequential boosting with learning rate tuning
4. **Linear Regression** - Baseline linear model
5. **K-Neighbors Regressor** - Instance-based learning
6. **XGBRegressor** - Extreme Gradient Boosting
7. **CatBoosting Regressor** - Handles categorical features natively
8. **AdaBoost Regressor** - Adaptive boosting

### Hyperparameter Optimization
Each model uses GridSearchCV with parameters tuned for optimal performance on the test set.

---

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git
- Optional: Docker (for containerized deployment)

---

## 📥 Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/UzairKhan313/ml-project-1-Student-Performance-Prediction-System.git
cd ml-project-1-Student-Performance-Prediction-System
```

### Step 2: Create Virtual Environment

#### On Windows (PowerShell):
```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1
```

#### On Windows (Command Prompt):
```cmd
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate.bat
```

#### On macOS/Linux:
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install -r requirements.txt

# Install the package in development mode
pip install -e .
```

**Note**: The `-e .` flag installs the package in editable mode, allowing you to import `src` modules directly in your code.

---

## 🎓 Usage

### Option 1: Train Model & Run Web Application

```bash
# Activate virtual environment (if not already active)
# Windows:
.\venv\Scripts\Activate.ps1
# macOS/Linux:
source venv/bin/activate

# Start the FastAPI server
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

**Output**: 
```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

**Access the application**:
- Open your browser and navigate to: `http://localhost:8000`
- Fill in student information in the form
- Submit to get math score prediction

### Option 2: Run Python Script for Model Training

```bash
# From the root directory with venv activated
python src/components/data_ingestion.py
```

This will:
1. Load the dataset from `notebook/data/stud.csv`
2. Split into train/test sets (80/20 split)
3. Transform features (scale numerical, encode categorical)
4. Train all 8 models
5. Save the best model and preprocessor to `artifacts/`

---

## 🐳 Docker Deployment

### Build Docker Image

```bash
docker build -t student-performance-app .
```

### Run Docker Container

```bash
docker run -p 8000:8000 student-performance-app
```

Access the application at: `http://localhost:8000`

---

## ☁️ Heroku Deployment

### Prerequisites
- Heroku CLI installed
- Heroku account

### Deploy Steps

```bash
# Login to Heroku
heroku login

# Create Heroku app
heroku create your-app-name

# Deploy code
git push heroku main

# View logs
heroku logs --tail
```

The app will be available at: `https://your-app-name.herokuapp.com`

---

## 📊 Project Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                      Data Ingestion                         │
│  Load stud.csv → Split 80/20 → Save to artifacts/          │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│                    Data Transformation                      │
│  • Numerical: StandardScaler (reading_score, writing_score) │
│  • Categorical: OneHotEncoding (gender, ethnicity, etc.)    │
│  • Handle missing values (median/most_frequent)             │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│                      Model Training                         │
│  • Initialize 8 models                                      │
│  • GridSearchCV for hyperparameter tuning                    │
│  • Evaluate on test set (R² score)                          │
│  • Save best model & preprocessor                           │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│                 Prediction Pipeline                         │
│  • Load preprocessor & model from artifacts/                │
│  • Transform new student data                               │
│  • Generate math score prediction                           │
│  • Return prediction via FastAPI endpoint                   │
└─────────────────────────────────────────────────────────────┘
```

---

## 📝 Logging & Monitoring

The application includes comprehensive logging:

- **Log Location**: `logs/` directory
- **Log Format**: Timestamp | Level | Message
- **Components Logged**:
  - Data ingestion progress
  - Data transformation steps
  - Model training metrics
  - Prediction requests
  - Errors and exceptions

### View Logs Example
```python
# Application automatically logs to console and file
# Check logs/ folder for detailed execution logs
```

---

## 🔍 Key Components Explained

### 1. **data_ingestion.py**
- Reads raw dataset from `notebook/data/stud.csv`
- Performs 80/20 train-test split
- Saves split data to `artifacts/` directory

### 2. **data_transformation.py**
- Creates preprocessing pipeline
- Numerical features: StandardScaler (removes mean, scales to unit variance)
- Categorical features: OneHotEncoding (converts categories to binary columns)
- Returns fitted preprocessor for later use

### 3. **model_trainer.py**
- Initializes 8 different regression models
- Defines hyperparameter grids for each model
- Uses GridSearchCV for hyperparameter optimization
- Evaluates models on test set using R² score
- Saves best model to `artifacts/model.pkl`

### 4. **predict_pipeline.py**
- Loads model and preprocessor from artifacts
- Accepts student data via `CustomData` class
- Transforms data using saved preprocessor
- Returns predicted math score

### 5. **app.py** (FastAPI)
- Routes:
  - `GET /`: Displays home page
  - `POST /predict-data`: Accepts form data, returns prediction

---

## 🛠️ Troubleshooting

### Issue: Module not found error
```
Solution: Ensure virtual environment is activated and pip install -e . was run
```

### Issue: Port 8000 already in use
```bash
# Run on different port
uvicorn app:app --port 8001
```

### Issue: Model not found in artifacts
```
Solution: Run python src/components/data_ingestion.py first to train model
```

### Issue: Can't activate virtual environment
```bash
# Try using full path:
C:\path\to\project\venv\Scripts\activate
# Or use source command on Unix
source /path/to/project/venv/bin/activate
```

---

## 📚 Additional Notes

- **Data Split**: Uses random_state=42 for reproducibility
- **Model Evaluation Metric**: R² Score (coefficient of determination)
- **Best Model**: Automatically selected based on test set R² score
- **Predictions Range**: Math scores typically 0-100

---

## 👤 Author

**Uzair Khan**  
📧 Email: uzairkhaan2003@gmail.com

---

## 📄 License

This project is open source and available for educational and learning purposes.

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests

---

## 📞 Support

For issues or questions, please open an issue in the repository or contact the author.

---

**Happy Learning! 🎓**
