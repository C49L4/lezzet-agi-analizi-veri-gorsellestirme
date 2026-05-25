from pyvis.network import Network
import networkx as nx
import community.community_louvain as community_louvain

# Veri seti
edges = [("Çikolata", "Süt", 5), ("Çikolata", "Şeker", 4), ("Çikolata", "Vanilya", 3),
         ("Süt", "Şeker", 4), ("Süt", "Tereyağı", 4), ("Süt", "Vanilya", 2),
         ("Soğan", "Sarımsak", 5), ("Sarımsak", "Tereyağı", 4)]

G = nx.Graph()
for s, t, w in edges:
    G.add_edge(s, t, weight=w)

partition = community_louvain.best_partition(G)
betweenness = nx.betweenness_centrality(G)

# filter_menu ve select_menu burada aktif
net = Network(height="600px", width="100%", bgcolor="#0c0e11", font_color="white", 
              cdn_resources='remote', filter_menu=True, select_menu=True)

colors = ["#FF5733", "#33FF57", "#3357FF"]

for node in G.nodes():
    size = 25 + (betweenness[node] * 200)
    color = colors[partition[node] % len(colors)]
    group_name = "Tatlılar Grubu" if partition[node] == 0 else "Sebze Grubu"
    net.add_node(node, label=node, title=f"Grup: {group_name}<br>Centrality: {betweenness[node]:.2f}", 
                 size=size, color=color, borderWidth=2)

for s, t, w in edges:
    is_bridge = (s == "Tereyağı" or t == "Tereyağı") and (s == "Süt" or t == "Süt")
    net.add_edge(s, t, width=w, color="#FFFFFF" if is_bridge else "#4a5568")

# Sabit fizik ayarları - hocanın "jump" (zıplama) istememesini engeller
net.set_options("""
var options = {
  "physics": {
    "barnesHut": { "gravitationalConstant": -5000, "springLength": 150 },
    "minVelocity": 0.75,
    "stabilization": { "enabled": true, "iterations": 200 }
  },
  "interaction": { "hover": true, "navigationButtons": true, "keyboard": true }
}
""")

net.save_graph("lezzet_agi_grafigi.html")
print("Grafik filtreleme menüsüyle güncellendi.")