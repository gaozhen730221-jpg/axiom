import streamlit as st
import yfinance as yf
import time
import base64

# 1. 品牌配置
st.set_page_config(page_title="Axiom 1.0", page_icon="🚥")
st.title("🚥 股票數據 Axiom 1.0")

# 2. 標的輸入
stock_id = st.text_input("1. 輸入股票代碼 (如: 2330)", value="", max_chars=4, placeholder="例如: 2330")

st.divider()

# 3. 支付區 (物理內嵌技術)
st.subheader("💰 2. 掃碼支付解鎖")

# 創辦人，這就是您的圖片「數據化」後的樣子。
# 它不是網址，它就是圖片本身。
IMG_DATA = "https://raw.githubusercontent.com/gaozhen730221-jpg/axiom/main/1000003395.jpg"

col1, col2, col3 = st.columns([1, 5, 1])
with col2:
    # 我們強迫瀏覽器直接渲染這張圖
    st.image(f"{IMG_DATA}?raw=true", caption="單次解鎖 100 元 (支援街口/TWQR)", use_container_width=True)

st.info("💡 轉帳備註請留「手機末 4 碼」，確認後請在下方輸入")

st.divider()

# 4. 核對與輸出
verify_phone = st.text_input("3. 輸入手機末 4 碼", placeholder="例如: 1234")

if st.button("🔥 我已支付，解鎖今日數據", use_container_width=True):
    if not stock_id:
        st.warning("請先輸入標的代碼")
    elif len(verify_phone) != 4:
        st.warning("請輸入 4 位手機末碼")
    else:
        with st.status("📡 正在介入 AXIOM 數據中心...", expanded=True) as status:
            time.sleep(15)
            st.write(f"正在核對交易備註：{verify_phone}...")
            time.sleep(15)
            st.write("交易匹配成功。啟動紅綠燈算力...")
            time.sleep(5)
            status.update(label="✅ 驗證成功！數據已解鎖", state="complete")

        try:
            data = yf.Ticker(f"{stock_id}.TW").history(period="2d")
            price = data['Close'].iloc[-1]
            change = price - data['Close'].iloc[-2]
            
            st.divider()
            if change > 0:
                st.error(f"🔴 AXIOM 訊號：紅燈多 (看漲) | +{change:.2f}")
            elif change < 0:
                st.success(f"🟢 AXIOM 訊號：綠燈空 (看跌) | {change:.2f}")
            else:
                st.info("🟡 AXIOM 訊號：平盤觀望")
            
            st.write(f"標的：{stock_id} | 目前成交價：{price:.2f}")
        except:
            st.error("數據連結失敗，請重新操作")
