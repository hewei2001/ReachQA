import matplotlib.pyplot as plt
import networkx as nx

# Define the countries as nodes in the network
countries = ["China", "India", "Sri Lanka", "Japan", "Kenya", 
             "UK", "USA", "Germany", "Pakistan", "Russia"]

# Define trade relationships as edges (connections)
trade_relationships = [
    ("China", "USA"), ("China", "Germany"), ("India", "UK"),
    ("Sri Lanka", "Russia"), ("Kenya", "Pakistan"),
    ("Japan", "USA"), ("China", "India"), ("India", "Russia"),
    ("Sri Lanka", "Germany"), ("Kenya", "UK"), ("China", "Pakistan"),
    ("Japan", "Russia"), ("India", "Germany"), ("Sri Lanka", "USA")
]

# Create a graph object
G = nx.Graph()
G.add_nodes_from(countries)
G.add_edges_from(trade_relationships)

# Related data for the bar chart (hypothetical trade volumes)
trade_volumes = {
    "China": 1500,
    "India": 1200,
    "Sri Lanka": 800,
    "Japan": 1000,
    "Kenya": 500,
    "UK": 1100,
    "USA": 1400,
    "Germany": 1300,
    "Pakistan": 600,
    "Russia": 900
}

# Create the figure and the subplot axes
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 10))

# Plot the network graph on the first subplot
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx_nodes(G, pos, ax=axes[0], node_size=3000, node_color='lightgreen', edgecolors='black')
nx.draw_networkx_edges(G, pos, ax=axes[0], width=1.5, alpha=0.7, edge_color='gray')
nx.draw_networkx_labels(G, pos, ax=axes[0], font_size=12, font_weight='bold')
edge_labels = {edge: 'Trade' for edge in G.edges()}
nx.draw_networkx_edge_labels(G, pos, ax=axes[0], edge_labels=edge_labels, font_color='gray', font_size=9, label_pos=0.3)
axes[0].set_title("Global Tea Trade Networks:\nKey Countries and Trade Relationships", fontsize=16, fontweight='bold')
axes[0].axis('off')

# Plot the bar chart on the second subplot
axes[1].bar(trade_volumes.keys(), trade_volumes.values(), color='skyblue')
axes[1].set_title("Trade Volume by Country (Hypothetical)", fontsize=16, fontweight='bold')
axes[1].set_ylabel('Trade Volume')
axes[1].set_xlabel('Country')
axes[1].tick_params(axis='x', rotation=45)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()