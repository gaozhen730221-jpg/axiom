import streamlit as st

# --- AXIOM 1.18 極致美學設定 ---
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
    }
    /* 支付區塊強化 */
    .pay-zone {
        border: 2px solid #00ff41; 
        background-color: #1a1d23; 
        padding: 30px; 
        border-radius: 8px;
        text-align: center;
        box-shadow: 0 0 20px rgba(0, 255, 65, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

# --- 標題 ---
st.markdown("<h1 style='text-align: center; font-weight: 300; letter-spacing: 5px;'>AXIOM 1.18</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>算力獵殺模式：今日最強三箭</p>", unsafe_allow_html=True)

# --- 第一戰區：最強三箭 (照截圖樣式) ---
with st.container():
    st.markdown("""
    <div class='tesla-card'>
        <p style='color: #00ff41; font-size: 12px; letter-spacing: 2px; text-align: center;'>● AXIOM REAL-TIME CLOUD</p>
        <div class='hunt-box'>🎯 標的 A：23** <span style='float: right; color: #00ff41;'>勝率預測 92%</span></div>
        <div class='hunt-box'>🎯 標的 B：62** <span style='float: right; color: #00ff41;'>多頭動能 89%</span></div>
        <div class='hunt-box'>🎯 標的 C：30** <span style='float: right; color: #ff4141;'>風險預警 94%</span></div>
        <p style='font-size: 12px; color: #555; text-align: center; margin-top: 10px;'>付費 100 元解鎖：完整代碼 + 未來 48H 算力波動區間</p>
    </div>
    """, unsafe_allow_html=True)

# --- 第二戰區：持股診斷 ---
st.markdown("<p style='text-align: center; color: #444;'>— 或診斷您的持股 —</p>", unsafe_allow_html=True)
stock_input = st.text_input("", placeholder="輸入台股代碼 (如: 2330)", key="stock_id")

# --- 第三戰區：QR Code 核心入金區 (只有輸入代碼後才會顯示) ---
if stock_input:
    st.markdown("---")
    st.markdown("<div class='pay-zone'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #00ff41;'>💳 算力通道授權</h3>", unsafe_allow_html=True)
    st.write("請掃碼支付 **NT$ 100** 以解鎖 1.18 深度算力報告")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        # 這裡會讀取您的圖檔
        try:
            st.image("pay_qr.png", width=220, caption="長按 QR Code 進入街口支付")
        except:
            st.error("請確認 pay_qr.png 已放在資料夾中")
            
    with col2:
        st.write("完成支付後，請輸入")
        last_4 = st.text_input("手機末 4 碼核對", max_chars=4, key="verify_4")
        if st.button("立即移除迷霧 (UNLOCK)", use_container_width=True):
            if len(last_4) == 4:
                st.success("算力正在加載... 請稍候")
            else:
                st.warning("請輸入正確末 4 碼")
    st.markdown("</div>", unsafe_allow_html=True)

# --- 頁尾 ---
st.markdown("<br><p style='text-align: center; color: #222; font-size: 11px;'>AXIOM 1.18 BLCK EDITION | DESIGNED IN TAIPEI</p>", unsafe_allow_html=True)
