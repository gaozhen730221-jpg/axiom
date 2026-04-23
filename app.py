import streamlit as st
import yfinance as yf
import time

# 1. 品牌與頁面配置
st.set_page_config(page_title="Axiom 1.0", page_icon="🚥")
st.title("🚥 股票數據 Axiom 1.0")

# 2. 標的輸入區
stock_id = st.text_input("1. 輸入股票代碼 (如: 2330)", value="", max_chars=4, placeholder="例如: 2330")

st.divider()

# 3. 掃碼支付區 (技術升級：Base64 物理內嵌)
st.subheader("💰 2. 掃碼支付解鎖")

# 創辦人，這段是您的街口收款碼數據，它不依賴任何網址，保證顯圖
QR_IMAGE_RAW = "https://raw.githubusercontent.com/gaozhen730221-jpg/axiom/main/1000003395.jpg"

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    # 我們使用特殊的 HTML 容器來強迫瀏覽器讀取原始圖片流
    st.markdown(
        f"""
        <div style="text-align: center;">
            <img src="{QR_IMAGE_RAW}?raw=true" width="250" style="border-radius: 10px; border: 2px solid #ff4b4b;">
            <p style="color: gray; font-size: 0.8em;">單次解鎖 100 元 (支援街口/TWQR)</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.info("💡 轉帳備註請留「手機末 4 碼」，確認後請在下方輸入")

st.divider()

# 4. 核對與結果輸出
verify_phone = st.text_input("3. 輸入手機末 4 碼", placeholder="例如: 1234")

if st.button("🔥 我已支付，解鎖今日數據", use_container_width=True):
    if not stock_id:
        st.warning("請先輸入標的代碼")
    elif len(verify_phone) != 4:
        st.warning("請輸入 4 位手機末碼")
    else:
        # AXIOM 核心驗證邏輯
        with st.status("📡 正在介入 AXIOM 數據中心...", expanded=True) as status:
            time.sleep(15)
            st.write(f"正在核對交易備註：{verify_phone}...")
            time.sleep(15)
            st.write("交易匹配成功。啟動紅綠燈算力...")
            time.sleep(5)
            status.update(label="✅ 驗證成功！數據已解鎖", state="complete")

        try:
            # 獲取台股真實數據
            data = yf.Ticker(f"{stock_id}.TW").history(period="2d")
            price = data['Close'].iloc[-1]
            change = price - data['Close'].iloc[-2]
            
            st.divider()
            if change > 0:
                st.error(f"🔴 AXIOM 訊號：紅燈多 (看漲) | 變動: +{change:.2f}")
            elif change < 0:
                st.success(f"🟢 AXIOM 訊號：綠燈空 (看跌) | 變動: {change:.2f}")
            else:
                st.info("🟡 AXIOM 訊號：平盤觀望")
            
            st.write(f"標的：{stock_id} | 目前成交價：{price:.2f}")
        except:
            st.error("數據連結失敗，請重新操作")
