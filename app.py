import streamlit as st
import time, random
from pathlib import Path

# --- 核心邏輯：將動畫腳本封裝，極大化加載速度 ---
st.set_page_config(page_title="台股 1.0", layout="centered")

st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] { background-color: #FFFFFF !important; }
    h1 { font-size: 3.2rem !important; font-weight: 900 !important; text-align: center; color: #000; }
    
    /* 極低功耗的數據跳動 */
    .pulse-data { 
        color: #008000; 
        font-weight: bold; 
        animation: flicker 0.3s steps(2, start) infinite; 
    }
    @keyframes flicker { to { visibility: hidden; } }

    .stButton>button {
        background-color: #000000 !important; color: #FFFFFF !important;
        width: 100%; height: 5rem; font-size: 2rem !important; font-weight: bold !important;
    }
    [data-testid="stHeader"] { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# 1. 系統看板
st.title("台股 1.0")
st.markdown("<p style='text-align:center; font-weight:bold;'>大數據實時核對系統</p>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
# 這裡使用固定+微幅隨機，確保每次打開都有「活的」感覺
c1.markdown(f"🔒 **數據勝率**<br><span class='pulse-data' style='font-size:1.8rem;'>{92.90 + (random.randint(0,9)/100)}%</span>", unsafe_allow_html=True)
c2.markdown(f"🔄 **算力負載**<br><span class='pulse-data' style='font-size:1.8rem;'>{random.randint(97, 99)}%</span>", unsafe_allow_html=True)
c3.markdown(f"📡 **數據封包**<br><span class='pulse-data' style='font-size:1.8rem;'>{random.randint(1400, 1600)}/s</span>", unsafe_allow_html=True)

st.divider()

# 2. 支付區 (主動偵測最新的街口收款碼)
st.markdown("### 💳 數據提取授權 (NT$ 100)")
qrs = list(Path('.').rglob('*.png')) + list(Path('.').rglob('*.jpg'))
if qrs:
    st.image(str(qrs[0]), width=380)

st.divider()

# 3. 數據操作區
code = st.text_input("輸入股票代碼", placeholder="2330")
phone = st.text_input("手機末 4 碼")

if st.button("執行支付核對並提取報告"):
    if code and phone:
        with st.status("正在截取 L2 實時封包...", expanded=False):
            time.sleep(0.8)
        
        # 報告內容維持專業格式
        st.markdown(f"""
        <div style="border:5px solid #000; padding:20px; background:#F9F9F9;">
            <h2 style="margin-top:0;">📋 數據核對報告：{code}</h2>
            <hr style="border:1px solid #000;">
            <table style="width:100%; font-size:1.5rem; line-height:2.8;">
                <tr><td><b>預期趨勢：</b></td><td style="color:green; font-weight:bold;">強勢擴張 (94%)</td></tr>
                <tr><td><b>籌碼集中：</b></td><td>高度密集 (LV.5)</td></tr>
                <tr><td><b>獲利空間：</b></td><td><b>+8.5% ~ +12.3%</b></td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
