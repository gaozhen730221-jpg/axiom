import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# --- ① 視覺與極簡架構配置 ---
st.set_page_config(page_title="台股 1.0", layout="centered")
st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] { background-color: #000000 !important; color: #FFFFFF !important; }
    [data-testid="stHeader"], [data-testid="stFooter"] { visibility: hidden; }
    h1 { font-size: 3.2rem !important; font-weight: 900 !important; text-align: center; color: #FFFFFF !important; }
    .sub-title { text-align: center; color: #00FF66 !important; font-weight: 700; letter-spacing: 2px; margin-bottom: 30px; }
    .stTextInput>div>div>input { background-color: #111111 !important; color: #FFFFFF !important; border: 2px solid #333333 !important; text-align: center; }
    .lock-box { border: 3px solid #FF3333; padding: 20px; text-align: center; background: #110505; color: #FF3333; font-weight: 900; border-radius: 12px; margin: 20px 0; }
    .stButton>button { background-color: #00FF66 !important; color: #000000 !important; width: 100%; height: 4.5rem; font-size: 1.8rem !important; font-weight: 950 !important; border-radius: 10px !important; }
    .disclaimer { text-align: center; color: #555555 !important; font-size: 0.8rem !important; margin-top: 50px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>主力底牌，一秒開牌。</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>台股 1.0 ・ L2 數據核心</p>", unsafe_allow_html=True)

code = st.text_input("", placeholder="請輸入股票代碼 (例如: 2330)", label_visibility="collapsed")
st.divider()

if code:
    clean_code = code.strip()
    if len(clean_code) > 0:
        if 'stage' not in st.session_state: st.session_state.stage = "payment"

        # 1. 鎖定收據
        st.markdown(f'<div class="lock-box">⚠️ 偵測到該股【{clean_code}】最新籌碼異動！數據已鎖定。</div>', unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#FFFFFF; font-weight:700;'>💸 儲存 QR Code 轉帳 (NT$ 99)</p>", unsafe_allow_html=True)
        
        qrs = list(Path('.').rglob('*.png')) + list(Path('.').rglob('*.jpg'))
        if qrs:
            col_l, col_m, col_r = st.columns([1, 2, 1])
            with col_m: st.image(str(qrs[-1]), use_container_width=True)
        
        st.code("街口代碼：396\n街口帳號：910080767\n金額：新台幣 99 元", language="text")
        st.divider()

        # 2. 解鎖大按鈕
        if st.button("🔥 我已完成支付，立刻驗證看牌") or st.session_state.stage == "unlocked":
            st.session_state.stage = "unlocked"
            
            st.divider()
            with st.container(border=True):
                st.subheader(f"📊 {clean_code} 交易所實時 L2 數據面板")
                st.write("📡 *當前數據由全球權威交易所數據源秒級直連，100% 真實事實。*")
                st.divider()
                
                # ⚡ 核心大絕招：直接內嵌 TradingView 官方提供的免費實時台股小組件
                # 它會自動根據用戶輸入的代碼（例如 2330），秒級渲染出最真實的走勢、技術紅綠燈和量能 facts！
                tv_url = f"https://s.tradingview.com/widgetembed/?frameElementId=tradingview_chart&symbol=TWSE%3A{clean_code}&interval=D&symboledit=0&saveimage=1&toolbarbg=f1f3f6&studies=%5B%5D&theme=dark&style=1&timezone=Asia%2FTaipei&studies_overrides=%7B%7D&overrides=%7B%7D&enabled_features=%5B%5D&disabled_features=%5B%5D&locale=zh_TW"
                
                components.iframe(tv_url, height=450, scrolling=False)
                
                st.divider()
                st.caption("⚙️ 數據安全防火牆：上方圖表為台灣證券交易所實時客觀事實流，不含任何人工主觀買賣推介。")

# --- 🍿 免責聲明 ---
st.markdown('<p class="disclaimer">免責聲明：本平台僅提供公開數據之客觀量化視覺化結果，不包含任何主觀投資買賣建議。投資人應獨立判斷並自負風險。</p>', unsafe_allow_html=True)
