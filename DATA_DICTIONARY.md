# 📖 Data Dictionary — Tập dữ liệu Bệnh Thận Mạn Tính (CKD)

> File này giải thích ý nghĩa và quy ước mã hóa của từng biến số trong file  
> `data/clean_KidneyDisease_data.csv` sau khi TV1 đã tiền xử lý và mã hóa.

---

## Biến Mục Tiêu (Target)

| Tên cột | Kiểu | Giá trị | Ý nghĩa |
|:---|:---:|:---|:---|
| `class` | int | `0` = **CKD** (Có bệnh thận mạn tính) | Nhãn gốc `ckd` được LabelEncoder mã hóa thành `0` (alphabetical) |
| | | `1` = **NotCKD** (Khỏe mạnh) | Nhãn gốc `notckd` được mã hóa thành `1` |

> ⚠️ **Lưu ý quan trọng:** Quy ước ngược với chuẩn y tế thông thường (dương tính = 1).  
> Trong project này: **0 = Có bệnh, 1 = Khỏe**. Khi báo cáo Recall/Precision phải chỉ rõ `pos_label=0`.

---

## Nhóm 1: Chỉ số Liên Tục (Continuous)

| Tên cột | Tên đầy đủ | Đơn vị | Giá trị bình thường | Ý nghĩa lâm sàng |
|:---|:---|:---:|:---|:---|
| `age` | Age | năm | 20 – 80 | Tuổi bệnh nhân |
| `bp` | Blood Pressure | mmHg | < 80 (tâm trương) | Huyết áp tâm trương |
| `bgr` | Blood Glucose Random | mg/dL | 70 – 140 | Đường huyết bất kỳ |
| `bu` | Blood Urea | mg/dL | 10 – 45 | Ure trong máu; tăng cao khi thận suy |
| `sc` | Serum Creatinine | mg/dL | 0.6 – 1.2 | Creatinine huyết thanh; chỉ số vàng chức năng thận |
| `sod` | Sodium | mEq/L | 135 – 145 | Natri máu |
| `pot` | Potassium | mEq/L | 3.5 – 5.0 | Kali máu; tăng nguy hiểm khi thận suy |
| `hemo` | Hemoglobin | g/dL | ≥ 13.0 (nam), ≥ 12.0 (nữ) | Huyết sắc tố; giảm do thận giảm tiết EPO |
| `pcv` | Packed Cell Volume | % | 38 – 54 | Thể tích khối hồng cầu (Hematocrit) |
| `wbcc` | White Blood Cell Count | tế bào/mcL | 4,000 – 11,000 | Số lượng bạch cầu |
| `rbcc` | Red Blood Cell Count | triệu/mcL | 4.5 – 6.0 | Số lượng hồng cầu |

---

## Nhóm 2: Chỉ số Phân Hạng Nước Tiểu (Ordinal — Mã hóa số)

| Tên cột | Tên đầy đủ | Mã số | Ý nghĩa mã |
|:---|:---|:---:|:---|
| `sg` | Specific Gravity | 0 | 1.005 (loãng bất thường — thận mất khả năng cô đặc) |
| | Tỷ trọng nước tiểu | 1 | 1.010 |
| | | 2 | 1.015 |
| | | 3 | 1.020 |
| | | 4 | 1.025 (bình thường) |
| `al` | Albumin (niệu) | 0 | Không có đạm (bình thường) |
| | Đạm trong nước tiểu | 1 | Vết (trace) |
| | | 2 | +1 (nhẹ) |
| | | 3 | +2 (trung bình) |
| | | 4 | +3 (nhiều) |
| | | 5 | +4 (rất nhiều — tổn thương cầu thận nặng) |
| `su` | Sugar (niệu) | 0 | Không có đường (bình thường) |
| | Đường trong nước tiểu | 1–5 | Mức độ tăng dần (thường kèm tiểu đường) |

---

## Nhóm 3: Biến Nhị Phân (Binary — 0/1)

| Tên cột | Tên đầy đủ | Mã `0` | Mã `1` |
|:---|:---|:---|:---|
| `rbc` | Red Blood Cells (Urine) | normal (bình thường) | abnormal (bất thường — có hồng cầu trong nước tiểu) |
| `pc` | Pus Cell | normal | abnormal (có tế bào mủ) |
| `pcc` | Pus Cell Clumps | notpresent (không có) | present (có cụm tế bào mủ) |
| `ba` | Bacteria | notpresent | present (có vi khuẩn trong nước tiểu) |
| `htn` | Hypertension | no (không bị tăng huyết áp) | yes (có tiền sử tăng huyết áp) |
| `dm` | Diabetes Mellitus | no (không bị tiểu đường) | yes (có tiền sử tiểu đường) |
| `pe` | Pedal Edema | no (không phù chân) | yes (có phù chân/mắt cá chân) |

---

## Nhóm 4: Biến Đa Trị (Multi-class — 3 giá trị)

| Tên cột | Tên đầy đủ | Mã `0` | Mã `1` | Mã `2` |
|:---|:---|:---|:---|:---|
| `cad` | Coronary Artery Disease | no (không bệnh mạch vành) | yes | *(giá trị lỗi gốc — 1 mẫu do lỗi nhập liệu, giữ nguyên để không thay đổi mã hóa của TV1)* |
| `appet` | Appetite | good (ăn ngon) | poor (chán ăn) | *(giá trị lỗi gốc — 1 mẫu)* |
| `ane` | Anemia | no (không thiếu máu) | yes (có thiếu máu) | *(giá trị lỗi gốc — 1 mẫu)* |

> ℹ️ **Lưu ý `cad`, `appet`, `ane`:** 3 cột này có 1 mẫu dữ liệu có giá trị `2`  
> do lỗi gõ phím trong dữ liệu gốc (UCI). TV1 giữ nguyên thay vì loại bỏ.  
> Trong thực tế, giá trị `2` tại đây không mang ý nghĩa lâm sàng khác biệt.

---

## Nguồn gốc & Tài liệu tham khảo

- **Nguồn dữ liệu gốc:** UCI Machine Learning Repository — Chronic Kidney Disease Dataset  
  Dua, D. & Graff, C. (2019). UCI Machine Learning Repository. Irvine, CA: University of California, School of Information and Computer Science.  
  🔗 https://archive.ics.uci.edu/dataset/336/chronic+kidney+disease

- **Nguồn Kaggle:** https://www.kaggle.com/datasets/akshayksingh/kidney-disease-dataset

- **Quy trình tiền xử lý:** Thực hiện bởi TV1 (EDA, Imputation, LabelEncoding).  
  Cột `class`: dùng `sklearn.preprocessing.LabelEncoder` theo thứ tự alphabetical → `ckd=0`, `notckd=1`.
