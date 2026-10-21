# Từ điển dữ liệu

Tài liệu này mô tả 24 biến đầu vào và biến mục tiêu trong `data/clean_KidneyDisease_data.csv` (397 dòng, 25 cột). Tên và ý nghĩa biến được đối chiếu với mô tả bộ Chronic Kidney Disease của [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/336/chronic+kidney+disease).

## Biến đầu vào

| Cột trong CSV | Ý nghĩa | Kiểu/đơn vị theo mô tả bộ dữ liệu | Ghi chú về CSV hiện tại |
|---|---|---|---|
| `age` | Tuổi | Số, năm | Giá trị số trong dữ liệu đã xử lý. |
| `bp` | Huyết áp | Số, mmHg | Bộ dữ liệu mô tả là blood pressure; không tự suy diễn thành chỉ số tâm thu/tâm trương nếu chưa xác nhận từ nguồn xử lý. |
| `sg` | Tỷ trọng riêng của nước tiểu (specific gravity) | Mức phân loại thứ bậc | CSV có mã nguyên 0–4; ánh xạ các mã về giá trị gốc (ví dụ 1.005–1.025) chưa có trong project. |
| `al` | Albumin niệu | Mức phân loại 0–5 | CSV có các mức nguyên 0–5. |
| `su` | Đường niệu | Mức phân loại 0–5 | CSV có các mức nguyên 0–5. |
| `rbc` | Hồng cầu trong nước tiểu | Phân loại: bình thường/bất thường trong dữ liệu gốc | CSV có mã 0–1; chưa tìm thấy bảng ánh xạ mã trong project. |
| `pc` | Tế bào mủ trong nước tiểu | Phân loại: bình thường/bất thường trong dữ liệu gốc | CSV có mã 0–1; chưa tìm thấy bảng ánh xạ mã trong project. |
| `pcc` | Cụm tế bào mủ | Phân loại: có/không có trong dữ liệu gốc | CSV có mã 0–1; chưa tìm thấy bảng ánh xạ mã trong project. |
| `ba` | Vi khuẩn trong nước tiểu | Phân loại: có/không có trong dữ liệu gốc | CSV có mã 0–1; chưa tìm thấy bảng ánh xạ mã trong project. |
| `bgr` | Đường huyết ngẫu nhiên | Số, mg/dL | Giá trị số trong dữ liệu đã xử lý. |
| `bu` | Ure máu | Số, mg/dL | Giá trị số trong dữ liệu đã xử lý. |
| `sc` | Creatinine huyết thanh | Số, mg/dL | Giá trị số trong dữ liệu đã xử lý. |
| `sod` | Natri huyết thanh | Số, mEq/L | Giá trị số trong dữ liệu đã xử lý. |
| `pot` | Kali huyết thanh | Số, mEq/L | Giá trị số trong dữ liệu đã xử lý. |
| `hemo` | Hemoglobin (huyết sắc tố) | Số, g/dL | Giá trị số trong dữ liệu đã xử lý. |
| `pcv` | Thể tích khối hồng cầu (packed cell volume) | Số, % | Giá trị số trong dữ liệu đã xử lý. |
| `wbcc` | Số lượng bạch cầu (UCI ghi `wc`) | Số lượng tế bào/cumm theo bộ dữ liệu gốc | Tên cột trong CSV đã xử lý là `wbcc`. |
| `rbcc` | Số lượng hồng cầu (UCI ghi `rc`) | Triệu tế bào/cmm theo bộ dữ liệu gốc | Tên cột trong CSV đã xử lý là `rbcc`. |
| `htn` | Tăng huyết áp | Phân loại: có/không trong dữ liệu gốc | CSV có mã 0–1; chưa tìm thấy bảng ánh xạ mã trong project. |
| `dm` | Đái tháo đường | Phân loại: có/không trong dữ liệu gốc | CSV có mã 0–1; chưa tìm thấy bảng ánh xạ mã trong project. |
| `cad` | Bệnh động mạch vành | Phân loại: có/không trong dữ liệu gốc | CSV có mã 0–2, khác với hai mức mô tả trong bộ dữ liệu gốc; cần xác minh mã hóa, không tự gán nghĩa cho từng mã. |
| `appet` | Tình trạng ăn uống (appetite) | Phân loại: tốt/kém trong dữ liệu gốc | CSV có mã 0–2, khác với hai mức mô tả trong bộ dữ liệu gốc; cần xác minh mã hóa, không tự gán nghĩa cho từng mã. |
| `pe` | Phù chân (pedal edema) | Phân loại: có/không trong dữ liệu gốc | CSV có mã 0–1; chưa tìm thấy bảng ánh xạ mã trong project. |
| `ane` | Thiếu máu | Phân loại: có/không trong dữ liệu gốc | CSV có mã 0–2, khác với hai mức mô tả trong bộ dữ liệu gốc; cần xác minh mã hóa, không tự gán nghĩa cho từng mã. |

## Biến mục tiêu

| Cột | Ý nghĩa mã trong project |
|---|---|
| `class` | `0` = CKD (có bệnh thận mạn); `1` = NotCKD (không thuộc lớp CKD), theo metadata mô hình hiện lưu trong project. |

## Lưu ý khi nhập dữ liệu vào app

- CSV này đã được xử lý và mã hóa, nhưng project hiện không có script tiền xử lý hoặc bảng ánh xạ đầy đủ từ mã số về nhãn gốc. Vì vậy, các mã của `rbc`, `pc`, `pcc`, `ba`, `htn`, `dm`, `cad`, `appet`, `pe`, `ane` không được diễn giải thành “có/không”, “bình thường/bất thường” trong app cho đến khi xác nhận được quy tắc mã hóa.
- `cad`, `appet`, `ane` có ba giá trị mã (0, 1, 2) trong CSV, trong khi mô tả dữ liệu gốc nêu hai mức. Cần kiểm tra file nguồn/quy trình xử lý để biết mã thứ ba biểu thị gì.
- `sg` trong CSV có mã 0–4; không thể coi các mã đó là giá trị specific gravity gốc nếu chưa có ánh xạ.
- Các mô tả thuộc tính và đơn vị tham khảo bộ dữ liệu UCI. Chúng không thay thế hướng dẫn chuyên môn y tế.
