import pandas as pd

df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

lost_customers = df[df["Churn"] == "Yes"]

monthly_revenue_lost = lost_customers["MonthlyCharges"].sum()

print("Customers Lost:", len(lost_customers))
print("Monthly Revenue Lost:", round(monthly_revenue_lost, 2))

print("\nChurn by Gender")
print(pd.crosstab(df["gender"], df["Churn"], normalize="index") * 100)

print("\nChurn by Senior Citizen")
print(pd.crosstab(df["SeniorCitizen"], df["Churn"], normalize="index") * 100)


churned = df[df["Churn"] == "Yes"]
not_churned = df[df["Churn"] == "No"]

print("Average Tenure of Churned Customers:")
print(churned["tenure"].mean())

print("\nAverage Tenure of Retained Customers:")
print(not_churned["tenure"].mean())