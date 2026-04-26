import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# --- AXIOM 1.18 核心配置：Tesla & X 聯名風格 ---
ST_NAME = "AXIOM 1.18"
ST_TAGLINE = "算力獵殺模式：今日最強三箭"
VERSION = "1.18.0 (進擊版)"

st.set_page_config(page_title=ST_NAME, layout="centered")

# --- Tesla 極致黑美學 CSS ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: #0e1111; color: #ffffff; }}
    .tesla-card {{ 
        border: 1px solid #333; padding: 25px; border-radius: 4px; 
        background: #161b22; text-align: center; margin-bottom: 20px;
    }}
    .hunt-box {{ 
        background: linear-gradient(90deg, #1e252e, #0e1111); 
        border-left: 5px solid #00ff41; padding: 18px; margin: 12px 0;
        font-family: 'Courier New', monospace; font-size: 1.1em;
        text-align: left;
    }}
    .unlock-btn {{ 
        background-color: #ffffff !important; color: #000000 !important; 
        border-radius: 0px !important; font-weight: bold; width: 100%; 
        border: none; height: 55px; margin-top: 20px;
    }}
    .stTextInput>div>div>input {{ 
        background-color: #161b22; color: white; border: 1px solid #333; 
        border-radius: 0px; height: 50px;
    }}
    hr {{ border: 0.5px solid #333; }}
    </style>
""", unsafe_allow_html=True)

# --- 第一戰區：主動獵殺 (針對貪婪) ---
st.markdown(f"<h1 style='text-align: center; font-weight: 300; letter-spacing: 5px;'>{ST_NAME}</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #888; font-size: 14px;'>{ST_TAGLINE}</p>", unsafe_allow_html=True)

with st.container():
    st.markdown("""
    <div class='tesla-card'>
        <p style='color: #00ff41; font-size: 12px; letter-spacing: 2px;'>● AXIOM REAL-TIME CLOUD</p>
        <div class='hunt-box'>🎯 標的 A：23** <span style='float: right; color: #00ff41;'>勝率預測 92%</span></div>
        <div class='hunt-box'>🎯 標的 B：62** <span style='float: right; color: #00ff41;'>多頭動能 89%</span></div>
        <div class='hunt-box'>🎯 標的 C：30** <span style='float: right; color: #ff4141;'>風險預警 94%</span></div>
        <p style='font-size: 12px; color: #555; margin-top: 15px;'>付費 100 元解鎖：完整代碼 + 未來 48H 算力波動區間</p>
    </div>
    """, unsafe_allow_html=True)

# --- 第二戰區：精準診斷 (針對恐懼) ---
st.markdown("<p style='text-align: center; color: #444;'>— 或診斷您的持股 —</p>", unsafe_allow_html=True)
stock_input = st.text_input("", placeholder="輸入台股代碼 (如: 2330)")

if stock_input:
    # 模擬 1.18 深度診斷厚度
    st.markdown("### 🔍 深度算力報告")
    c1, c2, c3 = st.columns(3)
    c1.metric("過去 (信任)", "82%", "歷史勝率")
    c2.metric("現在 (決策)", "待支付", "解鎖燈號")
    c3.metric("未來 (趨勢)", "待支付", "預測路徑")

    # --- 支付驗證區：黑盒鎖定 ---
    st.markdown("---")
    st.markdown("<div style='background-color: #161b22; padding: 30px; border: 1px solid #333;'>", unsafe_allow_html=True)
    st.write("💳 **解鎖 1.18 完整權限**")
    st.write("單次授權：NT$ 100 | 手機末 4 碼快速對帳")
    
    pay_col1, pay_col2 = st.columns([1, 1.2])
    with pay_col1:
        # 此處放置您的街口 QR Code 連結
        st.image("https://upload.wikimedia.org/wikipedia/commons/d/d0/QR_code_for_mobile_English_Wikipedia.svg", width=160, caption="掃碼支付 100 元")
    with pay_col2:
        phone_last_4 = st.text_input("手機末 4 碼驗證", max_chars=4, key="phone")
        if st.button("立即解鎖算力 (UNLOCK)", key="action"):
            if len(phone_last_4) == 4:
                st.info("驗證中... 算力通道正在開啟...")
                # 成功後顯示完整燈號與預測
            else:
                st.warning("請輸入正確的手機末 4 碼")
    st.markdown("</div>", unsafe_allow_html=True)

# --- 頁尾：品牌標誌 ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"""
    <hr>
    <p style='text-align: center; color: #333; font-size: 11px; letter-spacing: 1px;'>
        {ST_NAME} VERSION {VERSION} <br>
        POWERED BY AXIOM DATA CENTER. DESIGNED BY THE CHIEF.
    </p>
""", unsafe_allow_html=True)
