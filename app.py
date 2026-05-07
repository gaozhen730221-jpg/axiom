import streamlit as st
from pathlib import Path

# --- ① 視覺與行動端精簡排版定案 ---
st.set_page_config(page_title="台股 1.0", layout="centered")

# 使用暴力強制的強制 CSS 將行動端字體變小、收緊排版
st.markdown("""
    <style>
    /* 全局收緊 */
    [data-testid="stAppViewContainer"] { background-color: #000000; color: #FFFFFF; }
    [data-testid="stHeader"], [data-testid="stFooter"] { visibility: hidden; }
    [data-testid="stVerticalBlock"] > div { padding-top: 0rem !important; padding-bottom: 0.2rem !important; }

    /* ====== 🚀 核心修正：行動端降維壓縮 ====== */
    /* 針對手機屏幕的媒體查詢 */
    @media (max-width: 640px) {
        /* 主標題：變為單排小字 */
        h1 { font-size: 1.6rem !important; font-weight: 700 !important; text-align: center; color: #FFFFFF !important; margin: 10px 0 5px 0 !important; white-space: nowrap; }
        
        /* 副標題：變為极小號字 */
        .sub-title { font-size: 0.8rem !important; text-align: center; color: #00FF66 !important; margin: 0 0 15px 0 !important; }
        
        /* 輸入框：小號、緊湊 */
        .stTextInput>div>div>input { background-color: #111111 !important; color: #FFFFFF !important; font-size: 1.0rem !important; height: 3.0rem !important; margin-bottom: 10px; }
        .stTextInput>div>div>input::placeholder { font-size: 0.9rem !important; opacity: 1 !important; color: #AAAAAA !important; }
        
        /* 收款鎖定框：變極窄、字體變極小 */
        .lock-box { border: 2px solid #FF3333; padding: 10px; background: #110505; color: #FF3333; font-weight: 700; border-radius: 8px; font-size: 0.9rem !important; margin: 10px 0; }
        
        /* 轉帳文字說明：小號灰色 */
        .pay-instr { font-size: 0.8rem; color: #AAAAAA; text-align: center; margin: 5px 0 10px 0; }
        
        /* 街口代碼區域：緊湊排版、小號字 */
        stCodeBlock { padding: 5px !important; margin: 5px 0 !important; }
        .stCodeBlock code { font-size: 0.8rem !important; }
        
        /* 綠色大按鈕：收窄 */
        .stButton>button { background-color: #00FF66 !important; color: #000000 !important; width: 100%; height: 3.8rem; font-size: 1.3rem !important; font-weight: 800 !important; border-radius: 8px !important; margin: 10px 0; }
    }
    
    /* 免責聲明：行動端小號字 */
    .disclaimer { text-align: center; color: #555555; font-size: 0.8rem; margin-top: 30px; line-height: 1.4; padding: 0 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- ② 頂部固定品牌 ---
st.markdown("<h1>主力底牌，一秒開牌。</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>台股 1.0 ・ L2 數據核心</p>", unsafe_allow_html=True)

# 輸入框
code = st.text_input("", placeholder="請輸入股票代碼 (例如: 2330)", label_visibility="collapsed")

# --- ③ 商業漏斗：全開模式 ---
st.divider()

# 收款鎖定卡片（行動端壓縮）
target_code = code.strip() if code else "未指定"
st.markdown(f'<div class="lock-box">⚠️ 權限鎖定：開牌【 {target_code} 】最新L2籌碼數據包</div>', unsafe_allow_html=True)

# 轉帳說明
st.markdown("<p class='pay-instr pay-instr-white'>💸 長按儲存二維碼轉帳 (NT$ 99 / 檔)</p>", unsafe_allow_html=True)

# 自動偵測 QR Code 圖片
qrs = list(Path('.').rglob('*.png')) + list(Path('.').rglob('*.jpg'))
if qrs:
    col_l, col_m, col_r = st.columns([1, 2, 1])
    with col_m: 
        st.image(str(qrs[-1]), use_container_width=True)

st.code("街口代碼：396\n街口帳號：910080767\n金額：新台幣 99 元", language="text")
st.divider()

if 'stage' not in st.session_state: st.session_state.stage = "payment"
click_verify = st.button("🔥 完成支付，驗證開牌")

# 底部免責
st.markdown("""
    <p class="disclaimer">
        免責聲明：本平台僅提供客觀數據視覺化結果，不包含任何主觀投資買賣建議。歷史數據不代表未來表現。投資人應獨立判斷並自負風險。
    </p>
    """, unsafe_allow_html=True)
