import os

import pandas as pd

INPUT_FILE = "data/raw_fiscal_data.xlsx"

if not os.path.exists(INPUT_FILE):
    print(f"No workbook at {INPUT_FILE}.")
    print("The hackathon extract is not part of this repository.")
    print("Save your own panel there. See data/README.md for public sources and the expected columns.")
    print("Nothing was read.")
    raise SystemExit(0)

# Load Excel file
xls = pd.ExcelFile(INPUT_FILE)

print("Sheet names:", xls.sheet_names)
print("\n" + "="*80)

# Inspect each sheet
for sheet in xls.sheet_names:
    print(f"\n=== Sheet: {sheet} ===")
    df = pd.read_excel(xls, sheet_name=sheet)
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)[:10]}")
    print(f"\nFirst 3 rows:")
    print(df.head(3))
    print("\n" + "-"*80)
