import pandas as pd
from src.data_loader import (load_data, dataset_overview)
from src.data_cleaning import (
    clean_missing_values,
    remove_invalid_rows,
    create_features,
    save_clean_data
)
from src.analysis_sales import (
    revenue_over_time,
    revenue_by_year,
    revenue_by_week,
    revenue_by_hour,
    top_products_by_revenue
)
from src.analysis_customer_country import (
    top_customers,
    revenue_by_country,
    items_per_invoice,
    top_revenue_by_country
)
from src.visualization import (
    visualize_revenue_over_time,
    visualize_revenue_by_year,
    visualize_revenue_by_day,
    visualize_revenue_by_hour,
    visualize_top_products,
    visualize_top_customers,
    visualize_revenue_by_country,
    visualize_items_per_invoice,
    visualize_top_revenue_by_country
)

def main():
    print("START RETAIL ANALYSIS PIPELINE")
    #load data
    print("Loading data...")
    df = load_data()
    overall_info = dataset_overview(df)
    #clean data
    print("Cleaning data...")
    df = clean_missing_values(df)
    df = remove_invalid_rows(df)
    df = create_features(df)
    save_clean_data(df,"data/proccessed/online_retail_clean.csv")
    print("After cleaning:", df.shape)
    #revenue analysis
    print("Sales analysis...")
    revenue_month = revenue_over_time(df)
    revenue_year = revenue_by_year(df)
    revenue_day = revenue_by_week(df)   
    revenue_hour = revenue_by_hour(df)
    #product analysis
    print("Product analysis...")
    top_products = top_products_by_revenue(df, n=10)
    #country and customer
    print("Customer & country analysis...")
    top_cust = top_customers(df, n=10)
    revenue_country = revenue_by_country(df)
    items_invoice = items_per_invoice(df)
    top_country = top_revenue_by_country(df, n=5)
    #visualization
    print("Generating visualizations...")
    visualize_revenue_over_time(revenue_month)
    visualize_revenue_by_year(revenue_year)
    visualize_revenue_by_day(revenue_day)
    visualize_revenue_by_hour(revenue_hour)
    visualize_top_products(top_products, n=10)
    visualize_top_customers(top_cust, n=10)
    visualize_revenue_by_country(revenue_country, top_n=10)
    visualize_items_per_invoice(items_invoice)
    visualize_top_revenue_by_country(top_country, n=5)

if __name__ == "__main__":
    main()
