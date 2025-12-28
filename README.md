# Retail_analysis
## Thông tin bộ dữ liệu: Online Retail II

### 1. Lịch sử và Nguồn gốc
- **Nguồn gốc:** Bộ dữ liệu được lấy từ [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/502/online+retail+ii).
- **Bối cảnh:** Đây là bộ dữ liệu thực tế chứa toàn bộ giao dịch xảy ra trong khoảng thời gian từ 01/12/2009 đến 09/12/2011 đối với một công ty bán lẻ trực tuyến phi cửa hàng (non-store) có trụ sở tại Vương quốc Anh.

### 2. Công dụng và Mục đích
- **Công dụng:** Dùng để phân tích hành vi khách hàng, phân khúc khách hàng (RFM analysis), dự báo doanh thu, và phân tích xu hướng mua sắm.
- **Mục đích:** Giúp doanh nghiệp hiểu rõ hơn về thị trường, tối ưu hóa kho hàng và đưa ra các chiến dịch Marketing hiệu quả.

### 3. Lĩnh vực
- Thương mại điện tử (E-commerce), Bán lẻ (Retail), Phân tích kinh doanh (Business Analytics).

### 4. Danh sách các đặc trưng (Features)
1. **Invoice:** Mã hóa đơn. Nếu bắt đầu bằng 'C', đó là hóa đơn hủy.
2. **StockCode:** Mã sản phẩm (Định danh riêng cho mỗi mặt hàng).
3. **Description:** Tên hoặc mô tả sản phẩm.
4. **Quantity:** Số lượng mỗi mặt hàng trên mỗi giao dịch.
5. **InvoiceDate:** Ngày và giờ tạo hóa đơn.
6. **Price:** Đơn giá sản phẩm (Bảng Anh).
7. **Customer ID:** Mã số khách hàng (Định danh duy nhất cho mỗi khách hàng).
8. **Country:** Tên quốc gia nơi khách hàng cư trú.

### 5. Hạn chế và Khiếm khuyết
- **Dữ liệu thiếu (Missing values):** Một số lượng lớn bản ghi không có `Customer ID` (khoảng 20-25%). Một số ít thiếu `Description`.
- **Dữ liệu không hợp lệ:** Có các đơn hàng bị hủy (Invoice bắt đầu bằng 'C') và các dòng dữ liệu có số lượng (`Quantity`) hoặc đơn giá (`Price`) âm/bằng 0 do lỗi hệ thống hoặc điều chỉnh kho.
- **Nhiễu:** Có các mã StockCode không phải là hàng hóa (ví dụ: 'DOT' - Dotcom postage, 'POST' - Bưu phí).

# cài đặt và chạy
pip install openpyxl

