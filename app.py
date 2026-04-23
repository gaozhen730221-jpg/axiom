import streamlit as st

# 設定網頁標題
st.set_page_config(page_title="AXIOM 1.0", page_icon="💹")

# 標題與說明
st.title("💹 AXIOM 1.0 決策系統")
st.subheader("解鎖明早開盤核心燈號")

st.markdown("---")

# 核心公告
st.warning("🚨 目前僅對具備風險承受能力的投資者開放。")

# 收款碼區塊
st.info("💡 系統公告：請掃描下方 TWQR 萬用碼支付 100 元規費。")

# 這裡我換了一個更穩定的圖片顯示方式
st.image("https://raw.githubusercontent.com/gaozhen730221-jpg/axiom/main/1000003395.jpg", 
         caption="【1.0 官方指定收款碼】支援街口 / TWQR / 各家銀行", 
         use_container_width=True)

# 操作步驟
st.markdown("""
### 🔓 解鎖步驟：
1. **掃描上方 QR Code** 支付規費 **100 元**。
2. **截圖支付成功畫面**。
3. 系統驗證後，將立即解鎖 **1.0 核心波段燈號**。
""")

st.markdown("---")
# 底部文字（簡化版，避免錯誤）
st.text("Axiom 1.0 全自動核帳系統。本工具僅供參考。")
