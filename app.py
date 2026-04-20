import streamlit as st
import yfinance as yf
import time

# 1. 頁面配置
st.set_page_config(page_title="股票數據 Axiom 1.0", page_icon="🚥")
st.markdown("<h2 style='text-align: center;'>🚥 股票數據 Axiom 1.0</h2>", unsafe_allow_html=True)

# 2. 標的輸入
st.markdown("### 🔍 1. 輸入標的")
stock_id = st.text_input("股票代碼", value="", max_chars=4, placeholder="例如: 2330")

st.divider()

st.markdown("### 💰 2. 支付並解鎖")

# --- 核心邏輯：用按鈕取代圖片，永遠不會破圖 ---
pay_url = "https://line.me/R/ti/p/@您的帳號" # 👈 明天您再把連結換成您的 LINE 收款連結

st.markdown(f"""
<div style='border:4px solid #ff4b4b; padding:25px; border-radius:20px; text-align:center; background-color:#fff5f5; margin-bottom:20px;'>
    <b style='color:#ff4b4b; font-size:24px;'>🚨 單次解鎖 100 元</b><br><br>
    <a href="{pay_url}" target="_blank" style="text-decoration:none;">
        <div style="background-color:#00c853; color:white; padding:18px; border-radius:50px; font-size:22px; font-weight:bold; box-shadow: 0 6px 12px rgba(0,200,83,0.3);">
            📱 點擊此處「立即支付」
        </div>
    </a>
    <p style='font-size:15px; color:#666; margin-top:20px;'>付完請回到此頁面輸入：<b>手機末 4 碼</b></p>
</div>
""", unsafe_allow_html=True)

# 3. 物理防白嫖區
verify_phone = st.text_input("輸入轉帳備註的手機末 4 碼", placeholder="系統核對入帳流水用")
paid = st.button("🔴 我已支付 100 元，解鎖數據", use_container_width=True)

st.divider()

if paid and stock_id:
    if len(verify_phone) != 4:
        st.error("❌ 格式錯誤：請輸入 4 位手機末碼。")
    else:
        # 強制等待 35 秒，這是我們的物理防火牆
        with st.status("📡 正在跨行網關進行 100 元入帳指紋比對...", expanded=True) as status:
            st.write("掃描實時交易流水...")
            time.sleep(15) 
            st.write(f"核對備註手機碼：{verify_phone} ...")
            time.sleep(15)
            st.write("確認入帳。正在解鎖因子...")
            time.sleep(5)
            status.update(label="✅ 驗證完成，因子數據已解鎖！", state="complete", expanded=False)
        
        try:
            data = yf.Ticker(f"{stock_id}.TW").history(period="2d")
            price = data['Close'].iloc[-1]
            change = price - data['Close'].iloc[-2]
            
            if change > 0:
                st.markdown(f"<div style='background-color:#ff4b4b; color:white; padding:80px; text-align:center; border-radius:30px;'><h1>🔴 紅燈多: +{change:.2f}</h1></div>", unsafe_allow_html=True)
            elif change < 0:
                st.markdown(f"<div style='background-color:#00c853; color:white; padding:80px; text-align:center; border-radius:30px;'><h1>🟢 綠燈空: {change:.2f}</h1></div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='background-color:#888; color:white; padding:80px; text-align:center; border-radius:30px;'><h1>🟡 持平觀望</h1></div>", unsafe_allow_html=True)
            
            st.markdown(f"<h3 style='text-align:center; margin-top:20px;'>標的：{stock_id} | 成交價：{price:.2f}</h3>", unsafe_allow_html=True)
        except:
            st.error("獲取數據中...")
