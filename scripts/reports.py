import pandas as pd

df = pd.read_csv("data/sales.csv")

total_sales = df["sales"].sum()
avg_sales = df["sales"].mean()

with open("reports/report.txt", "w") as f:
    f.write("Sales Analytics Report\n")
    f.write("======================\n")
    f.write(f"Total Sales: {total_sales}\n")
    f.write(f"Average Sales: {avg_sales}\n")

print("Report generated!")
