import streamlit as st
import os
import time

# --- AXIOM 1.1 | TESLA DESIGN LANGUAGE ---
st.set_page_config(page_title="AXIOM 1.1", layout="centered")

# 強制注入特斯拉風格 CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    
    .stApp { background-color: #000000; color: #E7E7E7; font-family: 'Inter', sans-serif; text-align: center; }
    
    /* 標題與標語：冷淡且高級 */
    .hero-title { letter-spacing: 12px; font-weight: 300; margin-top: 40px; color: #FFFFFF; }
    .hero-tagline { color: #8E8E8E; font-size: 11px; letter-spacing: 4px; margin-bottom: 50px; }
    
    /* 卡片設計：無邊框，僅靠層次感分開 */
    .tesla-card { background: #111111; padding: 20px; border-radius: 4px; margin-bottom: 12px; text-align: left; }
    .status-dot { color: #00FF41; margin-right: 10px; font-size: 10px; }
    .card-title { font-size: 14px; font-weight: 600; color: #FFFFFF; }
    .card-meta { font-size: 12px; color: #666; float: right; }
    
    /* 入金區：細線條邊框，不臃腫 */
    .pay-zone { border: 1px solid #333; padding: 30px; margin-top: 40px; background: #000; }
    .pay-title { font-size: 13px; color: #8E8E8E; letter-spacing: 2px; margin-bottom: 20px; }
    
    /* 按鈕與輸入框縮小化 */
    div.stButton > button { 
        background-color: transparent; color: #00FF41; border: 1px solid #00FF41; 
        border-radius: 2px; width: 100%; font-size: 12px; letter-spacing: 2px;
    }
    div.stTextInput > div > div > input { 
        background-color: #111; color: white; border: 1px solid #333; font-size: 12px;
    }
    
    /* 頁尾文字：極小化 */
    .footer-text { color: #333; font-size: 10px; letter-spacing: 5px; margin-top: 80px; text-transform: uppercase; }
    </style>
""", unsafe_allow_html=True)

# --- 視覺呈現 ---
st.markdown("<h1 class='hero-title'>AXIOM 1.1</h1>", unsafe_allow_html=True)
st.markdown("<p class='hero-tagline'>ADVANCED PREDICTIVE ANALYTICS</p>", unsafe_allow_html=True)

# 1. 歷史 (信任維度)
st.markdown("<p style='text-align:left; font-size:10px; color:#444;'>PAST PERFORMANCE</p>", unsafe_allow_html=True)
st.markdown("""
<div class='tesla-card'><span class='status-dot'>●</span><span class='card-title'>2330.TW</span><span class='card-meta'>+4.2% ACHIEVED</span></div>
<div class='tesla-card'><span class='status-dot'>●</span><span class='card-title'>3231.TW</span><span class='card-meta'>+6.8% ACHIEVED</span></div>
""", unsafe_allow_html=True)

# 2. 未來 (慾望維度)
st.markdown("<p style='text-align:left; font-size:10px; color:#444; margin-top:30px;'>FUTURE PROJECTION</p>", unsafe_allow_html=True)
st.markdown("""
<div class='tesla-card' style='border-left: 2px solid #00FF41;'><span class='card-title'>TARGET A: 23**</span><span class='card-meta' style='color:#00FF41;'>92% PROBABILITY</span></div>
<div class='tesla-card' style='border-left: 2px solid #00FF41;'><span class='card-title'>TARGET B: 62**</span><span class='card-meta' style='color:#00FF41;'>89% PROBABILITY</span></div>
""", unsafe_allow_html=True)

# 3. 入金與核對 (隱藏後門)
st.markdown("<div class='pay-zone'>", unsafe_allow_html=True)
st.markdown("<p class='pay-title'>SECURE PAYMENT ACCESS</p>", unsafe_allow_html=True)

# 自動抓收款圖並縮小比例
img_files = [f for f in os.listdir('.') if f.lower().endswith(('.png', '.jpg', '.jpeg')) and f != 'app.py']
if img_files:
    st.image(img_files[0], width=220)

st.markdown("<br>", unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    s_id = st.text_input("SYMBOL", placeholder="Code", label_visibility="collapsed")
with c2:
    p_id = st.text_input("PHONE", placeholder="Last 4", label_visibility="collapsed")

if st.button("AUTHENTICATE"):
    if s_id and p_id:
        with st.spinner('VERIFYING...'):
            time.sleep(1.2)
        st.success(f"ACCESS GRANTED: {s_id} | TARGET +15%")
st.markdown("</div>", unsafe_allow_html=True)

# 4. 極致隱藏頁尾
st.markdown("<p class='footer-text'>Axiom Systems © 2026</p>", unsafe_allow_html=True)
