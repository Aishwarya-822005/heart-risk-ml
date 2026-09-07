# ❤️ Heart Disease Detection

A complete ML project to detect heart disease using the Cleveland Heart Disease dataset.

---

## 📁 Files

| File | Description |
|------|-------------|
| `heart_disease_detection.ipynb` | Main Jupyter notebook (run this) |
| `generate_data.py` | Synthetic data generator (fallback if URL fails) |
| `requirements.txt` | Python dependencies |

---

## 🚀 Quick Start

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Launch Jupyter
```bash
jupyter notebook heart_disease_detection.ipynb
```

### 3. Run all cells
Use **Kernel → Restart & Run All** to execute the full pipeline.

---

## 📊 What the notebook does

1. **Load Data** – Downloads the Cleveland dataset from UCI; falls back to synthetic data if offline
2. **EDA** – Distribution plots, correlation heatmap, target analysis
3. **Preprocessing** – Missing value handling, feature scaling, stratified train/test split
4. **Model Training** – 5 classifiers: Logistic Regression, Random Forest, Gradient Boosting, SVM, KNN
5. **Evaluation** – Accuracy, F1-Score, ROC-AUC, 5-fold cross-validation, confusion matrix
6. **Feature Importance** – Random Forest importance ranking
7. **Save Model** – Best model saved as `best_heart_model.pkl`
8. **Predict** – Interactive `predict_heart_disease()` function for new patients

---

## 🩺 Dataset Features

| Feature | Description |
|---------|-------------|
| age | Age in years |
| sex | 1 = Male, 0 = Female |
| cp | Chest pain type (0–3) |
| trestbps | Resting blood pressure (mm Hg) |
| chol | Serum cholesterol (mg/dl) |
| fbs | Fasting blood sugar > 120 mg/dl |
| restecg | Resting ECG results (0–2) |
| thalach | Maximum heart rate achieved |
| exang | Exercise-induced angina |
| oldpeak | ST depression by exercise |
| slope | Slope of peak exercise ST segment |
| ca | Number of major vessels (0–3) |
| thal | Thalassemia type |
| **target** | **1 = Heart Disease, 0 = No Disease** |

---

## ⚠️ Disclaimer
This project is for **educational purposes only**. Do not use as a substitute for professional medical advice.
