import streamlit as st
import time
from pathlib import Path

# --- ① 決策引擎 ---
def decision_engine(code):
    signals = {
        "2330": ("偏多", "外資持續流入 + 權值結構穩定支撐", "建議分批布局"),
        "2317": ("觀望", "內部籌碼分歧明顯，多空勢力拉鋸", "建議等待確認"),
        "2454": ("偏多", "短期技術量能放大，突破關鍵壓力", "可小量試單")
    }
    return signals.get(code, ("觀望", "數據不足以生成高勝率決策", "建議暫不操作"))

# --- ② 樣式設定 ---
st.set_page_config(page_title="台股 1.25", layout="centered")
st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] { background-color: #FFFFFF !important; color: #000000 !important; }
    h1 { font-size: 4rem !important; font-weight: 950 !important; text-align: center; }
    .stButton>button {
        background-color: #000000 !important; color: #FFFFFF !important;
        width: 100%; height: 5.5rem; font-size: 2rem !important; font-weight: 900 !important;
    }
    .penalty-box { 
        border: 5px solid #FF0000; padding: 25px; text-align: center; 
        background: #FFF5F5; color: #FF0000; font-weight: 900; 
        border-radius: 15px; margin: 20px 0;
    }
    [data-testid="stHeader"], [data-testid="stFooter"] { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- ③ 介面展示 ---
st.title("台股 1.25")
st.markdown("<p style='text-align:center; font-weight:bold;'>1.25 門禁識別系統：VIP 快速通道已開啟</p>", unsafe_allow_html=True)

st.divider()

# 支付入口
st.markdown("### 💳 深度數據提取授權 (NT$ 99 限時特價)")
qrs = list(Path('.').rglob('*.png')) + list(Path('.').rglob('*.jpg'))
if qrs:
    col_l, col_m, col_r = st.columns([1, 2, 1])
    with col_m:
        st.image(str(qrs[-1]), use_container_width=True) 

st.divider()

# 輸入區
code = st.text_input("輸入股票代碼", placeholder="例如: 2330")
phone = st.text_input("核對碼 (手機末 4 碼)", placeholder="未支付請留空")

# --- ④ 核心控制邏輯：VIP vs 罰站 ---
if st.button("執行 1.25 引擎深度資產核對"):
    if not code:
        st.error("請輸入股票代碼")
    else:
        main_container = st.empty()
        
        # 判斷是否為 VIP (是否有輸入手機後四碼)
        if phone.strip():
            # ✅ VIP 模式：秒出結果
            with st.status("正在快速核對支付憑證...") as status:
                time.sleep(0.8)
                status.update(label="核對成功！VIP 通道已開啟", state="complete")
        else:
            # 🚨 罰站模式：強制等待 180 秒
            for i in range(180, -1, -1):
                with main_container.container():
                    st.markdown(f"""
                    <div class="penalty-box">
                        <span style="font-size: 1.6rem;">⚠️ 未偵測到支付憑證（手機後四碼）</span><br>
                        <span style="font-size: 3.5rem;">強制等待中：{i} 秒</span><br>
                        <p style="font-size: 1.1rem;">若已支付，請輸入手機後四碼即可跳過等待</p>
                    </div>
                    """, unsafe_allow_html=True)
                    st.progress(int(((180 - i) / 180) * 100))
                time.sleep(1)
            main_container.empty()

        # 最終輸出結果 (無論是秒出還是罰站完，最後都會看到)
        market, reason, action = decision_engine(code)
        st.markdown(f"""
        <div style="border:10px solid #000; padding:30px; margin-top:20px; background:#FFFFFF;">
            <h2 style="margin-top:0; font-size: 2.2rem;">📊 {code} 最終決策</h2>
            <hr style="border:4px solid #000;">
            <p style="font-size:1.6rem;"><b>市場判斷：</b> <span style="color:red; font-weight:bold;">{market}</span></p>
            <p style="font-size:1.6rem;"><b>關鍵原因：</b> {reason}</p>
            <p style="font-size:1.6rem;"><b>操作建議：</b> <mark style="background: yellow; font-weight:bold;">{action}</mark></p>
        </div>
        """, unsafe_allow_html=True)
        st.success("✅ 提取完成")
