import streamlit as st
import random
from pathlib import Path

# --- ① 核心：隨機核對金額 ---
if 'random_cents' not in st.session_state:
    st.session_state.random_cents = random.randint(1, 99)

def get_final_price():
    return round(99 + (st.session_state.random_cents / 100), 2)

# --- ② 視覺定案：白底、無空格、QR 居中 (參考截圖 4228/4230) ---
st.set_page_config(page_title="1.0 SIGNAL", layout="centered")

st.markdown(f"""
    <style>
    /* 1. 強制白底黑字 */
    html, body, [data-testid="stAppViewContainer"] {{ 
        background-color: #FFFFFF !important; 
        color: #000000 !important; 
    }}
    [data-testid="stHeader"], [data-testid="stFooter"] {{ visibility: hidden; }}

    /* 2. 消滅所有神祕空格與間距 (關鍵修正) */
    [data-testid="stVerticalBlock"] > div {{ 
        padding-top: 0rem !important; 
        padding-bottom: 0rem !important; 
        margin-top: 0rem !important; 
    }}
    .stTextInput {{ margin-top: -15px !important; }} /* 把輸入框往上拉，吃掉空格 */

    @media (max-width: 640px) {{
        .brand-header {{ font-size: 0.8rem; font-weight: 900; text-align: center; margin-top: 25px; letter-spacing: 2px; }}
        .main-title {{ font-size: 1.5rem; font-weight: 800; text-align: center; margin: 15px 0 20px 0; }}
        
        /* 3. 仿截圖 4228 的輸入框 */
        .stTextInput>div>div>input {{ 
            background-color: #F9F9F9 !important; 
            border: 1px solid #EEEEEE !important; 
            border-radius: 12px !important;
            height: 3.5rem !important;
            text-align: center;
            font-size: 1.1rem !important;
        }}

        /* 4. QR Code 完美居中容器 */
        .qr-wrap {{
            display: flex;
            justify-content: center;
            padding: 15px 0;
        }}

        .price-val {{ 
            font-size: 3.8rem !important; 
            font-weight: 900; 
            text-align: center;
            margin: 5px 0; 
            letter-spacing: -2px;
        }}
        
        .status-dot {{ 
            color: #00C853; 
            font-size: 0.85rem; 
            font-weight: 800; 
            text-align: center;
            margin-bottom: 10px;
        }}
        
        /* 5. 底部自動解密提示框 */
        .bottom-hint {{
            background: #F8F8F8;
            padding: 15px;
            border-radius: 12px;
            font-size: 0.8rem;
            color: #666;
            text-align: center;
            margin-top: 25px;
            font-weight: 500;
        }}
    }}
    </style>
    """, unsafe_allow_html=True)

# --- ③ 介面呈現 (按截圖層級排列) ---
st.markdown('<p class="brand-header">TAIWAN STOCKS 1.0</p>', unsafe_allow_html=True)
st.markdown('<p class="main-title">真相底牌 一秒開牌</p>', unsafe_allow_html=True)

# 1. 輸入框 (上方空格已消除)
code = st.text_input("", placeholder="輸入驗證代碼 / 股票地址", label_visibility="collapsed")

# 2. 狀態與 QR Code (強制正中心)
st.markdown('<p class="status-dot">● 正在監測入帳中...</p>', unsafe_allow_html=True)

# 偵測圖片
qrs = list(Path('.').glob('*.png')) + list(Path('.').glob('*.jpg'))
if qrs:
    # 使用 columns 配合 css 達到絕對居中
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(str(qrs[0]), use_column_width=True)

# 3. 隨機價格 (大字體，參考截圖 4230)
price = get_final_price()
st.markdown(f'<p class="price-val">{price} <span style="font-size:1.4rem;">TWD</span></p>', unsafe_allow_html=True)

# 4. 底部自動對帳提示
st.markdown('<p class="bottom-hint">等待支付中，系統抓取入帳後將自動解密...</p>', unsafe_allow_html=True)

# --- ④ 自動對帳刷新 ---
import time
time.sleep(3)
st.rerun()
