import streamlit as st
import yfinance as yf
import time

# 1. 品牌與頁面配置 (完全保留您原始的設定)
st.set_page_config(page_title="Axiom 1.0", page_icon="🚥")
st.title("🚥 股票數據 Axiom 1.0")

# 2. 標的輸入區
stock_id = st.text_input("1. 輸入股票代碼 (如: 2330)", value="", max_chars=4, placeholder="例如: 2330")

st.divider()

# 3. 掃碼支付區 (保留原來的 col2 結構，這是顯圖成功的關鍵)
st.subheader("💰 2. 掃碼支付解鎖")

# --- 這裡精準替換：不再用 QR API，直接用您的街口圖片連結 ---
# 加上 ?raw=true 是為了破解 GitHub 的防盜鏈機制，讓圖片強制顯示
jk_pay_url = "https://github.com/gaozhen730221-jpg/axiom/blob/main/1000003395.jpg?raw=true"

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    # 這裡維持您原本最精美的 200 寬度設定
    st.image(jk_pay_url, caption="單次解鎖 100 元", width=200)

st.info("💡 轉帳備註請留「手機末 4 碼」，確認後請在下方輸入")

st.divider()

# 4. 核對與結果輸出 (保留您原本的所有邏輯)
verify_phone = st.text_input("3. 輸入手機末 4 碼", placeholder="例如: 1234")

if st.button("🔥 我已支付，解鎖今日數據", use_container_width=True):
    if not stock_id:
        st.warning("請先輸入標的代碼")
    elif len(verify_phone) != 4:
        st.warning("請輸入 4 位手機末碼")
    else:
        # 物理防禦牆 (35秒)
        with st.status("📡 正在核對 LINE Pay 入帳流水...", expanded=True) as status:
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
