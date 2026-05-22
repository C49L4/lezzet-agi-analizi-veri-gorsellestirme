import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import time

# 1. Sayfa Ayarları
st.set_page_config(page_title="Lezzet Analitik Portalı", layout="wide", page_icon="📈")

# 2. CSS Tasarımı
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] { overflow: hidden !important; }
    .main { background-color: #0c0e11 !important; color: #e0e0e0 !important; }
    h1, h2, h3 { color: #00ffcc !important; font-weight: 300 !important; }
    .metric-card { 
        background-color: #161b22; padding: 20px; border-radius: 10px; 
        border: 1px solid #30363d; margin-bottom: 15px;
    }
    .stDataFrame { border: 1px solid #30363d !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("👨‍🍳 Lezzet Analitik Portalı")
st.markdown("---")

if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame({'Uyum': [95.0]})

col_grafik, col_panel = st.columns([2.5, 1])

# Grafik Alanı
with col_grafik:
    st.subheader("Anlık Malzeme Ağı Etkileşim Haritası")
    try:
        with open("lezzet_agi_grafigi.html", 'r', encoding='utf-8') as f:
            components.html(f.read(), height=550)
    except:
        st.error("Grafik dosyası oluşturulmamış! 'ag_gorsellestirme.py' çalıştırın.")

# Panel Alanı (Yer tutucular ile titreşimi sıfırladık)
with col_panel:
    st.subheader("Canlı Performans")
    
    # Yer tutucular (Placeholders)
    metrik_ph = st.empty()
    grafik_ph = st.empty()
    tablo_ph = st.empty()

    # Veri güncelleme mantığı
    new_val = st.session_state.data.iloc[-1, 0] + np.random.randn() * 0.5
    st.session_state.data = pd.concat([st.session_state.data, pd.DataFrame({'Uyum': [new_val]})], ignore_index=True).tail(20)
    
    # Yer tutucuları doldur
    with metrik_ph.container():
        st.markdown(f"""
            <div class="metric-card">
                <div style="color: #8b949e; font-size: 0.8rem; text-transform: uppercase;">Güncel Uyum Skoru</div>
                <div style="color: #ffffff; font-size: 1.8rem; font-weight: 700; margin-top:5px;">%{new_val:.2f}</div>
            </div>
        """, unsafe_allow_html=True)
    
    with grafik_ph.container():
        st.line_chart(st.session_state.data, height=150)
    
    with tablo_ph.container():
        st.dataframe(pd.DataFrame({
            'Malzeme': ['Süt', 'Şeker', 'Soğan'],
            'Durum': ['Optimal', 'Düşük', 'Yüksek']
        }), use_container_width=True, hide_index=True)

# Stabil döngü
time.sleep(1)
st.rerun()