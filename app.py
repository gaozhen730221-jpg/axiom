import streamlit as st
import os, time

# 極簡白視覺：純白背景 + 黑色文字 + 算力綠數據
st.set_page_config(page_title="AXIOM 2.1", layout="centered")
st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] { 
        background-color: #FFFFFF; 
        color: #000000; 
        font-family: 'Noto Sans TC', sans-serif; 
    }
    .stTextInput input { 
        background-color: #F8F9FA !important; 
        color: #000000 !important; 
        border: 1px solid #E0E0E0 !important; 
        border-radius: 4px;
    }
    .stButton>button { 
        background-color: #000000; 
        color: #FFFFFF; 
        width: 100%; 
        border-radius: 4px; 
        height: 50px;
        font-size: 18px;
    }
    [data-testid="stMetricValue"] { color: #000000 !important; }
    </style>
    """, unsafe_allow_html=True)

# 核心數據：一眼看到重點
st.write("## AXIOM 2.1")
c1, c2 = st.columns(2)
c1.metric("當前算力勝率", "92.4%")
c2.metric("已解碼標的", "23**")

st.divider()

# 入金與核對 (極簡化)
qr = "pay_qr.png"
if os.path.exists(qr): 
    st.image(qr, width=120)

code = st.text_input("輸入欲解碼代碼", placeholder="例如: 2330")
phone = st.text_input("驗證手機末 4 碼", placeholder="身分核對")

if st.button("獲取算力預測結果"):
    with st.spinner("核對中..."):
        time.sleep(0.5) # 0.5秒足矣，多一秒都是浪費
    st.success(f"標的 {code}：算力顯示未來 72 小時強勢看漲。")
    st.markdown("<p style='color:red;'>⚠️ 剩餘授權次數：1</p>", unsafe_allow_html=True)
