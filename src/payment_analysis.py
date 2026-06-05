import pandas as pd

df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("\nChurn by Payment Method")
print(
    pd.crosstab(
        df["PaymentMethod"],
        df["Churn"],
        normalize="index"
    ) * 100
)


print(
    pd.crosstab(
        df["PaperlessBilling"],
        df["Churn"],
        normalize="index"
    ) * 100
)