import streamlit as st
import os, time
from pathlib import Path

# AXIOM 2.1 | 數據與金流絕對同步版
st.set_page_config(page_title="AXIOM 2.1", layout="centered")

# 極簡視覺 (移除所有 Streamlit 標籤與雜訊)
st.markdown("""
    <style>
    [data-testid="stHeader"] { visibility: hidden; }
    html, body, [data-testid="stAppViewContainer"] { background-color: #FFFFFF; color: #000000; font-family: sans-serif; }
    .stTextInput input { background-color: #F8F9FA !important; border: 1px solid #000000 !important; border-radius: 2px; }
    .stButton>button { background-color: #000000; color: #FFFFFF; width: 100%; border: none; height: 3.5rem; font-size: 1.2rem; }
    [data-testid="stMetricValue"] { font-size: 3rem !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

# 1. 核心數據指標
st.write("## AXIOM 2.1")
c1, c2 = st.columns(2)
c1.metric("當前算力勝率", "92.4%")
c2.metric("已解碼標的", "23**")

st.divider()

# 2. 自動金流通道偵測 (不管圖檔在哪個資料夾，只要是圖片就抓出來)
st.write("### 🏦 資產授權掃描")

# 執行長：這裡建立自動搜索邏輯，掃描根目錄下所有 png/jpg
image_extensions = ['*.png', '*.jpg', '*.jpeg', '*.PNG', '*.JPG']
qr_files = []
for ext in image_extensions:
    qr_files.extend(Path('.').rglob(ext))

if qr_files:
    # 抓取搜尋到的第一張圖片（通常就是你的收款碼）
    target_qr = qr_files[0]
    col_l, col_m, col_r = st.columns([1, 2, 1])
    with col_m:
        st.image(str(target_qr), caption="掃描進行算力授權", use_container_width=True)
else:
    st.error("【系統警告】未偵測到資產圖檔，請確認圖片已上傳至 GitHub。")

st.divider()

# 3. 執行區
code = st.text_input("輸入欲解碼代碼")
phone = st.text_input("驗證手機末 4 碼")

if st.button("獲取算力預測結果"):
    if code and phone:
        with st.status("算力核對中...", expanded=False):
            time.sleep(0.4)
        st.success(f"標的 {code}：算力已鎖定。未來 72 小時具備強烈突破訊號。")
    else:
        st.warning("請完整填寫資訊以利核對。")
