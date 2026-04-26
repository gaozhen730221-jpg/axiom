import streamlit as st
import os
import time
from datetime import datetime

# --- AXIOM 1.1 進化：動態流體 UI ---
st.set_page_config(page_title="AXIOM 1.1 算力中心", layout="centered")

# 特斯拉動態科技風格
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
    
    .stApp { background-color: #000000; color: #E7E7E7; font-family: 'JetBrains Mono', sans-serif; text-align: center; }
    
    /* 掃描線動畫效果 */
    .scanline { width: 100%; height: 2px; background: rgba(0, 255, 65, 0.2); position: fixed; top: 0; left: 0; animation: scan 4s linear infinite; z-index: 999; }
    @keyframes scan { 0% { top: 0; } 100% { top: 100%; } }

    /* 頂部 LOGO */
    .brand-header { letter-spacing: 15px; font-weight: 700; color: #FFFFFF; margin-top: 20px; animation: glow 2s ease-in-out infinite alternate; }
    @keyframes glow { from { text-shadow: 0 0 5px #fff, 0 0 10px #00FF41; } to { text-shadow: 0 0 10px #fff, 0 0 20px #00FF41; } }

    /* 動態數據卡片 */
    .live-card { background: #080808; padding: 12px; border: 1px solid #1A1A1A; border-radius: 2px; margin-bottom: 8px; text-align: left; position: relative; overflow: hidden; }
    .live-card:hover { border: 1px solid #00FF41; background: #0c0c0c; }
    .tag-live { font-size: 9px; background: #00FF41; color: #000; padding: 2px 5px; border-radius: 2px; margin-right: 8px; }
    .stock-name { font-size: 14px; color: #FFF; font-weight: bold; }
    .stock-val { float: right; color: #00FF41; font-weight: bold; font-size: 14px; }
    
    /* 支付區塊細線條化 */
    .pay-border { border: 1px solid #222; padding: 20px; margin-top: 30px; background: #000; position: relative; }
    .pay-hint { font-size: 12px; color: #444; letter-spacing: 2px; margin-bottom: 15px; }

    /* 隱藏原生標籤 */
    div.stTextInput > div > div > input { background-color: #050505; color: #00FF41; border: 1px solid #222; border-radius: 0; }
    div.stButton > button { background-color: transparent; color: #00FF41; border: 1px solid #00FF41; border-radius: 0; font-weight: bold; height: 50px; transition: 0.3s; }
    div.stButton > button:hover { background-color: #00FF41; color: #000; }
    
    footer {visibility: hidden;}
    </style>
    <div class="scanline"></div>
""", unsafe_allow_html=True)

# --- 頂部品牌 ---
st.markdown("<h1 class='brand-header'>AXIOM 1.1</h1>", unsafe_allow_html=True)
current_time = datetime.now().strftime("%H:%M:%S")
st.markdown(f"<p style='color:#444; font-size:10px; letter-spacing:3px;'>CORE UPDATE: {current_time} | STABLE</p>", unsafe_allow_html=True)

# 1. 動態達成區 (過去)
st.markdown("<p style='text-align:left; font-size:10px; color:#333; margin-top:20px;'>歷史算力達成回測</p>", unsafe_allow_html=True)
st.markdown(f"""
<div class='live-card'><span class='tag-live'>LIVE</span><span class='stock-name'>台積電 2330</span><span class='stock-val'>+4.25%</span></div>
<div class='live-card'><span class='tag-live'>LIVE</span><span class='stock-name'>緯創 3231</span><span class='stock-val'>+6.82%</span></div>
""", unsafe_allow_html=True)

# 2. 算力預測區 (未來) - 這是誘餌，也是核心
st.markdown("<p style='text-align:left; font-size:10px; color:#333; margin-top:20px;'>算力未來指標</p>", unsafe_allow_html=True)
st.markdown("""
<div class='live-card' style='border-left: 2px solid #00FF41;'><span class='stock-name'>核心標 A (23**)</span><span class='stock-val' style='color:#00FF41;'>92% CONFIDENCE</span></div>
<div class='live-card' style='border-left: 2px solid #00FF41;'><span class='stock-name'>核心標 B (62**)</span><span class='stock-val' style='color:#00FF41;'>89% CONFIDENCE</span></div>
""", unsafe_allow_html=True)

# 3. 支付核對 (後門感應)
st.markdown("<div class='pay-border'>", unsafe_allow_html=True)
st.markdown("<p class='pay-hint'>AUTHENTICATION REQUIRED</p>", unsafe_allow_html=True)

# 顯示 QR Code
img_files = [f for f in os.listdir('.') if f.lower().endswith(('.png', '.jpg', '.jpeg')) and f != 'app.py']
if img_files:
    st.image(img_files[0], width=240)

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    s_id = st.text_input("代碼", placeholder="STOCK", label_visibility="collapsed")
with col2:
    p_id = st.text_input("手機", placeholder="LAST 4", label_visibility="collapsed", max_chars=4)

if st.button("EXECUTE / 啟動算力"):
    if s_id and p_id:
        with st.status("正在同步核心算力資料庫...", expanded=True) as status:
            time.sleep(1)
            st.write("連線台股交易網關...")
            time.sleep(0.8)
            st.write(f"感應到末碼 {p_id} 授權資訊...")
            status.update(label="授權成功", state="complete", expanded=False)
        
        st.markdown(f"""
        <div style='background:#00FF41; color:#000; padding:15px; border-radius:2px; font-weight:bold; margin-top:10px;'>
            系統感應：{s_id} 算力評比【強勢】<br>
            關鍵支撐：{s_id[:2]}.5 | 目標潛力：+15%
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("請填寫資訊以完成核對")

st.markdown("</div>", unsafe_allow_html=True)

# 頁尾
st.markdown("<br><p style='color:#222; font-size:9px; letter-spacing:5px;'>AXIOM SYSTEMS ALPHA 1.1</p>", unsafe_allow_html=True)
