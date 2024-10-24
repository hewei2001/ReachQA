import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Data for the network graph
hubs = ['Earth', 'Mars', 'Europa', 'Vulcan', 'Andoria', 'Betazed', 'Qo\'noS', 'Risa', 'Bajor']
pathways = [
    ('Earth', 'Mars'), ('Earth', 'Europa'), ('Mars', 'Vulcan'), ('Europa', 'Andoria'),
    ('Vulcan', 'Betazed'), ('Betazed', 'Qo\'noS'), ('Qo\'noS', 'Risa'), ('Risa', 'Bajor'),
    ('Bajor', 'Earth'), ('Mars', 'Bajor'), ('Andoria', 'Qo\'noS')
]

# Data for edge labels (communication frequency)
edge_labels = {
    ('Earth', 'Mars'): '5 GHz', ('Earth', 'Europa'): '3 GHz', ('Mars', 'Vulcan'): '4 GHz',
    ('Europa', 'Andoria'): '2 GHz', ('Vulcan', 'Betazed'): '6 GHz', ('Betazed', 'Qo\'noS'): '7 GHz',
    ('Qo\'noS', 'Risa'): '2 GHz', ('Risa', 'Bajor'): '4 GHz', ('Bajor', 'Earth'): '5 GHz',
    ('Mars', 'Bajor'): '3 GHz', ('Andoria', 'Qo\'noS'): '6 GHz'
}

# Data for the new subplot (traffic load as an example metric)
traffic_load = {
    ('Earth', 'Mars'): 50, ('Earth', 'Europa'): 30, ('Mars', 'Vulcan'): 40,
    ('Europa', 'Andoria'): 20, ('Vulcan', 'Betazed'): 60, ('Betazed', 'Qo\'noS'): 70,
    ('Qo\'noS', 'Risa'): 20, ('Risa', 'Bajor'): 40, ('Bajor', 'Earth'): 50,
    ('Mars', 'Bajor'): 30, ('Andoria', 'Qo\'noS'): 60
}

# Create a directed graph
G = nx.DiGraph()
G.add_nodes_from(hubs)
G.add_edges_from(pathways)

# Layout for node positioning
pos = nx.spring_layout(G, seed=42)

# Plot configuration
fig, axs = plt.subplots(1, 2, figsize=(18, 9))
fig.suptitle("Intergalactic Communication Network Analysis", fontsize=20, fontweight='bold')

# Network plot on the first subplot
axs[0].set_title("Communication Pathways\nand Frequencies", fontsize=14, fontweight='bold')
nx.draw_networkx_nodes(G, pos, ax=axs[0], node_size=1000, node_color='skyblue', edgecolors='black', alpha=0.9)
nx.draw_networkx_edges(G, pos, ax=axs[0], edge_color='darkgray', arrows=True, arrowstyle='-|>', arrowsize=15)
nx.draw_networkx_labels(G, pos, ax=axs[0], font_size=10, font_family='sans-serif', font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=8, ax=axs[0])
axs[0].axis('off')

# Traffic load bar chart on the second subplot
axs[1].set_title("Traffic Load on Communication Pathways", fontsize=14, fontweight='bold')
edges, loads = zip(*traffic_load.items())
edge_strs = [f"{src} → {dst}" for src, dst in edges]
y_pos = np.arange(len(edge_strs))

axs[1].barh(y_pos, loads, color='seagreen')
axs[1].set_yticks(y_pos)
axs[1].set_yticklabels(edge_strs, fontsize=9)
axs[1].set_xlabel('Traffic Load (arbitrary units)', fontsize=10)
axs[1].invert_yaxis()  # To display the bars in descending order

# Adjust layout for better visibility
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display the plot
plt.show()