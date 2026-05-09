import streamlit as st
import random
import time
import base64
from pathlib import Path

# --- 1.0 核心邏輯 ---
if 'random_cents' not in st.session_state:
    st.session_state.random_cents = random.randint(1, 99)
    st.session_state.payment_confirmed = False

def get_final_price():
    return round(99 + (st.session_state.random_cents / 100), 2)

# --- 2.0 強制佈局修正 (解決跑版問題) ---
st.set_page_config(page_title="TAIWAN STOCKS 1.0", layout="centered")

st.markdown(f"""
    <style>
    /* 1. 強制消除 Streamlit 預設間距 */
    [data-testid="stAppViewContainer"] {{ 
        background-color: #FFFFFF !important; 
    }}
    [data-testid="stHeader"], [data-testid="stFooter"] {{ visibility: hidden !important; }}
    [data-testid="stVerticalBlock"] {{ gap: 0rem !important; }}
    
    /* 2. 標題區塊 */
    .brand-box {{
        text-align: center;
        padding-top: 40px;
        margin-bottom: 20px;
    }}
    .brand-header {{ font-size: 0.8rem; font-weight: 900; letter-spacing: 3px; color: #888; }}
    .main-title {{ font-size: 1.8rem; font-weight: 800; color: #000; margin-top: 5px; }}

    /* 3. 輸入框：限制寬度並置中 */
    .stTextInput {{ 
        display: flex; 
        justify-content: center; 
        padding: 0 10% !important; 
    }}
    .stTextInput>div>div>input {{ 
        background-color: #F7F7F7 !important; 
        border: none !important; 
        border-radius: 12px !important;
        height: 3.5rem !important;
        text-align: center;
        font-size: 1.2rem !important;
        font-weight: 700;
    }}

    /* 4. QR Code 完美容器 */
    .qr-wrapper {{
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        margin: 25px 0 !important;
    }}
    .qr-frame {{
        width: 200px;
        height: 200px;
        background: #FFF;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
    }}
    .qr-frame img {{
        max-width: 90%;
        height: auto;
    }}

    /* 5. 金額顯示 */
    .price-box {{
        text-align: center;
        margin-top: 10px;
    }}
    .price-val {{ font-size: 4rem; font-weight: 900; letter-spacing: -2px; color: #000; }}
    .price-unit {{ font-size: 1.2rem; font-weight: 800; margin-left: 5px; }}
    
    /* 6. 狀態文字 */
    .status-text {{
        color: #00C853;
        font-weight: 800;
        font-size: 0.9rem;
        text-align: center;
        margin: 15px 0;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 3.0 介面渲染 ---

# 標題區
st.markdown('<div class="brand-box"><p class="brand-header">TAIWAN STOCKS 1.0</p><p class="main-title">真相底牌 一秒開牌</p></div>', unsafe_allow_html=True)

if not st.session_state.payment_confirmed:
    # 輸入區
    stock_code = st.text_input("", placeholder="輸入股票代號", label_visibility="collapsed")
    
    # 狀態監測
    if stock_code:
        st.markdown(f'<p class="status-text">● 正在監測 {stock_code} 入帳狀態...</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p class="status-text" style="color:#CCC;">● 等待輸入代號</p>', unsafe_allow_html=True)

    # QR Code 顯示
    img_path = next(Path('.').glob('*.png'), None) or next(Path('.').glob('*.jpg'), None)
    if img_path:
        with open(img_path, "rb") as f:
            img_b64 = base64.b64encode(f.read()).decode()
        st.markdown(f'''
            <div class="qr-wrapper">
                <div class="qr-frame">
                    <img src="data:image/png;base64,{img_b64}">
                </div>
            </div>
            ''', unsafe_allow_html=True)
    else:
        st.markdown('<div class="qr-wrapper"><div class="qr-frame" style="color:#EEE; font-size:0.7rem;">無圖片</div></div>', unsafe_allow_html=True)

    # 金額顯示
    st.markdown(f'<div class="price-box"><span class="price-val">{get_final_price():.2f}</span><span class="price-unit">TWD</span></div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#999; font-size:0.8rem;">請支付精確金額即可自動解密</p>', unsafe_allow_html=True)

    # 若要測試自動跳轉，取消下方兩行註釋
    # time.sleep(3)
    # st.session_state.payment_confirmed = True
    # st.rerun()

else:
    # 成功支付後的開牌畫面
    st.balloons()
    st.markdown(f"""
        <div style="background:#000; color:#FFF; padding:30px; border-radius:20px; text-align:center; margin-top:20px;">
            <p style="font-size:0.9rem; opacity:0.7;">{stock_code} 訊號解碼完成</p>
            <h1 style="color:#FF3B30;">強勢進場</h1>
            <hr style="border-color:#333;">
            <p>主力籌碼高度集中</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("查詢下一檔", use_container_width=True):
        st.session_state.payment_confirmed = False
        st.session_state.random_cents = random.randint(1, 99)
        st.rerun()
