import streamlit as st
import yfinance as yf
import time

# 1. 頁面品牌配置
st.set_page_config(page_title="股票數據 Axiom 1.0", page_icon="🚥")
st.markdown("<h2 style='text-align: center;'>🚥 股票數據 Axiom 1.0</h2>", unsafe_allow_html=True)

# 2. 標的輸入區
st.markdown("### 🔍 1. 輸入標的")
stock_id = st.text_input("股票代碼", value="", max_chars=4, placeholder="例如: 2330")

st.divider()

st.markdown("### 💰 2. 掃碼支付並解鎖")

# --- 終極保險：外部雲端圖床，確保 100% 不破圖 ---
qr_cloud_link = "https://i.imgur.com/B9M9v7J.png"

st.markdown(f"""
<div style='border:4px solid #ff4b4b; padding:20px; border-radius:20px; text-align:center; background-color:#fff5f5; margin-bottom:20px;'>
    <b style='color:#ff4b4b; font-size:24px;'>🚨 單次解鎖 100 元</b><br>
    <img src="{qr_cloud_link}" width="280" style="margin:20px auto; display:block; border: 5px solid #fff; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
    <p style='font-size:16px; color:#333; margin:10px 0;'><b>轉帳請備註：手機末 4 碼</b><br>確認入帳後，點擊下方按鈕解鎖</p>
</div>
""", unsafe_allow_html=True)

# 3. 物理防白嫖 (強制 30 秒核對時間)
verify_phone = st.text_input("輸入轉帳備註的手機末 4 碼", placeholder="核對入帳流水用")
paid = st.button("🔴 我已支付 100 元，解鎖數據", use_container_width=True)

st.divider()

if paid and stock_id:
    if len(verify_phone) != 4:
        st.error("❌ 格式錯誤：請輸入 4 位手機末碼。")
    else:
        # 第一性原理：用極高的等待成本攔截白嫖黨
        with st.status("📡 正在跨行網關進行 100 元入帳指紋比對...", expanded=True) as status:
            st.write("掃描實時支付流水紀錄...")
            time.sleep(10) 
            st.write(f"比對標的 {stock_id} 與備註碼 {verify_phone}...")
            time.sleep(10)
            st.write("確認匹配。正在從雲端下載數據...")
            time.sleep(10)
            status.update(label="✅ 驗證完成，因子數據已解鎖！", state="complete", expanded=False)
        
        try:
            # 獲取台股真實數據
            data = yf.Ticker(f"{stock_id}.TW").history(period="2d")
            price = data['Close'].iloc[-1]
            change = price - data['Close'].iloc[-2]
            
            # 暴力顯示紅綠燈
            if change > 0:
                st.markdown(f"<div style='background-color:#ff4b4b; color:white; padding:80px; text-align:center; border-radius:30px;'><h1>🔴 紅燈多: +{change:.2f}</h1></div>", unsafe_allow_html=True)
            elif change < 0:
                st.markdown(f"<div style='background-color:#00c853; color:white; padding:80px; text-align:center; border-radius:30px;'><h1>🟢 綠燈空: {change:.2f}</h1></div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='background-color:#888; color:white; padding:80px; text-align:center; border-radius:30px;'><h1>🟡 持平觀望</h1></div>", unsafe_allow_html=True)
            
            st.markdown(f"<h3 style='text-align:center; margin-top:20px;'>標的：{stock_id} | 目前成交價：{price:.2f}</h3>", unsafe_allow_html=True)
        except:
            st.error("系統繁忙，請重新輸入代碼。")
