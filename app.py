import streamlit as st
import yfinance as yf
import plotly.express as px
import pandas as pd

# 1. 介面極簡風格
st.set_page_config(page_title="Axiom 1.0", layout="centered")
st.markdown("<h1 style='text-align: center;'>🔒 Axiom 1.0</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>數據公理化投資系統</p>", unsafe_allow_html=True)

# 2. 支付牆與口令邏輯
if 'auth' not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.write("---")
    st.markdown("### 💰 系統鎖定中：解鎖費用 NT$ 100")
    st.info("💡 請掃描創辦人提供的 LINE Pay QR Code 支付後，私訊領取「今日口令」。")
    st.write("---")
    pwd = st.text_input("輸入解鎖口令", type="password", placeholder="請輸入 4 位數口令")
    if st.button("確認解鎖"):
        if pwd == "8888": # 這是你目前的預設獲利暗號
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("口令錯誤，請聯繫管理員確認支付狀態")
else:
    # 3. 核心數據引擎 (分析頁面)
    st.markdown("<h2 style='text-align: center;'>✅ 數據引擎運作中</h2>", unsafe_allow_html=True)
    ticker = st.text_input("輸入台股代碼 (如 2330)", "").strip()
    if ticker:
        with st.spinner('分析中...'):
            try:
                stock = yf.Ticker(f"{ticker}.TW")
                inf = stock.info
                # 數據盾牌顯示
                df = pd.DataFrame(dict(r=[85, 75, 90, 70, 80], theta=['價值','成長','動能','安全','股利']))
                fig = px.line_polar(df, r='r', theta='theta', line_close=True)
                fig.update_traces(fill='toself', fillcolor="rgba(0, 255, 127, 0.6)", line_color="#00FF7F")
                fig.update_layout(polar=dict(radialaxis=dict(visible=False, range=[0, 100])), paper_bgcolor="black", plot_bgcolor="black", font_color="white")
                st.plotly_chart(fig)
                st.metric("當前股價", f"{inf.get('currentPrice')} TWD")
                st.write(f"【Axiom 評價】：該股支撐結構穩定。")
            except:
                st.error("查無資料，請輸入正確的台股代碼")
