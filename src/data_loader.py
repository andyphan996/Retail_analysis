import pandas as pd

def load_data(file_path):
    try:
        df = pd.read_csv(file_path, encoding='ISO-8859-1')
        print(f"--- Đã tải dữ liệu thành công từ {file_path} ---")
        return df
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
        return None

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

    print("\n=== TỔNG QUAN DỮ LIỆU ===")
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
    path = "data/processed/online_retail_II.csv"
    df = load_data(path)
    if df is not None:
        overview = dataset_overview(df)