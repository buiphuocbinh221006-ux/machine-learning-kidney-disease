# 🩺 ĐỒ ÁN HỌC MÁY: CHẨN ĐOÁN BỆNH THẬN (CHRONIC KIDNEY DISEASE)

> **Môn học:** Học Máy (Machine Learning)  
> **Bộ dữ liệu:** [Kaggle / UCI Kidney Disease Dataset](https://www.kaggle.com/datasets/akshayksingh/kidney-disease-dataset)  
> **Ứng dụng minh họa:** Giao diện Web chẩn đoán tương tác với Streamlit

---

## 👥 Phân Công Nhiệm Vụ Thành Viên

* **Thành viên 1:** Khám phá & Trực quan dữ liệu (EDA), Xử lý khuyết thiếu (Imputation), Mã hóa biến phân loại (Encoding), Huấn luyện mô hình cơ sở (Logistic Regression, Naive Bayes).
* **Thành viên 2 (Core ML Engineer):** Phân chia tập dữ liệu Stratified (80/20), Huấn luyện nhóm mô hình Cây (Decision Tree, Random Forest, LightGBM), Tối ưu hóa siêu tham số (Hyperparameter Tuning) qua 5-Fold Cross Validation, Trích xuất cấu trúc cây & Feature Importance, Xây dựng Web Demo.
* **Thành viên 3:** Xử lý ngoại lai, Chuẩn hóa dữ liệu (Scaling), Huấn luyện KNN & SVM, Đánh giá tổng hợp ROC Curve & Giải thích mô hình bằng SHAP/LIME.

---

## 📊 Bảng Tổng Hợp Kết Quả Nhóm Mô Hình Cây (TV2)

| # | Mô hình | Kỹ thuật / Siêu tham số | Test Accuracy | Đánh giá |
|:---:|:---|:---|:---:|:---|
| 1 | **Decision Tree** | Baseline (Max Depth = 5) | **93.75%** | Mô hình cơ sở, dễ diễn giải luật |
| 2 | **Random Forest** | 100 cây mặc định | **97.50%** | Giảm thiểu Overfitting |
| 3 | **LightGBM** | Baseline | **98.75%** | Tối ưu hóa theo gradient |
| 4 | **Random Forest (Tuned)** | 5-Fold Cross Validation | **97.50%** | Độ ổn định cao |
| 5 | **LightGBM (Tuned) 🏆** | `learning_rate=0.1`, `num_leaves=20` | **98.75%** | **Xuất sắc nhất (chỉ sai 1/80 ca)** |

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
│   ├── best_model.pkl                  # Mô hình LightGBM tối ưu đã đóng gói
│   ├── test_data.pkl                   # Tập dữ liệu kiểm thử (X_test, y_test)
│   ├── decision_tree_structure.png     # Sơ đồ cây trích xuất luật lâm sàng (Chương 5.2)
│   ├── feature_importance.png          # Biểu đồ Top 15 đặc trưng quan trọng (Chương 5.3)
│   └── hyperparameter_sensitivity.png  # Biểu đồ phân tích độ nhạy siêu tham số (Chương 4.4)
├── app.py                              # Mã nguồn ứng dụng Web Demo (Streamlit)
├── main.ipynb                          # File Jupyter Notebook chính của TV2
├── requirements.txt                    # Danh sách thư viện Python phụ thuộc
├── .gitignore                          # Cấu hình bỏ qua file rác
└── README.md                           # Tài liệu giới thiệu dự án
```
