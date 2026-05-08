import streamlit as st
import random
import time
import base64
from pathlib import Path

# --- 1.0 SIGNAL 第一性原理：核心指紋定價與自動對帳邏輯 ---
# 確保隨機金額在 session 中保持不變，直到支付成功
if 'random_cents' not in st.session_state:
    st.session_state.random_cents = random.randint(1, 99)
    st.session_state.payment_confirmed = False

def get_final_price():
    # 🚨 核心：99 塊台幣 (TWD) + 隨機指紋小數點 (例如 99.70)
    return round(99 + (st.session_state.random_cents / 100), 2)

# --- 2.0 視覺 UI 定案：台股 1.0 極簡白金款 ---
st.set_page_config(page_title="TAIWAN STOCKS 1.0", layout="centered")

# 消滅空格、鎖定比例、確保 QR Code 尺寸適中
st.markdown(f"""
    <style>
    /* 全局純白背景，消除視覺噪音 */
    html, body, [data-testid="stAppViewContainer"] {{ 
        background-color: #FFFFFF !important; 
        color: #000000 !important; 
    }}
    [data-testid="stHeader"], [data-testid="stFooter"] {{ visibility: hidden; }}

    /* 🚨 核心修正：徹底消滅 Streamlit 元件間的預設白色空格 */
    [data-testid="stVerticalBlock"] > div {{ 
        padding: 0 !important; 
        margin: 0 !important; 
    }}
    
    .brand-header {{ 
        font-size: 0.85rem; 
        font-weight: 900; 
        text-align: center; 
        margin-top: 30px !important; 
        letter-spacing: 2px; 
        color: #000000; 
    }}
    .main-title {{ 
        font-size: 1.5rem; 
        font-weight: 800; 
        text-align: center; 
        margin: 10px 0 20px 0 !important; 
        color: #000000; 
    }}

    /* 輸入框：背景微灰區隔，高度適中，置中對齊 */
    .stTextInput {{ margin-top: -5px !important; padding: 0 20px !important; }}
    .stTextInput>div>div>input {{ 
        background-color: #F7F7F7 !important; 
        border: none !important;
        border-radius: 12px !important;
        height: 3.5rem !important;
        text-align: center;
        font-weight: 600;
        font-size: 1.1rem !important;
    }}

    /* QR Code 完美置中與尺寸鎖定 (190px) */
    .qr-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 20px 0 !important;
    }}
    .qr-container img {{
        width: 190px !important;
        height: auto !important;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }}

    /* 指紋金額大字體設計 */
    .price-val {{ 
        font-size: 3.8rem !important; 
        font-weight: 900; 
        text-align: center;
        margin: 10px 0 !important; 
        letter-spacing: -2px;
        color: #000000;
    }}
    .price-unit {{ font-size: 1.4rem; font-weight: 800; }}
    
    /* 狀態顯示 */
    .status-msg {{ 
        color: #00C853; 
        font-size: 0.85rem; 
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

# --- 3.0 介面呈現與自動對帳跳轉 ---

st.markdown('<p class="brand-header">TAIWAN STOCKS 1.0</p>', unsafe_allow_html=True)
st.markdown('<p class="main-title">真相底牌 一秒開牌</p>', unsafe_allow_html=True)

if not st.session_state.payment_confirmed:
    # --- 收款監測模式 ---
    
    # 1. 輸入股票代號
    code = st.text_input("", placeholder="輸入股票代號 (例如: 2330)", label_visibility="collapsed")
    
    st.markdown('<p class="status-msg">● 正在監測入帳中...</p>', unsafe_allow_html=True)

    # 2. 自動偵測 QR Code 並強制 190px 尺寸
    qrs = list(Path('.').glob('*.png')) + list(Path('.').glob('*.jpg'))
    if qrs:
        with open(qrs[0], "rb") as f:
            img_b64 = base64.b64encode(f.read()).decode()
        st.markdown(f'<div class="qr-container"><img src="data:image/png;base64,{img_b64}"></div>', unsafe_allow_html=True)
    else:
        st.error("⚠️ 檔案夾內找不到 QR Code 圖片")

    # 3. 顯示台灣指紋金額 (例如 99.70 TWD)
    price = get_final_price()
    st.markdown(f'<p class="price-val">{price} <span class="price-unit">TWD</span></p>', unsafe_allow_html=True)
    
    st.markdown('<p class="hint-bar">請支付精確金額，入帳後系統將自動解密開牌</p>', unsafe_allow_html=True)

    # 🚨 全自動監測跳轉
    # 實際部署後，此處將對接後端帳本 API
    time.sleep(4)
    st.rerun()

else:
    # --- 數據開牌模式 ---
    st.success(f"✅ 已確認入帳 {get_final_price()} TWD")
    st.divider()
    st.markdown(f"### 📊 {code} 實時訊號解密完成")
    st.write("🔴 主力資金流向：特大單進場")
    st.write("🏆 核心籌碼：同步 L2 數據中心")
