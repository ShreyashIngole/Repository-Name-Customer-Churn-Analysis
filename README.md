# Customer Churn Analysis & Prediction

## Overview

This project analyzes customer churn behavior for a telecom company and develops machine learning models to predict customer attrition.

## Objectives

- Analyze customer churn patterns
- Identify key churn drivers
- Estimate revenue impact
- Build predictive churn models
- Generate actionable business recommendations

## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn
- VS Code

## Key Results

- Overall Churn Rate: 26.54%
- Monthly Revenue Lost: 139,130.85
- Decision Tree Accuracy: 72.49%
- Random Forest Accuracy: 79.25%

## Key Churn Drivers

- Contract Type
- Customer Tenure
- Monthly Charges
- Total Charges
- Payment Method
- Internet Service
---

## Business Problem

The telecom company is experiencing customer losses and needs to understand:

* Which customers are most likely to churn
* Factors contributing to churn
* Revenue impact of customer attrition
* Actions that can improve customer retention

---

## Dataset Information

| Metric            | Value  |
| ----------------- | ------ |
| Total Customers   | 7,043  |
| Churned Customers | 1,869  |
| Active Customers  | 5,174  |
| Churn Rate        | 26.54% |

---

## Executive Summary

The dataset contains 7,043 customers, of which 1,869 have churned, resulting in a churn rate of 26.54%. This indicates that approximately one in four customers discontinue service. Further analysis was conducted to identify customer segments contributing most to churn and develop targeted retention strategies.

---

# Analysis 1: Overall Churn Rate

## Objective

Determine the percentage of customers leaving the company.

### Python Code

```python
import pandas as pd

df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("Total Customers:", len(df))

print("\nChurn Count:")
print(df["Churn"].value_counts())

print("\nChurn Rate (%):")
print(df["Churn"].value_counts(normalize=True) * 100)
```

### Findings

* Total Customers: 7,043
* Customers Retained: 5,174
* Customers Churned: 1,869
* Churn Rate: 26.54%

### Business Insight

Approximately one out of every four customers leaves the company, indicating a significant customer retention challenge.

---

# Analysis 2: Churn by Contract Type

## Objective

Identify whether contract duration influences customer churn.

### Python Code

```python
print("\nChurn by Contract Type")
print(pd.crosstab(df["Contract"], df["Churn"], normalize="index") * 100)
```

### Findings

| Contract Type  | Churn Rate |
| -------------- | ---------- |
| Month-to-Month | 42.71%     |
| One Year       | 11.27%     |
| Two Year       | 2.83%      |

### Business Insight

Customers on month-to-month contracts are significantly more likely to leave compared to customers on long-term contracts.

The churn rate for month-to-month customers is approximately 15 times higher than the churn rate for customers on two-year contracts.

### Recommendation

* Encourage customers to move to annual contracts.
* Offer loyalty rewards and discounts.
* Create retention campaigns targeting month-to-month subscribers.

---

# Analysis 3: Churn by Internet Service

## Objective

Determine whether internet service type impacts churn behavior.

### Python Code

```python
print("\nChurn by Internet Service")
print(pd.crosstab(df["InternetService"], df["Churn"], normalize="index") * 100)
```

### Findings

| Internet Service | Churn Rate |
| ---------------- | ---------- |
| DSL              | 18.96%     |
| Fiber Optic      | 41.89%     |
| No Internet      | 7.40%      |

### Business Insight

Fiber-optic customers exhibit the highest churn rate among all service categories.

The churn rate among fiber-optic customers is more than double that of DSL customers.

This suggests potential issues related to pricing, service quality, customer expectations, or support experience.

### Recommendation

* Conduct customer satisfaction surveys for fiber customers.
* Review pricing strategy.
* Investigate network performance and service quality.
* Improve customer support responsiveness.

---

# Key Business Findings

