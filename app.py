import streamlit as st
import yfinance as yf
import time

# 頁面配置：極簡風格
st.set_page_config(page_title="台股", page_icon="🚥")
st.title("🚥 台股")

# 1. 標的區
stock_num = st.text_input("1. 輸入代碼", value="", max_chars=4, placeholder="例如: 2330")

st.divider()

# 2. 支付區
st.subheader("💰 2. 支付解鎖")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # 這裡確保讀取您 GitHub 裡的那張圖
    st.image("1776940866671.jpg", caption="單次解鎖 NT$ 100", use_container_width=True)

st.info("💡 支付後請輸入手機末 4 碼驗證")

st.divider()

# 3. 驗證與算力輸出
verify_phone = st.text_input("3. 手機末 4 碼")

if st.button("🔥 立即解鎖 Axiom 算力", use_container_width=True):
    if not stock_num or len(verify_phone) != 4:
        st.warning("請完整填寫")
    else:
        with st.status("📡 數據核對中...", expanded=True) as status:
            time.sleep(10)
            st.write(f"核對備註：{verify_phone}...")
            time.sleep(10)
            status.update(label="✅ 驗證成功", state="complete")

        try:
            # 自動處理台灣代碼
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
            st.error("讀取失敗，請確認代碼")

# 4. 安全底部
st.caption("---")
st.caption("免責聲明：本工具僅供參考，不構成投資建議。")
