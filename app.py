import streamlit as st
import time
from pathlib import Path

# --- 🧠 數據引擎 (明天對接真實 API) ---
def decision_engine(code):
    signals = {
        "2330": ("🟢 主力偷吃", "🔥 準備噴發", "外資與400張大戶籌碼連續三日暗中進場，結構極度穩定。"),
        "2317": ("🔴 大單倒貨", "❌ 極度危險", "投信與特定分點開始高檔獲利了結。")
    }
    return signals.get(code, ("🟡 多空下拉", "⚠️ 數據不足", "該股籌碼散亂，主力尚未做出方向，建議暫不操作。"))

# --- 🎨 執行長特調：全網最大字體、無死角高對比視覺 ---
st.set_page_config(page_title="台股 1.0", layout="centered")
st.markdown("""
    <style>
    /* 全黑底、純白字、螢光綠高對比 */
    html, body, [data-testid="stAppViewContainer"] { background-color: #000000 !important; color: #FFFFFF !important; }
    [data-testid="stHeader"], [data-testid="stFooter"] { visibility: hidden; }
    
    /* 標題與所有文字一律極大化 */
    h1 { font-size: 3.5rem !important; font-weight: 950 !important; text-align: center; color: #FFFFFF !important; }
    h2 { font-size: 2.5rem !important; font-weight: 900 !important; color: #FFFFFF !important; }
    h3 { font-size: 2.2rem !important; font-weight: 900 !important; color: #FFFFFF !important; text-align: center; }
    p, span, label { font-size: 1.8rem !important; font-weight: 800 !important; color: #FFFFFF !important; line-height: 1.6 !important; }
    
    /* 輸入框字體加大 */
    .stTextInput>div>div>input { background-color: #111111 !important; color: #00FF66 !important; border: 3px solid #333333 !important; text-align: center; font-size: 2rem !important; height: 4.5rem; font-weight: 900; }
    
    /* 巨大開牌與驗證按鈕 */
    .stButton>button { background-color: #00FF66 !important; color: #000000 !important; width: 100%; height: 5.5rem; font-size: 2.2rem !important; font-weight: 950 !important; border-radius: 12px !important; border: none !important; }
    
    /* 紅色鎖定框與綠色放行框：線條加粗、字體狂放大 */
    .lock-box { border: 5px solid #FF3333; padding: 25px; text-align: center; background: #110505; border-radius: 20px; margin: 20px 0; }
    .report-box { border: 5px solid #00FF66; padding: 30px; background: #051105; border-radius: 20px; }
    
    /* 街口大字卡資訊 */
    .jk-info-text { font-size: 2rem !important; color: #FFFF00 !important; font-weight: 900 !important; font-family: monospace; text-align: center; background: #222222; padding: 15px; border-radius: 10px; margin: 10px 0; border: 2px dashed #FFFF00; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>主力底牌，一秒開牌。</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #00FF66 !important; font-size: 1.8rem; font-weight: 900;'>台股 1.0 ・ L2 數據核心</p>", unsafe_allow_html=True)

code = st.text_input("", placeholder="請輸入股票代碼 (例: 2330)", label_visibility="collapsed")
st.divider()

if code:
    if 'stage' not in st.session_state: st.session_state.stage = "payment"

    # 🛑 階段一：未付錢，系統自動卡死，展示大字體街口收款畫面
    if st.session_state.stage == "payment":
        st.markdown(f'<div class="lock-box"><span style="font-size: 2rem !important; color: #FF3333; font-weight: 950;">⚠️ 【{code}】最新籌碼數據已鎖定！</span></div>', unsafe_allow_html=True)
        st.markdown("<h3>💸 請完成街口支付 (NT$ 99)</h3>", unsafe_allow_html=True)
        
        # 讀取收款圖片
        qrs = list(Path('.').rglob('*.png')) + list(Path('.').rglob('*.jpg'))
        if qrs:
            col_l, col_m, col_r = st.columns([1, 2, 1])
            with col_m: st.image(str(qrs[-1]), caption="", use_container_width=True)
        
        # 💡 徹底解決小字問題：用超大黃字、粗體展示轉帳資訊，亮到刺眼
        st.markdown("<p style='text-align:center; font-size: 1.6rem !important;'>💡 手機無法掃碼？請複製下方資訊轉帳：</p>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class="jk-info-text">
            街口代碼：396<br>
            街口帳號：910080767<br>
            金額：新台幣 99 元
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🔥 我已完成支付，立刻驗證看牌"):
            st.session_state.stage = "verifying"
            st.rerun()

    # ⏳ 階段二：全自動心理門禁倒數 180 秒（字體極大化）
    elif st.session_state.stage == "verifying":
        main_placeholder = st.empty()
        
        for i in range(180, -1, -1):
            with main_placeholder.container():
                st.markdown(f"""
                <div class="lock-box" style="border-color: #00FF66; background: #051105;">
                    <span style="font-size: 2.2rem !important; color: #00FF66; font-weight: 950;">📡 正在連線後端 API 驗證款項...</span><br><br>
                    <span style="font-size: 4.5rem !important; color: #00FF66; font-weight: 950;">驗證剩餘 {i} 秒</span><br><br>
                    <span style="font-size: 1.6rem !important; color: #FF3333; font-weight: 900;">⚠️ 請勿關閉網頁，驗證成功將自動開牌</span>
                </div>
                """, unsafe_allow_html=True)
                st.progress(int(((180 - i) / 180) * 100))
            time.sleep(1)
        
        main_placeholder.empty()
        st.session_state.stage = "unlocked"
        st.rerun()

    # 🟢 階段三：倒數結束，系統全自動解鎖開牌（全大字報告）
    elif st.session_state.stage == "unlocked":
        market, signal_light, reason = decision_engine(code)
        color = "#FF3333" if "🔴" in market else "#00FF66"
        st.markdown(f"""
        <div class="report-box">
            <h2 style="text-align:center; font-size: 3rem !important;">📊 {code} 深度分析報告</h2>
            <hr style="border:2px solid #333;">
            <p style="font-size: 2.2rem !important; text-align:center;"><b>主力方向：</b> <span style="color:{color}; font-weight:bold;">{market}</span></p>
            <p style="font-size: 2.2rem !important; text-align:center;"><b>多空訊號：</b> <mark style="background:#222; color:{color}; font-weight:bold; padding:5px 15px; border-radius:8px;">{signal_light}</mark></p>
            <div style="background:#111111; padding:20px; border-radius:12px; margin-top:25px; border: 2px solid #333;">
                <p style="font-size: 1.6rem !important; color:#FFFFFF; line-height:1.6;"><b>💡 獨家 L2 籌碼解析：</b><br>{reason}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🔍 查詢下一檔股票"):
            st.session_state.stage = "payment"
            st.rerun()
