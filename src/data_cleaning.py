import pandas as pd
import os

def clean_missing_values(df):
    """Xử lý missing values: Loại bỏ các dòng chứa giá trị null."""
    df_clean = df.dropna()
    return df_clean

def remove_invalid_rows(df):
    """Loại bỏ Quantity <= 0, Price <= 0"""
    mask = (df['Quantity'] > 0) & (df['Price'] > 0)
    df_valid = df[mask]
    return df_valid

def create_features(df):
    """Tạo Revenue theo Year/ Month"""
    # Chuyển đổi InvoiceDate
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    
    # Tạo Revenue
    df['Revenue'] = df['Quantity'] * df['Price']
    
    # Tạo Year, Month
    df['Year'] = df['InvoiceDate'].dt.year
    df['Month'] = df['InvoiceDate'].dt.month
    
    return df

def save_clean_data(df, output_path):
    """Lưu dữ liệu đã làm sạch vào đường dẫn chỉ định"""
    # Tạo thư mục cha nếu chưa tồn tại
    directory = os.path.dirname(output_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    
    df.to_csv(output_path, index=False)
    print(f"Dữ liệu đã được lưu thành công tại: {output_path}")

# --- Pipeline thực thi ---
if __name__ == "__main__":
    # Đọc dữ liệu
    df = pd.read_csv('data/processed/online_retail_II.csv')

    # Các bước xử lý
    df = clean_missing_values(df)
    df = remove_invalid_rows(df)
    df = create_features(df)

    # Lưu file vào đường dẫn yêu cầu
    output_file = 'data/processed/online_retail_clean.csv'
    save_clean_data(df, output_file)