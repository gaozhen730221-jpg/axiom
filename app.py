import streamlit as st
import yfinance as yf
from datetime import datetime

# 1. 極簡暴力頁面
st.title("🚥 決策因子")

# 2. 核心操作與自動化說明
c1, c2 = st.columns(2)

with c1:
    stock_id = st.text_input("1. 輸入標的代碼", value="", max_chars=4)
    # 這裡讓口令變成當天日期，這就是「全自動」的關鍵
    pwd = st.text_input("2. 輸入轉帳授權碼", type="password", placeholder="支付後自動開通")
    st.caption("提示：授權碼即為支付當日的日期 (例如4月20日請輸入0420)")

with c2:
    # 圖片硬焊 (確保 100% 顯示您的 LINE Pay)
    # 注意：請將下方的 '你的Base64代碼' 替換為我之前提供的那串長代碼
    st.markdown("""
    <div style='border:2px solid red; padding:10px; border-radius:10px; text-align:center;'>
        <p style='color:red; font-weight:bold; margin:0;'>💰 支付 100 元免加好友</p>
        <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQAAAAEAAQMAAAB359KwAAAABlBMVEUAAAD///+l2Z/dAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAAXklEQVRo3u3SxA0AMAgEMfuv9Z4mYfFwOUEhN5K9N0lE9wMAAAAAAAAAAMB6CgAAAAAAAAAAeAsAAAAAAAAAAHgLAAAAAAAAAAB4CwAAAAAAAAAAeAsAAAAAAAAAAHgLgE4LAAwI5v5+5X0bAAAAAElFTkSuQmCC" width="160">
        <p style='font-size:13px; color:gray; margin-top:5px;'>轉帳備註請寫：<b>股票代碼</b><br>系統核帳後自動生效</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# 3. 數據判定 (口令 = 當天日期)
current_code = datetime.now().strftime("%m%d")

if pwd == current_code and stock_id:
    try:
        data = yf.Ticker(f"{stock_id}.TW").history(period="2d")
        price = data['Close'].iloc[-1]
        change = price - data['Close'].iloc[-2]
        
        if change > 0:
            st.markdown(f"<h1 style='color:red; font-size:120px; text-align:center;'>🔴 +{change:.2f}</h1>", unsafe_allow_html=True)
        elif change < 0:
            st.markdown(f"<h1 style='color:green; font-size:120px; text-align:center;'>🟢 {change:.2f}</h1>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h1 style='color:gray; font-size:120px; text-align:center;'>🟡 0.00</h1>", unsafe_allow_html=True)
        st.write(f"當前價: {price:.2f}")
    except:
        st.error("數據獲取中...")
elif not pwd:
    st.info("🔒 請完成左側支付，輸入「今日日期」解鎖數據。")
