# 💳 Credit Card Fraud Detection Using Machine Learning

<p align="center">
  <strong>Detect suspicious transactions. Reduce financial risk. Build smarter fraud detection.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Machine-Learning-8A2BE2?style=for-the-badge" alt="Machine Learning"/>
  <img src="https://img.shields.io/badge/Scikit--learn-ML-orange?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="Scikit-learn"/>
  <img src="https://img.shields.io/badge/Status-Completed-2EA44F?style=for-the-badge" alt="Project Status"/>
</p>

---

## 🚀 About the Project

Credit card fraud is a major challenge in digital payments. Fraudulent transactions can cause financial losses, making accurate and reliable detection essential.

This project uses **Machine Learning classification algorithms** to identify potentially fraudulent credit card transactions by learning patterns from historical transaction data.

The project explores multiple models, evaluates their performance, and compares their ability to distinguish genuine transactions from fraudulent ones.

**The goal:** Build a data-driven system that helps identify suspicious transactions while carefully considering the trade-off between detecting fraud and incorrectly flagging genuine transactions.

## 🎯 Project Objectives

- Analyze and understand credit card transaction data.
- Perform data cleaning and exploratory data analysis.
- Handle the imbalance between genuine and fraudulent transactions.
- Train and evaluate multiple machine learning models.
- Compare model performance using fraud-relevant evaluation metrics.
- Identify influential features and save the trained model.
- Support predictions for new transactions.

## 🧠 Machine Learning Models

| Model | Purpose |
|---|---|
| Logistic Regression | Establish a baseline classification model. |
| Balanced Logistic Regression | Give greater consideration to the minority fraud class. |
| Random Forest Classifier | Combine multiple decision trees to identify complex patterns. |

### 🏆 Model Comparison

The original notebook produced the following test-set results:

| Model | Precision | Recall | F1-Score |
|---|---:|---:|---:|
| Logistic Regression | 82.89% | 64.29% | 72.41% |
| Balanced Logistic Regression | 6.10% | 91.84% | 11.44% |
| Random Forest | **96.05%** | 74.49% | **83.91%** |

**Best overall result in this comparison: Random Forest**, based on its highest F1-score and precision.

*Note: These are results from the original notebook evaluation. Performance can change with different data splits, preprocessing, or decision thresholds. The balanced model's higher recall comes with many more false-positive predictions.*

## 📊 Understanding the Dataset

The project uses a credit card transaction dataset with:

- **284,807** transactions in the original dataset.
- **31** columns, including transaction time, amount, anonymized features (`V1`–`V28`), and the target label (`Class`).
- **284,315** genuine transactions (`Class = 0`).
- **492** fraudulent transactions (`Class = 1`).

The dataset is highly imbalanced: fraudulent transactions represent approximately **0.17%** of the original records.

> **Important:** The full dataset is not stored in this GitHub repository because it exceeds GitHub's standard 100 MB per-file limit.

## ⚙️ Project Workflow

```text
Transaction Dataset
        |
        v
Data Exploration & Analysis
        |
        v
Data Cleaning & Preprocessing
        |
        v
Feature Selection (X) and Target (y)
        |
        v
Train-Test Split
        |
        v
Feature Scaling
        |
        v
Machine Learning Model Training
        |
        v
Model Evaluation & Comparison
        |
        v
Fraud Prediction for New Transactions
```

## ✨ Key Features

- 🔍 **Data Analysis:** Examine dataset structure, distributions, missing values, duplicates, and class imbalance.
- 🧹 **Data Preprocessing:** Prepare transaction data for machine learning.
- ⚖️ **Imbalance Handling:** Explore class-weighted learning for the minority fraud class.
- 🤖 **Multiple Models:** Compare Logistic Regression, balanced Logistic Regression, and Random Forest.
- 📈 **Performance Evaluation:** Use precision, recall, F1-score, confusion matrix, and ROC-AUC.
- 🔑 **Feature Importance:** Identify which anonymized input features contribute most to Random Forest predictions.
- 💾 **Model Persistence:** Save the trained model for later use.
- 🔮 **Transaction Prediction:** Apply the trained model to new transaction data.

## 🛠️ Technology Stack

