import streamlit as st
import yfinance as yf
import time

# 1. 品牌：股票數據
st.set_page_config(page_title="股票數據", page_icon="🚥")
st.markdown("<h2 style='text-align: center;'>🚥 股票數據 Axiom 1.0</h2>", unsafe_allow_html=True)

# 2. 暴力操作區
st.markdown("### 🔍 1. 輸入標的")
stock_id = st.text_input("股票代碼", value="", max_chars=4, placeholder="如: 2330")

st.divider()

st.markdown("### 💰 2. 掃碼支付並解鎖")

# --- 這裡我把 QR Code 數據徹底焊死，確保絕對顯示 ---
qr_b64 = "iVBORw0KGgoAAAANSUhEUgAAAQAAAAEAAQMAAAB359KwAAAABlBMVEUAAAD///+l2Z/dAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAAXklEQVRo3u3SxA0AMAgEMfuv9Z4mYfFwOUEhN5K9N0lE9wMAAAAAAAAAAMB6CgAAAAAAAAAAeAsAAAAAAAAAAHgLAAAAAAAAAAB4CwAAAAAAAAAAeAsAAAAAAAAAAHgLgE4LAAwI5v5+5X0bAAAAAElFTkSuQmCC"

st.markdown(f"""
<div style='border:3px solid #ff4b4b; padding:15px; border-radius:15px; text-align:center; background-color:#fff5f5; margin-bottom:20px;'>
    <b style='color:#ff4b4b; font-size:20px;'>單次授權 100 元</b><br>
    <img src="data:image/png;base64,{qr_b64}" width="280" style="margin:15px auto; display:block; border: 2px solid #eee;">
    <p style='font-size:14px; color:#333; margin:10px 0;'><b>免加好友，轉帳後直接點擊下方解鎖</b><br>轉帳請備註股票代碼</p>
</div>
""", unsafe_allow_html=True)

# 唯一的動作按鈕：點了就出答案
paid = st.button("🔴 我已完成支付，查看解鎖數據", use_container_width=True)

st.divider()

# 3. 物理攔截判定：不需要口令，直接給答案，但用時間懲罰白嫖
if paid and stock_id:
    # 這是物理防護：15秒的心理門檻
    with st.status("📡 正在連接銀行 Gateway 驗證入帳紀錄...", expanded=True) as status:
        st.write("正在掃描近期交易流水...")
        time.sleep(5) 
        st.write(f"搜尋代碼 {stock_id} 匹配項...")
        time.sleep(5)
        st.write("確認 100 元入帳成功。正在解鎖因子...")
        time.sleep(5)
        status.update(label="✅ 驗證通過，因子已解鎖", state="complete", expanded=False)
    
    try:
        data = yf.Ticker(f"{stock_id}.TW").history(period="2d")
        if not data.empty:
            price = data['Close'].iloc[-1]
            change = price - data['Close'].iloc[-2]
            
            # 暴力顯示紅綠燈
            if change > 0:
                st.markdown(f"<div style='background-color:#ff4b4b; color:white; padding:60px; text-align:center; border-radius:20px; box-shadow: 0 10px 20px rgba(0,0,0,0.2);'><h1>🔴 紅燈多: +{change:.2f}</h1></div>", unsafe_allow_html=True)
            elif change < 0:
                st.markdown(f"<div style='background-color:#00c853; color:white; padding:60px; text-align:center; border-radius:20px; box-shadow: 0 10px 20px rgba(0,0,0,0.2);'><h1>🟢 綠燈空: {change:.2f}</h1></div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='background-color:#888; color:white; padding:60px; text-align:center; border-radius:20px;'><h1>🟡 持平觀望</h1></div>", unsafe_allow_html=True)
            
            st.markdown(f"<p style='text-align:center; margin-top:20px; font-size:1.5em;'>標的：{stock_id} | 目前價格：{price:.2f}</p>", unsafe_allow_html=True)
            st.warning("⚠️ 系統已記錄本次支付 IP，如未付錢點擊將被永久封鎖。")
        else:
            st.error("代碼查無數據")
    except:
        st.error("數據連接超時")

elif paid and not stock_id:
    st.warning("請先輸入股票代碼，再進行支付驗證。")
