import streamlit as st

# --- 介面設定 ---
st.set_page_config(page_title="AXIOM 1.18 BLCK", layout="centered")

# --- Tesla Black Style CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #0c0e11; color: #ffffff; }
    .tesla-card { border: 1px solid #333; padding: 25px; border-radius: 4px; background: #14171c; margin-bottom: 20px; }
    .hunt-box { background: linear-gradient(90deg, #1d2229, #0c0e11); border-left: 5px solid #00ff41; padding: 18px; margin: 12px 0; }
    .stTextInput>div>div>input { background-color: #14171c; color: white; border: 1px solid #333; border-radius: 0px; }
    .pay-section { background-color: #1a1d23; border: 1px solid #00ff41; padding: 20px; border-radius: 4px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; letter-spacing: 5px;'>AXIOM 1.18</h1>", unsafe_allow_html=True)

# --- 1. 最強三箭 (誘惑區) ---
st.markdown("""
<div class='tesla-card'>
    <p style='color: #00ff41; font-size: 12px; letter-spacing: 2px; text-align: center;'>● AXIOM REAL-TIME CLOUD</p>
    <div class='hunt-box'>🎯 標 A：23** <span style='float: right; color: #00ff41;'>勝率 92%</span></div>
    <div class='hunt-box'>🎯 標 B：62** <span style='float: right; color: #00ff41;'>多頭 89%</span></div>
    <div class='hunt-box'>🎯 標 C：30** <span style='float: right; color: #ff4141;'>預警 94%</span></div>
</div>
""", unsafe_allow_html=True)

# --- 2. 持股診斷 (行動區) ---
st.markdown("<p style='text-align: center; color: #444;'>— 診斷持股 / 解鎖三箭 —</p>", unsafe_allow_html=True)
stock_input = st.text_input("", placeholder="請輸入台股代碼")

# --- 3. 關鍵支付區 (QR Code 強制彈出) ---
if stock_input:
    st.markdown("---")
    # 建立一個支付黑盒
    st.markdown("<div class='pay-section'>", unsafe_allow_html=True)
    st.markdown("### 💳 算力通道授權")
    st.write("解鎖費用：NT$ 100")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        # --- 重要：這裡請換成您的 QR Code 檔案名稱或連結 ---
        try:
            st.image("pay_qr.png", width=200, caption="長按掃碼支付")
        except:
            # 如果讀不到圖，就顯示一個提示，方便您測試
            st.warning("⚠️ 請上傳 QR Code 圖檔 (pay_qr.png)")
    
    with col2:
        st.write("請掃碼完成支付後")
        phone_last_4 = st.text_input("輸入手機末 4 碼核對", max_chars=4)
        if st.button("確認解鎖 (UNLOCK)"):
            if len(phone_last_4) == 4:
                st.success("1.18 數據加載中... 請稍候")
            else:
                st.error("末 4 碼格式錯誤")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><p style='text-align: center; color: #222; font-size: 10px;'>VERSION 1.18.0 BLCK</p>", unsafe_allow_html=True)
