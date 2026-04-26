import streamlit as st
import os

# --- AXIOM 1.0 最終純淨版 ---
st.set_page_config(page_title="AXIOM 1.0", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0c0e11; color: #ffffff; text-align: center; }
    .target-card { background: #1d2229; padding: 18px; border-left: 5px solid #00ff41; margin: 10px 0; text-align: left; font-size: 18px; }
    .gold-box { border: 2px solid #00ff41; padding: 25px; border-radius: 12px; background: #14171c; margin-top: 5px; }
    /* 徹底隱藏無用元件 */
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='letter-spacing: 10px;'>AXIOM 1.0</h1>", unsafe_allow_html=True)

# 1. 唯一保留的查詢功能 (放在最上方，人家要查代碼的地方)
st.text_input("", placeholder="🔍 請輸入台股代碼 (例如: 2330)")

# 2. 誘餌區 (直接展示)
st.markdown("""
<div class='target-card'>🎯 標 A：23** <span style='float: right; color: #00ff41;'>勝率 92%</span></div>
<div class='target-card'>🎯 標 B：62** <span style='float: right; color: #00ff41;'>大戶掃貨 89%</span></div>
<div class='target-card'>🎯 標 C：30** <span style='float: right; color: #ff4141;'>預警 94%</span></div>
""", unsafe_allow_html=True)

# 3. 入金區 (廢物框已徹底刪除，直接顯示 QR Code)
st.markdown("<div class='gold-box'>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #00ff41; margin-top: 0;'>💳 掃碼解鎖完整報告 (NT$ 100)</h3>", unsafe_allow_html=True)

# 自動抓取目錄下第一張圖檔
img_files = [f for f in os.listdir('.') if f.lower().endswith(('.png', '.jpg', '.jpeg')) and f != 'app.py']
if img_files:
    st.image(img_files[0], width=350)

st.markdown("<p style='font-size: 14px; color: #888; margin-top: 10px;'>支付成功後算力將自動啟動</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# 4. 品牌頁尾
st.markdown("<br><br><p style='color: #00ff41; font-size: 18px; letter-spacing: 4px; font-weight: bold; text-shadow: 0px 0px 15px #00ff41;'>AXIOM 1.0 | 讓算力為您工作</p>", unsafe_allow_html=True)
