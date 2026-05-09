import streamlit as st
import random
import time
import base64
from pathlib import Path

# --- 1.0 核心邏輯：指紋定價與狀態管理 ---
if 'random_cents' not in st.session_state:
    st.session_state.random_cents = random.randint(1, 99)
    st.session_state.payment_confirmed = False

def get_final_price():
    # 99 TWD + 隨機指紋小數
    return round(99 + (st.session_state.random_cents / 100), 2)

# --- 2.0 極簡白金 UI 樣式表 ---
st.set_page_config(page_title="TAIWAN STOCKS 1.0", layout="centered")

st.markdown(f"""
    <style>
    /* 全局去噪 */
    html, body, [data-testid="stAppViewContainer"] {{ 
        background-color: #FFFFFF !important; 
    }}
    [data-testid="stHeader"], [data-testid="stFooter"] {{ visibility: hidden; }}
    [data-testid="stVerticalBlock"] > div {{ padding: 0 !important; margin: 0 !important; }}

    /* 品牌與標題 */
    .brand-header {{ 
        font-size: 0.85rem; font-weight: 900; text-align: center; 
        margin-top: 50px !important; letter-spacing: 3px; color: #000; 
    }}
    .main-title {{ 
        font-size: 1.6rem; font-weight: 800; text-align: center; 
        margin: 10px 0 30px 0 !important; color: #000; 
    }}

    /* 輸入框優化 */
    .stTextInput {{ padding: 0 40px !important; }}
    .stTextInput>div>div>input {{ 
        background-color: #F2F2F2 !important; 
        border: none !important; border-radius: 15px !important;
        height: 3.8rem !important; text-align: center;
        font-weight: 700; font-size: 1.2rem !important;
    }}

    /* 支付金額大字體 */
    .price-val {{ 
        font-size: 4.8rem !important; font-weight: 900; text-align: center;
        margin: 15px 0 !important; letter-spacing: -3px; color: #000;
    }}
    .price-unit {{ font-size: 1.2rem; font-weight: 800; vertical-align: middle; }}
    
    /* 呼吸燈動畫：正在監測入帳 */
    @keyframes blink {{ 0% {{opacity: 0.3;}} 50% {{opacity: 1;}} 100% {{opacity: 0.3;}} }}
    .status-msg {{ 
        color: #00C853; font-size: 0.9rem; font-weight: 800; 
        text-align: center; margin: 15px 0 !important;
        animation: blink 1.5s infinite;
    }}
    
    /* QR Code 容器 */
    .qr-container {{
        display: flex; justify-content: center; margin: 20px 0 !important;
    }}
    .qr-container img {{
        width: 190px !important; border-radius: 12px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    }}

    /* 開牌訊號卡片 */
    .signal-card {{
        background: #F8F9FA; border-radius: 20px; padding: 30px;
        text-align: center; margin: 20px 40px !important;
    }}
    .signal-light {{ font-size: 2.5rem; font-weight: 900; margin-bottom: 10px; }}
    .red-light {{ color: #FF3B30; }}
    .green-light {{ color: #34C759; }}
    </style>
    """, unsafe_allow_html=True)

# --- 3.0 介面渲染 ---

st.markdown('<p class="brand-header">TAIWAN STOCKS 1.0</p>', unsafe_allow_html=True)
st.markdown('<p class="main-title">真相底牌 一秒開牌</p>', unsafe_allow_html=True)

if not st.session_state.payment_confirmed:
    # 模式 A：收款監測
    stock_code = st.text_input("", placeholder="輸入股票代號", key="stock_input", label_visibility="collapsed")
    
    if stock_code:
        st.markdown(f'<p class="status-msg">● 正在監測 {stock_code} 入帳狀態...</p>', unsafe_allow_html=True)

        # 自動尋找目錄下的圖片作為 QR Code
        img_path = next(Path('.').glob('*.png'), None) or next(Path('.').glob('*.jpg'), None)
        if img_path:
            with open(img_path, "rb") as f:
                img_b64 = base64.b64encode(f.read()).decode()
            st.markdown(f'<div class="qr-container"><img src="data:image/png;base64,{img_b64}"></div>', unsafe_allow_html=True)
        else:
            st.warning("請在目錄下放置支付 QR Code 圖片")

        # 顯示指紋金額
        current_price = get_final_price()
        st.markdown(f'<p class="price-val">{current_price:.2f} <span class="price-unit">TWD</span></p>', unsafe_allow_html=True)
        
        st.markdown('<p style="text-align:center; color:#888; font-size:0.8rem; font-weight:600;">請支付精確金額(含小數點)即可自動開牌</p>', unsafe_allow_html=True)

        # 模擬自動跳轉邏輯（實際對接 API）
        # time.sleep(5) 
        # st.session_state.payment_confirmed = True
        # st.rerun()

else:
    # 模式 B：紅綠燈開牌
    st.markdown(f"""
        <div class="signal-card">
            <p style="color:#666; font-weight:600;">{st.session_state.get('stock_input', '')} 核心信號</p>
            <p class="signal-light red-light">大單匯入・強勢</p>
            <hr style="border:0.5px solid #EEE;">
            <p style="font-size:0.9rem; color:#333;">主力資金流向：+1.2 億</p>
            <p style="font-size:0.9rem; color:#333;">籌碼集中度：極高</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("查詢下一檔", use_container_width=True):
        st.session_state.payment_confirmed = False
        st.session_state.random_cents = random.randint(1, 99)
        st.rerun()
