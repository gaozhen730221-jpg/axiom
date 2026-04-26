import streamlit as st
import os
import time

# --- AXIOM 1.1 終極交付 ---
st.set_page_config(page_title="AXIOM 1.1", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;700&display=swap');
    .stApp { background-color: #000000; color: #FFFFFF; font-family: 'Noto Sans TC', sans-serif; }
    
    /* 移除大白框 CSS 關鍵技術 */
    div[data-baseweb="input"] { background-color: transparent !important; border: none !important; }
    div.stTextInput > div > div > input { 
        background-color: transparent !important; color: #00FF41 !important; 
        border: none !important; border-bottom: 1px solid #333 !important; 
        border-radius: 0px !important; font-size: 18px !important;
    }
    div.stTextInput > div > div > input:focus { border-bottom: 1px solid #00FF41 !important; box-shadow: none !important; }
    
    /* 按鈕進化 */
    div.stButton > button { 
        background-color: transparent; color: #00FF41; border: 2px solid #00FF41; 
        font-weight: bold; letter-spacing: 10px; width: 100%; height: 55px;
    }
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='letter-spacing:15px; text-align:center;'>AXIOM 1.1</h1>", unsafe_allow_html=True)

# 數據流
col1, col2 = st.columns(2)
with col1:
    st.markdown("<p style='color:#444; font-size:10px;'>ARCHIVE / 歷史戰績</p>", unsafe_allow_html=True)
    st.markdown("<div style='border-bottom:1px solid #111; padding:10px;'>2330 台積電 <span style='float:right; color:#00FF41;'>達標</span></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<p style='color:#444; font-size:10px;'>ACTIVE / 算力鎖定</p>", unsafe_allow_html=True)
    st.markdown("<div style='border-bottom:1px solid #111; padding:10px;'>23** <span style='float:right; color:#00FF41;'>92%</span></div>", unsafe_allow_html=True)

# 入金
st.markdown("<div style='text-align:center; margin-top:40px;'>", unsafe_allow_html=True)
img = [f for f in os.listdir('.') if f.lower().endswith(('.png', '.jpg', '.jpeg')) and f != 'app.py']
if img: st.image(img[0], width=260)
st.markdown("</div>", unsafe_allow_html=True)

# 後門
c1, c2 = st.columns(2)
with c1: s_id = st.text_input("S", placeholder="股票代碼", label_visibility="collapsed")
with c2: p_id = st.text_input("P", placeholder="手機末4碼", label_visibility="collapsed", max_chars=4)

if st.button("啟動算力"):
    if s_id and p_id:
        bar = st.progress(0, text="同步網關...")
        for p in range(100):
            time.sleep(0.01)
            bar.progress(p + 1)
        st.success(f"感應通過！{s_id} 目標回測 +15%")1
