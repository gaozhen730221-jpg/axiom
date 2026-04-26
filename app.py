import streamlit as st
import os

# --- 1.1 極致簡約視覺 ---
st.set_page_config(page_title="AXIOM 1.1", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0c0e11; color: #ffffff; text-align: center; }
    .gold-box { border: 2px solid #00ff41; padding: 20px; border-radius: 10px; background: #14171c; margin-top: 10px; }
    .target-card { background: #1d2229; padding: 15px; border-left: 5px solid #00ff41; margin: 10px 0; text-align: left; font-size: 18px; }
    </style>
""", unsafe_allow_html=True)

# 標題
st.markdown("<h1 style='letter-spacing: 8px;'>AXIOM 1.1</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #00ff41;'>算力已鎖定：今日必賺三箭</p>", unsafe_allow_html=True)

# --- 第一層：誘餌 (直接給看一半，誘發 FOMO) ---
st.markdown("""
<div class='target-card'>🎯 潛力 A：23** <span style='float: right; color: #00ff41;'>預計漲幅 +7%</span></div>
<div class='target-card'>🎯 潛力 B：62** <span style='float: right; color: #00ff41;'>大戶掃貨 89%</span></div>
<div class='target-card'>🎯 潛力 C：30** <span style='float: right; color: #00ff41;'>主力洗盤結束</span></div>
""", unsafe_allow_html=True)

# --- 第二層：直接入金 (傻瓜式操作) ---
st.markdown("<div class='gold-box'>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #00ff41; margin-bottom: 0;'>🔑 掃碼解鎖完整代碼</h2>", unsafe_allow_html=True)
st.markdown("<p style='color: #888;'>單次授權費：NT$ 100</p>", unsafe_allow_html=True)

# 自動抓取圖檔
img_files = [f for f in os.listdir('.') if f.lower().endswith(('.png', '.jpg', '.jpeg')) and f != 'app.py']
if img_files:
    st.image(img_files[0], width=300)
else:
    st.error("圖檔讀取中...請重整網頁")

st.markdown("<p style='font-size: 14px; color: #555;'>付費後系統自動跳轉明牌頁面</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# 頁尾
st.markdown("<br><p style='color: #222;'>AXIOM 1.1 | 讓算力為您工作</p>", unsafe_allow_html=True)
