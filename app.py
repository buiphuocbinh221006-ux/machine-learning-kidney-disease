import os
import json
import streamlit as st
import pandas as pd
import joblib

# Cấu hình giao diện Streamlit
st.set_page_config(
    page_title="Chẩn Đoán Bệnh Thận Mạn (CKD) - AI Assistant",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Đường dẫn tài nguyên
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'outputs', 'best_model.pkl')
METADATA_PATH = os.path.join(os.path.dirname(__file__), 'outputs', 'model_metadata.json')
DT_IMG_PATH = os.path.join(os.path.dirname(__file__), 'outputs', 'decision_tree_structure.png')
FI_IMG_PATH = os.path.join(os.path.dirname(__file__), 'outputs', 'feature_importance.png')

def load_model():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    return None

def load_metadata():
    if os.path.exists(METADATA_PATH):
        with open(METADATA_PATH, encoding='utf-8') as metadata_file:
            return json.load(metadata_file)
    return None

metadata = load_metadata()
model = load_model() if metadata else None

# Dữ liệu mẫu cài đặt sẵn (Preset)
PRESET_CKD = {
    "age": 53.0, "bp": 90.0, "sg": 2.0, "al": 2.0, "su": 0.0,
    "rbc": 1.0, "pc": 1.0, "pcc": 0.0, "ba": 0.0,
    "bgr": 150.0, "bu": 55.0, "sc": 3.5, "sod": 135.0, "pot": 4.8,
    "hemo": 9.8, "pcv": 30.0, "wbcc": 6500.0, "rbcc": 3.4,
    "htn": 1.0, "dm": 1.0, "cad": 1.0, "appet": 2.0, "pe": 1.0, "ane": 2.0
}

PRESET_NORMAL = {
    "age": 28.0, "bp": 75.0, "sg": 3.0, "al": 0.0, "su": 0.0,
    "rbc": 1.0, "pc": 1.0, "pcc": 0.0, "ba": 0.0,
    "bgr": 92.0, "bu": 28.0, "sc": 0.9, "sod": 142.0, "pot": 4.0,
    "hemo": 15.2, "pcv": 45.0, "wbcc": 7200.0, "rbcc": 5.2,
    "htn": 0.0, "dm": 0.0, "cad": 1.0, "appet": 0.0, "pe": 0.0, "ane": 1.0
}

# Quản lý state cho form nhập liệu
if 'form_data' not in st.session_state:
    st.session_state['form_data'] = PRESET_NORMAL.copy()

def set_preset(preset_dict):
    st.session_state['form_data'] = preset_dict.copy()

# ================= SIDEBAR =================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2864/2864380.png", width=90)
    st.title("DEMO HỌC MÁY")
    st.markdown("**Đồ án Học Máy: Chẩn đoán Bệnh Thận Mạn (CKD)**")
    if metadata:
        st.info(
            f"🎯 **Mô hình:** {metadata['model_name']}\n\n"
            f"📊 **CV Balanced Accuracy:** {metadata['cv_balanced_accuracy_mean']:.3f} "
            f"(± {metadata['cv_balanced_accuracy_std']:.3f})\n\n"
            f"🔬 **Test Accuracy:** {metadata['test_accuracy']:.3f}\n\n"
            f"🩺 **Test Recall CKD:** {metadata['test_recall_ckd_class_0']:.3f}"
        )
    else:
        st.info("Chạy toàn bộ `main.ipynb` để tạo mô hình và metadata của lần huấn luyện hiện tại.")
    
    st.markdown("---")
    st.subheader("⚡ Nạp Dữ Liệu Nhanh (Demo Preset)")
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        if st.button("🧪 Mẫu minh họa A", use_container_width=True):
            set_preset(PRESET_CKD)
            st.rerun()
    with col_p2:
        if st.button("🧪 Mẫu minh họa B", use_container_width=True):
            set_preset(PRESET_NORMAL)
            st.rerun()

    st.markdown("---")
    st.caption("👨‍💻 **Thành viên thực hiện:**\n- TV1: Data Analyst & Thống kê\n- TV2: Core ML Engineer (Tree Models)\n- TV3: AI Evaluator & XAI")

# ================= MAIN PAGE =================
st.title("🩺 Demo phân loại dữ liệu bệnh thận mạn")
st.warning("Đồ án học thuật, không phải công cụ chẩn đoán hay tư vấn y tế. Các xác suất mô hình chưa được hiệu chuẩn lâm sàng.")
st.markdown("Nhập các đặc trưng đã được mã hóa theo đúng quy ước của bộ dữ liệu đã xử lý để xem đầu ra minh họa của mô hình.")

tab1, tab2, tab3 = st.tabs(["📋 Đầu vào & Kết quả mô hình", "📊 Trực quan mô hình", "ℹ️ Giới thiệu"])

