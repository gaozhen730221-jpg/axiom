import streamlit as st
import yfinance as yf

# 1. 專業品牌配置
st.set_page_config(page_title="Axiom 1.0", page_icon="🚥")
st.markdown("<h2 style='text-align: center;'>🛡️ Axiom 1.0 紅綠燈數據系統</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>數據公理：一眼看穿趨勢訊號</p>", unsafe_allow_html=True)

st.divider()

# 2. 第一步：【查詢區】與【創辦人聯絡門牌】（顧前：必備聯絡方式）
col1, col2 = st.columns([2, 1])

with col1:
    st.write("### 🔍 1. 查詢代號")
    stock_id = st.text_input("輸入台股 4 位數代碼 (如 2330)", value="2330")

with col2:
    st.write("### 📱 2. 創辦人")
    st.success("LINE ID: 0966154137")

# 強力加好友按鈕（絕不能掉）
st.link_button("👉 點我直接加 LINE 領取口令", f"https://line.me/ti/p/~0966154137")

st.divider()

# 3. 第二步：【紅綠燈核心】（顧後：口令 8888 鎖死）
st.write("### 🚥 3. 系統訊號狀態")
pwd = st.text_input("🔑 輸入 4 位數口令解鎖紅綠燈", type="password")

if pwd == "8888":
    try:
        # 獲取即時數據判定紅綠燈
        df = yf.Ticker(f"{stock_id}.TW").history(period="2d")
        if not df.empty and len(df) >= 2:
            now_p = df['Close'].iloc[-1]
            old_p = df['Close'].iloc[-2]
            diff = now_p - old_p
            
            # --- 核心紅綠燈判定（台股邏輯） ---
            if diff > 0:
                # 漲 = 紅燈
                st.markdown(f"<div style='background-color:#ff4b4b; color:white; padding:40px; text-align:center; border-radius:15px;'><h1>🔴 紅燈：多頭進場</h1><h3>價格上漲 {diff:.2f}</h3></div>", unsafe_allow_html=True)
            elif diff < 0:
                # 跌 = 綠燈
                st.markdown(f"<div style='background-color:#00c853; color:white; padding:40px; text-align:center; border-radius:15px;'><h1>🟢 綠燈：空頭警示</h1><h3>價格下跌 {abs(diff):.2f}</h3></div>", unsafe_allow_html=True)
            else:
                # 平 = 黃燈
                st.markdown(f"<div style='background-color:#ffd600; color:black; padding:40px; text-align:center; border-radius:15px;'><h1>🟡 黃燈：觀望盤整</h1><h3>價格持平</h3></div>", unsafe_allow_html=True)
            
            st.write(f"**{stock_id} 最新成交價：{now_p:.2f} TWD**")
        else:
            st.error("代碼查無數據，請確認後重新輸入。")
    except:
        st.error("系統數據接口連線繁忙，請稍後。")
else:
    # 未解鎖狀態
    st.info("📢 訊號已鎖定。請支付 100 元至 LINE 領取今日口令。")
    st.markdown("<div style='background-color:#333; height:200px; border-radius:15px; display:flex; align-items:center; justify-content:center; color:#777; font-size:24px;'>🔒 待口令解鎖紅綠燈訊號</div>", unsafe_allow_html=True)
    if pwd != "":
        st.error("❌ 口令錯誤，請聯繫創辦人領取正確口令。")
