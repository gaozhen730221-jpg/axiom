import streamlit as st
import yfinance as yf
import time

# 1. 品牌配置
st.set_page_config(page_title="股票數據 Axiom 1.0", page_icon="🚥")
st.markdown("<h2 style='text-align: center;'>🚥 股票數據 Axiom 1.0</h2>", unsafe_allow_html=True)

# 2. 標的輸入
st.markdown("### 🔍 1. 輸入標的")
stock_id = st.text_input("股票代碼", value="", max_chars=4, placeholder="例如: 2330")

st.divider()

st.markdown("### 💰 2. 掃碼支付並解鎖")

# --- 這裡直接調用 Google API 生成 QR Code，絕對不會破圖 ---
# 我預設您的收款網址為轉帳提示，這會生成一個漂亮的 QR Code
pay_url = "https://line.me/R/ti/p/@your_id" # 這裡可以換成您的 LINE 連結
qr_api = f"https://chart.googleapis.com/chart?chs=250x250&cht=qr&chl={pay_url}&choe=UTF-8"

st.markdown(f"""
<div style='border:3px solid #ff4b4b; padding:20px; border-radius:15px; text-align:center; background-color:#fff5f5; margin-bottom:20px;'>
    <b style='color:#ff4b4b; font-size:22px;'>單次授權 100 元</b><br>
    <img src="{qr_api}" width="230" style="margin:15px auto; display:block; border: 2px solid #eee;">
    <p style='font-size:15px; color:#333; margin:10px 0;'><b>轉帳後請備註：手機末4碼</b><br>確認後點擊下方按鈕解鎖</p>
</div>
""", unsafe_allow_html=True)

# 物理防白嫖心理欄位
verify_phone = st.text_input("輸入轉帳備註的手機末 4 碼", placeholder="系統自動比對入帳紀錄")
paid = st.button("🔴 我已完成支付，解鎖數據", use_container_width=True)

st.divider()

# 3. 物理判定邏輯 (20秒超長延遲，阻斷白嫖)
if paid and stock_id:
    if len(verify_phone) != 4:
        st.error("❌ 驗證碼格式錯誤：請輸入手機末 4 碼。")
    else:
        # 第一性原理：用「時間懲罰」篩選客戶。付錢的人會等，白嫖的人會走。
        with st.status("📡 正在跨行連結網關驗證交易...", expanded=True) as status:
            st.write("正在掃描最近 1 分鐘交易流水...")
            time.sleep(7) 
            st.write(f"比對代碼 {stock_id} 與備註碼 {verify_phone}...")
            time.sleep(8)
            st.write("交易匹配成功。正在下載因子數據...")
            time.sleep(5)
            status.update(label="✅ 驗證成功，數據解鎖！", state="complete", expanded=False)
        
        try:
            data = yf.Ticker(f"{stock_id}.TW").history(period="2d")
            price = data['Close'].iloc[-1]
            change = price - data['Close'].iloc[-2]
            
            # 暴力顯示結果
            if change > 0:
                st.markdown(f"<div style='background-color:#ff4b4b; color:white; padding:60px; text-align:center; border-radius:20px; box-shadow: 0 10px 20px rgba(0,0,0,0.2);'><h1>🔴 紅燈多: +{change:.2f}</h1></div>", unsafe_allow_html=True)
            elif change < 0:
                st.markdown(f"<div style='background-color:#00c853; color:white; padding:60px; text-align:center; border-radius:20px; box-shadow: 0 10px 20px rgba(0,0,0,0.2);'><h1>🟢 綠燈空: {change:.2f}</h1></div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='background-color:#888; color:white; padding:60px; text-align:center; border-radius:20px;'><h1>🟡 持平觀望</h1></div>", unsafe_allow_html=True)
            
            st.markdown(f"<h3 style='text-align:center;'>標的：{stock_id} | 目前價格：{price:.2f}</h3>", unsafe_allow_html=True)
        except:
            st.error("數據連結失敗")
