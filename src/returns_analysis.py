import pandas as pd
import matplotlib.pyplot as plt

def calculate_overall_return_rate(df, return_flag="Returned"):
    total_orders = len(df)
    total_returns = df[df[return_flag] == "Yes"].shape[0]
    return total_returns / total_orders

def return_rate_by_group(df, group_col, return_flag="Returned"):
    rates = df.groupby(group_col)[return_flag].apply(lambda x: (x == "Yes").mean())
    return (rates * 100).round(2)

def monthly_return_rate(df, date_col="Order Date", return_flag="Returned"):
    monthly = df.groupby(df[date_col].dt.to_period("M"))[return_flag].apply(lambda x: (x == "Yes").mean())
    monthly.plot(kind="line", title="Monthly Return Rate")
    plt.ylabel("Return Rate")
    plt.show()
    return monthly

def revenue_loss_due_to_returns(df, sales_col="Sales", return_flag="Returned"):
    total_sales = df[sales_col].sum()
    returned_sales = df.loc[df[return_flag] == "Yes", sales_col].sum()
    return {
        "total_sales": total_sales,
        "returned_sales": returned_sales,
        "loss_percentage": returned_sales / total_sales
    }

def return_rate_by_price_range(df, sales_col="Sales", return_flag="Returned"):
    bins = [0, 50, 200, 500, 1000, 5000]
    labels = ["Low", "Medium", "High", "Premium", "Luxury"]
    df["Price Range"] = pd.cut(df[sales_col], bins=bins, labels=labels)
    rates = df.groupby("Price Range", observed=True)[return_flag].apply(lambda x: (x == "Yes").mean())
    return (rates * 100).round(2)

def top_return_groups(df, group_col, return_flag="Returned", n=5):
    rates = df.groupby(group_col)[return_flag].apply(lambda x: (x == "Yes").mean())
    return rates.sort_values(ascending=False).head(n)