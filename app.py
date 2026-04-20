import streamlit as st
import yfinance as yf

# 1. 專業品牌配置
st.set_page_config(page_title="Axiom 1.2", page_icon="🚥")
st.markdown("<h2 style='text-align: center;'>🛡️ Axiom 1.2 公理隱私解碼版</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>快捷網絡時代的全新數據公理</p>", unsafe_allow_html=True)

st.divider()

# 2. 第一步：【查詢區】與【匿名支付解碼區】
col1, col2 = st.columns([1, 1])

with col1:
    st.write("### 🔍 1. 輸入台股代號")
    stock_id = st.text_input("輸入 4 位數代碼 (例如: 2330)", value="", max_chars=4)
    st.info("💡 請先輸入代碼，並至右側領取「11g專屬解碼」。")

with col2:
    st.write("### 💰 2. 匿名領取解碼")
    # 此處已換成您提供的官方轉帳 QR Code
    st.image("bd9a0ca4-9261-4489-b8a3-46671766ec9b.jpg", caption="[官方轉帳] 掃碼即付", use_column_width=True)
    st.markdown("<h4 style='text-align: center; color: #ff4b4b;'>支付 100 元，領取 11g 專屬解碼</h4>", unsafe_allow_html=True)
    st.caption("提示：支付後請於轉帳備註留言，我們將發放單次解碼密鑰。")

st.divider()

# 3. 第二步：【紅綠燈核心：11g 驗證】
st.write("### 🚥 3. 公理訊號判定")
pwd = st.text_input("🔑 輸入 11g 專屬解碼 (例如: 11g-xxxx)", type="password")

# 邏輯設定：目前暫定 11g-8888 為測試用密鑰，未來可隨機發放
if pwd.startswith("11g-") and pwd == "11g-8888":
    # 貫徹「不要看多」原則，這裡顯示警告
    st.warning("⚠️ 11g 解碼權限已開啟：本金鑰僅限本次單一標的查詢，請勿頻繁切換。")
    
    if stock_id:
        try:
            df = yf.Ticker(f"{stock_id}.TW").history(period="2d")
            if not df.empty and len(df) >= 2:
                now_p = df['Close'].iloc[-1]
                old_p = df['Close'].iloc[-2]
                diff = now_p - old_p
                
                # 視覺化輸出：移除華麗詞彙，只留真實數據
                if diff > 0:
                    st.markdown(f"<div style='background-color:#ff4b4b; color:white; padding:40px; text-align:center; border-radius:15px;'><h1>🔴 紅燈：多頭</h1><h3>漲跌：+{diff:.2f}</h3></div>", unsafe_allow_html=True)
                elif diff < 0:
                    st.markdown(f"<div style='background-color:#00c853; color:white; padding:40px; text-align:center; border-radius:15px;'><h1>🟢 綠燈：空頭</h1><h3>漲跌：{diff:.2f}</h3></div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div style='background-color:#ffd600; color:black; padding:40px; text-align:center; border-radius:15px;'><h1>🟡 黃燈：觀望</h1><h3>價格持平</h3></div>", unsafe_allow_html=True)
                
                st.write(f"**{stock_id} 最新成交價：{now_p:.2f} TWD**")
            else:
                st.error("代碼格式錯誤或查無數據。")
        except:
            st.error("數據接口繁忙，請稍後再試。")
    else:
        st.write("請在左上方輸入股票代碼以進行公理分析。")
elif pwd == "":
    st.info("🔒 數據加密中。請完成右上方匿名支付，輸入 11g 解碼以觀看紅綠燈訊號。")
else:
    st.error("❌ 無效或已過期之 11g 解碼金鑰。")
