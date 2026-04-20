import streamlit as st
import yfinance as yf
import plotly.express as px

# 1. 頁面極簡設定
st.set_page_config(page_title="Axiom 1.0")
st.markdown("<h2 style='text-align: center;'>📈 Axiom 1.0 數據查詢</h2>", unsafe_allow_html=True)

# 2. 核心查詢框（讓客人先動手試用）
st.write("### 🔍 第一步：輸入股票代號")
stock_id = st.text_input("在此輸入台股代碼 (如: 2330)", value="")

st.divider()

# 3. 解鎖區（誘惑與收錢）
st.write("### 🔒 第二步：解鎖專業圖表")
if stock_id:
    st.info(f"📊 股票 {stock_id} 的數據已連線，請輸入口令查看趨勢圖。")
else:
    st.write("請先在上方輸入代號。")

pwd = st.text_input("🔑 輸入 4 位數口令 (領取請加 LINE: 0966154137)", type="password")

# 4. 判斷邏輯
if pwd == "8888":
    if stock_id:
        try:
            # 抓取台股數據
            df = yf.Ticker(f"{stock_id}.TW").history(period="1mo")
            if not df.empty:
                st.success(f"✅ {stock_id} 數據解鎖成功！")
                # 畫出漂亮的趨勢線
                fig = px.line(df, y='Close', title=f"{stock_id} 近一個月走勢分析")
                st.plotly_chart(fig, use_container_width=True)
                # 顯示最新價格
                st.metric(label="最新成交價", value=f"{df['Close'].iloc[-1]:.2f} TWD")
            else:
                st.error("查無此代號，請確認數字是否正確。")
        except:
            st.error("數據連線異常，請稍後再試。")
    else:
        st.warning("請先輸入股票代號。")
elif pwd != "":
    st.error("❌ 口令錯誤，請聯繫創辦人領取。")
