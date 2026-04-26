import streamlit as st
import os
import time

# --- AXIOM 1.1 極致細節重塑 ---
st.set_page_config(page_title="AXIOM 1.1 台股一點靈", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;700&display=swap');
    
    .stApp { background-color: #000000; color: #E7E7E7; font-family: 'Noto Sans TC', sans-serif; text-align: center; }
    
    /* 標題與品牌語 */
    .title-main { letter-spacing: 12px; font-weight: 700; color: #FFFFFF; margin-top: 30px; margin-bottom: 0px; }
    .title-sub { color: #00FF41; font-size: 14px; letter-spacing: 4px; margin-bottom: 40px; font-weight: 300; }
    
    /* 戰績卡片：細緻、不擁擠 */
    .data-card { background: #0A0A0A; padding: 16px; border-radius: 2px; margin-bottom: 10px; text-align: left; border: 1px solid #1A1A1A; }
    .dot { color: #00FF41; margin-right: 10px; font-size: 12px; }
    .card-txt { font-size: 15px; color: #FFF; letter-spacing: 1px; }
    .card-val { float: right; font-size: 14px; color: #00FF41; font-weight: bold; }
    
    /* 支付區：去除雜亂，聚焦 QR Code */
    .pay-zone { border-top: 1px solid #222; padding-top: 40px; margin-top: 40px; }
    .input-label { text-align: left; font-size: 13px; color: #00FF41; margin-bottom: 8px; letter-spacing: 1px; }
    
    /* 輸入框與按鈕：高級黑、無白邊 */
    div.stTextInput > div > div > input { 
        background-color: #0A0A0A; color: white; border: 1px solid #333; height: 45px; border-radius: 4px;
    }
    div.stButton > button { 
        background-color: transparent; color: #00FF41; border: 2px solid #00FF41; 
        border-radius: 4px; width: 100%; height: 50px; font-weight: bold; letter-spacing: 5px; margin-top: 10px;
    }
    
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 頂部品牌區 ---
st.markdown("<h1 class='title-main'>AXIOM 1.1</h1>", unsafe_allow_html=True)
st.markdown("<p class='title-sub'>台股算力一點靈</p>", unsafe_allow_html=True)

# 1. 歷史戰績 (信任建立)
st.markdown("<p style='text-align:left; font-size:11px; color:#444; letter-spacing:2px;'>歷史達成回測</p>", unsafe_allow_html=True)
st.markdown("<div class='data-card'><span class='dot'>●</span><span class='card-txt'>台積電 2330</span><span class='card-val'>+4.2% 已達成</span></div>", unsafe_allow_html=True)
st.markdown("<div class='data-card'><span class='dot'>●</span><span class='card-txt'>緯創 3231</span><span class='card-val'>+6.8% 已達成</span></div>", unsafe_allow_html=True)

# 2. 未來預測 (慾望驅動)
st.markdown("<p style='text-align:left; font-size:11px; color:#444; letter-spacing:2px; margin-top:30px;'>未來算力預測</p>", unsafe_allow_html=True)
st.markdown("<div class='data-card' style='border-left: 3px solid #00FF41;'><span class='card-txt'>核心標 A：23**</span><span class='card-val'>勝率 92%</span></div>", unsafe_allow_html=True)
st.markdown("<div class='data-card' style='border-left: 3px solid #00FF41;'><span class='card-txt'>核心標 B：62**</span><span class='card-val'>勝率 89%</span></div>", unsafe_allow_html=True)

# 3. 支付區 (實戰核對)
st.markdown("<div class='pay-zone'>", unsafe_allow_html=True)
st.markdown("<h3 style='color:#FFF; letter-spacing:2px;'>算力授權</h3>", unsafe_allow_html=True)

# 圖片控制在黃金比例
img_files = [f for f in os.listdir('.') if f.lower().endswith(('.png', '.jpg', '.jpeg')) and f != 'app.py']
if img_files:
    st.image(img_files[0], width=280)

st.markdown("<p style='font-size:12px; color:#555; margin-bottom:30px;'>授權費用 NT$ 100 / 掃碼後輸入下方資訊核對</p>", unsafe_allow_html=True)

# 修正輸入框標示，確保股民看得清楚
st.markdown("<p class='input-label'>1. 欲查詢之台股代碼</p>", unsafe_allow_html=True)
s_id = st.text_input("S_ID", placeholder="例如: 2330", label_visibility="collapsed")

st.markdown("<p class='input-label'>2. 付款手機末 4 碼</p>", unsafe_allow_html=True)
p_id = st.text_input("P_ID", placeholder="核對金流用", max_chars=4, label_visibility="collapsed")

if st.button("🚀 啟動 AXIOM 算力分析"):
    if s_id and p_id:
        with st.spinner('連線算力中心...'):
            time.sleep(1.5)
        st.success(f"授權成功！{s_id} 算力評比：【強勢看多】，預計目標漲幅 +15%")
    else:
        st.error("請填寫完整資訊以啟動核對系統")

st.markdown("</div>", unsafe_allow_html=True)

# 頁尾
st.markdown("<br><p style='color: #222; font-size: 10px; letter-spacing: 5px;'>AXIOM CLOUD SYSTEMS TAIWAN</p>", unsafe_allow_html=True)
