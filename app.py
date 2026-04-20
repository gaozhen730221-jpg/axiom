import streamlit as st
import yfinance as yf

# 1. 專業品牌配置
st.set_page_config(page_title="Axiom 1.0 Pro", page_icon="🚥")
st.markdown("<h2 style='text-align: center;'>🛡️ Axiom 1.0 數據公理</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>最直接的紅綠燈判定系統</p>", unsafe_allow_html=True)

st.divider()

# 2. 核心操作區
col1, col2 = st.columns([1, 1])

with col1:
    st.write("### 🔍 1. 輸入代號")
    stock_id = st.text_input("輸入台股 4 位數代碼", value="", max_chars=4)

with col2:
    st.write("### 🔑 2. 領取口令")
    # 直接回歸 LINE 引流，不繞圈子
    st.markdown("#### [ 點擊加 LINE 領取今日口令 ]")
    st.info("請添加 ID: (你的LINE ID) 並支付 100 元")
    st.write("✅ 支付後即刻發放解鎖口令")

st.divider()

# 3. 判定顯示區
pwd = st.text_input("🔓 輸入解鎖口令", type="password")

if pwd == "8888":
    if stock_id:
        try:
            df = yf.Ticker(f"{stock_id}.TW").history(period="2d")
            if not df.empty and len(df) >= 2:
                now_p = df['Close'].iloc[-1]
                old_p = df['Close'].iloc[-2]
                diff = now_p - old_p
                
                # 暴力輸出
                if diff > 0:
                    st.markdown(f"<div style='background-color:#ff4b4b; color:white; padding:40px; text-align:center; border-radius:15px;'><h1>🔴 紅燈：多頭</h1><h3>漲跌：+{diff:.2f}</h3></div>", unsafe_allow_html=True)
                elif diff < 0:
                    st.markdown(f"<div style='background-color:#00c853; color:white; padding:40px; text-align:center; border-radius:15px;'><h1>🟢 綠燈：空頭</h1><h3>漲跌：{diff:.2f}</h3></div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div style='background-color:#ffd600; color:black; padding:40px; text-align:center; border-radius:15px;'><h1>🟡 黃燈：觀望</h1><h3>價格持平</h3></div>", unsafe_allow_html=True)
                
                st.write(f"**{stock_id} 當前價：{now_p:.2f}**")
            else:
                st.error("代碼錯誤")
        except:
            st.error("數據讀取中...")
else:
    st.warning("🔒 請輸入正確口令以開啟數據公理。")

st.divider()
st.caption("Axiom 系統：不提供建議，只提供物理級數據結果。")
