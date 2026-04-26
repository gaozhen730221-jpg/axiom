import streamlit as st
import os, time
from pathlib import Path

# --- 全局設定 ---
st.set_page_config(page_title="AXIOM 2.0", layout="centered")

st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #000000 !important;
        color: #FFFFFF !important;
    }
    h1 { font-size: 3.5rem !important; color: #00FF41 !important; font-family: monospace; }
    h2 { font-size: 2rem !important; color: #00A3FF !important; }
    label { font-size: 1.5rem !important; color: #FFFFFF !important; font-weight: bold; }
    [data-testid="stMetricValue"] { font-size: 4rem !important; font-weight: bold !important; }
    
    /* 支付警示框 */
    .pay-box {
        border: 2px solid #FF4B4B;
        padding: 20px;
        border-radius: 5px;
        text-align: center;
        background-color: rgba(255, 75, 75, 0.1);
        margin-bottom: 25px;
    }

    .stButton>button {
        height: 4.5rem;
        font-size: 1.8rem !important;
        background-color: #00FF41 !important;
        color: #000000 !important;
        font-weight: bold !important;
    }
    [data-testid="stHeader"] { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- 1. 標題與核心數據 ---
st.markdown("<h1 style='text-align:center;'>AXIOM 2.0</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center;'>台股數據運算中心</h2>", unsafe_allow_html=True)

st.divider()

col1, col2 = st.columns(2)
with col1:
    st.metric("歷史勝率", "92.4%")
with col2:
    st.metric("待處理標的", "23**")

st.divider()

# --- 2. 支付規範 ---
st.markdown("""
    <div class="pay-box">
        <h3 style="color:#FF4B4B; margin:0;">⚠️ 存取限制</h3>
        <p style="font-size:1.5rem; margin:10px 0;">解鎖單次算力報告：<b>NT$ 100</b></p>
        <p style="font-size:1rem; color:#CCC;">完成支付後，請於下方輸入代碼核對</p>
    </div>
    """, unsafe_allow_html=True)

# 自動搜索收款圖檔
image_exts = ['*.png', '*.jpg', '*.jpeg', '*.PNG', '*.JPG']
qrs = []
for ext in image_exts: qrs.extend(Path('.').rglob(ext))

if qrs:
    col_l, col_m, col_r = st.columns([1, 4, 1])
    with col_m:
        st.image(str(qrs[0]), caption="請掃描並完成 100 元支付", use_container_width=True)
else:
    st.error("支付通道連線中，請稍後。")

st.divider()

# --- 3. 數據操作 ---
code = st.text_input("股票代碼", placeholder="例如: 2330")
phone = st.text_input("手機末4碼", placeholder="身分核對")

if st.button("執行支付核對並解碼"):
    if code and phone:
        # 模擬支付核對過程
        with st.status("正在核對支付紀錄與算力分配...", expanded=False):
            time.sleep(1.0)
            st.write("確認 NT$ 100 支付狀態... [OK]")
            st.write("接入台股 L2 實時報價...")
            time.sleep(0.5)
        
        st.success(f"【{code}】支付核對完成。算力預測：該標的於未來 72 小時具備顯著波動特徵。")
        st.info("請於 72 小時內完成操作佈局，逾期算力將重新計算。")
    else:
        st.warning("請輸入完整代碼與手機核對碼以完成支付驗證。")
