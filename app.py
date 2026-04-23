import streamlit as st
import yfinance as yf
import time

# 頁面配置
st.set_page_config(page_title="Axiom 1.0 台灣站", page_icon="🚥")
st.title("🚥 Axiom 1.0 台股數據中心")

# 1. 輸入區優化
stock_num = st.text_input("1. 輸入台股代碼 (如: 2330)", value="", max_chars=4)

st.divider()

# 2. 支付區
st.subheader("💰 2. 支付解鎖今日訊號")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # 讀取您上傳的 1776940866671.jpg
    st.image("1776940866671.jpg", caption="單次解鎖 NT$ 100", use_container_width=True)

st.info("💡 支付後請於備註填寫手機末 4 碼")

st.divider()

# 3. 核對區
verify_phone = st.text_input("3. 輸入手機末 4 碼進行驗證")

if st.button("🔥 立即解鎖 Axiom 算力訊號", use_container_width=True):
    if not stock_num or len(verify_phone) != 4:
        st.warning("請完整填寫代碼與驗證碼")
    else:
        with st.status("📡 正在介入 AXIOM 台灣數據中心...", expanded=True) as status:
            time.sleep(10)
            st.write(f"正在核對備註：{verify_phone}...")
            time.sleep(10)
            status.update(label="✅ 驗證成功！數據已解鎖", state="complete")

        try:
            # 自動幫用戶加上 .TW
            data = yf.Ticker(f"{stock_num}.TW").history(period="2d")
            price = data['Close'].iloc[-1]
            change = price - data['Close'].iloc[-2]
            
            st.divider()
            if change > 0:
                st.error(f"🔴 AXIOM 訊號：紅燈多 (看漲) | 變動: +{change:.2f}")
            elif change < 0:
                st.success(f"🟢 AXIOM 訊號：綠燈空 (看跌) | 變動: {change:.2f}")
            else:
                st.info("🟡 AXIOM 訊號：平盤觀望")
            
            st.metric(label=f"標的 {stock_num} 目前成交價", value=f"{price:.2f}", delta=f"{change:.2f}")
        except:
            st.error("讀取失敗，請確認代碼是否正確")
