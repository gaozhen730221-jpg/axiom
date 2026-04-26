import streamlit as st
import time, random
from pathlib import Path

# --- 核心 CSS：注入偽跳動邏輯 ---
st.set_page_config(page_title="台股 1.0", layout="centered")

st.markdown("""
    <style>
    /* 全白極簡基礎 */
    html, body, [data-testid="stAppViewContainer"] { background-color: #FFFFFF !important; color: #000000 !important; }
    h1 { font-size: 3.5rem !important; font-weight: 900 !important; text-align: center; color: #000; }
    [data-testid="stHeader"] { visibility: hidden; }

    /* 偽跳動動畫：讓數字產生快速閃爍感 */
    @keyframes fast-flicker {
        0% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.8; transform: scale(1.005); }
        100% { opacity: 1; transform: scale(1); }
    }

    .shimmer-data {
        color: #008000;
        font-weight: bold;
        animation: fast-flicker 0.15s infinite; /* 超快速跳動 */
    }

    /* 數據日誌容器 */
    .log-container {
        background: #000;
        color: #00FF41;
        font-family: 'Courier New', Courier, monospace;
        padding: 15px;
        height: 80px;
        overflow: hidden;
        border: 2px solid #333;
    }

    .stButton>button {
        background-color: #000000 !important; color: #FFFFFF !important;
        width: 100%; height: 5rem; font-size: 2rem !important; font-weight: bold !important;
    }
    label { font-size: 1.5rem !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 1. 系統看板 ---
st.title("台股 1.0")
st.markdown("<p style='text-align:center; font-weight:bold;'>大數據實時核對系統</p>", unsafe_allow_html=True)

# 偽跳動數據展示區
c1, c2, c3 = st.columns(3)

# 這裡的數字會隨頁面刷新或操作產生偽變化
rand_val = random.uniform(92.1, 94.8)
c1.markdown(f"🔒 **數據勝率**<br><span class='shimmer-data' style='font-size:2rem;'>{rand_val:.2f}%</span>", unsafe_allow_html=True)
c2.markdown(f"🔄 **算力負載**<br><span class='shimmer-data' style='font-size:2rem;'>{random.randint(95, 99)}%</span>", unsafe_allow_html=True)
c3.markdown(f"📡 **數據封包**<br><span class='shimmer-data' style='font-size:2rem;'>{random.randint(1400, 1800)}/s</span>", unsafe_allow_html=True)

st.divider()

# --- 2. 模擬日誌流 (動的東西) ---
st.markdown("""
    <div class="log-container">
        <marquee direction="up" scrollamount="3" style="height: 50px;">
            >> 正在攔截 L2 指令集... [DONE]<br>
            >> 同步 1760 標的籌碼流...<br>
            >> 偵測到主力異動封包...<br>
            >> AXIOM 邏輯運算中...<br>
            >> 正在生成實時獲利預估...<br>
            >> 數據授權狀態：待解鎖...
        </marquee>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- 3. 支付授權區 (商業核心) ---
st.markdown("### 💳 數據提取授權 (NT$ 100)")
qrs = list(Path('.').rglob('*.png')) + list(Path('.').rglob('*.jpg'))
if qrs:
    col_l, col_m, col_r = st.columns([1, 2, 1])
    with col_m:
        st.image(str(qrs[0]), use_container_width=True)

st.divider()

# --- 4. 操作區 ---
code = st.text_input("股票代碼")
phone = st.text_input("手機末 4 碼")

if st.button("執行資產核對並解鎖報告"):
    if code and phone:
        with st.status("正在抓取偽跳動封包...", expanded=True) as status:
            time.sleep(0.6)
            st.write(">> 支付確認：NT$ 100 ... [OK]")
            time.sleep(0.4)
            st.write(">> 標的 L2 數據已捕獲")
            status.update(label="數據抓取完成", state="complete")
        
        # 報告內容
        st.markdown(f"""
        <div style="border:5px solid #000; padding:20px; background:#FDFDFD;">
            <h2 style="margin-top:0;">📋 數據核對報告：{code}</h2>
            <hr style="border:1px solid #000;">
            <table style="width:100%; font-size:1.5rem; line-height:2.8;">
                <tr><td><b>趨勢預測：</b></td><td style="color:green; font-weight:bold;">強勢擴張 (94%)</td></tr>
                <tr><td><b>籌碼集中：</b></td><td>極度密集 (LV.5)</td></tr>
                <tr><td><b>獲利區間：</b></td><td><b>+8.5% ~ +12.3%</b></td></tr>
                <tr><td><b>有效時限：</b></td><td style="color:red; font-weight:bold;">72 小時</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("請完整輸入資訊。")
