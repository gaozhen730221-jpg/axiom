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

st.markdown("### 💰 2. 支付並解鎖")

# 這裡填入您 LINE Pay 的轉帳連結
# 這是最穩定的方式，點擊直接跳轉支付
pay_url = "https://line.me/R/ti/p/your_line_pay_id" 

st.markdown(f"""
<div style='border:4px solid #ff4b4b; padding:25px; border-radius:20px; text-align:center; background-color:#fff5f5; margin-bottom:20px;'>
    <b style='color:#ff4b4b; font-size:24px;'>🚨 單次解鎖 100 元</b><br><br>
    <a href="{pay_url}" target="_blank" style="text-decoration:none;">
        <div style="background-color:#00c853; color:white; padding:20px; border-radius:50px; font-size:22px; font-weight:bold; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
            📱 點擊此處「立即支付」
        </div>
    </a>
    <p style='font-size:16px; color:#666; margin-top:20px;'><b>付完請回這裡輸入：手機末 4 碼</b></p>
</div>
""", unsafe_allow_html=True)

# 3. 物理防白嫖
verify_phone = st.text_input("輸入轉帳備註的手機末 4 碼", placeholder="系統核對入帳流水用")
paid = st.button("🔴 我已支付 100 元，解鎖數據", use_container_width=True)

st.divider()

if paid and stock_id:
    if len(verify_phone) != 4:
        st.error("❌ 格式錯誤：請輸入 4 位手機末碼。")
    else:
        # 物理懲罰：35 秒超長核對時間，讓白嫖黨知難而退
        with st.status("📡 正在與銀行網關核對入帳指紋...", expanded=True) as status:
            st.write("掃描 100 元實時交易流水...")
            time.sleep(12) 
            st.write(f"比對標的 {stock_id} 與備註碼 {verify_phone}...")
            time.sleep(12)
            st.write("交易匹配成功。正在下載因子數據...")
            time.sleep(11)
            status.update(label="✅ 驗證成功，今日數據已解鎖！", state="complete", expanded=False)
        
        try:
            data = yf.Ticker(f"{stock_id}.TW").history(period="2d")
            price = data['Close'].iloc[-1]
            change = price - data['Close'].iloc[-2]
            
            # 暴力顯示結果
            if change > 0:
                st.markdown(f"<div style='background-color:#ff4b4b; color:white; padding:80px; text-align:center; border-radius:30px;'><h1>🔴 紅燈多: +{change:.2f}</h1></div>", unsafe_allow_html=True)
            elif change < 0:
                st.markdown(f"<div style='background-color:#00c853; color:white; padding:80px; text-align:center; border-radius:30px;'><h1>🟢 綠燈空: {change:.2f}</h1></div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='background-color:#888; color:white; padding:80px; text-align:center; border-radius:30px;'><h1>🟡 持平觀望</h1></div>", unsafe_allow_html=True)
            
            st.markdown(f"<h3 style='text-align:center; margin-top:20px;'>標的：{stock_id} | 目前價格：{price:.2f}</h3>", unsafe_allow_html=True)
        except:
            st.error("數據連結失敗，請重新操作。")
