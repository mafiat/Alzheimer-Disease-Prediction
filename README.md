# Alzheimer's Disease Prediction - Machine Learning Workflow

This project demonstrates a comprehensive machine learning workflow for predicting Alzheimer's disease diagnosis using a rich clinical and demographic dataset. The notebook covers data cleaning, exploratory analysis, feature engineering, model training, evaluation, and model saving.

---

## Table of Contents

- [Dataset Preparation](#dataset-preparation)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Feature Engineering](#feature-engineering)
- [Model Training & Evaluation](#model-training--evaluation)
- [Model Comparison](#model-comparison)
- [Model Saving & Inference](#model-saving--inference)
- [Key Variables](#key-variables)
- [Requirements](#requirements)
- [How to Run](#how-to-run)

---

## Dataset Preparation

- **Dropped Columns:** Removed `DoctorInCharge` and `PatientID` as non-informative.
- **Missing Values:** Checked and confirmed no missing data.
- **Duplicates:** Verified no duplicate records.
- **Data Types:** Validated all feature types.
- **Encoding:** Ensured categorical variables are properly encoded.

---

## Exploratory Data Analysis

- **Distribution Plots:** Age, gender, diagnosis status, ethnicity, and education level.
- **Correlation Matrix:** Visualized feature relationships and checked for multicollinearity.
- **Pairplots:** Explored feature interactions by diagnosis status.

---

## Feature Engineering

- **Scaling:** Standardized features for models sensitive to scale.
- **Dimensionality Reduction:** Performed PCA for exploratory purposes (not for feature elimination).
- **Feature Selection:** Used model-based importance to select top features for retraining.

---

## Model Training & Evaluation

Trained and evaluated multiple supervised learning models:

- **Logistic Regression**
- **Decision Tree**
- **Random Forest**
- **Gradient Boosting**
- **XGBoost**
- **LightGBM**
- **CatBoost**
- **Support Vector Machine (SVC)**
- **K-Nearest Neighbors (KNN)**
- **Neural Network (MLPClassifier)**

**Evaluation Metrics:**
- Accuracy
- Confusion Matrix
- Classification Report (Precision, Recall, F1)
- ROC Curve & AUC

---

## Model Comparison

| Model                | Accuracy | F1 Score       | Notes                                   |
|----------------------|----------|----------------|-----------------------------------------|
| Logistic Regression  | 0.83     | 0.87/0.75      | Interpretable, good baseline            |
| Decision Tree        | 0.93     | 0.94/0.90      | Simple, interpretable                   |
| Random Forest        | 0.95     | 0.96/0.92      | Robust, handles feature interactions    |
| Gradient Boosting    | 0.96     | 0.97/0.94      | Best overall performance                |
| XGBoost              | 0.95     | 0.96/0.93      | Fast, accurate, handles missing data    |
| LightGBM             | 0.96     | 0.97/0.94      | Efficient, top accuracy                 |
| CatBoost             | 0.95     | 0.96/0.93      | Handles categorical features well       |
| SVC                  | 0.83     | 0.87/0.74      | Effective in high-dimensional space     |
| KNN                  | 0.63     | 0.76/0.18      | Simple, non-parametric                  |
| Neural Network (MLP) | 0.79     | 0.82/0.73      | Learns complex patterns, robust         |

- **Best Model:** Gradient Boosting Classifier (highest accuracy and F1).

---

## Model Saving & Inference

- **Model Saved:** Gradient Boosting Classifier (`model_gb.joblib`, `model_gb.sav`)
- **How to Load:**
    ```python
    import pickle
    model = pickle.load(open('model_gb.sav', 'rb'))
    ```
- **How to Predict:**
    ```python
    y_pred = model.predict(X_new)
    y_proba = model.predict_proba(X_new)[:, 1]
    ```

---

## Key Variables

- `df`: Cleaned DataFrame.
- `X_train_class`, `X_test_class`: Train/test features for classification.
- `y_train_class`, `y_test_class`: Train/test labels for classification.
- `y_proba_top10_rf`: Predicted probabilities from Random Forest (top 10 features).
- `y_proba_top6`: Predicted probabilities from Decision Tree (top 6 features).
- `y_proba_xgb`: Predicted probabilities from XGBoost.
- `y_score_svc`: Decision function scores from SVC.

---

## Requirements

- Python 3.7+
- pandas, numpy, scikit-learn, seaborn, matplotlib, plotly
- xgboost, lightgbm, catboost
- joblib, pickle

Install requirements:
```bash
pip install pandas numpy scikit-learn seaborn matplotlib plotly xgboost lightgbm catboost joblib
```

---

## How to Run

1. Clone this repository or download the notebook and data.
2. Install the required packages.
3. Open the notebook in Jupyter and run all cells sequentially.
4. The best model will be saved as `model_gb.joblib` and `model_gb.sav`.

---

## License

This project is for educational and research purposes only.

---

## Acknowledgements

- Dataset and variable descriptions are based on a hypothetical Alzheimer's Disease dataset for demonstration.
- Machine learning workflow inspired by best practices in healthcare data science.

#### Source

Dataset Author: Rabie El Kharoua  
Kaggle Dataset Link: [Alzheimer's Disease Risk Prediction Dataset](https://www.kaggle.com/datasets/rabieelkharoua/alzheimers-disease-risk-prediction)

---