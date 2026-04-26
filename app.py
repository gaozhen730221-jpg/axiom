import streamlit as st
import os

# --- AXIOM 1.18 極致黑魂版 ---
st.set_page_config(page_title="AXIOM 1.18", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0c0e11; color: #ffffff; }
    .tesla-card { border: 1px solid #333; padding: 25px; border-radius: 4px; background: #14171c; margin-bottom: 20px; text-align: center; }
    .hunt-box { background: linear-gradient(90deg, #1d2229, #0c0e11); border-left: 5px solid #00ff41; padding: 18px; margin: 12px 0; text-align: left; }
    .pay-zone { border: 2px solid #00ff41; background-color: #1a1d23; padding: 25px; border-radius: 8px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; letter-spacing: 5px;'>AXIOM 1.18</h1>", unsafe_allow_html=True)

# --- 第一區：今日獵殺 (遮蔽誘惑) ---
st.markdown("""
<div class='tesla-card'>
    <div class='hunt-box'>🎯 標 A：23** <span style='float: right; color: #00ff41;'>勝率 92%</span></div>
    <div class='hunt-box'>🎯 標 B：62** <span style='float: right; color: #00ff41;'>多頭 89%</span></div>
    <div class='hunt-box'>🎯 標 C：30** <span style='float: right; color: #ff4141;'>預警 94%</span></div>
</div>
""", unsafe_allow_html=True)

# --- 第二區：輸入代碼 ---
target_id = st.text_input("", placeholder="輸入代碼 (如: 2330) 移除算力迷霧")

# --- 第三區：強制入金門戶 ---
if target_id:
    st.markdown("---")
    st.markdown("<div class='pay-zone'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #00ff41;'>💳 算力通道授權</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        # 【核心修正】直接點名截圖中的那個收錢檔名
        QR_PATH = "1776940866671.jpg"
        
        if os.path.exists(QR_PATH):
            st.image(QR_PATH, width=220, caption="街口支付 QR Code")
        else:
            # 這是最終防線：如果檔案沒上傳，直接顯示錯誤引導
            st.error(f"❌ 警告：伺服器找不到 {QR_PATH}")
            st.info("請檢查 GitHub 目錄是否有此圖檔")
            
    with col2:
        st.write("單次授權 NT$ 100")
        last_4 = st.text_input("手機末 4 碼", max_chars=4, key="v4")
        if st.button("立即解鎖 (UNLOCK)", use_container_width=True):
            if len(last_4) == 4:
                st.success("算力解析中... 請稍候")
            else:
                st.error("末 4 碼不全")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><p style='text-align: center; color: #333; font-size: 10px;'>AXIOM 1.18 BLCK | POWERED BY CHIEF</p>", unsafe_allow_html=True)
