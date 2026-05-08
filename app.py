import streamlit as st
import random
import time
from pathlib import Path

# --- ① 核心：隨機金額與自動對帳狀態 ---
if 'random_cents' not in st.session_state:
    st.session_state.random_cents = random.randint(1, 99)
    st.session_state.payment_confirmed = False

def get_final_price():
    return round(99 + (st.session_state.random_cents / 100), 2)

# 模擬後端抓取：實際執行時，這裡會去接 API 或刷帳單截圖 OCR
def check_payment_status(target_price):
    # 這裡放對接邏輯，目前模擬「等待中」
    return st.session_state.payment_confirmed

# --- ② 視覺定案：1.0 SIGNAL 白金款 ---
st.set_page_config(page_title="1.0 SIGNAL", layout="centered")
st.markdown(f"""
    <style>
    html, body, [data-testid="stAppViewContainer"] {{ background-color: #FFFFFF !important; color: #000000 !important; }}
    [data-testid="stHeader"], [data-testid="stFooter"] {{ visibility: hidden; }}
    
    @media (max-width: 640px) {{
        .brand-header {{ font-size: 0.85rem; font-weight: 900; text-align: center; margin-top: 20px; }}
        .main-title {{ font-size: 1.5rem; font-weight: 800; text-align: center; margin: 15px 0; }}
        .pay-card {{
            border: 1px solid #F2F2F2;
            border-radius: 25px;
            padding: 20px;
            margin: 20px 0;
            text-align: center;
            box-shadow: 0 10px 40px rgba(0,0,0,0.04);
        }}
        .price-val {{ font-size: 3.2rem !important; font-weight: 900; margin: 10px 0; }}
        .sync-status {{ color: #00C853; font-size: 0.8rem; font-weight: 800; }}
        .waiting-box {{ 
            background: #F8F8F8; border-radius: 12px; padding: 15px; 
            text-align: center; font-weight: 700; color: #666; margin-top: 10px;
        }}
    }}
    </style>
    """, unsafe_allow_html=True)

# --- ③ 介面呈現 ---
st.markdown('<p class="brand-header">TAIWAN STOCKS 1.0</p>', unsafe_allow_html=True)
st.markdown('<p class="main-title">真相底牌 一秒開牌</p>', unsafe_allow_html=True)

# 1. 輸入區
code = st.text_input("", placeholder="輸入驗證代碼 / 股票地址", label_visibility="collapsed")

if not st.session_state.payment_confirmed:
    # 2. 支付卡片 (未付錢狀態)
    price = get_final_price()
    st.markdown('<div class="pay-card">', unsafe_allow_html=True)
    st.markdown('<p class="sync-status">● 正在監測入帳中...</p>', unsafe_allow_html=True)
    
    qrs = list(Path('.').glob('*.png')) + list(Path('.').glob('*.jpg'))
    if qrs: st.image(str(qrs[0]), width=200)
    
    st.markdown(f'<p class="price-val">{price} <span style="font-size:1.2rem;">TWD</span></p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 3. 自動刷新狀態 (Polling)
    st.markdown('<div class="waiting-box">等待支付中，系統抓取入帳後將自動解密...</div>', unsafe_allow_html=True)
    
    # 🚨 執行長注意：這裡就是「自動抓取」的循環
    # 在實際部署時，這裡會放一個 check API，如果抓到 99.01，就 set payment_confirmed = True
    time.sleep(2) 
    st.rerun() 

else:
    # 4. 🚨 支付成功後自動跳出來的結果頁面
    st.balloons()
    st.success(f"✅ 已確認入帳 {get_final_price()} TWD！正在開牌...")
    st.markdown(f"### 📊 {code} 核心數據")
    st.write("🔴 主力資金爆量流入")
    st.write("🏆 核心籌碼：美商高盛 (淨買超)")
    # 此處直接顯示數據結果，不需再點按鈕