1. Overall churn rate is 26.54%.
2. Month-to-month customers represent the highest-risk segment.
3. Fiber-optic customers have a significantly elevated churn rate.
4. Long-term contracts strongly improve customer retention.
5. Targeted retention initiatives could substantially reduce customer losses.

---

# Strategic Recommendations

## Short-Term Actions

* Launch retention campaigns for month-to-month customers.
* Offer contract upgrade incentives.
* Contact high-risk fiber-optic customers.

## Medium-Term Actions

* Improve customer onboarding processes.
* Enhance support quality.
* Introduce loyalty and rewards programs.

## Long-Term Actions

* Develop predictive churn models.
* Implement proactive retention strategies.
* Create executive dashboards for continuous churn monitoring.

---

# Conclusion

Analysis of 7,043 telecom customers revealed a churn rate of 26.54%, indicating a substantial customer retention challenge. Month-to-month contracts and fiber-optic service subscriptions emerged as the strongest indicators of churn. By focusing retention efforts on these high-risk customer segments, the company can reduce customer attrition, improve customer satisfaction, and increase long-term revenue stability.

---

# Next Phase

* Revenue Impact Analysis
* Customer Segmentation
* Predictive Churn Modeling
* Power BI Dashboard Development
* Executive Reporting Dashboard

# Analysis 4: Revenue Impact

## Objective

Estimate the revenue lost due to customer churn.

### Findings

| Metric | Value |
|---------|---------|
| Customers Lost | 1,869 |
| Monthly Revenue Lost | 139,130.85 |
| Annual Revenue Impact | 1,669,570.20 |

### Business Insight

Customer churn is not only reducing the customer base but also causing substantial recurring revenue loss. If churn levels remain unchanged, the company could lose approximately 1.67 million in annual recurring revenue.

### Recommendation

Prioritize retention efforts toward high-value customers and segments with elevated churn risk to protect recurring revenue streams.




# Analysis 5: Customer Segmentation

## Objective

Identify customer groups with higher churn rates and determine whether demographic factors influence customer retention.

---

## Gender Analysis

### Python Code

```python
print("\nChurn by Gender")
print(pd.crosstab(df["gender"], df["Churn"], normalize="index") * 100)
```

### Findings

| Gender | Churn Rate |
|----------|----------|
| Female | 26.92% |
| Male | 26.16% |

### Business Insight

The difference in churn rates between male and female customers is minimal.

### Recommendation

Gender-based retention campaigns are unlikely to provide significant business value and should not be prioritized.

---

## Senior Citizen Analysis

### Python Code

```python
print("\nChurn by Senior Citizen")
print(pd.crosstab(df["SeniorCitizen"], df["Churn"], normalize="index") * 100)
```

### Findings

| Customer Type | Churn Rate |
|--------------|------------|
| Non-Senior Citizen | 23.61% |
| Senior Citizen | 41.68% |

### Business Insight

Senior citizens exhibit significantly higher churn rates compared to non-senior customers.

The churn rate among senior citizens is approximately 76% higher than that of non-senior customers.

### Recommendation

- Develop specialized retention programs for senior customers.
- Improve customer support accessibility.
- Offer personalized onboarding and assistance.
- Review pricing plans for senior customer segments.

---

## Conclusion

Senior citizens represent a high-risk customer segment and should be prioritized in customer retention initiatives. Gender does not appear to be a significant factor influencing churn behavior.




# Analysis 6: Customer Tenure Analysis

## Objective

Determine whether customer tenure influences churn behavior.

### Findings

| Customer Group | Average Tenure (Months) |
|---------------|------------------------|
| Churned Customers | 17.98 |
| Retained Customers | 37.57 |

### Business Insight

Customers who churn have significantly lower tenure than retained customers. This indicates that churn is concentrated among relatively new customers.

### Recommendation

- Improve onboarding processes
- Increase customer engagement during the first 24 months
- Implement early-warning retention campaigns
- Monitor new customer satisfaction more closely





# High-Risk Customer Profile

