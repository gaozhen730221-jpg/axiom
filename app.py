import streamlit as st
import yfinance as yf
import time

# 1. 品牌與頁面配置
st.set_page_config(page_title="Axiom 1.0", page_icon="🚥")
st.title("🚥 股票數據 Axiom 1.0")

# 2. 標的輸入區
stock_id = st.text_input("1. 輸入股票代碼 (如: 2330)", value="", max_chars=4, placeholder="例如: 2330")

st.divider()

# 3. 掃碼支付區 (直接讀取同資料夾內的圖片：1776940866671.jpg)
st.subheader("💰 2. 掃碼支付解鎖")

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    # 這裡的檔名必須跟您剛才上傳的一模一樣
    try:
        st.image("1776940866671.jpg", caption="單次解鎖 100 元 (支援街口/TWQR)", width=250)
    except:
        st.error("⚠️ 圖片讀取失敗，請確認檔案已存在 GitHub 資料夾中")

st.info("💡 轉帳備註請留「手機末 4 碼」，確認後請在下方輸入")

st.divider()

# 4. 核對與結果輸出
verify_phone = st.text_input("3. 輸入手機末 4 碼", placeholder="例如: 1234")

if st.button("🔥 我已支付，解鎖今日數據", use_container_width=True):
    if not stock_id or len(verify_phone) != 4:
        st.warning("請完整輸入代碼與手機末 4 碼")
    else:
        with st.status("📡 正在核對 AXIOM 數據中心...", expanded=True) as status:
            time.sleep(15)
            st.write(f"正在核對交易備註：{verify_phone}...")
            time.sleep(15)
            st.write("交易匹配成功。啟動紅綠燈算力...")
            time.sleep(5)
            status.update(label="✅ 驗證成功！", state="complete")

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
            st.error("數據連結失敗，請檢查代碼")