with tab1:
    st.subheader("1. Thông tin xét nghiệm của bệnh nhân")
    
    col1, col2, col3 = st.columns(3)
    curr = st.session_state['form_data']
    
    with col1:
        st.markdown("##### 🩸 Nhóm Huyết Học & Thể Trạng")
        age = st.number_input("Tuổi (age)", min_value=1.0, max_value=120.0, value=float(curr.get("age", 45.0)), step=1.0)
        bp = st.number_input("Huyết áp tâm trương (bp - mmHg)", min_value=40.0, max_value=200.0, value=float(curr.get("bp", 80.0)), step=5.0)
        hemo = st.number_input("Huyết sắc tố (hemo - g/dL) [Quan trọng]", min_value=2.0, max_value=20.0, value=float(curr.get("hemo", 12.5)), step=0.1)
        pcv = st.number_input("Dung tích hồng cầu (pcv - %)", min_value=5.0, max_value=60.0, value=float(curr.get("pcv", 38.0)), step=1.0)
        rbcc = st.number_input("Số lượng hồng cầu (rbcc - triệu/mcL)", min_value=1.0, max_value=10.0, value=float(curr.get("rbcc", 4.5)), step=0.1)
        wbcc = st.number_input("Số lượng bạch cầu (wbcc - tế bào/mcL)", min_value=1000.0, max_value=30000.0, value=float(curr.get("wbcc", 7500.0)), step=100.0)
        
    with col2:
        st.markdown("##### 🧪 Nhóm Sinh Hóa Máu & Điện Giải")
        bgr = st.number_input("Đường huyết lúc đói (bgr - mg/dL)", min_value=30.0, max_value=500.0, value=float(curr.get("bgr", 120.0)), step=1.0)
        bu = st.number_input("Ure máu (bu - mg/dL)", min_value=1.0, max_value=400.0, value=float(curr.get("bu", 45.0)), step=1.0)
        sc = st.number_input("Creatinine huyết thanh (sc - mg/dL) [Vàng]", min_value=0.1, max_value=80.0, value=float(curr.get("sc", 1.2)), step=0.1)
        sod = st.number_input("Natri máu (sod - mEq/L)", min_value=50.0, max_value=180.0, value=float(curr.get("sod", 138.0)), step=1.0)
        pot = st.number_input("Kali máu (pot - mEq/L)", min_value=1.0, max_value=15.0, value=float(curr.get("pot", 4.3)), step=0.1)

    with col3:
        st.markdown("##### 🔬 Nước Tiểu & Bệnh Lý Kèm Theo")
        sg = st.number_input("Mã tỷ trọng nước tiểu (sg: 0-4)", min_value=0, max_value=4, value=int(curr.get("sg", 2)))
        al = st.number_input("Mức Albumin niệu (al: 0-5)", min_value=0, max_value=5, value=int(curr.get("al", 0)))
        su = st.number_input("Mức Đường niệu (su: 0-5)", min_value=0, max_value=5, value=int(curr.get("su", 0)))
        st.caption("Các biến phân loại hiển thị theo mã số trong CSV đã xử lý. Đối chiếu data dictionary của TV1 trước khi diễn giải.")
        rbc = st.selectbox("Mã rbc", [0, 1], index=int(curr.get("rbc", 1)))
        pc = st.selectbox("Mã pc", [0, 1], index=int(curr.get("pc", 1)))
        pcc = st.selectbox("Mã pcc", [0, 1], index=int(curr.get("pcc", 0)))
        ba = st.selectbox("Mã ba", [0, 1], index=int(curr.get("ba", 0)))
        pe = st.selectbox("Mã pe", [0, 1], index=int(curr.get("pe", 0)))
        htn = st.selectbox("Mã htn", [0, 1], index=int(curr.get("htn", 0)))
        dm = st.selectbox("Mã dm", [0, 1], index=int(curr.get("dm", 0)))
        cad = st.selectbox("Mã cad", [0, 1, 2], index=int(curr.get("cad", 1)))
        appet = st.selectbox("Mã appet", [0, 1, 2], index=int(curr.get("appet", 0)))
        ane = st.selectbox("Mã ane", [0, 1, 2], index=int(curr.get("ane", 1)))

    st.markdown("---")
    
    # Nút bấm dự đoán
    if st.button("🚀 Chạy demo phân loại", type="primary", use_container_width=True):
        if model is None:
            st.error("Chưa có mô hình gắn với metadata của lần chạy mới. Chạy toàn bộ `main.ipynb` rồi khởi động lại ứng dụng.")
        else:
            # Thu thập dữ liệu input theo đúng 24 cột đã mã hóa
            input_dict = {
                'age': float(age), 'bp': float(bp), 'sg': float(sg), 'al': float(al), 'su': float(su),
                'rbc': float(rbc), 'pc': float(pc), 'pcc': float(pcc), 'ba': float(ba),
                'bgr': float(bgr), 'bu': float(bu), 'sc': float(sc), 'sod': float(sod), 'pot': float(pot),
                'hemo': float(hemo), 'pcv': float(pcv), 'wbcc': float(wbcc), 'rbcc': float(rbcc),
                'htn': float(htn), 'dm': float(dm), 'cad': float(cad),
                'appet': float(appet), 'pe': float(pe), 'ane': float(ane)
            }
            
            input_df = pd.DataFrame([input_dict])
            if hasattr(model, 'feature_names_in_'):
                input_df = input_df.reindex(columns=model.feature_names_in_)
            
            # Dự đoán
            pred = model.predict(input_df)[0]
            probas = model.predict_proba(input_df)[0]
            probability_by_class = dict(zip(model.classes_, probas))
            proba_ckd = float(probability_by_class.get(0, 0.0))
            proba_normal = float(probability_by_class.get(1, 0.0))

            st.markdown("### Đầu ra của mô hình")
            st.write(f"Nhãn dự đoán đã mã hóa: **{pred}**")
            
            if pred == 0:  # Có bệnh
                st.error(f"""
                Mô hình gán mẫu vào lớp **CKD (class 0)**.
                Xác suất đầu ra của mô hình: `{proba_ckd * 100:.2f}%` (chưa hiệu chuẩn lâm sàng).
                """)
            else:  # Khỏe mạnh
                st.success(f"""
                Mô hình gán mẫu vào lớp **NotCKD (class 1)**.
                Xác suất đầu ra của mô hình: `{proba_normal * 100:.2f}%` (chưa hiệu chuẩn lâm sàng).
                """)
                
            # Thanh tiến trình thể hiện xác suất
            col_b1, col_b2 = st.columns(2)
            with col_b1:
                st.metric("Xác suất mắc bệnh CKD", f"{proba_ckd*100:.2f}%")
                st.progress(float(proba_ckd))
            with col_b2:
                st.metric("Xác suất bình thường", f"{proba_normal*100:.2f}%")
                st.progress(float(proba_normal))

