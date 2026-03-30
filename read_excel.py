import pandas as pd
import json

file_path = r'c:\Users\Axioo Pongo\Documents\Antigravity\quick_html\LKE Penilaian Desa Cantik 2026.xlsx'
try:
    xl = pd.ExcelFile(file_path)
    print(f"Sheet names: {xl.sheet_names}")
    for sheet in xl.sheet_names:
        print(f"\n--- Sheet: {sheet} ---")
        df = xl.parse(sheet)
        print(df.head(5).to_csv(index=False))
        # Save entire sheet to a JSON file so I can read it cleanly later
        df.to_json("lke_data.json", orient='records')
except Exception as e:
    print(f"Error: {e}")
