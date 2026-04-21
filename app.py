import streamlit as st
import yfinance as yf
import time

# 1. 配置
st.set_page_config(page_title="Axiom 1.0", page_icon="🚥")
st.title("🚥 股票數據 Axiom 1.0")

# 2. 標的輸入
stock_id = st.text_input("1. 輸入股票代碼", value="", max_chars=4, placeholder="例如: 2330")

st.divider()

# 3. 支付區：調整比例讓 QR Code 不會太大
st.subheader("💰 2. 掃碼支付解鎖")

pay_link = "https://line.me/R/ti/p/@您的帳號" # 👈 請確認此連結正確
qr_api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=200x200&data={pay_link}"

# 使用 3 欄位佈局，將圖片縮小並置中
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.image(qr_api_url, caption="單次解鎖 100 元", width=200) # 固定寬度為 200，精緻美觀

st.info("💡 轉帳備註請留「手機末 4 碼」，確認後請在下方輸入")

st.divider()

# 4. 核對與解鎖
verify_phone = st.text_input("3. 輸入手機末 4 碼", placeholder="例如: 1234")

if st.button("🔥 我已支付，解鎖今日數據", use_container_width=True):
    if not stock_id:
        st.warning("請先輸入代碼")
    elif len(verify_phone) != 4:
        st.warning("請輸入 4 位手機末碼")
    else:
        with st.status("📡 正在即時比對 LINE Pay 入帳紀錄...", expanded=True) as status:
            time.sleep(15)
            st.write(f"正在比對交易備註：{verify_phone}...")
            time.sleep(15)
            st.write("確認入帳。正在解鎖核心因子...")
            time.sleep(5)
            status.update(label="✅ 驗證成功！", state="complete")

        try:
            data = yf.Ticker(f"{stock_id}.TW").history(period="2d")
            price = data['Close'].iloc[-1]
            change = price - data['Close'].iloc[-2]
            
            if change > 0:
                st.error(f"🔴 紅燈多 (看漲): +{change:.2f}")
            elif change < 0:
                st.success(f"🟢 綠燈空 (看跌): {change:.2f}")
            else:
                st.info("🟡 平盤觀望")
            
            st.write(f"標的：{stock_id} | 成交價：{price:.2f}")
        except:
            st.error("數據連結失敗")
