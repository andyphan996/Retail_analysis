import os
import matplotlib.pyplot as plt
import pandas as pd

OUTPUT_DIR = "outputs/figures"

# biểu đồ biểu đồ doanh thu theo tháng
def visualize_revenue_over_time(revenue_month):
    #tao thu muc neu khong ton tai
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    plt.figure(figsize=(12, 6))
    plt.plot(
        revenue_month['InvoiceDate'],
        revenue_month['Revenue'],
        marker='o'
    )
    plt.title("Monthly Revenue Over Time", fontsize=14)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Revenue (£)", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    # lưu hình
    output_path = os.path.join(OUTPUT_DIR, "monthly_revenue.png")
    plt.savefig(output_path)
    plt.show()

# biểu đồ doanh thu theo năm
def visualize_revenue_by_year(revenue_year):
    #tao thu muc neu khong ton tai
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    plt.figure(figsize=(8, 6))
    plt.bar(
        revenue_year['InvoiceDate'].astype(str),
        revenue_year['Revenue']
    )
    plt.title("Revenue by Year", fontsize=14)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Revenue (£)", fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    # lưu hình
    output_path = os.path.join(OUTPUT_DIR, "revenue_by_year.png")
    plt.savefig(output_path)
    plt.show()

# biểu đồ doanh thu theo ngày
def visualize_revenue_by_day(revenue_day):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    revenue_day['InvoiceDate'] = pd.to_datetime(revenue_day['InvoiceDate'])
    plt.figure(figsize=(14, 6))
    plt.plot(
        revenue_day['InvoiceDate'],
        revenue_day['Revenue']
    )
    plt.title("Daily Revenue Over Time", fontsize=14)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Revenue (£)", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    # lưu hình
    output_path = os.path.join(OUTPUT_DIR, "daily_revenue.png")
    plt.savefig(output_path)
    plt.show()

#biểu đồ doanh thu theo giờ
def visualize_revenue_by_hour(revenue_hour):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    plt.figure(figsize=(10, 6))
    plt.bar(
        revenue_hour['InvoiceDate'],
        revenue_hour['Revenue']
    )
    plt.title("Revenue by Hour of Day", fontsize=14)
    plt.xlabel("Hour (0–23)", fontsize=12)
    plt.ylabel("Revenue (£)", fontsize=12)
    plt.xticks(range(0, 24))
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    # lưu hình
    output_path = os.path.join(OUTPUT_DIR, "revenue_by_hour.png")
    plt.savefig(output_path)
    plt.show()

#biểu đồ các sản phẩm có doanh thu cao nhất
def visualize_top_products(top_products, n=10):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    plt.figure(figsize=(10, 6))
    plt.barh(
        top_products['Description'],
        top_products['Revenue']
    )
    plt.gca().invert_yaxis()  # sản phẩm doanh thu cao nhất ở trên cùng
    plt.title(f"Top {n} Products by Revenue", fontsize=14)
    plt.xlabel("Revenue (£)", fontsize=12)
    plt.ylabel("Product", fontsize=12)
    plt.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, "top_products_by_revenue.png")
    plt.savefig(output_path)
    plt.show()


#biểu đồ top khách hàng mua nhiều nhất
def visualize_top_customers(top_customers_df, n=10):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    top_customers_df['Customer ID'] = top_customers_df['Customer ID'].astype(str)
    plt.figure(figsize=(10, 6))
    plt.barh(
        top_customers_df['Customer ID'],
        top_customers_df['Revenue']
    )
    plt.gca().invert_yaxis()  # khách hàng doanh thu cao nhất ở trên cùng
    plt.title(f"Top {n} Customers by Revenue", fontsize=14)
    plt.xlabel("Revenue (£)", fontsize=12)
    plt.ylabel("Customer ID", fontsize=12)
    plt.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, "top_customers_by_revenue.png")
    plt.savefig(output_path)
    plt.show()

# biểu đồ doanh thu theo quốc gia
def visualize_revenue_by_country(rev_country, top_n=10):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    top_country = rev_country.head(top_n)
    plt.figure(figsize=(10, 6))
    plt.barh(
        top_country['Country'],
        top_country['Revenue']
    )
    plt.gca().invert_yaxis()  # quốc gia doanh thu cao nhất ở trên
    plt.title(f"Top {top_n} Countries by Revenue", fontsize=14)
    plt.xlabel("Revenue (£)", fontsize=12)
    plt.ylabel("Country", fontsize=12)
    plt.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, "revenue_by_country.png")
    plt.savefig(output_path)
    plt.show()
    
#biểu đô phân phối số lượng sản phẩm trên mỗi đơn hàng
def visualize_items_per_invoice(items_per):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    plt.figure(figsize=(10, 6))
    plt.hist(
        items_per['TotalItems'],
        bins=30
    )
    plt.title("Distribution of Items per Invoice", fontsize=14)
    plt.xlabel("Number of Items per Invoice", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, "items_per_invoice_distribution.png")
    plt.savefig(output_path)
    plt.show()


#biểu đồ top n quốc gia có doanh thu cao nhất
def visualize_top_revenue_by_country(top_country, n=5):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    plt.figure(figsize=(8, 6))
    plt.barh(
        top_country['Country'],
        top_country['Revenue']
    )
    plt.gca().invert_yaxis()  # quốc gia doanh thu cao nhất ở trên
    plt.title(f"Top {n} Countries by Revenue", fontsize=14)
    plt.xlabel("Revenue (£)", fontsize=12)
    plt.ylabel("Country", fontsize=12)
    plt.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, "top_revenue_by_country.png")
    plt.savefig(output_path)
    plt.show()
