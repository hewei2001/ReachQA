import matplotlib.pyplot as plt
import networkx as nx

# Define community hubs
hubs = [
    "Community Center", "Central Library", "Main Park", 
    "Sports Complex", "Art Gallery", "Science Museum", 
    "Farmers Market", "Aquatic Center"
]

# Define connections between hubs (shared patronage or events)
connections = [
    ("Community Center", "Central Library"),
    ("Community Center", "Main Park"),
    ("Main Park", "Sports Complex"),
    ("Central Library", "Art Gallery"),
    ("Art Gallery", "Science Museum"),
    ("Science Museum", "Farmers Market"),
    ("Farmers Market", "Aquatic Center"),
    ("Aquatic Center", "Community Center"),
    ("Sports Complex", "Aquatic Center"),
    ("Main Park", "Art Gallery")
]

# Create undirected graph
G = nx.Graph()
G.add_nodes_from(hubs)
G.add_edges_from(connections)

# Define positions for nodes using spring layout
pos = nx.spring_layout(G, seed=42)

# Plot setup
fig, axs = plt.subplots(1, 2, figsize=(15, 7))

# Subplot 1: Network Graph
node_colors = ['#AEDFF7', '#90EE90', '#FFB6C1', '#FFD700', '#E6E6FA', '#FFDAB9', '#B0C4DE', '#FFC0CB']
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color=node_colors, edgecolors='black', ax=axs[0])
nx.draw_networkx_edges(G, pos, edge_color='grey', width=2, ax=axs[0])
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', ax=axs[0])
axs[0].set_title("Interconnected Community Hubs\nin New Urbania", fontsize=14, fontweight='bold')
axs[0].axis('off')

# Constructing new data for the bar chart
events_data = {
    "Community Center": 120,
    "Central Library": 85,
    "Main Park": 150,
    "Sports Complex": 95,
    "Art Gallery": 60,
    "Science Museum": 70,
    "Farmers Market": 110,
    "Aquatic Center": 100
}

# Subplot 2: Bar Chart of Events
hubs_list = list(events_data.keys())
events_count = list(events_data.values())
bar_colors = node_colors

axs[1].barh(hubs_list, events_count, color=bar_colors, edgecolor='black')
axs[1].set_title("Annual Events Hosted\nby Each Hub", fontsize=14, fontweight='bold')
axs[1].set_xlabel("Number of Events")
axs[1].set_ylabel("Hubs")

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()