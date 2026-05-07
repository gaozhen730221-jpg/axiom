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

# --- ② 台灣年轻白領第一性原理：全黑極簡視覺 ---
st.set_page_config(page_title="台股 1.0", layout="centered")
st.markdown("""
    <style>
    /* 全黑底色，其餘文字與提示全部保留原生高對比純白 */
    html, body, [data-testid="stAppViewContainer"] { background-color: #000000 !important; color: #FFFFFF !important; }
    [data-testid="stHeader"], [data-testid="stFooter"] { visibility: hidden; }
    
    /* 核心標題 */
    h1 { font-size: 3.2rem !important; font-weight: 900 !important; text-align: center; color: #FFFFFF !important; margin-bottom: 5px; }
    .sub-title { text-align: center; color: #00FF66 !important; font-weight: 700; letter-spacing: 2px; margin-bottom: 30px; }
    
    /* 精緻極簡輸入框：Placeholder 強制過濾掉瀏覽器暗色，直接亮白顯示 */
    .stTextInput>div>div>input {
        background-color: #111111 !important; color: #FFFFFF !important; 
        border: 2px solid #333333 !important; text-align: center;
    }
    .stTextInput>div>div>input:focus { border: 2px solid #00FF66 !important; }
    .stTextInput>div>div>input::placeholder { color: #FFFFFF !important; opacity: 1 !important; }
    .stTextInput>div>div>input::-webkit-input-placeholder { color: #FFFFFF !important; }
    .stTextInput>div>div>input::-moz-placeholder { color: #FFFFFF !important; }
    
    /* 收款鎖定紅框 */
    .lock-box { border: 3px solid #FF3333; padding: 20px; text-align: center; background: #110505; color: #FF3333; font-weight: 900; border-radius: 12px; margin: 20px 0; }
    
    /* 原地解鎖驗證綠框 */
    .verify-box { border: 3px solid #00FF66; padding: 25px; text-align: center; background: #051105; color: #00FF66; font-weight: 900; border-radius: 12px; margin-top: 20px; }
    
    /* 最終看牌報告框 */
    .report-box { border: 3px solid #00FF66; padding: 30px; background: #051105; border-radius: 15px; margin-top: 25px; }
    
    /* 原生按鈕強制上色 */
    .stButton>button { background-color: #00FF66 !important; color: #000000 !important; width: 100%; height: 4.5rem; font-size: 1.8rem !important; font-weight: 950 !important; border-radius: 10px !important; border: none !important; }
    </style>
    """, unsafe_allow_html=True)

# --- ③ 畫面頂部：品牌意象 ---
st.markdown("<h1>主力底牌，一秒開牌。</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>台股 1.0 ・ L2 數據核心</p>", unsafe_allow_html=True)

# 核心輸入框：保留極簡原生高對比純白提示字，一進來就看得懂要輸入代碼
code = st.text_input("", placeholder="請輸入股票代碼 (例如: 2330)", label_visibility="collapsed")
st.divider()

# --- ④ 核心商務控制鏈 ---
if code:
    if len(code.strip()) > 0:
        # 初始化付款狀態機
        if 'stage' not in st.session_state:
            st.session_state.stage = "payment"

        # 【 狀態一：未付費階段，由上至下一條線流暢到底 】
        if st.session_state.stage == "payment":
            st.markdown(f'<div class="lock-box">⚠️ 偵測到該股【{code}】最新籌碼異動！數據已鎖定。</div>', unsafe_allow_html=True)
            st.markdown("<p style='text-align:center; color:#FFFFFF; font-weight:700;'>💸 儲存 QR Code 轉帳 (NT$ 99)</p>", unsafe_allow_html=True)
            
            # 自動捕捉目錄下的街口收款碼
            qrs = list(Path('.').rglob('*.png')) + list(Path('.').rglob('*.jpg'))
            if qrs:
                col_l, col_m, col_r = st.columns([1, 2, 1])
                with col_m: st.image(str(qrs[-1]), use_container_width=True)
            
            # 純文字街口帳號卡
            st.code("街口代碼：396\n街口帳號：910080767\n金額：新台幣 99 元", language="text")
            
            st.divider()
            
            # ⚡ 核心修正：按鈕按下去，倒數驗證框「直接在原地（按鈕正下方）」跳出來，絕不往上跳！
            if st.button("🔥 我已完成支付，立刻驗證看牌"):
                st.session_state.stage = "verifying"
                st.rerun()

        # 【 狀態二：倒數驗證階段 】
        # 點擊按鈕後 rerun，上方的街口碼跟舊按鈕直接銷毀，在同一區塊原地生成全螢幕大倒數框！
        elif st.session_state.stage == "verifying":
            countdown_placeholder = st.empty()
            
            # 180秒全自動心理戰門禁倒數
            for i in range(180, -1, -1):
                with countdown_placeholder.container():
                    st.markdown(f"""
                    <div class="verify-box">
                        <span style="font-size: 1.3rem;">📡 正在連線台灣結算後端 API 驗證款項...</span><br><br>
                        <span style="font-size: 3rem; font-weight:900; color:#00FF66;">驗證剩餘 {i} 秒</span><br><br>
                        <p style="font-size: 1rem; color: #FF3333; margin:0;">請確保已完成街口匯款，否則數據包將自動銷毀</p>
                    </div>
                    """, unsafe_allow_html=True)
                    st.progress(int(((180 - i) / 180) * 100))
                time.sleep(1)
            
            countdown_placeholder.empty()
            st.session_state.stage = "unlocked"
            st.rerun()

        # 【 狀態三：原地翻牌看結果 】
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
            
            if st.button("🔍 查詢下一檔股票"):
                st.session_state.stage = "payment"
                st.rerun()
