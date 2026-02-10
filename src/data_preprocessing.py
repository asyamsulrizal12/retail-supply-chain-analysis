# Import the library
import pandas as pd

# Load raw dataset
file_path = "../data/raw/Retail-Supply-Chain-Sales-Dataset.xlsx"

# Read "Main" sheet
main_df = pd.read_excel(file_path, sheet_name = "Retails Order Full Dataset")

# Read "Support" sheet
support_df = pd.read_excel(file_path, sheet_name = "Calendar Table")

# Save into "Interim" folder as .csv file
main_df.to_csv("../data/interim/main_dataset.csv", index = False)
support_df.to_csv("../data/interim/supporting_dataset.csv", index = False)

print("The extraction is completed! Main dataset:", main_df.shape, "Supporting dataset:", support_df.shape)