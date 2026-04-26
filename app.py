import streamlit as st
import os
import time

# --- AXIOM 1.1 時空進階版 ---
st.set_page_config(page_title="AXIOM 1.1", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0c0e11; color: #ffffff; text-align: center; }
    .history-card { background: #14171c; border: 1px solid #333; padding: 15px; border-radius: 8px; margin-bottom: 10px; text-align: left; }
    .future-card { background: linear-gradient(135deg, #1d2229 0%, #0c0e11 100%); border-left: 5px solid #00ff41; padding: 18px; margin: 12px 0; text-align: left; }
    .pay-zone { border: 2px solid #00ff41; padding: 25px; border-radius: 12px; background: #0c0e11; margin-top: 20px; }
    .success-box { padding: 20px; background: #00ff41; color: #000; border-radius: 12px; font-weight: bold; margin-top: 20px; }
    .badge { background-color: #333; color: #00ff41; padding: 2px 8px; border-radius: 4px; font-size: 12px; margin-right: 5px; }
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='letter-spacing: 10px;'>AXIOM 1.1</h1>", unsafe_allow_html=True)

# --- 1. 過去 (歷史戰績：建立信任) ---
st.markdown("<p style='color: #888; font-size: 14px; text-align: left;'>PREVIOUS | 過去 48H 算力達成</p>", unsafe_allow_html=True)
st.markdown("""
<div class='history-card'>
    <span class='badge'>已達成</span> 標的 2330：漲幅 +4.2% <span style='float: right; color: #888;'>達標時分 13:02</span>
</div>
<div class='history-card'>
    <span class='badge'>已達成</span> 標的 3231：漲幅 +6.8% <span style='float: right; color: #888;'>達標時分 10:45</span>
</div>
""", unsafe_allow_html=True)

# --- 2. 未來 (算力預測：引發慾望) ---
st.markdown("<p style='color: #00ff41; font-size: 14px; text-align: left; margin-top: 20px;'>FUTURE | 未來 72H 爆發預測</p>", unsafe_allow_html=True)
st.markdown("""
<div class='future-card'>🎯 標 A：23** <span style='color: #00ff41; float: right;'>期待值 92%</span><br><small style='color: #555;'>算力提示：主力籌碼高度集中，洗盤即將結束</small></div>
<div class='future-card'>🎯 標 B：62** <span style='color: #00ff41; float: right;'>期待值 89%</span><br><small style='color: #555;'>算力提示：突破關鍵壓力位，展開第二波攻勢</small></div>
""", unsafe_allow_html=True)

# --- 3. 入金與虛擬感應後門 ---
st.markdown("<div class='pay-zone'>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #00ff41; margin-top: 0;'>🔑 掃碼解鎖完整未來報告</h3>", unsafe_allow_html=True)

# 收款圖
files = [f for f in os.listdir('.') if f.lower().endswith(('.png', '.jpg', '.jpeg')) and f != 'app.py']
if files:
    st.image(files[0], width=320)

st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    stock_id = st.text_input("輸入查詢代碼", placeholder="2330")
with col2:
    phone_id = st.text_input("手機末 4 碼", placeholder="核對金流", max_chars=4)

if st.button("🚀 啟動算力核對", use_container_width=True):
    if stock_id and phone_id:
        with st.spinner('連線 AXIOM 核心算力...'):
            time.sleep(1.5)
        st.markdown(f"""
        <div class='success-box'>
            ✅ 系統感應末碼 {phone_id} 授權通過！<br>
            🔥 {stock_id} 未來 72H 報告：大戶成本位 {stock_id[:2]}.5，目標價上看 +12%
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("請輸入完整資訊以供核對")
st.markdown("</div>", unsafe_allow_html=True)

# 4. 品牌頁尾
st.markdown("<br><p style='color: #00ff41; font-weight: bold; letter-spacing: 3px;'>AXIOM 1.1 | 讓算力為您工作</p>", unsafe_allow_html=True)
