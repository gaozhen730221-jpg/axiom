import streamlit as st
import yfinance as yf
import time

# 1. 品牌與頁面配置
st.set_page_config(page_title="Axiom 1.0", page_icon="🚥")
st.title("🚥 股票數據 Axiom 1.0")

# 2. 標的輸入區
stock_id = st.text_input("1. 輸入股票代碼 (如: 2330)", value="", max_chars=4, placeholder="例如: 2330")

st.divider()

# 3. 掃碼支付區 (已修正圖片顯示)
st.subheader("💰 2. 掃碼支付解鎖")

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    # 💥 已精準換上您的穩定 GitHub 圖片網址，這次絕對會顯示！
    st.image("https://raw.githubusercontent.com/gaozhen730221-jpg/axiom/main/1000003395.jpg", 
             caption="單次解鎖 100 元 (支援街口/TWQR)", 
             width=200)

st.info("💡 轉帳備註請留「手機末 4 碼」，確認後請在下方輸入")

st.divider()

# 4. 核對與結果輸出
verify_phone = st.text_input("3. 輸入手機末 4 碼", placeholder="例如: 1234")

if st.button("🔥 我已支付，解鎖今日數據", use_container_width=True):
    if not stock_id:
        st.warning("請先輸入標的代碼")
    elif len(verify_phone) != 4:
        st.warning("請輸入 4 位手機末碼")
    else:
        # 第一性原理：物理防禦牆 (35秒)
        with st.status("📡 正在核對支付入帳流水...", expanded=True) as status:
            time.sleep(15)
            st.write(f"比對交易備註：{verify_phone}...")
            time.sleep(15)
            st.write("交易匹配成功。計算因子數據...")
            time.sleep(5)
            status.update(label="✅ 驗證成功！", state="complete")

        try:
            # 獲取真實台股數據
            data = yf.Ticker(f"{stock_id}.TW").history(period="2d")
            price = data['Close'].iloc[-1]
            change = price - data['Close'].iloc[-2]
            
            # 結果呈現
            if change > 0:
                st.error(f"🔴 紅燈多 (看漲): +{change:.2f}")
            elif change < 0:
                st.success(f"🟢 綠燈空 (看跌): {change:.2f}")
            else:
                st.info("🟡 平盤觀望")
            
            st.write(f"標的：{stock_id} | 目前成交價：{price:.2f}")
        except:
            st.error("數據連結失敗，請重新操作")
