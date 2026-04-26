import streamlit as st
import os

# --- 1.0 極致視覺設定 ---
st.set_page_config(page_title="AXIOM 1.0", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0c0e11; color: #ffffff; }
    .tesla-card { border: 1px solid #333; padding: 25px; border-radius: 4px; background: #14171c; margin-bottom: 20px; }
    .hunt-box { background: linear-gradient(90deg, #1d2229, #0c0e11); border-left: 5px solid #00ff41; padding: 18px; margin: 12px 0; }
    .pay-zone { border: 2px solid #00ff41; background-color: #1a1d23; padding: 25px; border-radius: 8px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; letter-spacing: 5px;'>AXIOM 1.0</h1>", unsafe_allow_html=True)

# --- 1. 誘惑區：最強三箭 ---
st.markdown("""
<div class='tesla-card'>
    <p style='color: #00ff41; font-size: 12px; letter-spacing: 2px; text-align: center;'>● AXIOM REAL-TIME CLOUD</p>
    <div class='hunt-box'>🎯 標 A：23** <span style='float: right; color: #00ff41;'>勝率 92%</span></div>
    <div class='hunt-box'>🎯 標 B：62** <span style='float: right; color: #00ff41;'>多頭 89%</span></div>
    <div class='hunt-box'>🎯 標 C：30** <span style='float: right; color: #ff4141;'>預警 94%</span></div>
</div>
""", unsafe_allow_html=True)

# --- 2. 診斷輸入區 ---
stock_input = st.text_input("", placeholder="輸入代碼解鎖算力 (如: 2330)")

# --- 3. 核心入金門戶 (只要輸入代碼就強制掃描圖檔) ---
if stock_input:
    st.markdown("---")
    st.markdown("<div class='pay-zone'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #00ff41;'>💳 算力通道授權</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        # --- 暴力掃描邏輯：抓取目錄下除了 app.py 以外的任何圖片 ---
        valid_exts = ('.jpg', '.jpeg', '.png', '.JPG', '.PNG')
        all_files = os.listdir('.')
        # 排除 app.py，抓取第一張圖
        img_files = [f for f in all_files if f.lower().endswith(valid_exts) and f != 'app.py']
        
        if img_files:
            # 優先顯示你剛剛上傳的那張圖
            st.image(img_files[0], width=230, caption="長按掃碼支付 NT$ 100")
        else:
            st.error("⚠️ 倉庫偵測不到圖檔")
            st.info("請確認 GitHub Commit 成功。")
            
    with col2:
        st.write("支付完成後核對：")
        last_4 = st.text_input("手機末 4 碼", max_chars=4, key="v4")
        if st.button("確認解鎖 (UNLOCK)", use_container_width=True):
            st.success("算力正在開啟... 請稍候")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><p style='text-align: center; color: #222; font-size: 10px;'>AXIOM 1.0 | POWERED BY CHIEF</p>", unsafe_allow_html=True)
