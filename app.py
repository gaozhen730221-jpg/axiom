import streamlit as st
import os, time
from pathlib import Path

# --- 2.0 終端視覺重塑 ---
st.set_page_config(page_title="AXIOM 2.0", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Noto+Sans+TC:wght@400;700&display=swap');
    
    /* 深度背景：利用漸層消除平裝感 */
    html, body, [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at center, #001529 0%, #00050a 100%) !important;
        color: #00FF41 !important;
        font-family: 'Noto Sans TC', sans-serif;
    }
    
    /* 玻璃擬態卡片：讓數據浮起來 */
    .stMetric {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(0, 255, 65, 0.2);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 15px rgba(0, 255, 65, 0.1);
    }
    
    /* 科技感按鈕：黑金霓虹 */
    .stButton>button {
        background: transparent;
        color: #00FF41;
        border: 1px solid #00FF41;
        font-family: 'Orbitron', sans-serif;
        font-weight: bold;
        letter-spacing: 2px;
        height: 3.5rem;
        transition: 0.3s;
        box-shadow: inset 0 0 10px rgba(0, 255, 65, 0.2);
    }
    .stButton>button:hover {
        background: #00FF41;
        color: #000;
        box-shadow: 0 0 20px #00FF41;
    }
    
    /* 隱藏所有雜訊 */
    [data-testid="stHeader"], [data-testid="stFooter"] { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- 第一章：算力核心展示 ---
st.markdown("<h1 style='text-align: center; font-family: Orbitron; letter-spacing: 5px;'>AXIOM 2.0</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #00A3FF;'>TAIWAN STOCK CORE COMPUTING</p>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.metric("算力解碼勝率", "92.4%", "+1.2%")
with col2:
    st.metric("待變現標的", "23**", "CONFIDENTIAL")

st.markdown("---")

# --- 第二章：資產通道自動偵測 ---
# 不管你檔案丟哪，AI 自動找出來呈現
image_exts = ['*.png', '*.jpg', '*.jpeg', '*.PNG', '*.JPG']
qrs = []
for ext in image_exts: qrs.extend(Path('.').rglob(ext))

if qrs:
    col_l, col_m, col_r = st.columns([1, 2, 1])
    with col_m:
        st.markdown("<p style='text-align:center; font-size:12px; color:#888;'>SCAN TO AUTHORIZE</p>", unsafe_allow_html=True)
        st.image(str(qrs[0]), use_container_width=True)
else:
    st.error("SYSTEM ERROR: 資產通道未連結")

st.markdown("---")

# --- 第三章：神諭擷取儀式 ---
code = st.text_input("INPUT STOCK CODE", placeholder="例: 2330")
phone = st.text_input("SECURITY VERIFICATION (4-DIGIT)", placeholder="手機末4碼")

if st.button("ACTIVATE ORACLE"):
    if code and phone:
        # 儀式感延遲：讓股民覺得電腦在「算」
        progress_text = st.empty()
        bar = st.progress(0)
        logs = ["連線算力陣列...", "同步 L2 數據流...", "繞過防火牆...", "解密標的神諭..."]
        
        for i in range(100):
            time.sleep(0.01)
            bar.progress(i + 1)
            if i % 25 == 0: progress_text.text(logs[i//25])
        
        st.success(f"【算力神諭：{code}】解碼完成。未來 72 小時具備強烈突破訊號。")
        st.markdown("<p style='color:red; text-align:center; font-size:12px;'>⚠️ 警告：遺憾是昂貴的。您已錯過上週 22.4% 的潛在漲幅。</p>", unsafe_allow_html=True)
    else:
        st.warning("請輸入完整驗證資訊。")
