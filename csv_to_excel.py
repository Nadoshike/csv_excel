import os
import pandas as pd

def generate_excel_summary(csv_file: str, output_excel: str):
    if not os.path.exists(csv_file):
        print(f"Error: Could not find '{csv_file}'. Please make sure it is in the same folder.")
        return

    print(f"Reading data from {csv_file}...")
    df = pd.read_csv(csv_file)
    print(f"Successfully loaded {len(df)} rows.")

    print("Generating summaries...")
    
    # Summary 1: Total Revenue by Product
    product_summary = df.groupby('Product')['Revenue'].sum().reset_index()
    product_summary = product_summary.sort_values(by='Revenue', ascending=False)
    
    # Summary 2: Total Revenue and Units by Region
    region_summary = df.groupby('Region').agg({
        'Units Sold': 'sum',
        'Revenue': 'sum'
    }).reset_index()

    # Write to Excel with multiple sheets
    print(f"Saving to {output_excel}...")
    with pd.ExcelWriter(output_excel, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Raw Data', index=False)
        product_summary.to_excel(writer, sheet_name='Product Summary', index=False)
        region_summary.to_excel(writer, sheet_name='Region Summary', index=False)
        
    print(f"✅ Success! Open '{output_excel}' in Excel to see your formatted data.")

if __name__ == "__main__":
    input_csv = "sales_data.csv"
    output_xlsx = "sales_summary.xlsx"
    generate_excel_summary(input_csv, output_xlsx)
