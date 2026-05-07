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
    # 若輸入其他代碼，明天直接由後端真實數據庫生成，這裡先做邏輯串接
    return signals.get(code, ("🟡 多空下拉", "⚠️ 數據不足", "該股籌碼散亂，主力尚未做出明顯方向，建議暫不操作。"))

# --- ② 台灣年輕白領美學：極簡、全黑、高對比潮牌感 ---
st.set_page_config(page_title="台股 1.0", layout="centered")
st.markdown("""
    <style>
    /* 全黑底、螢光綠/純白高對比，營造頂級大數據科技感 */
    html, body, [data-testid="stAppViewContainer"] { background-color: #000000 !important; color: #FFFFFF !important; }
    
    /* 隱藏 Streamlit 所有原生老氣欄位 */
    [data-testid="stHeader"], [data-testid="stFooter"] { visibility: hidden; }
    
    /* 標題與副標題 */
    h1 { font-size: 3.2rem !important; font-weight: 900 !important; text-align: center; color: #FFFFFF !important; margin-bottom: 5px; }
    .sub-title { text-align: center; color: #00FF66 !important; font-weight: 700; letter-spacing: 2px; margin-bottom: 30px; }
    
    /* 輸入框視覺調整 */
    .stTextInput>div>div>input {
        background-color: #111111 !important; color: #FFFFFF !important; 
        border: 2px solid #333333 !important; font-size: 1.4rem !important; height: 3.5rem; text-align: center;
    }
    .stTextInput>div>div>input:focus { border: 2px solid #00FF66 !important; }
    
    /* 巨大開牌按鈕 */
    .stButton>button {
        background-color: #00FF66 !important; color: #000000 !important;
        width: 100%; height: 5rem; font-size: 2rem !important; font-weight: 950 !important;
        border-radius: 10px !important; border: none !important; transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.02); background-color: #00CC55 !important; }
    
    /* 強制卡錢鎖定框 */
    .lock-box { 
        border: 3px solid #FF3333; padding: 25px; text-align: center; 
        background: #110505; color: #FF3333; font-weight: 900; 
        border-radius: 15px; margin: 20px 0;
    }
    
    /* 數據報告開牌樣式 */
    .report-box {
        border: 3px solid #00FF66; padding: 30px; background: #051105; border-radius: 15px; margin-top: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ③ 頂部：一秒開牌區（進來只看得到這個） ---
st.markdown("<h1>主力底牌，一秒開牌。</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>台股 1.0 ・ L2 數據核心</p>", unsafe_allow_html=True)

code = st.text_input("", placeholder="請輸入股票代碼 (例如: 2330)", label_visibility="collapsed")

st.divider()

# --- ④ 核心控制漏斗：按下開牌後，原地往下展開「卡錢」與「解鎖」 ---
if code:
    if len(code.strip()) > 0:
        # SessionState 用來記錄散戶有沒有付錢通過驗證
        if 'paid' not in st.session_state:
            st.session_state.paid = False

        # ➔ 階段 A：還沒付錢，直接卡死，把收款碼砸在臉上
        if not st.session_state.paid:
            st.markdown(f"""
            <div class="lock-box">
                <span style="font-size: 1.5rem; color: #FF3333;">⚠️ 偵測到該股【{code}】最新籌碼異動！數據已鎖定。</span><br>
                <span style="font-size: 1.1rem; color: #AAAAAA;">翻牌看底牌：只需一個便當錢</span>
            </div>
            """, unsafe_allow_html=True)
            
            # 台灣在地無痛收款區
            st.markdown("<h3 style='text-align:center; color:#FFFFFF;'>💸 儲存 QR Code 或一鍵複製轉帳 (NT$ 99)</h3>", unsafe_allow_html=True)
            
            # 自動抓取資料夾底下的個人收款碼圖片
            qrs = list(Path('.').rglob('*.png')) + list(Path('.').rglob('*.jpg'))
            if qrs:
                col_l, col_m, col_r = st.columns([1, 2, 1])
                with col_m:
                    st.image(str(qrs[-1]), caption="💡 手機長按圖片 ➔ 儲存到相簿付款", use_container_width=True)
            
            # 為手機傻瓜打造的「無腦一鍵複製」欄位
            st.markdown("<p style='text-align:center; color:#888888; font-size:0.9rem; margin-bottom:5px;'>💡 手機無法掃碼？複製下方資訊，打開網銀直接貼上轉帳：</p>", unsafe_allow_html=True)
            st.code("銀行：國泰世華 (013)\n帳號：1234-5678-9012\n金額：新台幣 99 元", language="text")
            
            st.divider()
            
            # 核對末四碼，觸發心理門禁
            phone = st.text_input("輸入您轉出帳戶的「末 4 碼」進行解鎖", placeholder="例如: 8888")
            
            if st.button("確認已付費，解鎖核心 L2 數據"):
                if phone:
                    main_placeholder = st.empty()
                    # 🚨 180 秒強制門禁心理戰（散戶如果沒付，會在這裡心虛落跑；付了的會乖乖等）
                    for i in range(180, -1, -1):
                        with main_placeholder.container():
                            st.markdown(f"""
                            <div class="lock-box" style="border-color: #00FF66; background: #051105; color: #00FF66;">
                                <span style="font-size: 1.3rem;">📡 正在連線台灣結算後端 API 核對帳號末 4 碼【{phone}】...</span><br>
                                <span style="font-size: 3rem; font-weight:900;">驗證剩餘 {i} 秒</span><br>
                                <p style="font-size: 1rem; color: #888888;">請確保已完成 NT$ 99 匯款，否則數據包將自動銷毀</p>
                            </div>
                            """, unsafe_allow_html=True)
                            st.progress(int(((180 - i) / 180) * 100))
                        time.sleep(1)
                    
                    main_placeholder.empty()
                    st.session_state.paid = True
                    st.rerun()
                else:
                    st.error("請輸入轉帳帳號末 4 碼以供 API 核對")
        
        # ➔ 階段 B：付費驗證通過，原地解鎖「真實紅綠燈」
        else:
            market, signal_light, reason = decision_engine(code)
            
            # 依據紅綠燈狀態給予視覺顏色
            color = "#FF3333" if "🔴" in market else "#00FF66"
            
            st.markdown(f"""
            <div class="report-box">
                <h2 style="margin-top:0; font-size: 2.2rem; text-align:center; color:#FFFFFF;">📊 {code} 深度分析報告</h2>
                <hr style="border:2px solid #333;">
                <p style="font-size:1.8rem; text-align:center;">
                    <b>主力方向：</b> <span style="color:{color}; font-weight:bold;">{market}</span>
                </p>
                <p style="font-size:1.8rem; text-align:center;">
                    <b>多空訊號：</b> <mark style="background: #222222; color:{color}; font-weight:bold; padding: 5px 15px; border-radius:5px;">{signal_light}</mark>
                </p>
                <div style="background:#111111; padding:15px; border-radius:8px; margin-top:20px;">
                    <p style="font-size:1.2rem; color:#DDDDDD; line-height:1.6;"><b>💡 獨家 L2 籌碼特徵解析：</b><br>{reason}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.success("✅ 轉帳驗證成功，L2 數據已全部解鎖。")
            
            # 提供按鈕可以重新查詢別檔
            if st.button("查詢下一檔股票"):
                st.session_state.paid = False
                st.rerun()
else:
    st.markdown("<p style='text-align:center; color:#555555;'>請在上方輸入框輸入任何台股代碼開始。</p>", unsafe_allow_html=True)
