import streamlit as st
import random
from pathlib import Path

# --- ① 邏輯：隨機核對金額 ---
if 'random_cents' not in st.session_state:
    st.session_state.random_cents = random.randint(1, 99)

def get_final_price():
    return round(99 + (st.session_state.random_cents / 100), 2)

# --- ② 視覺定案：控制圖片大小、消滅空格 ---
st.set_page_config(page_title="1.0 SIGNAL", layout="centered")

st.markdown(f"""
    <style>
    /* 全局背景與字體 */
    html, body, [data-testid="stAppViewContainer"] {{ 
        background-color: #FFFFFF !important; 
        color: #000000 !important; 
    }}
    [data-testid="stHeader"], [data-testid="stFooter"] {{ visibility: hidden; }}

    /* 🚨 消滅預設間距：讓所有元件緊貼 */
    [data-testid="stVerticalBlock"] > div {{ 
        padding: 0 !important; 
        margin: 0 !important; 
    }}
    
    /* 修正標題間距 */
    .brand-header {{ font-size: 0.8rem; font-weight: 900; text-align: center; margin-top: 20px !important; letter-spacing: 2px; }}
    .main-title {{ font-size: 1.4rem; font-weight: 800; text-align: center; margin: 10px 0 15px 0 !important; }}

    /* 修正輸入框位置與高度 */
    .stTextInput {{ margin-top: -5px !important; padding: 0 20px !important; }}
    .stTextInput>div>div>input {{ 
        background-color: #F7F7F7 !important; 
        border: none !important;
        border-radius: 10px !important;
        height: 3rem !important;
        text-align: center;
    }}

    /* 🚨 核心修正：控制 QR Code 大小與置中 */
    .qr-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 15px 0 !important;
    }}
    .qr-container img {{
        width: 190px !important; /* 👈 這裡控制 QR Code 尺寸，保證不爆屏 */
        height: auto !important;
        border-radius: 15px;
    }}

    .price-val {{ 
        font-size: 3.5rem !important; 
        font-weight: 900; 
        text-align: center;
        margin: 5px 0 !important; 
        letter-spacing: -2px;
    }}
    
    .status-msg {{ 
        color: #00D100; 
        font-size: 0.8rem; 
        font-weight: 800; 
        text-align: center;
        margin: 10px 0 !important;
    }}
    
    .hint-bar {{
        background: #F2F2F2;
        padding: 12px;
        border-radius: 10px;
        font-size: 0.75rem;
        color: #888;
        text-align: center;
        margin: 20px 20px 0 20px !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- ③ 介面呈現 ---
st.markdown('<p class="brand-header">TAIWAN STOCKS 1.0</p>', unsafe_allow_html=True)
st.markdown('<p class="main-title">真相底牌 一秒開牌</p>', unsafe_allow_html=True)

# 1. 輸入區
code = st.text_input("", placeholder="輸入驗證代碼 / 股票地址", label_visibility="collapsed")

# 2. 狀態
st.markdown('<p class="status-msg">● 系統正在監測入帳中...</p>', unsafe_allow_html=True)

# 3. QR Code (使用自定義容器強制控制大小)
qrs = list(Path('.').glob('*.png')) + list(Path('.').glob('*.jpg'))
if qrs:
    # 直接用 HTML 標籤寫入，繞過 Streamlit 預設的寬度限制
    import base64
    def get_image_base64(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    
    img_base64 = get_image_base64(qrs[0])
    st.markdown(f'<div class="qr-container"><img src="data:image/png;base64,{img_base64}"></div>', unsafe_allow_html=True)

# 4. 隨機價格
price = get_final_price()
st.markdown(f'<p class="price-val">{price} <span style="font-size:1.2rem;">TWD</span></p>', unsafe_allow_html=True)

# 5. 底部提示
st.markdown('<p class="hint-bar">等待支付中，入帳後系統將自動跳轉數據...</p>', unsafe_allow_html=True)

# --- ④ 自動刷新 ---
import time
time.sleep(4)
st.rerun()
