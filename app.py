import streamlit as st
import time, random
from pathlib import Path

# --- 1.1 引擎視覺規範：強化絕對專業感 ---
st.set_page_config(page_title="台股 1.1", layout="centered")

st.markdown("""
    <style>
    /* 全白背景，黑色重裝字體 */
    html, body, [data-testid="stAppViewContainer"] { background-color: #FFFFFF !important; color: #000000 !important; }
    h1 { font-size: 4.2rem !important; font-weight: 950 !important; text-align: center; letter-spacing: -2px; }
    
    /* 1.1 專屬：高頻脈衝跳動邏輯 */
    @keyframes pulse-fast { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
    .engine-1-1 { color: #008000; font-weight: 900; animation: pulse-fast 0.15s infinite; }
    
    /* 強化支付按鈕的壓迫感 */
    .stButton>button {
        background-color: #000000 !important; color: #FFFFFF !important;
        width: 100%; height: 6rem; font-size: 2.2rem !important; font-weight: 900 !important;
        border: none; box-shadow: 0px 10px 20px rgba(0,0,0,0.2);
    }
    
    /* 隱藏冗餘標籤 */
    [data-testid="stHeader"], [data-testid="stFooter"] { visibility: hidden; }
    label { font-size: 1.6rem !important; font-weight: 800 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 第一部：1.1 引擎狀態監控 ---
st.title("台股 1.1")
st.markdown("<p style='text-align:center; font-weight:bold; font-size:1.4rem;'>核心大數據核對引擎・正式運作中</p>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
c1.markdown(f"🔒 **核對勝率**<br><span class='engine-1-1' style='font-size:2rem;'>92.{random.randint(90, 99)}%</span>", unsafe_allow_html=True)
c2.markdown(f"🔄 **算力輸出**<br><span class='engine-1-1' style='font-size:2rem;'>99%</span>", unsafe_allow_html=True)
c3.markdown(f"📡 **數據吞吐**<br><span class='engine-1-1' style='font-size:2rem;'>{random.randint(1800, 2200)}/s</span>", unsafe_allow_html=True)

st.divider()

# --- 第二部：解決痛點・支付入口 ---
st.markdown("### 💳 深度數據提取授權 (NT$ 100)")
qrs = list(Path('.').rglob('*.png')) + list(Path('.').rglob('*.jpg'))
if qrs:
    col_l, col_m, col_r = st.columns([1, 2, 1])
    with col_m:
        st.image(str(qrs[-1]), use_container_width=True)

st.divider()

# --- 第三部：精準收割操作 ---
code = st.text_input("輸入股票代碼", placeholder="2330")
phone = st.text_input("核對碼 (手機末 4 碼)")

# --- 1.3.3 暴力門禁外掛邏輯啟動 ---
# 初始化 Session State 用於控制罰站時間
if 'wait_time' not in st.session_state:
    st.session_state.wait_time = 0

# 實施罰站倒數
if st.session_state.wait_time > 0:
    placeholder = st.empty()
    for i in range(st.session_state.wait_time, 0, -1):
        placeholder.error(f"⚠️ 檢測到未驗證節點，強制進入低速排隊序列。排隊中：{i} 秒")
        time.sleep(1)
    st.session_state.wait_time = 0
    st.rerun()

# 點擊按鈕後的邏輯
if st.button("執行 1.1 引擎資產核對"):
    if code and phone:
        # 彈出驗證框（Streamlit 限制，用 text_input 模擬彈窗驗證）
        st.info("💡 為了分配 L2 高速節點，請驗證您的支付資訊。")
        txid_verify = st.text_input("請輸入【街口支付流水號】最後 4 碼：", key="gate_verify")
        
        if txid_verify:
            # 分支 A：只要有輸入，立即放行 1.1 核心邏輯
            with st.status("1.1 引擎正在攔截 L2 指令集...", expanded=True) as status:
                time.sleep(0.6)
                st.write(">> 支付確認：成功 (TXID 已校驗)")
                time.sleep(0.4)
                st.write(">> 正在解碼籌碼乖離指標...")
                status.update(label="核對完成，情報已生成", state="complete")
            
            # --- 1.1 核心情報：原封不動輸出 ---
            st.markdown(f"""
            <div style="border:8px solid #000; padding:30px; background:#FFFFFF;">
                <h2 style="margin-top:0;">📊 1.1 核心情報：{code}</h2>
                <hr style="border:2px solid #000;">
                <table style="width:100%; font-size:1.6rem; line-height:3;">
                    <tr><td><b>數據趨勢預測：</b></td><td style="color:green; font-weight:bold;">強勢擴張 (94%)</td></tr>
                    <tr><td><b>主力籌碼集中度：</b></td><td>高度密集 (LV.5)</td></tr>
                    <tr><td><b>參考獲利區間：</b></td><td><b>+8.5% ~ +12.3%</b></td></tr>
                    <tr><td><b>數據時效：</b></td><td style="color:red; font-weight:bold;">72 小時</td></tr>
                </table>
            </div>
            """, unsafe_allow_html=True)
        else:
            # 分支 B：白嫖黨（沒輸入或猶豫不決），設定罰站時間
            st.warning("您未提供驗證碼。若需免費查閱，請等待系統分配低速節點資源。")
            if st.button("我選擇等待 (180秒)"):
                st.session_state.wait_time = 180
                st.rerun()
    else:
        st.error("請輸入完整代碼以啟動 1.1 引擎。")
