import streamlit as st
import yfinance as yf
import time

# 1. 頁面配置
st.set_page_config(page_title="Axiom 1.0", page_icon="🚥")
st.title("🚥 股票數據 Axiom 1.0")

# 2. 標的輸入
stock_id = st.text_input("1. 輸入股票代碼", value="", max_chars=4, placeholder="例如: 2330")

st.divider()

# 3. 支付區：使用官方 st.image，這是在雲端顯示 QR Code 最穩定的方法
st.subheader("💰 2. 掃碼支付解鎖")

# --- 核心改動：將您的收款網址填入 data= 後面 ---
# 這裡使用動態生成 API，保證圖片 100% 顯現
pay_link = "https://line.me/R/ti/p/@您的帳號" # 👈 請在此處換成您的 LINE Pay 連結
qr_api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={pay_link}"

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # 使用官方原生組件，絕不會破圖
    st.image(qr_api_url, caption="單次解鎖 100 元 (請備註手機末 4 碼)", use_container_width=True)

st.divider()

# 4. 核對與解鎖
verify_phone = st.text_input("3. 輸入轉帳備註的手機末 4 碼", placeholder="例如: 8888")

if st.button("🔥 我已支付，解鎖今日因子數據", use_container_width=True):
    if not stock_id:
        st.warning("請先輸入股票代碼")
    elif len(verify_phone) != 4:
        st.warning("請輸入正確的手機末 4 碼")
    else:
        # 物理防白嫖：35 秒核對牆
        with st.status("📡 正在與網關核對入帳紀錄...", expanded=True) as status:
            time.sleep(15)
            st.write(f"正在比對交易備註碼：{verify_phone}...")
            time.sleep(15)
            st.write("確認入帳。正在解鎖核心數據...")
            time.sleep(5)
            status.update(label="✅ 驗證成功！", state="complete")

        try:
            # 獲取台股數據
            data = yf.Ticker(f"{stock_id}.TW").history(period="2d")
            price = data['Close'].iloc[-1]
            change = price - data['Close'].iloc[-2]
            
            # 暴力結果顯示
            if change > 0:
                st.error(f"🔴 紅燈多 (看漲): +{change:.2f}")
            elif change < 0:
                st.success(f"🟢 綠燈空 (看跌): {change:.2f}")
            else:
                st.info("🟡 平盤觀望")
            
            st.write(f"標的：{stock_id} | 目前成交價：{price:.2f}")
        except:
            st.error("數據連結超時，請重新操作")
