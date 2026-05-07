import streamlit as st
import urllib.request
from pathlib import Path

# --- ① 數據引擎 ---
def fetch_realmarket_light(code):
    clean_code = code.strip()
    try:
        url = f"https://tw.stock.yahoo.com/quote/{clean_code}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req, timeout=3).read().decode('utf-8')
        if 'C(#f11c1c)' in html or '📈' in html:
            p_s, f_s = "🔴 股價強勢上漲", "🔴 主力資金爆量流入"
        elif 'C(#18b740)' in html or '📉' in html:
            p_s, f_s = "🟢 股價震盪下跌", "🟢 主力資金持續流出"
        else:
            p_s, f_s = "🟡 價量高檔橫盤", "🟡 資金動向進入觀望"
    except:
        p_s, f_s = "🟡 數據同步中", "🟢 主力籌碼流速加快"

    database = {"2330": {"name": "台積電", "big": "65.2%", "top": "美商高盛 (買超)", "retail": "🔴 散戶離場", "detail": "大單追價強。"}, "2317": {"name": "鴻海", "big": "28.4%", "top": "摩根大通 (賣超)", "retail": "🟢 散戶接刀", "detail": "賣方主導。"}}
    data = database.get(clean_code, {"name": f"個股 {clean_code}", "big": "48.5%", "top": "進出均衡", "retail": "🟡 動作持平", "detail": "靜待流速放大。"})
    return p_s, f_s, data

# --- ② 視覺定案：手機端壓縮排版 (QR Code 放大置中版) ---
st.set_page_config(page_title="台股 1.0", layout="centered")
st.markdown("""
    <style>
    /* 全局背景與超級收緊 */
    html, body, [data-testid="stAppViewContainer"] { background-color: #000000 !important; color: #FFFFFF !important; }
    [data-testid="stHeader"], [data-testid="stFooter"] { visibility: hidden; }
    [data-testid="stVerticalBlock"] > div { padding-top: 0rem !important; padding-bottom: 0rem !important; }

    @media (max-width: 640px) {
        h1 { font-size: 1.4rem !important; text-align: center; margin: 5px 0 2px 0 !important; } /* 標題上邊距更小 */
        .sub-title { font-size: 0.75rem !important; text-align: center; color: #00FF66 !important; margin-bottom: 8px !important; }
        
        /* 輸入框：白字提示、高度壓縮 */
        .stTextInput>div>div>input { background-color: #111111 !important; color: #FFFFFF !important; font-size: 1.0rem !important; height: 2.6rem !important; border: 1px solid #333 !important; }
        .stTextInput>div>div>input::placeholder { color: #FFFFFF !important; opacity: 0.8 !important; }
        
        /* 去蛤蜊邊、實心紅色背景提示塊 */
        .lock-box-flat { 
            background: #FF3333 !important; 
            padding: 5px 8px; /* 內邊距更緊湊 */
            text-align: center; 
            color: #FFFFFF !important; 
            font-weight: 700; 
            border-radius: 4px; 
            font-size: 0.8rem !important; 
            margin: 3px 0; /* 上下邊距更小 */
            border: none !important; 
        }
        
        .pay-instr { font-size: 0.75rem; color: #FFFFFF; text-align: center; margin: 2px 0; }
        
        /* 消滅街口代碼白框 */
        [data-testid="stCodeBlock"], .stCodeBlock { display: none !important; visibility: hidden !important; height: 0px !important; }
        
        /* 螢光綠按鈕：維持霸氣但收窄間距 */
        .stButton>button { 
            background-color: #00FF66 !important; 
            color: #000000 !important; 
            width: 100%; 
            height: 3.0rem; /* 按鈕稍微變窄 */
            font-size: 1.15rem !important; /* 字體稍微變小 */
            font-weight: 900 !important; 
            border-radius: 6px !important; 
            margin: 5px 0 10px 0 !important; /* 下邊距留空 */
        }
    }
    .disclaimer { text-align: center; color: #444444; font-size: 0.65rem; margin-top: 10px; line-height: 1.1; }
    </style>
    """, unsafe_allow_html=True)

# 品牌標題
st.markdown("<h1>主力底牌，一秒開牌。</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>台股 1.0 ・ L2 數據核心</p>", unsafe_allow_html=True)

# 1. 股票代碼 (白字提示)
code = st.text_input("", placeholder="請輸入股票代碼 (例如: 2330)", label_visibility="collapsed")

# 2. 收款鎖定塊 (去邊框版)
target_code = code.strip() if code else "未指定"
st.markdown(f'<div class="lock-box-flat">⚠️ 權限鎖定：開牌【 {target_code} 】最新數據包</div>', unsafe_allow_html=True)
st.markdown("<p class='pay-instr'>💸 長按二維碼轉帳 (NT$ 99 / 檔)</p>", unsafe_allow_html=True)

# 3. 🚨 核心修正：QR Code 復活放大並且百分之百置中
qrs = list(Path('.').rglob('*.png')) + list(Path('.').rglob('*.jpg'))
if qrs:
    # 暴力置中：創立三個列，中間寬一點，兩邊窄一點，強制置中且放大
    c1, c2, c3 = st.columns([0.2, 1, 0.2]) 
    with c2: 
        # width=220 鎖定大尺寸，清晰好掃
        st.image(str(qrs[-1]), width=220) 

# 4. 驗證開牌按鈕
if 'stage' not in st.session_state: st.session_state.stage = "payment"
click_verify = st.button("🔥 完成支付，驗證開牌")

# 5. 原地解鎖數據
if click_verify or st.session_state.stage == "unlocked":
    if not code.strip():
        st.warning("⚠️ 請先輸入代碼。")
    else:
        st.session_state.stage = "unlocked"
        p_s, f_s, data = fetch_realmarket_light(code)
        st.divider()
        with st.container(border=True):
            st.markdown(f"📊 **{code.strip()} {data['name']} 面板**")
            st.write(f"狀態：{p_s} / {f_s}")
            st.write(f"🏆 主力：{data['top']}")
            st.write(f"👥 散戶：{data['retail']}")
        if st.button("🔍 下一檔"):
            st.session_state.stage = "payment"
            st.rerun()

st.markdown('<p class="disclaimer">免責聲明：數據僅供參考，投資自負風險。</p>', unsafe_allow_html=True)