with tab2:
    if not metadata:
        st.warning("Các hình hiện có thuộc lần chạy cũ. Chạy toàn bộ `main.ipynb` để cập nhật mô hình và biểu đồ trước khi xem.")
    else:
        st.subheader("🔍 Cấu trúc mô hình & độ quan trọng đặc trưng")
        st.markdown("Các biểu đồ minh họa mô hình đã chọn và cách mô hình xếp hạng đặc trưng; chúng không chứng minh quan hệ nhân quả.")
    
        col_v1, col_v2 = st.columns([1, 1])
    
        with col_v1:
            st.markdown("##### 🌳 Cấu trúc Decision Tree")
            if os.path.exists(DT_IMG_PATH):
                st.image(DT_IMG_PATH, caption="Cây baseline được cắt ở độ sâu hiển thị 3.", use_container_width=True)
            else:
                st.warning("Chưa tìm thấy file ảnh `decision_tree_structure.png`")
            
        with col_v2:
            st.markdown("##### 📊 Feature Importance")
            if os.path.exists(FI_IMG_PATH):
                st.image(FI_IMG_PATH, caption="Top đặc trưng được mô hình đã chọn xếp hạng.", use_container_width=True)
            else:
                st.warning("Chưa tìm thấy file ảnh `feature_importance.png`")

with tab3:
    st.subheader("📖 Thông Tin Dự Án Học Máy")
    st.markdown("""
    * **Tên đề tài:** Chẩn đoán Bệnh Thận Mạn tính (Chronic Kidney Disease Classification)
    * **Bộ dữ liệu:** Kaggle / UCI Machine Learning Repository (397 mẫu bệnh nhân, 24 đặc trưng y tế).
    * **Phân bổ vai trò:**
      * **Thành viên 1:** Khám phá & Trực quan dữ liệu (EDA), Xử lý khuyết thiếu, Mã hóa biến, Mô hình Logistic Regression & Naive Bayes.
      * **Thành viên 2:** Kỹ thuật chia tập Stratified, Huấn luyện nhóm mô hình Cây (Decision Tree, Random Forest, LightGBM), Tối ưu siêu tham số & Đóng gói mô hình.
      * **Thành viên 3:** Chuẩn hóa dữ liệu (Scaling), Mô hình khoảng cách (KNN, SVM), Đánh giá tổng hợp ROC Curve & Giải thích mô hình (SHAP/LIME).
    """)
    if metadata:
        st.success(f"Mô hình đang nạp: **{metadata['model_name']}**. Chỉ số được tạo từ lần chạy notebook gần nhất.")
    else:
        st.warning("Chưa có metadata cho lần chạy hiện tại. Chạy toàn bộ notebook để cập nhật mô hình, chỉ số và ứng dụng.")
