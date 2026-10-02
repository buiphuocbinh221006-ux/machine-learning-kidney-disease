import os
import streamlit as st
import pandas as pd
import numpy as np
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
DATA_PATH = os.path.join(os.path.dirname(__file__), 'outputs', 'test_data.pkl')
DT_IMG_PATH = os.path.join(os.path.dirname(__file__), 'outputs', 'decision_tree_structure.png')
FI_IMG_PATH = os.path.join(os.path.dirname(__file__), 'outputs', 'feature_importance.png')

@st.cache_resource
def load_model():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    return None

model = load_model()

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
    st.title("HỆ THỐNG AI Y TẾ")
    st.markdown("**Đồ án Học Máy: Chẩn đoán Bệnh Thận Mạn (CKD)**")
    st.info("🎯 **Mô hình triển khai:** LightGBM (Tuned)\n\n📊 **Độ chính xác (Accuracy):** 98.75%\n\n🔬 **Kỹ thuật tối ưu:** 5-Fold Cross Validation")
    
    st.markdown("---")
    st.subheader("⚡ Nạp Dữ Liệu Nhanh (Demo Preset)")
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        if st.button("🔴 Ca Suy Thận", use_container_width=True):
            set_preset(PRESET_CKD)
            st.rerun()
    with col_p2:
        if st.button("🟢 Ca Khỏe Mạnh", use_container_width=True):
            set_preset(PRESET_NORMAL)
            st.rerun()

    st.markdown("---")
    st.caption("👨‍💻 **Thành viên thực hiện:**\n- TV1: Data Analyst & Thống kê\n- TV2: Core ML Engineer (Tree Models)\n- TV3: AI Evaluator & XAI")

# ================= MAIN PAGE =================
st.title("🩺 Ứng Dụng Hỗ Trợ Chẩn Đoán Bệnh Thận Mạn Tính")
st.markdown("Nhập các chỉ số xét nghiệm huyết học và sinh hóa của bệnh nhân để mô hình AI đưa ra chẩn đoán tiên lượng tức thì.")

