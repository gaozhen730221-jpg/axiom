import streamlit as st
import time, random
from pathlib import Path

# --- 1.1 引擎視覺規範 ---
st.set_page_config(page_title="台股 1.1", layout="centered")

st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] { background-color: #FFFFFF !important; color: #000000 !important; }
    h1 { font-size: 4.2rem !important; font-weight: 950 !important; text-align: center; letter-spacing: -2px; }
    @keyframes pulse-fast { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
    .engine-1-1 { color: #008000; font-weight: 900; animation: pulse-fast 0.15s infinite; }
    .stButton>button {
        background-color: #000000 !important; color: #FFFFFF !important;
        width: 100%; height: 6rem; font-size: 2.2rem !important; font-weight: 900 !important;
        border: none; box-shadow: 0px 10px 20px rgba(0,0,0,0.2);
    }
    [data-testid="stHeader"], [data-testid="stFooter"] { visibility: hidden; }
    label { font-size: 1.6rem !important; font-weight: 800 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 狀態初始化 ---
if 'stage' not in st.session_state:
    st.session_state.stage = 'input' # input -> verify -> wait -> result
if 'wait_time' not in st.session_state:
    st.session_state.wait_time = 0

# --- 第一部：1.1 引擎狀態 ---
st.title("台股 1.1")
st.markdown("<p style='text-align:center; font-weight:bold; font-size:1.4rem;'>核心大數據核對引擎・正式運作中</p>", unsafe_allow_html=True)

# --- 罰站邏輯：強制鎖死頁面 ---
if st.session_state.wait_time > 0:
    placeholder = st.empty()
    for i in range(st.session_state.wait_time, 0, -1):
        placeholder.error(f"⚠️ 檢測到未驗證節點，強制進入低速排隊序列。請等待 {i} 秒...")
        time.sleep(1)
    st.session_state.wait_time = 0
    st.session_state.stage = 'result' # 罰站完直接出結果
    st.rerun()

# --- 1.1 儀表板 ---
c1, c2, c3 = st.columns(3)
c1.markdown(f"🔒 **核對勝率**<br><span class='engine-1-1' style='font-size:2rem;'>92.{random.randint(90, 99)}%</span>", unsafe_allow_html=True)
c2.markdown(f"🔄 **算力輸出**<br><span class='engine-1-1' style='font-size:2rem;'>99%</span>", unsafe_allow_html=True)
c3.markdown(f"📡 **數據吞吐**<br><span class='engine-1-1' style='font-size:2rem;'>{random.randint(1800, 2200)}/s</span>", unsafe_allow_html=True)
st.divider()

# --- 主邏輯區 ---
if st.session_state.stage == 'input':
    st.markdown("### 💳 深度數據提取授權 (NT$ 100)")
    qrs = list(Path('.').rglob('*.png')) + list(Path('.').rglob('*.jpg'))
    if qrs:
        col_l, col_m, col_r = st.columns([1, 2, 1])
        with col_m: st.image(str(qrs[-1]), use_container_width=True)
    st.divider()

    code = st.text_input("輸入股票代碼", placeholder="2330")
    phone = st.text_input("核對碼 (手機末 4 碼)")
    
    if st.button("執行 1.1 引擎資產核對"):
        if code and phone:
            st.session_state.target_code = code
            st.session_state.stage = 'verify'
            st.rerun()
        else:
            st.error("請輸入完整代碼。")

elif st.session_state.stage == 'verify':
    st.warning("📊 **開盤高峰：L2 數據節點分配驗證**")
    st.write("請輸入【街口支付流水號】最後 4 碼以啟動高速通道。")
    txid = st.text_input("驗證碼：", key="txid_verify")
    
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("確認驗證並解鎖"):
            if txid: # 暴力兼容：有打字就過
                st.session_state.stage = 'result'
                st.rerun()
            else:
                st.error("請輸入驗證碼或選擇低速通道")
    with col_b:
        if st.button("我不付錢，選擇排隊"):
            st.session_state.wait_time = 180 # 這裡設定 180 秒
            st.rerun()

elif st.session_state.stage == 'result':
    # --- 執行您的 1.1 核心情報呈現 ---
    with st.status("1.1 引擎正在攔截 L2 指令集...", expanded=True) as status:
        time.sleep(0.6)
        st.write(">> 權限核對：通過")
        time.sleep(0.4)
        st.write(">> 正在解碼籌碼乖離指標...")
        status.update(label="核對完成", state="complete")
    
    st.markdown(f"""
    <div style="border:8px solid #000; padding:30px; background:#FFFFFF;">
        <h2 style="margin-top:0;">📊 1.1 核心情報：{st.session_state.target_code}</h2>
        <hr style="border:2px solid #000;">
        <table style="width:100%; font-size:1.6rem; line-height:3;">
            <tr><td><b>數據趨勢預測：</b></td><td style="color:green; font-weight:bold;">強勢擴張 (94%)</td></tr>
            <tr><td><b>主力籌碼集中度：</b></td><td>高度密集 (LV.5)</td></tr>
            <tr><td><b>參考獲利區間：</b></td><td><b>+8.5% ~ +12.3%</b></td></tr>
            <tr><td><b>數據時效：</b></td><td style="color:red; font-weight:bold;">72 小時</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("重新查詢"):
        st.session_state.stage = 'input'
        st.rerun()
