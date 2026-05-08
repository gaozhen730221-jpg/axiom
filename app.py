import streamlit as st
import random
import time
import base64
from pathlib import Path

# --- ① 邏輯核心：隨機指紋定價與自動對帳狀態 ---
if 'random_cents' not in st.session_state:
    st.session_state.random_cents = random.randint(1, 99)
    st.session_state.payment_confirmed = False

def get_final_price():
    # 生成如 99.61 的隨機指紋金額
    return round(99 + (st.session_state.random_cents / 100), 2)

# --- ② 視覺定案：白金極簡、消滅空格、QR 尺寸適中 ---
st.set_page_config(page_title="1.0 SIGNAL", layout="centered")

st.markdown(f"""
    <style>
    /* 全局純白背景 */
    html, body, [data-testid="stAppViewContainer"] {{ 
        background-color: #FFFFFF !important; 
        color: #000000 !important; 
    }}
    [data-testid="stHeader"], [data-testid="stFooter"] {{ visibility: hidden; }}

    /* 消滅所有元件間的預設空格 */
    [data-testid="stVerticalBlock"] > div {{ 
        padding: 0 !important; 
        margin: 0 !important; 
    }}
    
    .brand-header {{ font-size: 0.8rem; font-weight: 900; text-align: center; margin-top: 25px !important; letter-spacing: 2px; }}
    .main-title {{ font-size: 1.4rem; font-weight: 800; text-align: center; margin: 10px 0 15px 0 !important; }}

    /* 輸入框：收緊間距、極簡線條 */
    .stTextInput {{ margin-top: -5px !important; padding: 0 20px !important; }}
    .stTextInput>div>div>input {{ 
        background-color: #F7F7F7 !important; 
        border: none !important;
        border-radius: 10px !important;
        height: 3.2rem !important;
        text-align: center;
        font-weight: 600;
    }}

    /* QR Code 置中且尺寸鎖定 (190px) */
    .qr-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 15px 0 !important;
    }}
    .qr-container img {{
        width: 190px !important;
        height: auto !important;
        border-radius: 15px;
    }}

    /* 隨機指紋金額字體 */
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
        padding: 15px;
        border-radius: 12px;
        font-size: 0.75rem;
        color: #888;
        text-align: center;
        margin: 25px 20px 0 20px !important;
        font-weight: 600;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- ③ 介面呈現 (One-Page 一條龍模式) ---
st.markdown('<p class="brand-header">TAIWAN STOCKS 1.0</p>', unsafe_allow_html=True)
st.markdown('<p class="main-title">真相底牌 一秒開牌</p>', unsafe_allow_html=True)

if not st.session_state.payment_confirmed:
    # --- 收款模式 ---
    code = st.text_input("", placeholder="輸入驗證代碼 / 股票地址", label_visibility="collapsed")
    
    st.markdown('<p class="status-msg">● 正在監測入帳中...</p>', unsafe_allow_html=True)

    # QR Code 處理
    qrs = list(Path('.').glob('*.png')) + list(Path('.').glob('*.jpg'))
    if qrs:
        with open(qrs[0], "rb") as f:
            img_base64 = base64.b64encode(f.read()).decode()
        st.markdown(f'<div class="qr-container"><img src="data:image/png;base64,{img_base64}"></div>', unsafe_allow_html=True)

    # 顯示指紋金額
    price = get_final_price()
    st.markdown(f'<p class="price-val">{price} <span style="font-size:1.2rem;">TWD</span></p>', unsafe_allow_html=True)
    
    st.markdown('<p class="hint-bar">等待支付中，入帳後系統將自動跳轉數據...</p>', unsafe_allow_html=True)

    # 🚨 全自動對帳監控邏輯
    # 這裡未來會接 API 判斷：if check_api(price) == True: st.session_state.payment_confirmed = True
    time.sleep(4) 
    st.rerun()

else:
    # --- 自動開牌模式 (數據結果) ---
    st.success("✅ 指紋金額核對成功！正在解密 1.0 SIGNAL...")
    st.divider()
    # 這裡顯示實時數據內容
    st.markdown("### 📊 實時訊號分析")
    st.write("● 數據中心：L2 Core")
    st.write("● 資金流向：特大單強勢掃貨")