tab1, tab2, tab3 = st.tabs(["📋 Nhập Chỉ Số & Chẩn Đoán", "📊 Trực Quan Hóa Mô Hình (XAI)", "ℹ️ Giới Thiệu & Báo Cáo"])

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
        htn_choice = st.selectbox("Tiền sử tăng huyết áp (htn)?", ["Không (0)", "Có (1)"], index=int(curr.get("htn", 0)))
        dm_choice = st.selectbox("Tiền sử đái tháo đường (dm)?", ["Không (0)", "Có (1)"], index=int(curr.get("dm", 0)))
        
    with col3:
        st.markdown("##### 🔬 Nước Tiểu & Bệnh Lý Kèm Theo")
        sg = st.number_input("Mã tỷ trọng nước tiểu (sg: 0-4)", min_value=0, max_value=4, value=int(curr.get("sg", 2)))
        al = st.number_input("Mức Albumin niệu (al: 0-5)", min_value=0, max_value=5, value=int(curr.get("al", 0)))
        su = st.number_input("Mức Đường niệu (su: 0-5)", min_value=0, max_value=5, value=int(curr.get("su", 0)))
        rbc = st.selectbox("Hồng cầu trong nước tiểu (rbc)", ["Bình thường (1)", "Bất thường (0)"], index=1 if curr.get("rbc", 1.0) == 1.0 else 0)
        pc = st.selectbox("Bạch cầu trong nước tiểu (pc)", ["Bình thường (1)", "Bất thường (0)"], index=1 if curr.get("pc", 1.0) == 1.0 else 0)
        pcc = st.selectbox("Cụm tế bào mủ (pcc)", ["Không có (0)", "Có (1)"], index=int(curr.get("pcc", 0)))
        ba = st.selectbox("Vi khuẩn trong nước tiểu (ba)", ["Không có (0)", "Có (1)"], index=int(curr.get("ba", 0)))
        pe = st.selectbox("Phù chân / ngoại biên (pe)", ["Không phù (0)", "Có phù (1)"], index=int(curr.get("pe", 0)))
        ane = st.selectbox("Biểu hiện thiếu máu (ane)", ["Bình thường (1)", "Thiếu máu (2)"], index=0 if curr.get("ane", 1.0) == 1.0 else 1)
        cad = curr.get("cad", 1.0)
        appet = curr.get("appet", 0.0)

    st.markdown("---")
    
    # Nút bấm dự đoán
    if st.button("🚀 TIẾN HÀNH CHẨN ĐOÁN NGAY", type="primary", use_container_width=True):
        if model is None:
            st.error("❌ Không tìm thấy file mô hình `best_model.pkl` trong thư mục `outputs/`!")
        else:
            # Thu thập dữ liệu input theo đúng 24 cột
            htn_val = 1.0 if "Có" in htn_choice else 0.0
            dm_val = 1.0 if "Có" in dm_choice else 0.0
            rbc_val = 1.0 if "Bình thường" in rbc else 0.0
            pc_val = 1.0 if "Bình thường" in pc else 0.0
            pcc_val = 1.0 if "Có" in pcc else 0.0
            ba_val = 1.0 if "Có" in ba else 0.0
            pe_val = 1.0 if "Có phù" in pe else 0.0
            ane_val = 2.0 if "Thiếu máu" in ane else 1.0

            input_dict = {
                'age': float(age), 'bp': float(bp), 'sg': float(sg), 'al': float(al), 'su': float(su),
                'rbc': float(rbc_val), 'pc': float(pc_val), 'pcc': float(pcc_val), 'ba': float(ba_val),
                'bgr': float(bgr), 'bu': float(bu), 'sc': float(sc), 'sod': float(sod), 'pot': float(pot),
                'hemo': float(hemo), 'pcv': float(pcv), 'wbcc': float(wbcc), 'rbcc': float(rbcc),
                'htn': float(htn_val), 'dm': float(dm_val), 'cad': float(cad),
                'appet': float(appet), 'pe': float(pe_val), 'ane': float(ane_val)
            }
            
            input_df = pd.DataFrame([input_dict])
            
            # Dự đoán
            pred = model.predict(input_df)[0]
            probas = model.predict_proba(input_df)[0]
            
            # Ghi nhớ quy ước: class 0 = CKD (Có bệnh), class 1 = NotCKD (Khỏe mạnh)
            proba_ckd = probas[0]
            proba_normal = probas[1]
            
            st.markdown("### 📋 KẾT QUẢ TIÊN LƯỢNG LÂM SÀNG")
            
            if pred == 0:  # Có bệnh
                st.error(f"""
                ### ⚠️ NGUY CƠ CAO MẮC BỆNH THẬN MẠN TÍNH (CKD - Chronic Kidney Disease)
                * **Độ tin cậy của chẩn đoán (Confidence Score):** `{proba_ckd * 100:.2f}%`
                * **Cảnh báo chỉ số bất thường:** Huyết sắc tố (Hemo: {hemo} g/dL), Creatinine máu (SC: {sc} mg/dL).
                * **Khuyến nghị lâm sàng:** Đề nghị chuyển bệnh nhân đến chuyên khoa Thận - Tiết niệu để làm xét nghiệm đo độ lọc cầu thận (eGFR) và siêu âm hệ tiết niệu khẩn cấp.
                """)
            else:  # Khỏe mạnh
                st.success(f"""
                ### ✅ BỆNH NHÂN KHÔNG CÓ DẤU HIỆU BỆNH THẬN MẠN TÍNH (BÌNH THƯỜNG)
                * **Độ tin cậy của chẩn đoán:** `{proba_normal * 100:.2f}%`
                * **Đánh giá:** Các chỉ số sinh hóa và chức năng lọc của cầu thận nằm trong giới hạn cho phép.
                * **Khuyến nghị:** Duy trì lối sống lành mạnh, uống đủ nước và kiểm tra sức khỏe định kỳ mỗi 6 - 12 tháng.
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
    st.subheader("🔍 Trực Quan Hóa Cấu Trúc Mô Hình & Độ Quan Trọng Đặc Trưng")
    st.markdown("Giúp bác sĩ hiểu rõ tại sao mô hình AI lại đưa ra quyết định chẩn đoán (Giải thích được - Explainable AI).")
    
    col_v1, col_v2 = st.columns([1, 1])
    
    with col_v1:
        st.markdown("##### 🌳 1. Cấu trúc Cây Quyết định (Decision Tree Structure)")
        if os.path.exists(DT_IMG_PATH):
            st.image(DT_IMG_PATH, caption="Biểu đồ cây trích xuất luật IF-ELSE (Chương 5.2)", use_container_width=True)
        else:
            st.warning("Chưa tìm thấy file ảnh `decision_tree_structure.png`")
            
    with col_v2:
        st.markdown("##### 📊 2. Xếp hạng độ quan trọng đặc trưng (Feature Importance)")
        if os.path.exists(FI_IMG_PATH):
            st.image(FI_IMG_PATH, caption="Top đặc trưng ảnh hưởng nhiều nhất đến chẩn đoán (Chương 5.3)", use_container_width=True)
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
    st.success("🏆 Mô hình LightGBM (Tuned) của TV2 được chọn làm Backbone cho Web App nhờ đạt Test Accuracy xuất sắc: 98.75%!")
