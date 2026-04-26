import streamlit as st
import os

# --- AXIOM 1.1 全軍出動版 ---
st.set_page_config(page_title="AXIOM 1.1", layout="centered")

# 極簡黑魂視覺 CSS
st.markdown("""
    <style>
    .stApp { background-color: #0c0e11; color: #ffffff; text-align: center; }
    .gold-box { border: 2px solid #00ff41; padding: 25px; border-radius: 12px; background: #14171c; margin-top: 15px; }
    .target-card { background: #1d2229; padding: 18px; border-left: 5px solid #00ff41; margin: 12px 0; text-align: left; font-size: 18px; }
    /* 強制修改頁尾連結樣式 */
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 標題區
st.markdown("<h1 style='letter-spacing: 10px; margin-bottom: 0;'>AXIOM 1.1</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #00ff41; font-weight: bold; letter-spacing: 2px;'>● 核心算力已鎖定：今日最強三箭</p>", unsafe_allow_html=True)

# --- 第一層：誘餌 (FOMO 觸發) ---
st.markdown("""
<div class='target-card'>🎯 標 A：23** <span style='float: right; color: #00ff41;'>勝率 92%</span></div>
<div class='target-card'>🎯 標 B：62** <span style='float: right; color: #00ff41;'>大戶掃貨 89%</span></div>
<div class='target-card'>🎯 標 C：30** <span style='float: right; color: #ff4141;'>預警 94%</span></div>
""", unsafe_allow_html=True)

# --- 第二層：暴力入金區 (傻瓜化) ---
st.markdown("<div class='gold-box'>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #00ff41; margin-top: 0;'>💳 掃碼解鎖完整代碼</h2>", unsafe_allow_html=True)
st.markdown("<p style='color: #ffffff; font-size: 16px;'>單次授權費用：NT$ 100</p>", unsafe_allow_html=True)

# 自動偵測目錄下所有圖檔，第一張即為收款碼
valid_exts = ('.jpg', '.jpeg', '.png', '.JPG', '.PNG')
files = [f for f in os.listdir('.') if f.lower().endswith(valid_exts) and f != 'app.py']

if files:
    # 顯示上傳的第一張圖片
    st.image(files[0], width=300)
else:
    st.error("⚠️ 系統偵測中：請確保 GitHub 內已 Commit 圖檔")

st.markdown("<p style='font-size: 14px; color: #888;'>支付成功後請保留截圖，算力系統將自動比對</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- 第三層：持股診斷 (備用) ---
st.text_input("", placeholder="或輸入台股代碼進行算力分析")

# --- 最終頁尾：強制高亮白色 ---
st.markdown(f"""
    <br><br>
    <p style='text-align: center; color: #00ff41; font-size: 16px; letter-spacing: 3px; font-weight: bold; text-shadow: 0px 0px 10px #00ff41;'>
        AXIOM 1.1 | 讓算力為您工作
    </p>
    <p style='text-align: center; color: #555; font-size: 10px;'>
        AXIOM CLOUD SYSTEMS SECURITY ENCRYPTED
    </p>
""", unsafe_allow_html=True)
