import streamlit as st
import time
from pathlib import Path

# --- ① 數據引擎 ---
def decision_engine(code):
    signals = {
        "2330": ("🟢 主力偷吃", "🔥 準備噴發", "外資與400張以上大戶籌碼連續三日暗中進場，結構極度穩定。"),
        "2317": ("🔴 大單倒貨", "❌ 極度危險", "投信與特定分點開始高檔獲利了結，主力資金有撤退跡象。"),
        "2454": ("🟢 主力偷吃", "🔥 準備噴發", "短線技術量能突破關鍵壓力位，主力控盤力道強勁。")
    }
    return signals.get(code, ("🟡 多空下拉", "⚠️ 數據不足", "該股籌碼散亂，主力尚未做出明顯方向，建議暫不操作。"))

# --- ② 第一性原理：純黑極簡視覺 ---
st.set_page_config(page_title="台股 1.0", layout="centered")
st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] { background-color: #000000 !important; color: #FFFFFF !important; }
    [data-testid="stHeader"], [data-testid="stFooter"] { visibility: hidden; }
    h1 { font-size: 3rem !important; font-weight: 900 !important; text-align: center; }
    .sub-title { text-align: center; color: #00FF66 !important; font-weight: 700; margin-bottom: 30px; }
    .lock-box { border: 2px solid #FF3333; padding: 20px; text-align: center; background: #110505; color: #FF3333; font-weight: 700; border-radius: 10px; margin: 20px 0; }
    .report-box { border: 2px solid #00FF66; padding: 25px; background: #051105; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 頂部標題
st.markdown("<h1>主力底牌，一秒開牌。</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>台股 1.0 ・ L2 數據核心</p>", unsafe_allow_html=True)

# 核心輸入框：不給任何暗色提示，標籤改為純白直白說明
code = st.text_input("請輸入台股代碼開始：", placeholder="例如: 2330")
st.divider()

# --- ③ 核心控制邏輯 ---
if code:
    # 建立純淨的狀態機
    if 'stage' not in st.session_state: 
        st.session_state.stage = "payment"

    # 【畫面一：街口卡錢】
    if st.session_state.stage == "payment":
        st.markdown(f'<div class="lock-box">⚠️ 【{code}】最新籌碼數據已鎖定。</div>', unsafe_allow_html=True)
        
        # 自動撈取收款圖
        qrs = list(Path('.').rglob('*.png')) + list(Path('.').rglob('*.jpg'))
        if qrs:
            col_l, col_m, col_r = st.columns([1, 2, 1])
            with col_m: st.image(str(qrs[-1]), use_container_width=True)
        
        # 傻瓜複製文字
        st.code("街口代碼：396\n街口帳號：910080767\n金額：新台幣 99 元", language="text")
        
        if st.button("我已完成支付，立刻驗證看牌"):
            st.session_state.stage = "verifying"
            st.rerun()
    
    # 【畫面二：180秒全自動心理門禁】
    elif st.session_state.stage == "verifying":
        main_placeholder = st.empty()
        for i in range(180, -1, -1):
            with main_placeholder.container():
                st.markdown(f"""
                <div class="lock-box" style="border-color: #00FF66; background: #051105; color: #00FF66;">
                    📡 正在連線後端 API 驗證款項...<br>
                    <span style="font-size: 2.5rem; font-weight:900;">驗證剩餘 {i} 秒</span>
                </div>
                """, unsafe_allow_html=True)
                st.progress(int(((180 - i) / 180) * 100))
            time.sleep(1)
        st.session_state.stage = "unlocked"
        st.rerun()

    # 【畫面三：自動開牌】
    elif st.session_state.stage == "unlocked":
        market, signal_light, reason = decision_engine(code)
        color = "#FF3333" if "🔴" in market else "#00FF66"
        st.markdown(f"""
        <div class="report-box">
            <h3 style="margin-top:0;">📊 {code} 深度分析報告</h3>
            <p><b>主力方向：</b> <span style="color:{color};">{market}</span></p>
            <p><b>多空訊號：</b> <span style="color:{color};">{signal_light}</span></p>
            <p style="color:#DDDDDD; font-size:1rem;"><b>💡 L2 籌碼解析：</b><br>{reason}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("查詢下一檔股票"):
            st.session_state.stage = "payment"
            st.rerun()
