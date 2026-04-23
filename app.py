import streamlit as st

# --- 1. 網頁基礎設定 ---
st.set_page_config(
    page_title="AXIOM 1.0 - 贏家核心數據",
    page_icon="💹",
    layout="centered"
)

# --- 2. 標題與視覺頭部 ---
st.title("💹 AXIOM 1.0 決策系統")
st.subheader("解鎖明早開盤核心燈號")
st.markdown("---")

# --- 3. 核心警告文案 (建立專業感) ---
st.warning("🚨 注意：本數據僅對具備風險承受能力之投資者開放。")

# --- 4. 關鍵收款區塊 (這是最重要的部分) ---
st.info("💡 系統公告：為確保支付順暢，請掃描下方 TWQR 萬用碼支付 100 元規費。")

# 這裡精準嵌入您的街口/TWQR 收款碼
# 確保圖片能撐滿螢幕，讓股民掃得清楚
st.image(
    "https://raw.githubusercontent.com/gaozhen730221-jpg/axiom/main/1000003395.jpg", 
    caption="【1.0 官方指定收款碼】支援：街口支付 / TWQR / 全支付 / 各家銀行 App", 
    use_container_width=True
)

# --- 5. 操作流程說明 ---
st.markdown("""
### 🔓 解鎖步驟：
1. **掃描上方 QR Code** 支付規費 **100 元**。
2. **截圖支付成功畫面**。
3. 系統驗證後，將立即解鎖 **1.0 核心波段燈號**。
""")

st.markdown("---")

# --- 6. 頁尾資訊 ---
st.caption("Axiom 1.0 全自動核帳系統。100 元僅為數據運算成本。投資請謹慎。")
st.text("當前狀態：1.0 核心運作中 | 數據延遲：0.03ms")
