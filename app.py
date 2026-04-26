import streamlit as st

# --- AXIOM 1.18 BLCK 品牌視覺 ---
st.set_page_config(page_title="AXIOM 1.18 BLCK", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0c0e11; color: #ffffff; }
    .tesla-card { 
        border: 1px solid #333; padding: 25px; border-radius: 4px; 
        background: #14171c; margin-bottom: 20px;
    }
    .hunt-box { 
        background: linear-gradient(90deg, #1d2229, #0c0e11); 
        border-left: 5px solid #00ff41; padding: 18px; margin: 12px 0;
        text-align: left;
    }
    .pay-zone {
        border: 2px solid #00ff41; 
        background-color: #1a1d23; 
        padding: 25px; 
        border-radius: 8px;
        text-align: center;
        box-shadow: 0 0 15px rgba(0, 255, 65, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; font-weight: 300; letter-spacing: 5px;'>AXIOM 1.18</h1>", unsafe_allow_html=True)

# --- 誘惑區：最強三箭 ---
st.markdown("""
<div class='tesla-card'>
    <p style='color: #00ff41; font-size: 12px; letter-spacing: 2px; text-align: center;'>● AXIOM REAL-TIME CLOUD</p>
    <div class='hunt-box'>🎯 標 A：23** <span style='float: right; color: #00ff41;'>勝率 92%</span></div>
    <div class='hunt-box'>🎯 標 B：62** <span style='float: right; color: #00ff41;'>多頭 89%</span></div>
    <div class='hunt-box'>🎯 標 C：30** <span style='float: right; color: #ff4141;'>預警 94%</span></div>
</div>
""", unsafe_allow_html=True)

# --- 行動區：持股診斷 ---
stock_input = st.text_input("", placeholder="輸入代碼 (如: 2330)")

# --- 關鍵：入金區 (直接讀取您的 GitHub 檔案) ---
if stock_input:
    st.markdown("---")
    st.markdown("<div class='pay-zone'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #00ff41;'>💳 算力通道授權</h3>", unsafe_allow_html=True)
    st.write("請掃碼支付 **NT$ 100** 以解鎖 1.18 深度報告")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        # 直接鎖定您截圖中的那個檔名
        try:
            st.image("1776940866671.jpg", width=220, caption="街口支付 QR Code")
        except:
            st.warning("⚠️ 系統偵測：請確保 1776940866671.jpg 已上傳至 GitHub")
            
    with col2:
        st.write("完成支付後驗證：")
        last_4 = st.text_input("手機末 4 碼", max_chars=4, key="v4")
        if st.button("立即解鎖 (UNLOCK)", use_container_width=True):
            if len(last_4) == 4:
                st.success("算力正在加載...")
            else:
                st.error("請輸入正確末 4 碼")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><p style='text-align: center; color: #222; font-size: 10px;'>AXIOM 1.18 BLCK | DESIGNED IN TAIPEI</p>", unsafe_allow_html=True)
