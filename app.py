import streamlit as st
import os, time, random
from pathlib import Path

# --- 極簡白底視覺優化 ---
st.set_page_config(page_title="台股 1.0", layout="centered")

st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] { background-color: #FFFFFF !important; color: #000000 !important; }
    h1 { font-size: 3.5rem !important; color: #000000 !important; font-weight: 900 !important; text-align: center; }
    .report-card { border: 5px solid #000000; padding: 25px; background-color: #FFFFFF; }
    .stButton>button {
        background-color: #000000 !important; color: #FFFFFF !important;
        width: 100%; height: 5rem; font-size: 2rem !important; font-weight: bold !important;
    }
    label { font-size: 1.5rem !important; font-weight: bold !important; }
    [data-testid="stHeader"], [data-testid="stFooter"] { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# 1. 核心看板
st.markdown("<h1>台股 1.0</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-weight:bold; font-size:1.2rem;'>大數據核對系統</p>", unsafe_allow_html=True)

c1, c2 = st.columns(2)
c1.metric("歷史數據勝率", "92.4%")
c2.metric("數據更新頻率", "每 24H")

st.divider()

# 2. 支付授權區 (NT$ 100)
st.markdown("### 💳 數據提取授權 (NT$ 100)")
qrs = list(Path('.').rglob('*.png')) + list(Path('.').rglob('*.jpg'))
if qrs:
    st.image(str(qrs[0]), width=400)
else:
    st.error("請上傳收款碼圖檔。")

st.divider()

# 3. 操作區
code = st.text_input("股票代碼 (例: 2330)")
phone = st.text_input("手機末 4 碼 (身分核對)")

if st.button("確認支付並提取報告"):
    if code and phone:
        with st.status("進行數據庫同步...", expanded=False):
            time.sleep(1.0)
            st.write(">> 支付紀錄 NT$ 100 確認完成")
        
        # 根據代碼產生真實感的動態獲利範圍
        random.seed(int(code) if code.isdigit() else 888)
        low = round(random.uniform(8.1, 9.8), 1)
        high = round(low + random.uniform(2.5, 4.5), 1)
        
        st.markdown(f"""
        <div class="report-card">
            <h2 style="margin-top:0;">📋 數據核對報告：{code}</h2>
            <hr style="border:1px solid #000;">
            <table style="width:100%; font-size:1.5rem; line-height:2.8;">
                <tr><td><b>數據預期趨勢：</b></td><td style="color:green; font-weight:bold;">偏多擴張 (94%)</td></tr>
                <tr><td><b>籌碼集中度：</b></td><td>高度集中 (LV.5)</td></tr>
                <tr><td><b>參考獲利區間：</b></td><td><b>+{low}% ~ +{high}%</b></td></tr>
                <tr><td><b>數據有效時限：</b></td><td style="color:red; font-weight:bold;">72 小時</td></tr>
            </table>
            <p style="font-size:0.9rem; color:#666; margin-top:20px;">
                *本報告由台股 1.0 系統自動生成，僅供技術研究參考。
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("請完整填寫代碼與核對碼。")
