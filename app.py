import streamlit as st
import yfinance as yf

# 1. 專業品牌配置 (顧形象)
st.set_page_config(page_title="Axiom 1.0", page_icon="🚥")
st.markdown("<h2 style='text-align: center;'>🛡️ Axiom 1.0 紅綠燈數據系統</h2>", unsafe_allow_html=True)

st.divider()

# 2. 查詢與門牌 (顧前：給甜頭 + 留聯絡)
col1, col2 = st.columns([2, 1])
with col1:
    st.write("### 🔍 1. 查詢代號")
    stock_id = st.text_input("輸入台股 4 位數代碼", value="2330")
with col2:
    st.write("### 📱 2. 創辦人")
    st.success("ID: 0966154137")

# 自動跳轉按鈕，確保手機用戶能一鍵加 LINE
st.link_button("👉 點我直接加 LINE 領取口令", f"https://line.me/ti/p/~0966154137")

st.divider()

# 3. 核心紅綠燈預警 (顧後：口令 8888 是唯一鑰匙)
st.write("### 🚥 3. 系統訊號狀態")
pwd = st.text_input("🔑 輸入 4 位數口令解鎖紅綠燈", type="password")

if pwd == "8888":
    st.balloons()
    try:
        # 抓取即時數據進行紅綠燈判定
        df = yf.Ticker(f"{stock_id}.TW").history(period="2d")
        if not df.empty and len(df) >= 2:
            now_price = df['Close'].iloc[-1]
            old_price = df['Close'].iloc[-2]
            diff = now_price - old_price
            
            # --- 紅綠燈視覺判斷 (專業第一性原理) ---
            if diff > 0:
                st.markdown(f"<div style='background-color:#ff4b4b; color:white; padding:30px; text-align:center; border-radius:15px;'><h1>🔴 紅燈：多頭進場</h1><p>價格上漲 {diff:.2f}</p></div>", unsafe_allow_html=True)
            elif diff < 0:
                st.markdown(f"<div style='background-color:#00c853; color:white; padding:30px; text-align:center; border-radius:15px;'><h1>🟢 綠燈：空頭警示</h1><p>價格下跌 {abs(diff):.2f}</p></div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='background-color:#ffd600; color:black; padding:30px; text-align:center; border-radius:15px;'><h1>🟡 黃燈：觀望盤整</h1><p>價格持平</p></div>", unsafe_allow_html=True)
            
            st.write(f"**{stock_id} 最新成交價：{now_price:.2f} TWD**")
        else:
            st.error("代碼查無數據。")
    except:
        st.error("系統連線繁忙。")
else:
    # 沒解鎖時的狀態
    st.warning("💡 訊號已鎖定，請加 LINE 並支付 100 元領取今日口令。")
    st.markdown("<div style='background-color:#333; height:150px; border-radius:15px; display:flex; align-items:center; justify-content:center; color:#555;'>訊號解鎖後顯示紅綠燈顏色</div>", unsafe_allow_html=True)
    if pwd != "":
        st.error("❌ 口令錯誤，請洽詢創辦人。")
