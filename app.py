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
st.warning("請完成以下步驟領取『今日口令』：")

# 顯示你的 LINE ID 並加粗
st.error("第一步：複製創辦人 LINE ID")
st.code("0966154137", language=None)

st.info("第二步：打開 LINE 搜尋 ID 並加好友")
st.write("📢 私訊告知：『我要領取 Axiom 1.0 口令』並傳送支付截圖。")

# 備用按鈕（保留給部分能跳轉的手機）
st.link_button("直接加 LINE (若沒反應請用 ID 搜尋)", "https://line.me/ti/p/~0966154137")

st.divider()

# 4. 口令輸入
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
                else:
                    st.error("找不到數據。")
            except:
                st.error("系統繁忙。")
    elif pwd != "":
        st.error("❌ 口令錯誤，請聯繫創辦人。")
