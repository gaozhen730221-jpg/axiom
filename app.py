import streamlit as st
import os
from PIL import Image

# --- 極致黑魂視覺 ---
st.set_page_config(page_title="AXIOM 1.18 BLCK", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0c0e11; color: #ffffff; }
    .tesla-card { border: 1px solid #333; padding: 25px; border-radius: 4px; background: #14171c; margin-bottom: 20px; text-align: center; }
    .hunt-box { background: linear-gradient(90deg, #1d2229, #0c0e11); border-left: 5px solid #00ff41; padding: 18px; margin: 12px 0; text-align: left; }
    .pay-zone { border: 2px solid #00ff41; background-color: #1a1d23; padding: 25px; border-radius: 8px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; letter-spacing: 5px;'>AXIOM 1.18</h1>", unsafe_allow_html=True)

# --- 誘惑區 ---
st.markdown("""
<div class='tesla-card'>
    <div class='hunt-box'>🎯 標 A：23** <span style='float: right; color: #00ff41;'>勝率 92%</span></div>
    <div class='hunt-box'>🎯 標 B：62** <span style='float: right; color: #00ff41;'>多頭 89%</span></div>
    <div class='hunt-box'>🎯 標 C：30** <span style='float: right; color: #ff4141;'>預警 94%</span></div>
</div>
""", unsafe_allow_html=True)

# --- 輸入區 ---
target_id = st.text_input("", placeholder="請輸入台股代碼以解鎖算力報告")

# --- 強制顯示 QR Code 邏輯 ---
if target_id:
    st.markdown("---")
    st.markdown("<div class='pay-zone'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #00ff41;'>💳 算力通道授權</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        # 鎖定您截圖中的檔名
        QR_FILE = "1776940866671.jpg"
        
        # 暴力路徑掃描與讀取
        current_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(current_dir, QR_FILE)
        
        if os.path.exists(full_path):
            # 使用 PIL 開啟以確保圖檔完整性
            img = Image.open(full_path)
            st.image(img, width=240, caption="街口掃碼支付 100 元")
        elif os.path.exists(QR_FILE):
            st.image(QR_FILE, width=240, caption="街口掃碼支付 100 元")
        else:
            # 這是最後的報錯診斷，如果還是沒有，它會告訴你「兇手」是誰
            st.error(f"❌ 嚴重錯誤：找不到收款圖檔 {QR_FILE}")
            st.write("🔍 目前伺服器目錄下的檔案：", os.listdir("."))
            
    with col2:
        st.write("解鎖費用：NT$ 100")
        last_4 = st.text_input("手機末 4 碼核對", max_chars=4, key="v4")
        if st.button("立即解鎖 (UNLOCK)", use_container_width=True):
            if len(last_4) == 4:
                st.success("算力正在加載...")
            else:
                st.error("末 4 碼不正確")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><p style='text-align: center; color: #222; font-size: 10px;'>AXIOM 1.18 | DESIGNED BY CHIEF</p>", unsafe_allow_html=True)
