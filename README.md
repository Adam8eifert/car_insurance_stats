# Car Insurance Claim Prediction and Feature Importance Analysis

## 🎯 Project Goal

This project aims to build a predictive model to identify customers most likely to purchase car insurance (the `Response` variable) after an initial offer. The primary business objective is to **maximize the Recall rate** (True Positive Rate) to minimize missed sales opportunities (False Negatives), thereby optimizing marketing spend and increasing revenue.

## 📊 Key Results (Executive Summary)

The analysis found that standard linear models (Logistic Regression) failed due to extreme class imbalance (approx. 90:10). The final **Random Forest** model was robust and achieved significant performance gains.

| Metric | Baseline (LR) | Final Model (Random Forest) | Improvement |
| :--- | :--- | :--- | :--- |
| **Recall** (Ability to capture buyers) | 52.45% | **74.77%** | **+22.32%** |
| **F1-Score** (Overall Performance) | 0.5371 | **0.6620** | Significant |
| **Missed Buyers (FN)** | 456 | **242** | Reduced by 47% |

The Random Forest model is recommended for deployment as it is highly effective at identifying profitable target customers.

---

## 💡 Actionable Insights for Management

The model revealed the true drivers of customer conversion. These factors should guide the marketing and pricing strategies:

1.  **Risk Metrics Dominate:** Factors related to **driving history** (`past_accidents`, `speeding_violations`) are the strongest predictors, accounting for over 50% of the predictive power.
2.  **Credit Score vs. Accidents:** Financial stability (`credit_score`, `Credit_to_Mileage_Ratio`) remains vital, but **direct risk history** is marginally more important in the final decision.
3.  **Target Profile:** Focus marketing resources on individuals with **low past accident counts**, clear driving records, and proven vehicle ownership.

---

## 🛠️ Project Structure and Methodology

This project is organized into two primary Jupyter Notebooks:

1.  **`01_EDA_and_Feature_Engineering.ipynb`**
    * Initial Exploratory Data Analysis (EDA), confirming extreme class imbalance.
    * Feature Engineering (e.g., `Credit_to_Mileage_Ratio`, `Mileage_Category`).
    * Initial attempt at Logistic Regression, which failed due to numerical instability (`ConvergenceWarning`).
2.  **`02_Model_Evaluation.ipynb`**
    * Attempted threshold optimization on the unstable Logistic Regression model.
    * Training and evaluation of the robust **Random Forest Classifier** with `class_weight='balanced'` to correct for the data imbalance.
    * Final model selection based on highest **Recall** and **F1-Score**.

## 💻 Technical Dependencies

This project requires Python 3.x and the following libraries, as defined in `requirements.txt`:

* `pandas`
* `numpy`
* `scikit-learn` (for models and metrics)
* `statsmodels` (for initial statistical analysis)
* `matplotlib` / `seaborn` (for visualization)

## 🚀 How to Run the Project

1.  **Clone the repository.**
2.  **Set up the environment:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the analysis:** Open and execute the cells sequentially in both Jupyter Notebooks (`01_EDA_and_Feature_Engineering.ipynb` and `02_Model_Evaluation.ipynb`). The final results and insights are generated in **Cell 9** of the second notebook.