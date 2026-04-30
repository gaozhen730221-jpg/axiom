import streamlit as st
import time
from pathlib import Path

# --- ① 決策引擎 ---
def decision_engine(code):
    signals = {
        "2330": ("偏多", "外資持續流入 + 權值結構穩定支撐", "建議分批布局"),
        "2317": ("觀望", "內部籌碼分歧明顯，多空勢力拉鋸", "建議等待確認"),
        "2454": ("偏多", "短期技術量能放大，突破關鍵壓力", "可小量試單")
    }
    return signals.get(code, ("觀望", "數據不足以生成高勝率決策", "建議暫不操作"))

# --- ② 樣式設定 ---
st.set_page_config(page_title="台股 1.28", layout="centered")
st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] { background-color: #FFFFFF !important; color: #000000 !important; }
    h1 { font-size: 3.5rem !important; font-weight: 950 !important; text-align: center; }
    .stButton>button {
        background-color: #000000 !important; color: #FFFFFF !important;
        width: 100%; height: 5.5rem; font-size: 2rem !important; font-weight: 900 !important;
    }
    .wait-box { 
        border: 5px solid #FF0000; padding: 25px; text-align: center; 
        background: #FFF5F5; color: #FF0000; font-weight: 900; 
        border-radius: 15px; margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("台股 1.28")
st.markdown("<p style='text-align:center; font-weight:bold;'>核心對帳引擎・Axiom 1.28</p>", unsafe_allow_html=True)

# 顯示支付圖（自動抓目錄下的圖片）
qrs = list(Path('.').rglob('*.png')) + list(Path('.').rglob('*.jpg'))
if qrs:
    col_l, col_m, col_r = st.columns([1, 2, 1])
    with col_m:
        st.image(str(qrs[-1]), use_container_width=True) 

st.divider()

code = st.text_input("輸入股票代碼", placeholder="例如: 2330")
verify_input = st.text_input("核對碼 (轉帳帳號末 4 碼)", placeholder="請輸入您轉出帳戶的最後四位數字")

# --- ③ 「空城計」核心邏輯 ---
if st.button("啟動 1.28 引擎進行深度核對"):
    if not code:
        st.error("請輸入股票代碼")
    elif not verify_input:
        # ❌ 連數字都沒填的，直接罰站 180 秒
        placeholder = st.empty()
        for i in range(180, -1, -1):
            with placeholder.container():
                st.markdown(f"""
                <div class="wait-box">
                    <span style="font-size: 1.4rem;">🚨 系統偵測到未授權存取：未輸入核對碼</span><br>
                    <span style="font-size: 3.5rem;">冷卻倒數 {i} 秒</span><br>
                    <p style="font-size: 1.1rem;">請填寫轉帳末 4 碼以啟動核對，否則持續鎖定。</p>
                </div>
                """, unsafe_allow_html=True)
            time.sleep(1)
        st.error("倒數結束，請輸入核對碼後重試。")
    else:
        # ✅ 只要有填任何數字（不管是對是錯），直接閃電噴結論！
        market, reason, action = decision_engine(code)
        st.markdown(f"""
        <div style="border:10px solid #000; padding:30px; margin-top:20px; background:#FFFFFF;">
            <h2 style="margin-top:0; font-size: 2.2rem;">📊 {code} 深度分析報告</h2>
            <hr style="border:4px solid #000;">
            <p style="font-size:1.6rem;"><b>市場趨勢：</b> <span style="color:red; font-weight:bold;">{market}</span></p>
            <p style="font-size:1.6rem;"><b>主力動向：</b> {reason}</p>
            <p style="font-size:1.6rem;"><b>決策建議：</b> <mark style="background: yellow; font-weight:bold; padding: 5px;">{action}</mark></p>
        </div>
        """, unsafe_allow_html=True)
        st.success(f"✅ 帳號末 4 碼【{verify_input}】核對成功！")
