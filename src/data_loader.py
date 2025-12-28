import pandas as pd

import pandas as pd
from pathlib import Path

DATA_PATH = Path("data") / "raw" / "online_retail_II.xlsx"
def load_data():
    xls = pd.ExcelFile(DATA_PATH)
    df_list = []
    for sheet in xls.sheet_names:
        print(f"Loading sheet: {sheet}")
        df = pd.read_excel(xls, sheet_name=sheet)
        df["SourceSheet"] = sheet   
        df_list.append(df)

    df_all = pd.concat(df_list, ignore_index=True)
    return df_all

def dataset_overview(df):

    if df is None:
        return "DataFrame không tồn tại."

    info = {
        "num_rows": df.shape[0],
        "num_cols": df.shape[1],
        "columns": df.columns.tolist(),
        "data_types": df.dtypes.to_dict(),
        "missing_values": df.isnull().sum().to_dict()
    }
    print("\nTỔNG QUAN DỮ LIỆU ")
    print(f"Số dòng: {info['num_rows']}")
    print(f"Số cột: {info['num_cols']}")
    print("-" * 30)
    print("Danh sách cột và kiểu dữ liệu:")
    for col, dtype in info['data_types'].items():
        print(f" - {col}: {dtype}")
    print("-" * 30)
    print("Số lượng giá trị thiếu (Missing values):")
    for col, null_count in info['missing_values'].items():
        print(f" - {col}: {null_count}")

    return info

if __name__ == "__main__":
    df = load_data()
    if df is not None:
        overview = dataset_overview(df)