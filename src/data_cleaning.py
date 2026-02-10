# Import some libraries
import pandas as pd
import numpy as np


# 1. Cleaning "main_dataset.csv"
def clean_main_dataset(input_path = "../data/interim/main_dataset.csv",
                      output_path = "../data/cleaned/sales_clean.csv"):
    df = pd.read_csv(input_path)

    # Convert dates
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors = "coerce")
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors = "coerce")

    # Validate ship date >= order date
    invalid_dates = df[df["Ship Date"] < df["Order Date"]]
    if not invalid_dates.empty:
        print("Warning: Found invalid ship date")

    # Numeric columns
    for col in ["Sales", "Profit", "Discount", "Quantity"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors = "coerce")

    # Normalize discount (0-1)
    df.loc[df["Discount"] > 1, "Discount"] = df["Discount"] / 100.0

    # Handle missing values
    if "Postal Code" in df.columns:
        df["Postal Code"] = df["Postal Code"].fillna(0)
    if "Returned" in df.columns:
        df["Returned"] = df["Returned"].fillna("No")

    # Standardize categorical
    for col in ["Segment", "Category", "Region", "Ship Mode"]:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.title()

    # Drop duplicates
    df = df.drop_duplicates()

    # Save the cleaned data
    df.to_csv(output_path, index = False)
    print(f"Main dataset cleaned -> {output_path}")


# 2. Cleaning "supporting_dataset.csv"
def clean_supporting_dataset(input_path = "../data/interim/supporting_dataset.csv",
                            output_path = "../data/cleaned/time_dimension.csv"):
    df = pd.read_csv(input_path)

    # Convert date
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Validate consistency
    df["Day"] = df["Date"].dt.day
    df["Year_check"] = df["Date"].dt.year
    df["Month_check"] = df["Date"].dt.month
    df["Day_check"] = df["Date"].dt.day

    mismatches = df[(df["Year"] != df["Year_check"]) |
                    (df["Month"] != df["Month_check"]) |
                    (df["Day"] != df["Day_check"])]
    if not mismatches.empty:
        print("Warning: Found mismatches in supporting dataset")

    df = df.drop(columns=["Year_check", "Month_check", "Day_check"])

    # Drop duplicates
    df = df.drop_duplicates()

    # Save the cleaned data
    df.to_csv(output_path, index = False)
    print(f"Supporting dataset cleaned -> {output_path}")

if __name__ == "__main__":
    clean_main_dataset()
    clean_supporting_dataset()