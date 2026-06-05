import pandas as pd

df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("Total Customers:", len(df))

print("\nChurn Count:")
print(df["Churn"].value_counts())

print("\nChurn Rate (%):")
print(df["Churn"].value_counts(normalize=True) * 100)



import pandas as pd

df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("\nChurn by Contract Type")
print(pd.crosstab(df["Contract"], df["Churn"], normalize="index") * 100)

print("\nChurn by Internet Service")
print(pd.crosstab(df["InternetService"], df["Churn"], normalize="index") * 100)



