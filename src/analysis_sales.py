import pandas as pd
import os


def revenue_over_time(df):
    """Tính doanh thu theo tháng"""
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Revenue'] = df['UnitPrice'] * df['Quantity']
    revenue_month = df.resample('M', on='InvoiceDate')['Revenue'].sum().reset_index()
    output_path = 'outputs/tables/revenue_by_month.csv'
    revenue_month.to_csv(output_path, index=False)
    return revenue_month


def revenue_by_year(df):
    """Doanh thu theo năm"""
    revenue_year = df.groupby(df['InvoiceDate'].dt.year)['Revenue'].sum().reset_index()
    return revenue_year


def revenue_by_week(df):
    """Doanh thu theo ngày (như yêu cầu mô tả của bạn)"""
    revenue_day = df.groupby(df['InvoiceDate'].dt.date)['Revenue'].sum().reset_index()
    return revenue_day


def revenue_by_hour(df):
    """Doanh thu theo giờ"""
    revenue_hour = df.groupby(df['InvoiceDate'].dt.hour)['Revenue'].sum().reset_index()
    return revenue_hour


def top_products_by_revenue(df, n=10):
    """Top sản phẩm theo doanh thu"""
    top_products = df.groupby('Description')['Revenue'].sum().sort_values(ascending=False).head(n).reset_index()

    output_path = 'outputs/tables/top_products.csv'
    top_products.to_csv(output_path, index=False)

    return top_products