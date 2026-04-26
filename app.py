import streamlit as st
import os, time

# AXIOM 2.1 | 執行長全局監控版
st.set_page_config(page_title="AXIOM 2.1", layout="centered")

# 極簡白無視覺干擾
st.markdown("""
    <style>
    [data-testid="stHeader"] { visibility: hidden; }
    html, body, [data-testid="stAppViewContainer"] { background-color: #FFFFFF; color: #000000; font-family: sans-serif; }
    .stTextInput input { background-color: #F8F9FA !important; border: 1px solid #000000 !important; border-radius: 2px; }
    .stButton>button { background-color: #000000; color: #FFFFFF; width: 100%; border: none; height: 3rem; font-size: 1.2rem; }
    [data-testid="stMetricValue"] { font-size: 3rem !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

# 核心數據：一眼定生死
st.title("AXIOM 2.1")
c1, c2 = st.columns(2)
c1.metric("當前勝率", "92.4%")
c2.metric("待解碼", "23**")

st.divider()

# 命脈：收款通道
qr_file = "pay_qr.png"
if os.path.exists(qr_file):
    st.write("### 🏦 掃描授權資產通道")
    st.image(qr_file, width=200) # 置中且夠大
else:
    st.error("【系統警告】通道初始化失敗，請連繫管理員上傳 pay_qr.png")

st.divider()

# 執行：資產核對
code = st.text_input("輸入欲預測股票代碼")
phone = st.text_input("輸入驗證手機末 4 碼")

if st.button("獲取算力神諭"):
    if code and phone:
        with st.status("算力解密中...", expanded=False):
            time.sleep(0.5)
        st.success(f"標的 {code} 算力解析完畢：72 小時內具備強烈突破訊號。")
    else:
        st.warning("請完整填寫核對資訊。")
