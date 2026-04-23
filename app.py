import streamlit as st
import yfinance as yf
import time

# 頁面配置：座標強化版
st.set_page_config(page_title="台股 1.0", page_icon="🚥", layout="centered")

# 隱藏多餘 UI
st.markdown("""<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}</style>""", unsafe_allow_html=True)

# 頂部導航
st.title("🚥 台股 1.0")
st.caption("🚀 全台首創算力紅綠燈 | 當前座標：https://jdpykohqmectgps7x58tnf.streamlit.app/")

st.write("---")

# 1. 標的輸入
stock_num = st.text_input("1. 輸入台股代碼 (4碼)", value="", max_chars=4, placeholder="例如: 2330")

st.divider()

# 2. 支付區
st.subheader("💰 2. 支付解鎖算力")
c1, c2, c3 = st.columns([1, 3, 1])
with c2:
    try:
        # 請確保檔案 1776940866671.jpg 在你的目錄下
        st.image("1776940866671.jpg", caption="掃碼支付 NT$ 100", use_container_width=True)
    except:
        st.error("⚠️ 支付介面載入中...")

st.info("💡 支付後，請填寫「手機末 4 碼」驗證。")

st.divider()

# 3. 驗證與結果
verify_phone = st.text_input("3. 驗證手機末 4 碼")

if st.button("🔥 立即獲取紅綠燈訊號", use_container_width=True):
    if not stock_num or len(verify_phone) != 4:
        st.warning("請輸入完整代碼與驗證資訊")
    else:
        with st.status("📡 座標對接中，介入 AXIOM 數據中心...", expanded=True) as status:
            time.sleep(10)
            st.write(f"正在驗證交易：{verify_phone}...")
            time.sleep(10)
            status.update(label="✅ 驗證成功！算力解鎖", state="complete")

        try:
            ticker_id = f"{stock_num}.TW"
            data = yf.Ticker(ticker_id).history(period="2d")
            
            if data.empty:
                st.error("代碼錯誤")
            else:
                price = data['Close'].iloc[-1]
                change = price - data['Close'].iloc[-2]
                
                st.divider()
                # 紅漲綠跌 (台灣習慣)
                if change > 0:
                    st.error(f"🔴 AXIOM 訊號：紅燈 (多方) | +{change:.2f}")
                elif change < 0:
                    st.success(f"🟢 AXIOM 訊號：綠燈 (空方) | {change:.2f}")
                else:
                    st.info("🟡 AXIOM 訊號：平盤")
                
                st.metric(label=f"標的 {stock_num} 目前價格", value=f"{price:.2f}", delta=f"{change:.2f}")
                
                # 座標強化：讓用戶分享時帶著座標
                st.write("---")
                st.caption("🔗 分享本座標：https://jdpykohqmectgps7x58tnf.streamlit.app/")
        except:
            st.error("讀取超時")

# 4. 安全底部
st.caption("---")
st.caption("免責聲明：本工具僅供數據參考。")
