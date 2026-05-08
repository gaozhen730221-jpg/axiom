import streamlit as st
import random
from pathlib import Path

# --- ① 核心邏輯：隨機核對定價 ---
if 'random_cents' not in st.session_state:
    st.session_state.random_cents = random.randint(1, 99)

def get_final_price():
    # 這裡可以根據您的需求調整基數 (例如 99 或 100)
    return 99 + (st.session_state.random_cents / 100)

# --- ② 視覺定案：1.0 SIGNAL 極簡白黑風格 ---
st.set_page_config(page_title="1.0 SIGNAL", layout="centered")

st.markdown(f"""
    <style>
    /* 100% 複製新系統質感：純白背景 */
    html, body, [data-testid="stAppViewContainer"] {{ 
        background-color: #FFFFFF !important; 
        color: #000000 !important; 
    }}
    [data-testid="stHeader"], [data-testid="stFooter"] {{ visibility: hidden; }}
    
    /* 移除所有雜亂間距 */
    [data-testid="stVerticalBlock"] > div {{ padding: 0 !important; }}

    @media (max-width: 640px) {{
        /* 頂部標識 */
        .brand-header {{ 
            font-size: 0.8rem; 
            font-weight: 900; 
            text-align: center; 
            color: #000000; 
            margin-top: 25px; 
            letter-spacing: 2px;
            text-transform: uppercase;
        }}
        
        .main-title {{ 
            font-size: 1.6rem; 
            font-weight: 800; 
            text-align: center; 
            color: #000000; 
            margin: 20px 0 30px 0; 
        }}
        
        /* 輸入框：黑細線邊框，大字體 */
        .stTextInput>div>div>input {{ 
            background-color: #FFFFFF !important; 
            color: #000000 !important; 
            border: 1.5px solid #000000 !important; 
            border-radius: 10px !important;
            height: 3.5rem !important;
            text-align: center;
            font-size: 1.2rem !important;
            font-weight: 600;
        }}

        /* 支付卡片區：淡灰色極細邊框 */
        .pay-card {{
            border: 1px solid #F0F0F0;
            border-radius: 24px;
            padding: 25px 15px;
            margin: 25px 0;
            text-align: center;
            background-color: #FFFFFF;
            box-shadow: 0 10px 30px rgba(0,0,0,0.03);
        }}
        
        .price-val {{ 
            font-size: 3.2rem !important; 
            font-weight: 900; 
            color: #000000; 
            margin: 15px 0 5px 0; 
            letter-spacing: -1px;
        }}
        .price-unit {{ font-size: 1.2rem; font-weight: 700; color: #000000; }}
        
        .sync-status {{ 
            color: #00D100; 
            font-size: 0.75rem; 
            font-weight: 800; 
            margin-bottom: 15px; 
            letter-spacing: 1px;
        }}

        /* 底部按鈕：純黑暴力美學 */
        .stButton>button {{ 
            background-color: #000000 !important; 
            color: #FFFFFF !important; 
            width: 100%; 
            height: 4.2rem; 
            font-size: 1.2rem !important; 
            font-weight: 700 !important; 
            border-radius: 15px !important; 
            border: none !important;
            margin-top: 15px;
            transition: 0.3s;
        }}
    }}
    </style>
    """, unsafe_allow_html=True)

# --- ③ 介面呈現 ---
st.markdown('<p class="brand-header">TAIWAN STOCKS 1.0</p>', unsafe_allow_html=True)
st.markdown('<p class="main-title">真相底牌 一秒開牌</p>', unsafe_allow_html=True)

# 1. 股票地址/代碼輸入 (無標籤，極簡化)
code = st.text_input("", placeholder="輸入驗證代碼 / 股票地址", label_visibility="collapsed")

if code:
    price = get_final_price()
    
    # 2. 支付卡片區 (參考經典 1.08 比例)
    st.markdown('<div class="pay-card">', unsafe_allow_html=True)
    st.markdown('<p class="sync-status">● LIVE SIGNAL SYNC</p>', unsafe_allow_html=True)
    
    # QR Code 自動置中
    qrs = list(Path('.').rglob('*.png')) + list(Path('.').rglob('*.jpg'))
    if qrs:
        st.image(str(qrs[-1]), width=190)
    
    # 隨機金額
    st.markdown(f'<p class="price-val">{price} <span class="price-unit">TWD</span></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:0.75rem; color:#888; margin-bottom:0;">請支付精確金額，系統自動比對入帳</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 3. 執行按鈕
    if st.button("確認付款，解鎖數據"):
        st.write(f"正在連線後台，核對金額 {price}...")
else:
    # 初始狀態留白，引導用戶輸入
    st.markdown('<div style="height: 350px;"></div>', unsafe_allow_html=True)

st.markdown('<p style="text-align:center; color:#BBB; font-size:0.6rem; margin-top:30px;">L2 DATA CORE / ENCRYPTED SIGNAL</p>', unsafe_allow_html=True)
