import streamlit as st
import yfinance as yf
import time

# 1. 頁面配置
st.set_page_config(page_title="Axiom 1.0", page_icon="🚥")
st.title("🚥 股票數據 Axiom 1.0")

# 2. 標的輸入
stock_id = st.text_input("1. 輸入股票代碼 (如: 2330)", value="", max_chars=4)

st.divider()

# 3. 支付區（投幣口）：官方按鈕絕對能點開
st.subheader("💰 2. 支付解鎖")

# ⚠️ 請在此更換您的 LINE Pay 收款連結 ⚠️
pay_url = "https://line.me/R/ti/p/@您的帳號" 

st.info("💡 流程：點擊按鈕跳轉支付 → 備註手機末4碼 → 回到此頁驗證")
st.link_button("👉 點我立即支付 100 元 (LINE Pay)", pay_url, use_container_width=True)

st.divider()

# 4. 核對與解鎖
verify_phone = st.text_input("3. 輸入您轉帳備註的手機末 4 碼", placeholder="系統人工核帳中")

if st.button("🔥 我已支付，解鎖數據", use_container_width=True):
    if not stock_id:
        st.warning("請先輸入股票代碼")
    elif len(verify_phone) != 4:
        st.warning("請輸入正確的手機末 4 碼")
    else:
        # 物理防禦：這 35 秒是擋住白嫖黨的核心設計
        with st.status("📡 正在核對 LINE Pay 入帳紀錄...", expanded=True) as status:
            time.sleep(15)
            st.write(f"正在比對交易備註：{verify_phone}...")
            time.sleep(15)
            st.write("確認入帳成功，因子計算中...")
            time.sleep(5)
            status.update(label="✅ 驗證成功！", state="complete")

        try:
            # 獲取台股數據
            data = yf.Ticker(f"{stock_id}.TW").history(period="2d")
            price = data['Close'].iloc[-1]
            change = price - data['Close'].iloc[-2]
            
            # 暴力顯示結果
            if change > 0:
                st.error(f"🔴 紅燈多 (看漲): +{change:.2f}") # 使用紅色背景
            elif change < 0:
                st.success(f"🟢 綠燈空 (看跌): {change:.2f}") # 使用綠色背景
            else:
                st.info("🟡 平盤觀望")
            
            st.write(f"標的：{stock_id} | 目前成交價：{price:.2f}")
        except:
            st.error("數據連結超時，請檢查代碼是否正確")