Based on the analysis, customers most likely to churn typically exhibit the following characteristics:

- Month-to-month contract
- Fiber-optic internet service
- Senior citizen status
- Lower customer tenure

## Business Recommendation

Retention campaigns should prioritize customers matching these characteristics. Early intervention strategies targeting these segments can significantly reduce churn and protect recurring revenue.






# Analysis 7: Payment Method Analysis

## Objective

Determine whether payment methods influence customer churn behavior.

### Findings

| Payment Method | Churn Rate |
|---------------|------------|
| Bank Transfer (Automatic) | 16.71% |
| Credit Card (Automatic) | 15.24% |
| Electronic Check | 45.29% |
| Mailed Check | 19.11% |

### Business Insight

Electronic check customers demonstrate the highest churn rate at 45.29%, while customers enrolled in automatic payment methods show substantially lower churn rates.

### Recommendation

- Encourage automatic payment enrollment.
- Offer incentives for AutoPay adoption.
- Investigate potential issues affecting electronic check customers.



# Analysis 8: Paperless Billing Analysis

## Objective

Determine whether paperless billing is associated with customer churn.

### Findings

| Paperless Billing | Churn Rate |
|------------------|------------|
| No | 16.33% |
| Yes | 33.57% |

### Business Insight

Customers enrolled in paperless billing exhibit a significantly higher churn rate than customers using traditional billing methods.

While this does not imply causation, paperless billing appears to be associated with elevated churn risk and warrants further investigation.

### Recommendation

- Analyze the relationship between paperless billing and contract types.
- Include paperless billing customers in churn monitoring programs.
- Investigate behavioral differences between billing segments.




# Analysis 9: Predictive Churn Modeling

## Objective

Develop a machine learning model capable of predicting customer churn using customer demographics, service information, billing details, and account characteristics.

## Model Used

Decision Tree Classifier

## Model Performance

| Metric | Value |
|---------|---------|
| Accuracy | 72.49% |

### Business Interpretation

The model correctly predicts customer churn status for approximately 72% of customers, demonstrating the feasibility of proactive churn prediction.

## Top Predictive Features

| Feature | Importance |
|---------|------------|
| TotalCharges | 20.97% |
| MonthlyCharges | 20.25% |
| Contract | 17.43% |
| Tenure | 9.52% |
| OnlineSecurity | 4.69% |
| PaymentMethod | 4.61% |
| InternetService | 3.41% |

### Key Insights

The machine learning model identified billing characteristics, contract type, customer tenure, payment methods, and internet services as the most influential factors affecting churn.

These findings closely align with the descriptive analysis performed earlier, strengthening confidence in the identified churn drivers.

### Recommendation

Implement a churn monitoring system that identifies high-risk customers and triggers retention interventions before churn occurs.




# Analysis 10: Random Forest Churn Prediction Model

## Objective

Improve churn prediction accuracy using an ensemble machine learning model.

## Model Used

Random Forest Classifier

## Model Performance

| Model | Accuracy |
|---------|---------|
| Decision Tree | 72.49% |
| Random Forest | 79.25% |

### Improvement

The Random Forest model improved prediction accuracy by 6.76 percentage points compared to the Decision Tree model.

## Top Predictive Features

| Feature | Importance |
|---------|------------|
| TotalCharges | 18.50% |
| MonthlyCharges | 17.80% |
| Tenure | 15.45% |
| Contract | 8.06% |
| PaymentMethod | 5.20% |
| OnlineSecurity | 4.85% |
| TechSupport | 4.76% |

### Key Insights

The Random Forest model confirms that customer billing characteristics, contract type, tenure, and payment behavior are major predictors of churn.

The model also identifies Online Security and Tech Support services as influential factors that warrant additional investigation.

### Recommendation

Implement proactive retention campaigns targeting customers with:

- Low tenure
- Month-to-month contracts
- High monthly charges
- Electronic check payments
- No security or support services