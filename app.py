import streamlit as st
import os

# --- AXIOM 1.0 極致視覺設定 ---
st.set_page_config(page_title="AXIOM 1.0", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0c0e11; color: #ffffff; text-align: center; }
    /* 誘餌卡片樣式 */
    .target-card { background: #1d2229; padding: 18px; border-left: 5px solid #00ff41; margin: 10px 0; text-align: left; font-size: 18px; }
    /* 入金區塊樣式 */
    .gold-box { border: 2px solid #00ff41; padding: 25px; border-radius: 12px; background: #14171c; margin-top: 5px; }
    /* 隱藏官方多餘元件 */
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 標題
st.markdown("<h1 style='letter-spacing: 10px; margin-bottom: 20px;'>AXIOM 1.0</h1>", unsafe_allow_html=True)

# --- 1. 核心查詢區 (放在最上方，供股民輸入代碼) ---
stock_id = st.text_input("", placeholder="🔍 請輸入台股代碼 (例如: 2330)")

# --- 2. 誘餌區 (今日明牌提示) ---
st.markdown("""
<div class='target-card'>🎯 標 A：23** <span style='float: right; color: #00ff41;'>勝率 92%</span></div>
<div class='target-card'>🎯 標 B：62** <span style='float: right; color: #00ff41;'>大戶掃貨 89%</span></div>
<div class='target-card'>🎯 標 C：30** <span style='float: right; color: #ff4141;'>預警 94%</span></div>
""", unsafe_allow_html=True)

# --- 3. 暴力入金區 (直接顯示，無廢物框) ---
st.markdown("<div class='gold-box'>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #00ff41; margin-top: 0;'>💳 掃碼解鎖完整報告 (NT$ 100)</h3>", unsafe_allow_html=True)

# 暴力搜尋目錄下的收款圖片
valid_exts = ('.jpg', '.jpeg', '.png', '.JPG', '.PNG')
files = [f for f in os.listdir('.') if f.lower().endswith(valid_exts) and f != 'app.py']

if files:
    # 顯示搜尋到的第一張收款圖
    st.image(files[0], width=350)
else:
    st.error("⚠️ 收款碼載入中，請確保 GitHub 已上傳圖片")

st.markdown("<p style='font-size: 14px; color: #888; margin-top: 10px;'>支付成功後算力將自動啟動</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- 4. 霓虹高亮頁尾 ---
st.markdown(f"""
    <br><br>
    <p style='text-align: center; color: #00ff41; font-size: 18px; letter-spacing: 4px; font-weight: bold; text-shadow: 0px 0px 15px #00ff41;'>
        AXIOM 1.0 | 讓算力為您工作
    </p>
    <p style='text-align: center; color: #444; font-size: 10px;'>
        AXIOM SYSTEMS SECURITY ENCRYPTED
    </p>
""", unsafe_allow_html=True)
