import streamlit as st
import os

# --- AXIOM 1.1 精準收割 ---
st.set_page_config(page_title="AXIOM 1.1", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0c0e11; color: #ffffff; text-align: center; }
    .gold-box { border: 2px solid #00ff41; padding: 25px; border-radius: 12px; background: #14171c; margin-top: 10px; }
    .target-card { background: #1d2229; padding: 18px; border-left: 5px solid #00ff41; margin: 12px 0; text-align: left; font-size: 18px; }
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 標題
st.markdown("<h1 style='letter-spacing: 10px;'>AXIOM 1.1</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #00ff41; font-weight: bold;'>● 核心算力已鎖定：今日最強三箭</p>", unsafe_allow_html=True)

# --- 第一層：誘餌 (FOMO) ---
st.markdown("""
<div class='target-card'>🎯 標 A：23** <span style='float: right; color: #00ff41;'>預計漲幅 +7%</span></div>
<div class='target-card'>🎯 標 B：62** <span style='float: right; color: #00ff41;'>大戶掃貨 89%</span></div>
<div class='target-card'>🎯 標 C：30** <span style='float: right; color: #ff4141;'>主力洗盤結束</span></div>
""", unsafe_allow_html=True)

# --- 第二層：暴力入金區 (移除多餘輸入框) ---
st.markdown("<div class='gold-box'>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #00ff41; margin-top: 0;'>🔑 掃碼解鎖完整代碼</h2>", unsafe_allow_html=True)
st.markdown("<p style='color: #ffffff;'>單次授權費：NT$ 100</p>", unsafe_allow_html=True)

# 自動偵測圖片
valid_exts = ('.jpg', '.jpeg', '.png', '.JPG', '.PNG')
files = [f for f in os.listdir('.') if f.lower().endswith(valid_exts) and f != 'app.py']

if files:
    st.image(files[0], width=320)
else:
    st.error("系統正在載入收款碼...")

st.markdown("<p style='font-size: 14px; color: #888; margin-top: 15px;'>支付成功後算力將自動啟動</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- 第三層：強化的頁尾 ---
st.markdown(f"""
    <br><br>
    <p style='text-align: center; color: #00ff41; font-size: 18px; letter-spacing: 4px; font-weight: bold; text-shadow: 0px 0px 15px #00ff41;'>
        AXIOM 1.1 | 讓算力為您工作
    </p>
""", unsafe_allow_html=True)
