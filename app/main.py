from loader import load_sales
from analysis import sales_summary
from visualize import plot_sales
from insights import sales_trend

sales = load_sales("data/sales.csv")

print("📊 Sales Summary")
summary = sales_summary(sales)
for k, v in summary.items():
    print(f"{k}: {v}")

print("\n📈 Plotting sales graph...")
plot_sales(sales, "output/sales_trend.png")


trend = sales_trend(sales)
print("\n📈 Insights")
print(f"Trend: {trend}")


























