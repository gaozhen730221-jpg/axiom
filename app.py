import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

# 1. 頁面設定
st.set_page_config(page_title="Axiom 1.0", page_icon="📈")

# 2. 標題與品牌
st.markdown("<h1 style='text-align: center;'>🔒 Axiom 1.0</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>數據公理化投資系統</p>", unsafe_allow_html=True)

st.divider()

# 3. 收錢與加 LINE 區塊
st.subheader("💰 系統鎖定中：解鎖費用 NT$ 100")
st.warning("請先支付費用後，聯繫創辦人領取『今日口令』")

# 顯示你的 LINE ID
st.success(f"📱 **LINE ID: 0966-154-137**")

# 超強按鈕：點了直接加你的 LINE
st.link_button("👉 點我加創辦人 LINE 領取口令", f"https://line.me/ti/p/~0966154137")

st.write("📢 私訊請告知：『我要領取 Axiom 1.0 口令』並傳送支付截圖。")

st.divider()

# 4. 口令輸入與解鎖邏輯
pwd = st.text_input("🔑 請輸入 4 位數解鎖口令", type="password")

if st.button("確認解鎖"):
    if pwd == "8888":
        st.balloons()
        st.success("✅ 解鎖成功！歡迎使用 Axiom 1.0")
        ticker = st.text_input("輸入台股代碼 (例如 2330)", "2330")
        if ticker:
            try:
                data = yf.Ticker(f"{ticker}.TW").history(period="1mo")
                if not data.empty:
                    fig = px.line(data, y='Close', title=f"{ticker} 近一個月走勢")
                    st.plotly_chart(fig, use_container_width=True)
                    st.dataframe(data.tail())
                else:
                    st.error("找不到數據，請檢查代號。")
            except:
                st.error("系統查詢繁忙，請稍後再試。")
    elif pwd != "":
        st.error("❌ 口令錯誤，請聯繫創辦人。")
