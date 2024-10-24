import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Define park features as nodes
features = [
    "Playground", "Picnic Area", "Fountain", "Walking Path", 
    "Dog Park", "Garden", "Amphitheater", "Restrooms", "Food Stall"
]

# Define connections between features as edges
connections = [
    ("Playground", "Picnic Area"),
    ("Picnic Area", "Garden"),
    ("Garden", "Fountain"),
    ("Fountain", "Walking Path"),
    ("Walking Path", "Amphitheater"),
    ("Amphitheater", "Restrooms"),
    ("Restrooms", "Food Stall"),
    ("Food Stall", "Dog Park"),
    ("Dog Park", "Playground")
]

# Create an undirected graph
G = nx.Graph()
G.add_nodes_from(features)
G.add_edges_from(connections)

# Position nodes using spring layout
pos = nx.spring_layout(G, seed=42)

# Define node colors and sizes
node_colors = ['#9acd32', '#ff6347', '#1e90ff', '#ffeb3b', '#f4a460', '#adff2f', '#dda0dd', '#8b4513', '#ff69b4']
node_sizes = [1200, 1000, 800, 1100, 900, 950, 1050, 850, 800]

# Create a matrix representing hypothetical visitor interaction over a week
visitor_interactions = np.array([
    [50, 60, 70, 60, 80, 90, 100],  # Playground
    [80, 85, 90, 85, 95, 80, 70],   # Picnic Area
    [30, 35, 40, 45, 50, 55, 60],   # Fountain
    [90, 85, 80, 85, 90, 100, 105], # Walking Path
    [25, 30, 35, 40, 30, 25, 20],   # Dog Park
    [60, 65, 70, 75, 80, 85, 90],   # Garden
    [100, 105, 110, 115, 120, 125, 130],  # Amphitheater
    [40, 45, 50, 45, 40, 35, 30],   # Restrooms
    [70, 75, 80, 85, 80, 75, 70]    # Food Stall
])

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Initialize the figure and create subplots
fig, axes = plt.subplots(1, 2, figsize=(18, 10))

# Plot the network graph on the first subplot
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=node_sizes,
        font_size=10, font_weight='bold', edge_color='gray', width=2.0, alpha=0.7, ax=axes[0])

# Add a title for the network graph
axes[0].set_title('Network of Urban Park Features', fontsize=14, fontweight='bold')

# Plot the heatmap on the second subplot
heatmap = axes[1].imshow(visitor_interactions, cmap='YlGnBu', aspect='auto')

# Add labels and title for the heatmap
axes[1].set_xticks(np.arange(len(days)))
axes[1].set_xticklabels(days)
axes[1].set_yticks(np.arange(len(features)))
axes[1].set_yticklabels(features)
axes[1].set_title('Visitor Interactions Over a Week', fontsize=14, fontweight='bold')

# Add color bar to the heatmap
cbar = fig.colorbar(heatmap, ax=axes[1], orientation='vertical')
cbar.set_label('Number of Visitors', fontsize=12)

# Overall title for both plots
plt.suptitle(
    'Urban Park Analysis: Connectivity and Visitor Interaction\nEnhancing Visitor Experience Through Visual Insights',
    fontsize=16, fontweight='bold', y=1.02
)

# Clean up and adjust layout
for ax in axes:
    ax.set_xlabel('Day', fontsize=12)
    ax.set_ylabel('Feature', fontsize=12)
    ax.label_outer()  # Only show outer labels and ticks

plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout to accommodate the suptitle
plt.show()