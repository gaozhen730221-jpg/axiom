import streamlit as st
import yfinance as yf
import os

# 1. 極簡頁面設置
st.set_page_config(page_title="Axiom", page_icon="🚥")
st.markdown("<h2 style='text-align: center;'>🚥 Axiom 數據公理</h2>", unsafe_allow_html=True)

# 2. 核心成交區 (單頁完成)
col1, col2 = st.columns([1, 1])

with col1:
    st.write("### 🔍 第一步：輸入代號")
    stock_id = st.text_input("台股代碼 (如: 2330)", value="", max_chars=4)
    pwd = st.text_input("🔓 輸入解鎖口令", type="password", placeholder="請向右側領取口令")

with col2:
    st.write("### 💰 第二步：領取口令")
    # 強制讀取你給的那張 QR Code，若找不到則顯示文字備案
    img_name = "bd9a0ca4-9261-4489-b8a3-46671766ec9b.jpg"
    if os.path.exists(img_name):
        st.image(img_name, width=200)
    else:
        st.warning("請掃描 LINE Pay 轉帳 100 元")
    
    st.write("👉 **轉帳 100 元並備註代碼**")
    st.write("👉 **私訊領取口令：`8888`**")

st.divider()

# 3. 暴力輸出結果
if pwd == "8888":
    if stock_id:
        try:
            df = yf.Ticker(f"{stock_id}.TW").history(period="2d")
            now_p = df['Close'].iloc[-1]
            diff = now_p - df['Close'].iloc[-2]
            
            if diff > 0:
                st.markdown(f"<div style='background-color:#ff4b4b; color:white; padding:30px; text-align:center; border-radius:10px;'><h1>🔴 紅燈多</h1></div>", unsafe_allow_html=True)
            elif diff < 0:
                st.markdown(f"<div style='background-color:#00c853; color:white; padding:30px; text-align:center; border-radius:10px;'><h1>🟢 綠燈空</h1></div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='background-color:#888; color:white; padding:30px; text-align:center; border-radius:10px;'><h1>🟡 黃燈</h1></div>", unsafe_allow_html=True)
            st.write(f"當前價格：{now_p:.2f}")
        except:
            st.error("代碼有誤或數據讀取中")
else:
    st.info("🔒 請完成支付後輸入口令解鎖訊號")
