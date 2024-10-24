import matplotlib.pyplot as plt
import networkx as nx

# Define the departments (nodes) and additional data for the bar chart
departments = [
    "R&D", "Product Management", "Marketing", 
    "Sales", "Customer Support", "IT Support", "HR", "Finance"
]
budgets = [120, 100, 90, 110, 85, 95, 70, 105]  # Example budget allocations (in thousands)

# Define the collaborations (edges) with weights representing collaborative projects
collaborations = [
    ("R&D", "Product Management", 8),
    ("R&D", "Marketing", 5),
    ("R&D", "Sales", 4),
    ("Product Management", "Marketing", 7),
    ("Marketing", "Sales", 9),
    ("Sales", "Customer Support", 6),
    ("Customer Support", "IT Support", 5),
    ("IT Support", "HR", 3),
    ("HR", "Finance", 2),
    ("Finance", "Product Management", 4)
]

# Create an undirected graph
G = nx.Graph()
G.add_nodes_from(departments)
G.add_weighted_edges_from(collaborations)

# Define positions using spring layout
pos = nx.spring_layout(G, seed=42)

# Node attributes
node_colors = ['#FFDDC1', '#FFABAB', '#FFC3A0', '#FF677D', '#D4A5A5', '#392F5A', '#31A2AC', '#61C0BF']
node_sizes = [budget * 10 for budget in budgets]  # Scale budgets for node sizes

# Set up subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
plt.subplots_adjust(wspace=0.4)

# Plot 1: Network Graph
nx.draw_networkx_nodes(G, pos, ax=axes[0], node_size=node_sizes, node_color=node_colors, alpha=0.9)
edge_weights = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edges(G, pos, ax=axes[0], width=[0.2 * weight for weight in edge_weights.values()], alpha=0.7)
nx.draw_networkx_labels(G, pos, ax=axes[0], font_size=9, font_family='sans-serif', verticalalignment='bottom')
edge_labels = {(u, v): f"{d['weight']} proj." for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, ax=axes[0], edge_labels=edge_labels, font_color='darkgreen', font_size=8)
axes[0].set_title("InnovateTech Interdepartmental Collaborations\n2023", fontsize=12, fontweight='bold')
axes[0].axis('off')

# Plot 2: Bar Chart for Department Budgets
axes[1].bar(departments, budgets, color=node_colors, alpha=0.8)
axes[1].set_title("Department Budgets (in thousands)", fontsize=12, fontweight='bold')
axes[1].set_ylabel("Budget (in $1000s)")
axes[1].set_xlabel("Departments")
axes[1].tick_params(axis='x', rotation=45)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()