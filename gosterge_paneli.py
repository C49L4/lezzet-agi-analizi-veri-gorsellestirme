import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Lezzet Analitik Portalı", layout="wide")

# CSS: Dashboard'a profesyonel, "Dark-Mode" kurumsal görünüm kazandırıyoruz
st.markdown("""
    <style>
    .stApp { background-color: #0c0e11; }
    h1 { color: #00ffcc !important; text-align: center; }
    .stInfo, .stWarning { background-color: #161b22 !important; border-left: 5px solid #30363d !important; }
    </style>
""", unsafe_allow_html=True)

st.title("👨‍🍳 Sosyal Ağ ve Lezzet Analitik Portalı")

col_g, col_a = st.columns([2, 1])

with col_g:
    st.subheader("İnteraktif Ağ Görselleştirme")
    # Filtreleme menüleri grafiğin üstüne eklendiği için yüksekliği 700px yaptık
    try:
        with open("lezzet_agi_grafigi.html", 'r', encoding='utf-8') as f:
            components.html(f.read(), height=700, scrolling=True)
    except FileNotFoundError:
        st.error("HTML dosyası bulunamadı! 'python ag_gorsellestirme.py' çalıştırın.")

with col_a:
    st.subheader("📊 Network Intelligence")
    
    # 1. Community Narrative (Akademik Dil ile Geliştirildi)
    with st.expander("🔍 Topluluk Analizi (Community Detection)", expanded=True):
        st.markdown("""
        **Louvain Modularity** algoritması ile ağ iki ana kümeye (partition) ayrılmıştır[cite: 52]:
        * **Cluster A (Tatlılar Grubu):** Merkezcil düğümler (Çikolata, Şeker, Vanilya). Yüksek bağlantı yoğunluğuna sahip, ağın "hub" yapısını oluşturan ana kümedir[cite: 53].
        * **Cluster B (Sebze Grubu):** Daha dışsal bir yapıda konumlanan, spesifik lezzet fonksiyonlarına sahip küme (Soğan, Sarımsak)[cite: 53].
        """)
    
    # 2. Köprü Analizi (Teknik Derinlik)
    with st.expander("🌉 Köprü (Bridge) Analizi", expanded=True):
        st.markdown("""
        **Betweenness Centrality** metriği ile ağın geçit bekçileri tanımlanmıştır[cite: 57]:
        * **Kritik Düğüm:** *Tereyağı*.
        * **Stratejik Önemi:** İki farklı küme (Tatlı ve Sebze) arasındaki tek doğrudan bilgi/lezzet transfer noktasıdır[cite: 68].
        * **Risk Analizi:** Ağdan kaldırılması durumunda *graph fragmentation* (ağ parçalanması) yaşanacak ve iki küme arasındaki iletişim tamamen izole olacaktır[cite: 69].
        """)

    # 3. Visualization Critique (Hocanın rapor için istediği eleştiri kısmı)
    with st.expander("🛠 Görselleştirme Tasarım Notları"):
        st.markdown("""
        * **Layout Justification:** `Force-Directed (Barnes-Hut)` algoritması, küme ayrışmasını ve köprü düğümlerin (bridge nodes) belirginleşmesini sağlamıştır[cite: 63].
        * **Visual Hierarchy:** Düğüm boyutları `Betweenness Centrality` ile ölçeklenerek, ağdaki "Key Actors" (kilit oyuncular) görsel olarak ön plana çıkarılmıştır[cite: 55, 61].
        """)