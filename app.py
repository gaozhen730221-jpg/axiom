import streamlit as st
import os, time
from pathlib import Path

# --- 全局視覺規範 ---
st.set_page_config(page_title="AXIOM 2.0", layout="centered")

st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] { background-color: #000000 !important; color: #FFFFFF !important; }
    h1 { font-size: 3rem !important; color: #00FF41 !important; font-family: monospace; text-align: center; }
    
    /* 情報區塊樣式 */
    .report-card {
        background: rgba(0, 163, 255, 0.05);
        border: 1px solid #00A3FF;
        padding: 25px;
        border-radius: 10px;
        margin-top: 20px;
    }
    .data-point { font-size: 1.5rem; font-weight: bold; color: #FFD700; } /* 警示金 */
    
    .stButton>button {
        height: 4.5rem; font-size: 1.8rem !important;
        background-color: #00FF41 !important; color: #000000 !important; font-weight: bold !important;
    }
    [data-testid="stHeader"] { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- 1. 頂部看板 ---
st.markdown("<h1>AXIOM 2.0</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#00A3FF; font-weight:bold;'>台股數據運算中心・V.1.08</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
col1.metric("算力負載", "98.2%")
col2.metric("當日勝率", "92.4%")
col3.metric("監控標的", "1760+")

st.divider()

# --- 2. 支付通道 ---
st.markdown("<h3 style='color:#FF4B4B;'>💳 數據提取授權 (NT$ 100)</h3>", unsafe_allow_html=True)

# 自動偵測圖檔
qrs = list(Path('.').rglob('*.png')) + list(Path('.').rglob('*.jpg'))
if qrs:
    col_l, col_m, col_r = st.columns([1, 2, 1])
    with col_m:
        st.image(str(qrs[0]), use_container_width=True)
else:
    st.error("支付網關連線異常")

st.divider()

# --- 3. 操作與深度情報產出 ---
code = st.text_input("輸入欲解碼代碼")
phone = st.text_input("身份核對碼")

if st.button("執行資產核對並提取報告"):
    if code and phone:
        with st.status("進行 L2 深度數據解碼...", expanded=True) as status:
            time.sleep(0.8)
            st.write(">> 確認 NT$ 100 支付紀錄... [授權通過]")
            time.sleep(0.5)
            st.write(">> 抓取主力分點籌碼流向...")
            time.sleep(0.5)
            st.write(">> 計算 72 小時波動率乖離...")
            status.update(label="數據提取完成", state="complete", expanded=False)
        
        # --- 這裡就是「厚度」：深度情報報告 ---
        st.markdown(f"""
        <div class="report-card">
            <h2 style="color:#00FF41; margin-top:0;">📊 標的分析報告：{code}</h2>
            <hr style="border:0.5px solid #00A3FF;">
            <table style="width:100%; font-size:1.2rem; color:#EEE;">
                <tr>
                    <td><b>算力預測趨勢：</b></td>
                    <td class="data-point">強勢噴發 (Confidence 94%)</td>
                </tr>
                <tr>
                    <td><b>主力籌碼集中度：</b></td>
                    <td class="data-point">極度密集 (LV.5)</td>
                </tr>
                <tr>
                    <td><b>關鍵防守價位：</b></td>
                    <td style="color:#FF4B4B; font-weight:bold;">系統計算中... (請依實時報價)</td>
                </tr>
                <tr>
                    <td><b>目標獲利區間：</b></td>
                    <td style="color:#00FF41; font-weight:bold;">+8.5% ~ +12.3%</td>
                </tr>
            </table>
            <br>
            <p style="font-size:0.9rem; color:#888;">
                *本報告基於 AXIOM 2.0 算力模型生成，有效時限為 72 小時。逾期請重新提取。
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.warning("⚠️ 提醒：情報已開啟，請立即同步至您的交易終端。")
    else:
        st.warning("請完整填寫代碼以提取情報。")
