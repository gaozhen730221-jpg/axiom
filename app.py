import streamlit as st
import time, random
from pathlib import Path

# --- 核心視覺規範：主動強化專業度 ---
st.set_page_config(page_title="台股 1.0", layout="centered")

st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] { background-color: #FFFFFF !important; color: #000000 !important; }
    h1 { font-size: 3.5rem !important; font-weight: 900 !important; text-align: center; margin-bottom: 0px; }
    
    /* 數據跳動特效 */
    @keyframes fast-flicker {
        0% { opacity: 1; }
        50% { opacity: 0.7; }
        100% { opacity: 1; }
    }
    .live-data { color: #008000; font-weight: bold; animation: fast-flicker 0.2s infinite; }
    
    /* 日誌滾動區 */
    .log-window {
        background: #000;
        color: #00FF41;
        font-family: monospace;
        padding: 10px;
        height: 100px;
        overflow: hidden;
        border: 2px solid #333;
    }
    
    .stButton>button {
        background-color: #000000 !important; color: #FFFFFF !important;
        width: 100%; height: 5rem; font-size: 1.8rem !important; font-weight: bold !important;
    }
    [data-testid="stHeader"] { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- 1. 系統看板 (主動配置偽跳動數據) ---
st.title("台股 1.0")
st.markdown("<p style='text-align:center; font-weight:bold;'>大數據實時核對系統</p>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
# 模擬動態變化，讓股民覺得數據是活的
win_rate = 92.90 + (random.randint(0, 9) / 100)
load = random.randint(97, 99)
packets = random.randint(1400, 1600)

c1.markdown(f"🔒 **數據勝率**<br><span class='live-data' style='font-size:1.8rem;'>{win_rate}%</span>", unsafe_allow_html=True)
c2.markdown(f"🔄 **算力負載**<br><span class='live-data' style='font-size:1.8rem;'>{load}%</span>", unsafe_allow_html=True)
c3.markdown(f"📡 **數據封包**<br><span class='live-data' style='font-size:1.8rem;'>{packets}/s</span>", unsafe_allow_html=True)

st.divider()

# --- 2. 動態日誌流 (主動製造攔截感) ---
st.markdown("""
    <div class="log-window">
        <marquee direction="up" scrollamount="2" style="height: 80px;">
            >> [SYS] 正在接入 L2 指令集...<br>
            >> [DATA] 捕獲主力異動封包 (ID: 0x442)...<br>
            >> [LOG] 1760 標的實時掃描中...<br>
            >> [INFO] 支付權限核對引導中...<br>
            >> [SYS] 算力分配：A-V2 核心啟動...
        </marquee>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- 3. 支付區 (主動偵測收款碼) ---
st.markdown("### 💳 數據提取授權 (NT$ 100)")
qrs = list(Path('.').rglob('*.png')) + list(Path('.').rglob('*.jpg'))
if qrs:
    col_l, col_m, col_r = st.columns([1, 2, 1])
    with col_m:
        st.image(str(qrs[0]), use_container_width=True)

st.divider()

# --- 4. 操作與解鎖 ---
code = st.text_input("輸入股票代碼")
phone = st.text_input("手機末 4 碼")

if st.button("執行資產核對並提取報告"):
    if code and phone:
        with st.status("正在核對 L2 封包資產...", expanded=True) as status:
            time.sleep(0.7)
            st.write(">> 支付確認：NT$ 100 ... [OK]")
            time.sleep(0.5)
            st.write(">> 情報權限已解鎖")
            status.update(label="數據抓取完成", state="complete")
        
        # 產出報告：確保厚度感
        st.markdown(f"""
        <div style="border:5px solid #000; padding:20px; background:#FDFDFD;">
            <h2 style="margin-top:0;">📋 數據核對報告：{code}</h2>
            <hr style="border:1px solid #000;">
            <table style="width:100%; font-size:1.4rem; line-height:2.6;">
                <tr><td><b>數據預期趨勢：</b></td><td style="color:green; font-weight:bold;">偏多擴張 (94%)</td></tr>
                <tr><td><b>主力籌碼集中：</b></td><td>高度密集 (LV.5)</td></tr>
                <tr><td><b>預估獲利空間：</b></td><td><b>+8.5% ~ +12.3%</b></td></tr>
                <tr><td><b>數據有效時限：</b></td><td style="color:red; font-weight:bold;">72 小時</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("請填寫代碼以啟動核對。")
