# 🩺 ĐỒ ÁN HỌC MÁY: CHẨN ĐOÁN BỆNH THẬN (CHRONIC KIDNEY DISEASE)

> **Môn học:** Học Máy (Machine Learning)  
> **Bộ dữ liệu:** [Kaggle / UCI Kidney Disease Dataset](https://www.kaggle.com/datasets/akshayksingh/kidney-disease-dataset)  
> **Ứng dụng minh họa:** Demo phân loại Streamlit dùng cho mục đích học thuật

---

## 🌳 Phạm Vi Mô Hình

Project phân loại CKD / NotCKD bằng Decision Tree, Random Forest và LightGBM. Notebook có phân tích dữ liệu khám phá (EDA), chia tập stratified 80/20, chọn mô hình bằng 5-fold cross-validation trên tập train, đánh giá cuối trên tập test và lưu mô hình để ứng dụng Streamlit sử dụng.

---

## 📊 Kết quả nhóm mô hình cây

Notebook chọn mô hình theo **Balanced Accuracy trung bình trên 5 fold của tập train**. Tập test được giữ riêng để báo cáo đánh giá cuối và không dùng để chọn mô hình hay siêu tham số. Sau khi chạy toàn bộ notebook, bảng metrics được lưu tại `outputs/model_comparison.csv`; cấu hình mô hình và metrics của mô hình được chọn được lưu tại `outputs/model_metadata.json`.

Không ghi sẵn các con số trong README để tránh lệch với kết quả từ lần chạy mới nhất. Với bài toán này, cần đọc riêng Precision, Recall và F1 của lớp CKD (class `0`); không kết luận chỉ từ Accuracy.

---

## 🚀 Hướng Dẫn Cài Đặt & Chạy Thử Nghiệm

### 1. Clone repository về máy:
```bash
git clone https://github.com/buiphuocbinh221006-ux/machine-learning-kidney-disease.git
cd machine-learning-kidney-disease
```

### 2. Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

### 3. Xem và chạy Notebook:
Mở file `main.ipynb` trong Jupyter Notebook hoặc VS Code và bấm **Run All**.
Việc này huấn luyện lại các mô hình, cập nhật metrics, hình ảnh và metadata trong `outputs/`.

### 4. Khởi động Ứng dụng Web Demo:
```bash
streamlit run app.py
```
Trình duyệt sẽ tự động mở tại địa chỉ `http://localhost:8501`.

---

## 📁 Cấu Trúc Thư Mục Dự Án

```
├── data/
│   └── clean_KidneyDisease_data.csv    # Dữ liệu bệnh thận đã làm sạch
├── outputs/
│   ├── best_model.pkl                  # Mô hình được chọn bằng cross-validation
│   ├── model_metadata.json             # Cấu hình và metrics của lần chạy gần nhất
│   ├── model_comparison.csv            # Metrics CV và tập test cho nhóm mô hình cây
│   ├── test_data.pkl                   # Tập dữ liệu kiểm thử (X_test, y_test)
│   ├── feature_importance.png          # Biểu đồ Top 15 đặc trưng quan trọng (Chương 5.3)
│   ├── hyperparameter_sensitivity.png  # Biểu đồ phân tích độ nhạy siêu tham số (Chương 4.4)
│   ├── confusion_matrix.png             # Confusion matrix dạng heatmap
│   └── roc_curve.png                    # ROC curve và ROC-AUC trên tập test
├── app.py                              # Mã nguồn ứng dụng Web Demo (Streamlit)
├── main.ipynb                          # Notebook EDA, huấn luyện và đánh giá mô hình
├── requirements.txt                    # Danh sách thư viện Python phụ thuộc
├── .gitignore                          # Cấu hình bỏ qua file rác
└── README.md                           # Tài liệu giới thiệu dự án
```

## ⚠️ Phạm vi sử dụng

Ứng dụng Streamlit chỉ là demo học thuật trên dữ liệu đã mã hóa. Các xác suất do mô hình trả về chưa được hiệu chuẩn hoặc xác nhận lâm sàng; không dùng để chẩn đoán, sàng lọc hay quyết định điều trị. Các biến phân loại trong form nhập theo mã số của CSV đã xử lý; cần đối chiếu data dictionary trước khi diễn giải mã thành nhãn.

## 🧾 Khả năng tái lập dữ liệu

`data/clean_KidneyDisease_data.csv` là dữ liệu đã xử lý. Thư mục hiện chưa kèm dữ liệu thô, mã tạo CSV này hoặc data dictionary đầy đủ cho các mã phân loại. Trước khi chốt báo cáo, cần bổ sung nguồn và quy tắc làm sạch/mã hóa, đồng thời xác nhận mọi bước học tham số tiền xử lý chỉ dùng tập train.
