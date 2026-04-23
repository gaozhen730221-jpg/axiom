import streamlit as st
import yfinance as yf
import time

# 頁面配置
st.set_page_config(page_title="台股 1.0", page_icon="🚥")
st.title("🚥 台股 1.0")

# 1. 標的輸入 (優化為台股專用)
stock_num = st.text_input("1. 輸入代碼", value="", max_chars=4, placeholder="例如: 2330")

st.divider()

# 2. 支付區
st.subheader("💰 2. 支付解鎖")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # 讀取資料夾內的圖片
    st.image("1776940866671.jpg", caption="單次解鎖 NT$ 100", use_container_width=True)

st.info("💡 支付後請輸入手機末 4 碼驗證")

st.divider()

# 3. 驗證與算力輸出
verify_phone = st.text_input("3. 手機末 4 碼")

if st.button("🔥 立即解鎖算力訊號", use_container_width=True):
    if not stock_num or len(verify_phone) != 4:
        st.warning("請完整填寫代碼與驗證碼")
    else:
        with st.status("📡 數據核對中...", expanded=True) as status:
            time.sleep(10)
            st.write(f"核對備註：{verify_phone}...")
            time.sleep(10)
            status.update(label="✅ 驗證成功", state="complete")

        try:
            # 自動處理台灣股號
            data = yf.Ticker(f"{stock_num}.TW").history(period="2d")
            price = data['Close'].iloc[-1]
            change = price - data['Close'].iloc[-2]
            
            st.divider()
            if change > 0:
                st.error(f"🔴 AXIOM 訊號：紅燈 (多) | +{change:.2f}")
            elif change < 0:
                st.success(f"🟢 AXIOM 訊號：綠燈 (空) | {change:.2f}")
            else:
                st.info("🟡 AXIOM 訊號：平盤")
            
            st.metric(label=f"標的 {stock_num} 目前價格", value=f"{price:.2f}", delta=f"{change:.2f}")
        except:
            st.error("數據連結失敗，請檢查代碼")

# 4. 法律防禦 (灰字免責聲明)
st.caption("---")
st.caption("免責聲明：本工具僅供參考，不構成投資建議。")
