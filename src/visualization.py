# Import some libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10,6)


# 1. Forecasting sales retail
def plot_sales_trend(monthly_sales):
    """Line chart monthly sales trend"""
    sns.lineplot(data=monthly_sales, x="YearMonth", y="Sales", marker="o")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.tight_layout()
    plt.savefig("../reports/figures/sales_trend.png", dpi=300)
    plt.show()

def plot_sales_heatmap(monthly_sales):
    """Seasonal heatmap"""
    pivot = monthly_sales.pivot(index="Month", columns="Year", values="Sales")
    sns.heatmap(pivot, cmap="Blues", annot=True, fmt=".0f")
    plt.title("Monthly vs Annual Sales Heatmap")
    plt.tight_layout()
    plt.savefig("../reports/figures/sales_heatmap.png", dpi=300)
    plt.show()


# 2. Profitability vs Discounts
def plot_discount_vs_profit(df):
    """Scatter Plot: Discount vs Profit"""
    sns.scatterplot(data=df, x="Discount", y="Profit", alpha=0.5)
    plt.title("Scatter Plot: Discount vs Profit")
    plt.xlabel("Discount")
    plt.ylabel("Profit")
    plt.tight_layout()
    plt.savefig("../reports/figures/discount_vs_profit.png", dpi=300)
    plt.show()

def plot_profit_by_discount_bin(df):
    """Boxplot of profit per discount category"""
    df["Discount_bin"] = pd.cut(df["Discount"], bins=[0,0.1,0.2,0.5,1],
                                labels=["0-10%","10-20%","20-50%","50-100%"])
    sns.boxplot(data=df, x="Discount_bin", y="Profit")
    plt.title("Distribution of Profit per Discount Category")
    plt.tight_layout()
    plt.savefig("../reports/figures/profit_by_discount_bin.png", dpi=300)
    plt.show()


# 3. Customer Segmentation
def plot_segment_sales(seg_summary):
    """Bar chart total sales per segment"""
    sns.barplot(data=seg_summary, x="Segment", y="Sales")
    plt.title("Total Sales per Segment")
    plt.tight_layout()
    plt.savefig("../reports/figures/segment_sales.png", dpi=300)
    plt.show()

def plot_segment_pie(seg_summary):
    """Pie chart proportion sales per segment"""
    plt.pie(seg_summary["Sales"], labels=seg_summary["Segment"], autopct="%1.1f%%")
    plt.title("Share of Sales per Segment")
    plt.tight_layout()
    plt.savefig("../reports/figures/segment_pie.png", dpi=300)
    plt.show()


# 4. Returns Analysis
def plot_return_rate_category(return_rate_category):
    """Bar chart return rate per product category"""
    sns.barplot(data=return_rate_category, x="Category", y="ReturnRate")
    plt.title("Return Rate per Category")
    plt.tight_layout()
    plt.savefig("../reports/figures/return_rate.png", dpi=300)
    plt.show()

def plot_return_rate_region(crosstab_region):
    """Bar chart return rate per region (stacked)"""
    crosstab_region.plot(kind="bar", stacked=True)
    plt.title("Return Rate per Region")
    plt.tight_layout()
    plt.savefig("../reports/figures/return_crosstab.png", dpi=300)
    plt.show()


# 5. Quality Check Visualizations
def plot_sales_outliers(df):
    """Boxplot for sales outlier check"""
    sns.boxplot(data=df, x="Sales")
    plt.title("Boxplot Sales (Outlier Check)")
    plt.tight_layout()
    plt.savefig("../reports/figures/sales_outliers.png", dpi=300)
    plt.show()

def plot_profit_outliers(df):
    """Boxplot for profit outlier check"""
    sns.boxplot(data=df, x="Profit")
    plt.title("Boxplot Profit (Outlier Check)")
    plt.tight_layout()
    plt.savefig("../reports/figures/profit_outliers.png", dpi=300)
    plt.show()
