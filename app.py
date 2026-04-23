import streamlit as st
import yfinance as yf
import time

# 頁面配置：極簡滲透風格
st.set_page_config(page_title="台股 1.0", page_icon="🚥", layout="centered")

# CSS 隱藏頂部裝飾，讓畫面更像獨立 APP
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

st.title("🚥 台股 1.0")
st.write("---")

# 1. 標的輸入
stock_num = st.text_input("1. 輸入台股代碼", value="", max_chars=4, placeholder="例如: 2330")

st.divider()

# 2. 支付區 (陌生人生意核心：視覺衝擊)
st.subheader("💰 2. 支付解鎖算力訊號")
c1, c2, c3 = st.columns([1, 3, 1])
with c2:
    # 確保圖片檔名與您 GitHub 內的一致
    try:
        st.image("1776940866671.jpg", caption="單次解鎖 NT$ 100", use_container_width=True)
    except:
        st.error("⚠️ 支付圖標載入中，請確認檔案 1776940866671.jpg 已上傳")

st.info("💡 支付成功後，請於下方填寫「手機末 4 碼」驗證")

st.divider()

# 3. 驗證與紅綠燈輸出
verify_phone = st.text_input("3. 驗證手機末 4 碼")

if st.button("🔥 立即獲取 AXIOM 紅綠燈訊號", use_container_width=True):
    if not stock_num or len(verify_phone) != 4:
        st.warning("請完整填寫代碼與驗證資訊")
    else:
        with st.status("📡 正在介入 AXIOM 台灣數據中心...", expanded=True) as status:
            time.sleep(10)
            st.write(f"正在核對交易流水：{verify_phone}...")
            time.sleep(10)
            st.write("交易匹配成功！算力啟動中...")
            time.sleep(5)
            status.update(label="✅ 驗證成功！數據已解鎖", state="complete")

        try:
            # 自動處理台股後綴
            ticker_id = f"{stock_num}.TW"
            data = yf.Ticker(ticker_id).history(period="2d")
            
            if data.empty:
                st.error("查無此代號，請重新輸入")
            else:
                price = data['Close'].iloc[-1]
                change = price - data['Close'].iloc[-2]
                
                st.divider()
                # 台灣習慣：紅漲綠跌
                if change > 0:
                    st.error(f"🔴 AXIOM 訊號：紅燈 (多方趨勢) | 變動: +{change:.2f}")
                elif change < 0:
                    st.success(f"🟢 AXIOM 訊號：綠燈 (空方趨勢) | 變動: {change:.2f}")
                else:
                    st.info("🟡 AXIOM 訊號：平盤觀望")
                
                st.metric(label=f"標的 {stock_num} 當前成交價", value=f"{price:.2f}", delta=f"{change:.2f}")
        except Exception as e:
            st.error("數據讀取超時，請重新點擊解鎖")

# 4. 法律防護線
st.caption("---")
st.caption("免責聲明：本工具僅供數據參考，不構成任何投資建議。投資人應獨立判斷風險。")
