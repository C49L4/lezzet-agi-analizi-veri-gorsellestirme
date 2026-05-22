from pyvis.network import Network
import networkx as nx

# 1. Veri setini tanımla
edges = [
    ("Çikolata", "Süt", 5), ("Çikolata", "Şeker", 4), ("Çikolata", "Vanilya", 3),
    ("Süt", "Şeker", 4), ("Süt", "Tereyağı", 3), ("Süt", "Vanilya", 2),
    ("Soğan", "Sarımsak", 5), ("Sarımsak", "Tereyağı", 4)
]

G = nx.Graph()
for source, target, weight in edges:
    G.add_edge(source, target, weight=weight)

# 2. Network ayarları
net = Network(height="550px", width="100%", bgcolor="#0c0e11", font_color="white")

# 3. DİNAMİK BOYUTLANDIRMA MANTIĞI
# Derece (bağlantı sayısı) hesapla
degrees = dict(G.degree())

# Her düğümü manuel ekle ki boyutlarını kontrol edebilelim
for node in G.nodes():
    # Bağlantı sayısı ne kadar fazlaysa o kadar büyük (min 20, max 50)
    size = 20 + (degrees[node] * 5) 
    # Renkleri gruplandır (Örn: Süt/Çikolata vs. Soğan/Sarımsak)
    color = "#FF5733" if node in ["Çikolata", "Süt", "Şeker", "Vanilya", "Tereyağı"] else "#33FF57"
    
    net.add_node(node, label=node, size=size, color=color, font={"color": "white", "size": 16})

# Kenarları ekle
for s, t, w in edges:
    net.add_edge(s, t, width=w)

# 4. Fizik ve Görünüm Ayarları
net.set_options("""
var options = {
  "nodes": { "borderWidth": 2, "shadow": true },
  "edges": { "color": { "color": "#4a5568" }, "smooth": true },
  "physics": {
    "barnesHut": { "gravitationalConstant": -3000, "springLength": 150 },
    "stabilization": { "enabled": true, "iterations": 100 }
  }
}
""")

net.save_graph("lezzet_agi_grafigi.html")
print("Dinamik boyutlu grafik başarıyla oluşturuldu!")