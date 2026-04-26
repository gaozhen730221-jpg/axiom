import streamlit as st
import os

# --- AXIOM 1.0 絕對純淨 ---
st.set_page_config(page_title="AXIOM 1.0", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0c0e11; color: #ffffff; text-align: center; }
    .target-card { background: #1d2229; padding: 18px; border-left: 5px solid #00ff41; margin: 10px 0; text-align: left; font-size: 18px; }
    /* 移除所有可能產生綠框的裝飾，只留收款區底色 */
    .pay-zone { padding: 20px; background: #14171c; border-radius: 12px; margin-top: 10px; }
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='letter-spacing: 10px;'>AXIOM 1.0</h1>", unsafe_allow_html=True)

# 1. 唯一查詢框 (放在最頂)
st.text_input("", placeholder="🔍 請輸入台股代碼 (例如: 2330)")

# 2. 誘餌區
st.markdown("""
<div class='target-card'>🎯 標 A：23** <span style='float: right; color: #00ff41;'>勝率 92%</span></div>
<div class='target-card'>🎯 標 B：62** <span style='float: right; color: #00ff41;'>大戶掃貨 89%</span></div>
<div class='target-card'>🎯 標 C：30** <span style='float: right; color: #ff4141;'>預警 94%</span></div>
""", unsafe_allow_html=True)

# 3. 收款區 (徹底刪除多餘框，直接噴圖)
st.markdown("<div class='pay-zone'>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #00ff41; margin-top: 0;'>💳 掃碼解鎖完整報告 (NT$ 100)</h3>", unsafe_allow_html=True)

# 抓圖邏輯
files = [f for f in os.listdir('.') if f.lower().endswith(('.png', '.jpg', '.jpeg')) and f != 'app.py']
if files:
    st.image(files[0], width=350)

st.markdown("<p style='font-size: 14px; color: #888; margin-top: 10px;'>支付成功後算力將自動啟動</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# 4. 品牌頁尾
st.markdown("<br><p style='color: #00ff41; font-size: 18px; font-weight: bold; text-shadow: 0px 0px 10px #00ff41;'>AXIOM 1.0 | 讓算力為您工作</p>", unsafe_allow_html=True)
