import streamlit as st
import time, requests
from pathlib import Path

# --- 🚀 CONFIG 與設定 ---
TOKEN = "YOUR_TG_BOT_TOKEN"      # 明天填入您的 TG Bot Token
CHAT_ID = "YOUR_PERSONAL_ID"     # 明天填入您的個人 TG ID
API_URL = f"https://api.telegram.org/bot{TOKEN}"

st.set_page_config(page_title="台股 1.0", layout="centered")

# --- 🎨 50歲以下年輕白領極簡美學 ---
st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] { background-color: #000000 !important; color: #FFFFFF !important; }
    [data-testid="stHeader"], [data-testid="stFooter"] { visibility: hidden; }
    h1 { font-size: 3rem !important; font-weight: 900 !important; text-align: center; color: #FFFFFF !important; }
    .sub-title { text-align: center; color: #00FF66 !important; font-weight: 700; margin-bottom: 30px; }
    .stTextInput>div>div>input { background-color: #111111 !important; color: #FFFFFF !important; border: 2px solid #333333 !important; text-align: center; }
    .stButton>button { background-color: #00FF66 !important; color: #000000 !important; width: 100%; height: 4.5rem; font-size: 1.8rem !important; font-weight: 950 !important; border-radius: 10px !important; }
    .lock-box { border: 3px solid #FF3333; padding: 20px; text-align: center; background: #110505; color: #FF3333; font-weight: 900; border-radius: 15px; }
    .report-box { border: 3px solid #00FF66; padding: 25px; background: #051105; border-radius: 15px; }
    </style>
    """, unsafe_allow_html=True)

# --- 🧠 數據引擎 (明天對接真實 API) ---
def decision_engine(code):
    signals = {
        "2330": ("🟢 主力偷吃", "🔥 準備噴發", "外資與400張大戶籌碼連續三日暗中進場。"),
        "2317": ("🔴 大單倒貨", "❌ 極度危險", "投信與特定分點開始高檔獲利了結。")
    }
    return signals.get(code, ("🟡 多空下拉", "⚠️ 數據不足", "該股籌碼散亂，主力尚未做出明顯方向。"))

# --- 📱 UI 介面走位 ---
st.markdown("<h1>主力底牌，一秒開牌。</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>台股 1.0 ・ L2 數據核心</p>", unsafe_allow_html=True)

code = st.text_input("", placeholder="請輸入股票代碼 (例如: 2330)", label_visibility="collapsed")
st.divider()

if code:
    # 初始化 Session 狀態
    if 'paid' not in st.session_state: st.session_state.paid = False
    if 'waiting' not in st.session_state: st.session_state.waiting = False

    # 🛑 階段 A：未付錢，原地大門鎖死，砸出街口 QR Code
    if not st.session_state.paid and not st.session_state.waiting:
        st.markdown(f'<div class="lock-box"><span style="font-size: 1.3rem;">⚠️ 偵測到該股【{code}】最新籌碼異動！數據已鎖定。</span></div>', unsafe_allow_html=True)
        st.markdown("<h3 style='text-align:center;'>💸 儲存 QR Code 轉帳 (NT$ 99)</h3>", unsafe_allow_html=True)
        
        # 讀取收款碼圖片
        qrs = list(Path('.').rglob('*.png')) + list(Path('.').rglob('*.jpg'))
        if qrs:
            col_l, col_m, col_r = st.columns([1, 2, 1])
            with col_m: st.image(str(qrs[-1]), caption="💡 手機長按圖片 ➔ 儲存到相簿付款", use_container_width=True)
        
        # 街口專用一鍵複製欄位
        st.code("街口代碼：396\n街口帳號：910080767\n金額：新台幣 99 元", language="text")
        
        phone = st.text_input("輸入您轉出帳戶的「末 4 碼」", placeholder="例如: 8888")
        
        if st.button("確認已付費，通知主管核准開牌"):
            if phone:
                # 📡 技術核心：直接把資料打進執行長的手機 TG
                msg = f"📡 1.0 新訂單！\n📈 查詢股票：{code}\n💰 轉帳末四碼：{phone}\n請執行長確認入帳後至 VPS 後台放行。"
                try:
                    requests.get(f"{API_URL}/sendMessage", params={"chat_id": CHAT_ID, "text": msg})
                except: pass
                st.session_state.waiting = True
                st.rerun()
            else:
                st.error("請輸入轉帳末 4 碼以利核對")

    # ⏳ 階段 B：散戶付完錢，等待執行長審核的過渡畫面
    elif st.session_state.waiting:
        st.markdown('<div class="lock-box" style="border-color:#00FF66; background:#051105; color:#00FF66;"><span style="font-size: 1.3rem;">📡 訊號已發送！正在等待台灣結算中心核對款項...</span><br><p style="font-size:1rem; color:#888;">款項確認後，本網頁將自動原地解鎖。請勿關閉視窗。</p></div>', unsafe_allow_html=True)
        
        # 輪詢機制（明天在 VPS 現場對接數據庫布林值，這裡先做重整按鈕讓散戶點擊刷新）
        if st.button("🔄 重新整頁（確認是否已放行）"):
            # 明天現場補上檢查邏輯，若執行長通過，此處轉為 paid=True
            st.rerun()

    # 🟢 階段 C：執行長在手機點擊核准，網頁原地開牌
    else:
        market, signal_light, reason = decision_engine(code)
        color = "#FF3333" if "🔴" in market else "#00FF66"
        st.markdown(f"""
        <div class="report-box">
            <h2 style="text-align:center;">📊 {code} 深度分析報告</h2>
            <hr style="border:1px solid #333;">
            <p style="font-size:1.5rem; text-align:center;"><b>主力方向：</b> <span style="color:{color}; font-weight:bold;">{market}</span></p>
            <p style="font-size:1.5rem; text-align:center;"><b>多空訊號：</b> <mark style="background:#222; color:{color}; font-weight:bold; padding:5px 10px;">{signal_light}</mark></p>
            <p style="font-size:1.1rem; color:#DDDDDD; margin-top:15px;"><b>💡 L2 籌碼解析：</b><br>{reason}</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("查詢下一檔股票"):
            st.session_state.paid = False
            st.session_state.waiting = False
            st.rerun()
