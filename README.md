# CSV to Excel Summary Generator

A Python script that reads raw CSV sales data, processes it using the `pandas` library, and automatically exports a multi-sheet Excel workbook with calculated summaries.

## Windows & VS Code Setup Instructions

1. **Extract this folder** into your `Documents/Project` directory (e.g., `csv-to-excel`).
2. **Open the folder in VS Code**:
   - Open VS Code, click `File > Open Folder`, and select your new extracted folder.
3. **Open the Integrated Terminal** (`Terminal > New Terminal`).
4. **Set up your Python environment**:
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Usage
Simply run the script in your terminal:
```cmd
python csv_to_excel.py
```

The script will read the provided `sales_data.csv` and instantly generate a new file named `sales_summary.xlsx` containing your raw data alongside summarized reports.