| Technology | Usage |
|---|---|
| Python | Core programming language |
| Jupyter Notebook | Interactive development and experimentation |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Scikit-learn | Preprocessing, model training, and evaluation |
| Joblib / Pickle | Saving and loading trained model artifacts |
| Streamlit | Optional web interface, if included in the repository |

## 📁 Project Structure

```text
CreditCardFraudDetection/
│
├── Data/
│   └── creditcard.csv             # Local dataset; excluded from GitHub
│
├── notebooks/
│   └── CreditCardFraudDetection.ipynb
│
├── app.py                         # Optional Streamlit interface
├── rf_fraud_detection_model.pkl    # Saved Random Forest model
├── scaler.pkl                     # Saved feature scaler, if included
├── requirements.txt               # Project dependencies, if included
├── .gitignore
└── README.md
```

*The structure above is illustrative. Keep only the filenames and folders that actually exist in your repository.*

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Deepikajanarthanan/Creditcard_Fraud_Detection.git
```

### 2. Open the Project Folder

```bash
cd Creditcard_Fraud_Detection
```

### 3. Create a Virtual Environment (Recommended)

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

If the repository contains `requirements.txt`:

```bash
pip install -r requirements.txt
```

Otherwise, install the main libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter joblib
```

For a Streamlit interface, install Streamlit too:

```bash
pip install streamlit
```

### 5. Add the Dataset Locally

Obtain the credit card fraud dataset from its original source and place `creditcard.csv` in the `Data/` directory, matching the path expected by your notebook or application.

**Dataset source:** [Kaggle — Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

The dataset is not included in this repository because of its file size. Follow the dataset provider's access and usage terms.

### 6. Run the Notebook

```bash
jupyter notebook
```

Open `notebooks/CreditCardFraudDetection.ipynb` and run the cells in order.

### 7. Launch the Optional Web Application

If `app.py` is present and configured:

```bash
streamlit run app.py
```

## 📐 Evaluation Metrics Explained

- **Precision:** Of all transactions predicted as fraud, how many were actually fraudulent?
- **Recall:** Of all actual fraudulent transactions, how many did the model detect?
- **F1-Score:** A combined measure of precision and recall.
- **Confusion Matrix:** Shows correct and incorrect predictions for each class.
- **ROC-AUC:** Measures how well the model separates the two classes across classification thresholds.

In fraud detection, accuracy alone can be misleading because genuine transactions greatly outnumber fraudulent transactions. Precision and recall are particularly important.

## 🔐 Important Considerations

- A model prediction is an indication of potential fraud, not proof of fraudulent activity.
- False positives can inconvenience genuine cardholders.
- False negatives can allow fraudulent transactions to go undetected.
- The dataset's `V1`–`V28` features are anonymized; their individual real-world meanings are not established by this project.
- Production deployment would require additional validation, monitoring, privacy safeguards, and appropriate security controls.

## 🔮 Future Enhancements

- Hyperparameter tuning and cross-validation.
- Precision-Recall curve analysis and threshold optimization.
- Testing additional algorithms and resampling methods.
- Developing an interactive Streamlit dashboard.
- Adding transaction-level explanations and risk indicators.
- Monitoring model performance as transaction patterns change.

## 🎓 Learning Outcomes

Through this project, I explored:

- Data preprocessing and exploratory data analysis.
- Supervised machine learning classification.
- Class imbalance and its impact on model performance.
- Model evaluation using precision, recall, F1-score, and ROC-AUC.
- Feature importance and model persistence.
- The practical challenges of applying machine learning to financial fraud detection.

## 👩‍💻 Author

**Deepika Janarthanan**

B.Tech — Information Science & Engineering

<p>
  <a href="https://github.com/Deepikajanarthanan">
    <img src="https://img.shields.io/badge/GitHub-Profile-181717?style=for-the-badge&logo=github" alt="GitHub Profile"/>
  </a>
  <a href="https://www.linkedin.com/in/deepika-j-b012503a7/">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
  </a>
</p>

---

<p align="center">
  <strong>Turning transaction data into smarter fraud detection.</strong>
  <br/>
  Built with Python and Machine Learning.
</p>
