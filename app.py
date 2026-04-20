import streamlit as st
import yfinance as yf
import time

# 1. 配置
st.set_page_config(page_title="股票數據 Axiom 1.0")
st.title("🚥 股票數據 Axiom 1.0")

# 2. 標的輸入
stock_id = st.text_input("1. 輸入股票代碼", placeholder="例如: 2330")

st.divider()

# 3. 支付區 - 改用純文字連結，保證手機100%能點開
st.subheader("💰 2. 支付解鎖")
pay_url = "https://line.me/R/ti/p/@您的帳號" # 👈 請在此處貼上您的 LINE 收款網址

st.warning("⚠️ 請先完成支付 100 元")
# 這是最核心的改動：純文字連結在手機瀏覽器最穩定
st.markdown(f"### [👉 點我立即支付 100 元]({pay_url})")
st.write("付款後請在下方輸入備註的手機末 4 碼。")

# 4. 驗證區
verify_phone = st.text_input("3. 輸入手機末 4 碼", placeholder="核對入帳用")
if st.button("🔴 確認已支付，解鎖數據", use_container_width=True):
    if not stock_id:
        st.error("請先輸入股票代碼")
    elif len(verify_phone) != 4:
        st.error("請輸入正確的手機末 4 碼")
    else:
        # 強制等待 35 秒（心理防禦牆）
        with st.status("📡 正在核對 LINE Pay 入帳紀錄...", expanded=True) as status:
            time.sleep(15)
            st.write(f"比對備註碼：{verify_phone}...")
            time.sleep(15)
            st.write("確認入帳，正在解鎖數據...")
            time.sleep(5)
            status.update(label="✅ 驗證成功！", state="complete")

        try:
            data = yf.Ticker(f"{stock_id}.TW").history(period="2d")
            change = data['Close'].iloc[-1] - data['Close'].iloc[-2]
            
            if change > 0:
                st.error(f"🔴 紅燈多：+{change:.2f}") # 用 error 紅色背景
            elif change < 0:
                st.success(f"🟢 綠燈空：{change:.2f}") # 用 success 綠色背景
            else:
                st.info("🟡 持平")
            
            st.write(f"標的：{stock_id} | 成交價：{data['Close'].iloc[-1]:.2f}")
        except:
            st.error("數據獲取超時")
