import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

churn_counts = df["Churn"].value_counts()

plt.figure(figsize=(6,4))
plt.bar(churn_counts.index, churn_counts.values)

plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig("reports/churn_distribution.png")

plt.show()