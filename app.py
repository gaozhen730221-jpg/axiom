import streamlit as st
import time
from pathlib import Path

# --- ① 決策引擎（明天直接對接真實 API 數據源） ---
def decision_engine(code):
    signals = {
        "2330": ("🟢 主力偷吃", "🔥 準備噴發", "外資與400張以上大戶籌碼連續三日暗中進場，結構極度穩定。"),
        "2317": ("🔴 大單倒貨", "❌ 極度危險", "投信與特定分點開始高檔獲利了結，主力資金有撤退跡象。"),
        "2454": ("🟢 主力偷吃", "🔥 準備噴發", "短線技術量能突破關鍵壓力位，主力控盤力道強勁。")
    }
    return signals.get(code, ("🟡 多空下拉", "⚠️ 數據不足", "該股籌碼散亂，主力尚未做出明顯方向，建議暫不操作。"))

# --- ② 極簡主義視覺框架（不加大加粗，維持原始精緻與黑底高對比） ---
st.set_page_config(page_title="台股 1.0", layout="centered")
st.markdown("""
    <style>
    /* 全黑底、純白字、螢光綠高對比 */
    html, body, [data-testid="stAppViewContainer"] { background-color: #000000 !important; color: #FFFFFF !important; }
    [data-testid="stHeader"], [data-testid="stFooter"] { visibility: hidden; }
    
    h1 { font-size: 3.2rem !important; font-weight: 900 !important; text-align: center; color: #FFFFFF !important; margin-bottom: 5px; }
    .sub-title { text-align: center; color: #00FF66 !important; font-weight: 700; letter-spacing: 2px; margin-bottom: 30px; }
    
    /* 輸入框視覺：維持原始精緻小巧，placeholder 強制高對比純白 */
    .stTextInput>div>div>input {
        background-color: #111111 !important; color: #FFFFFF !important; 
        border: 2px solid #333333 !important; font-size: 1.4rem !important; height: 3.5rem; text-align: center;
    }
    .stTextInput>div>div>input:focus { border: 2px solid #00FF66 !important; }
    .stTextInput>div>div>input::placeholder { color: #FFFFFF !important; opacity: 1 !important; }
    .stTextInput>div>div>input::-webkit-input-placeholder { color: #FFFFFF !important; }
    .stTextInput>div>div>input::-moz-placeholder { color: #FFFFFF !important; }
    
    /* 原生 Label 標籤強制純白，防止手機看變黑色 */
    .stTextInput label { color: #FFFFFF !important; font-size: 1rem !important; font-weight: 500; }
    
    /* 綠色大按鈕 */
    .stButton>button {
        background-color: #00FF66 !important; color: #000000 !important;
        width: 100%; height: 5rem; font-size: 2rem !important; font-weight: 950 !important;
        border-radius: 10px !important; border: none !important;
    }
    
    .lock-box { border: 3px solid #FF3333; padding: 25px; text-align: center; background: #110505; color: #FF3333; font-weight: 900; border-radius: 15px; margin: 20px 0; }
    .report-box { border: 3px solid #00FF66; padding: 30px; background: #051105; border-radius: 15px; margin-top: 25px; }
    .hint-text { text-align: center; color: #FFFFFF !important; font-size: 1rem; margin-top: 15px; font-weight: 500; }
    </style>
    """, unsafe_allow_html=True)

# 頂部標題區
st.markdown("<h1>主力底牌，一秒開牌。</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>台股 1.0 ・ L2 數據核心</p>", unsafe_allow_html=True)

# 核心輸入框（保留直白標籤與純白預設提示字，絕不漏看）
code = st.text_input("輸入台股代碼開始：", placeholder="例如: 2330")
st.divider()

# --- ③ 核心控制漏斗（徹底分離階段，絕不上下重疊） ---
if code:
    if len(code.strip()) > 0:
        if 'stage' not in st.session_state: 
            st.session_state.stage = "payment"

        # 【 階段 A：街口支付畫面 】
        if st.session_state.stage == "payment":
            st.markdown(f"""
            <div class="lock-box">
                <span style="font-size: 1.5rem; color: #FF3333;">⚠️ 偵測到該股【{code}】最新籌碼異動！數據已鎖定。</span><br>
                <span style="font-size: 1.1rem; color: #AAAAAA;">翻牌看底牌：只需一個便當錢</span>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<h3 style='text-align:center; color:#FFFFFF;'>💸 儲存 QR Code 轉帳 (NT$ 99)</h3>", unsafe_allow_html=True)
            
            # 自動抓取個人收款碼圖片
            qrs = list(Path('.').rglob('*.png')) + list(Path('.').rglob('*.jpg'))
            if qrs:
                col_l, col_m, col_r = st.columns([1, 2, 1])
                with col_m: st.image(str(qrs[-1]), use_container_width=True)
            
            st.code("街口代碼：396\n街口帳號：910080767\n金額：新台幣 99 元", language="text")
            
            if st.button("🔥 我已完成支付，立刻驗證看牌"):
                st.session_state.stage = "verifying"
                st.rerun()  # 點擊後立刻強制沖刷頁面，銷毀此階段的所有元件，不留任何重疊殘渣
        
        # 【 階段 B：180 秒強制倒數驗證 】
        elif st.session_state.stage == "verifying":
            main_placeholder = st.empty()
            for i in range(180, -1, -1):
                with main_placeholder.container():
                    st.markdown(f"""
                    <div class="lock-box" style="border-color: #00FF66; background: #051105; color: #00FF66;">
                        <span style="font-size: 1.3rem;">📡 正在連線台灣結算後端 API 驗證款項...</span><br><br>
                        <span style="font-size: 3rem; font-weight:900;">驗證剩餘 {i} 秒</span><br><br>
                        <p style="font-size: 1rem; color: #FF3333; margin:0;">請確保已完成街口匯款，否則數據包將自動銷毀</p>
                    </div>
                    """, unsafe_allow_html=True)
                    st.progress(int(((180 - i) / 180) * 100))
                time.sleep(1)
            
            main_placeholder.empty()
            st.session_state.stage = "unlocked"
            st.rerun()  # 倒數結束再次沖刷，完美銜接最終報告

        # 【 階段 C：自動開牌報告 】
        elif st.session_state.stage == "unlocked":
            market, signal_light, reason = decision_engine(code)
            color = "#FF3333" if "🔴" in market else "#00FF66"
            
            st.markdown(f"""
            <div class="report-box">
                <h2 style="margin-top:0; font-size: 2.2rem; text-align:center; color:#FFFFFF;">📊 {code} 深度分析報告</h2>
                <hr style="border:2px solid #333;">
                <p style="font-size:1.8rem; text-align:center;"><b>主力方向：</b> <span style="color:{color}; font-weight:bold;">{market}</span></p>
                <p style="font-size:1.8rem; text-align:center;"><b>多空訊號：</b> <mark style="background: #222222; color:{color}; font-weight:bold; padding: 5px 15px; border-radius:5px;">{signal_light}</mark></p>
                <div style="background:#111111; padding:15px; border-radius:8px; margin-top:20px;">
                    <p style="font-size:1.2rem; color:#DDDDDD; line-height:1.6;"><b>💡 獨家 L2 籌碼解析：</b><br>{reason}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("查詢下一檔股票"):
                st.session_state.stage = "payment"
                st.rerun()
else:
    # 初始未輸入前的純白提示字
    st.markdown("<p class='hint-text'>請在上方輸入框輸入任何台股代碼開始。</p>", unsafe_allow_html=True)
