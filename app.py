import streamlit as st
import os
import time

# --- AXIOM 1.1 終極修正版 ---
st.set_page_config(page_title="AXIOM 1.1", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;700&display=swap');
    .stApp { background-color: #000000; color: #FFFFFF; font-family: 'Noto Sans TC', sans-serif; }
    
    /* 徹底消滅大白框：強制背景透明與細線設計 */
    div[data-baseweb="input"] { background-color: transparent !important; border: none !important; }
    div.stTextInput > div > div > input { 
        background-color: transparent !important; 
        color: #00FF41 !important; 
        border: none !important; 
        border-bottom: 1px solid #333 !important; 
        border-radius: 0px !important;
        font-size: 18px !important;
        padding: 10px 0px !important;
    }
    div.stTextInput > div > div > input:focus { border-bottom: 1px solid #00FF41 !important; box-shadow: none !important; }
    
    /* 按鈕特斯拉化 */
    div.stButton > button { 
        background-color: transparent; color: #00FF41; border: 2px solid #00FF41; 
        font-weight: bold; letter-spacing: 10px; width: 100%; height: 55px;
        margin-top: 20px;
    }
    div.stButton > button:hover { background-color: #00FF41; color: #000; }
    
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 標題
st.markdown("<h1 style='letter-spacing:15px; text-align:center; margin-top:30px;'>AXIOM 1.1</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#444; font-size:12px; letter-spacing:5px;'>台股算力中心</p>", unsafe_allow_html=True)

# 數據呈現
col1, col2 = st.columns(2)
with col1:
    st.markdown("<p style='color:#333; font-size:10px;'>歷史戰績記錄</p>", unsafe_allow_html=True)
    st.markdown("<div style='border-bottom:1px solid #111; padding:10px;'>2330 台積電 <span style='float:right; color:#00FF41;'>已達成</span></div>", unsafe_allow_html=True)
    st.markdown("<div style='border-bottom:1px solid #111; padding:10px;'>3231 緯創 <span style='float:right; color:#00FF41;'>已達成</span></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<p style='color:#333; font-size:10px;'>算力未來鎖定</p>", unsafe_allow_html=True)
    st.markdown("<div style='border-bottom:1px solid #111; padding:10px;'>標 A: 23** <span style='float:right; color:#00FF41;'>92%</span></div>", unsafe_allow_html=True)
    st.markdown("<div style='border-bottom:1px solid #111; padding:10px;'>標 B: 62** <span style='float:right; color:#00FF41;'>89%</span></div>", unsafe_allow_html=True)

# 收款圖區
st.markdown("<div style='text-align:center; margin-top:40px;'>", unsafe_allow_html=True)
img = [f for f in os.listdir('.') if f.lower().endswith(('.png', '.jpg', '.jpeg')) and f != 'app.py']
if img:
    st.image(img[0], width=260)
st.markdown("<p style='color:#444; font-size:12px; margin-top:10px;'>單次授權費：NT$ 100</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# 解鎖輸入區
st.markdown("<br>", unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    s_id = st.text_input("股票", placeholder="股票代碼", label_visibility="collapsed")
with c2:
    p_id = st.text_input("手機", placeholder="手機末4碼", label_visibility="collapsed", max_chars=4)

if st.button("啟動 AXIOM 算力解鎖"):
    if s_id and p_id:
        bar = st.progress(0, text="連線算力中心...")
        for p in range(100):
            time.sleep(0.01)
            bar.progress(p + 1)
        st.success(f"感應通過！{s_id} 算力評比：【強勢看多】")
    else:
        st.error("請輸入代碼與手機末4碼")
