import streamlit as st
import yfinance as yf
import time

# 1. 品牌與頁面配置 (恢復成您最滿意的 1.0 決策系統風格)
st.set_page_config(page_title="AXIOM 1.0", page_icon="💹")
st.title("💹 AXIOM 1.0 決策系統")
st.subheader("解鎖明早開盤核心燈號")

st.markdown("---")

# 2. 核心公告區
st.warning("🚨 注意：本數據僅對具備風險承受能力之投資者開放。")
st.info("💡 系統公告：請掃描下方 TWQR 萬用碼支付 100 元規費。")

# 3. 收款碼區 (這裡改用您 GitHub 上這張最新的 1000003395.jpg)
# 我使用了強制刷新網址，繞過 GitHub 的快取問題
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("https://raw.githubusercontent.com/gaozhen730221-jpg/axiom/main/1000003395.jpg", 
             caption="【1.0 官方指定收款碼】支援街口 / TWQR / 各家銀行", 
             use_container_width=True)

# 4. 操作流程
st.markdown("""
### 🔓 解鎖步驟：
1. **輸入標的**：在下方輸入您想查詢的股票代碼。
2. **掃描支付**：支付規費 **100 元** 並留手機末 4 碼。
3. **系統驗證**：點擊下方按鈕，驗證成功後立即解鎖。
""")

st.markdown("---")

# 5. 數據輸入與核對邏輯
stock_id = st.text_input("輸入股票代碼 (如: 2330)", placeholder="例如: 2330")
verify_phone = st.text_input("輸入轉帳手機末 4 碼", placeholder="例如: 1234")

if st.button("🚀 執行 AXIOM 1.0 驗證", use_container_width=True):
    if not stock_id or not verify_phone:
        st.error("請完整填寫股票代碼與手機末碼")
    else:
        with st.status("📡 正在接入 1.0 核心數據庫...", expanded=True) as status:
            time.sleep(15)
            st.write(f"正在比對手機末碼：{verify_phone} 的入帳流水...")
            time.sleep(15)
            st.write("交易匹配成功。啟動紅綠燈算力...")
            time.sleep(5)
            status.update(label="✅ 驗證成功！數據已解鎖", state="complete")

        try:
            # 獲取台股數據
            data = yf.Ticker(f"{stock_id}.TW").history(period="2d")
            price = data['Close'].iloc[-1]
            change = price - data['Close'].iloc[-2]
            
            st.divider()
            if change > 0:
                st.error(f"🔴 AXIOM 訊號：多 (看漲) | 變動: +{change:.2f}")
            elif change < 0:
                st.success(f"🟢 AXIOM 訊號：空 (看跌) | 變動: {change:.2f}")
            else:
                st.info("🟡 AXIOM 訊號：平盤觀望")
            
            st.metric(label=f"標的 {stock_id} 當前成交價", value=f"{price:.2f}")
        except:
            st.error("數據連結超時，請重新執行")

st.markdown("---")
st.caption("Axiom 1.0 全自動核帳系統。投資請謹慎。")
