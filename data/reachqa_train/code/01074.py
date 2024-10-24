import matplotlib.pyplot as plt
import networkx as nx

# Define the departments as nodes
departments = ["Physics", "Chemistry", "Biology", "Computer Science", "Mathematics", "Engineering", "Psychology"]

# Define collaborations between departments (edges) with the number of joint projects
collaborations = {
    ("Physics", "Chemistry"): 5,
    ("Physics", "Mathematics"): 4,
    ("Chemistry", "Biology"): 6,
    ("Biology", "Psychology"): 3,
    ("Computer Science", "Mathematics"): 7,
    ("Computer Science", "Engineering"): 6,
    ("Engineering", "Physics"): 2,
    ("Psychology", "Mathematics"): 4
}

# Create a graph
G = nx.Graph()

# Add nodes
G.add_nodes_from(departments)

# Add edges with weights based on collaborations
for (dept1, dept2), projects in collaborations.items():
    G.add_edge(dept1, dept2, weight=projects)

# Define position for nodes using a spring layout for better readability
pos = nx.spring_layout(G, seed=42)

# Extract edge weights for setting line width
edges, weights = zip(*nx.get_edge_attributes(G, 'weight').items())

# Draw the nodes with varying sizes based on their degree
node_sizes = [nx.degree(G, node) * 400 for node in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=node_sizes)

# Draw the edges with varying thickness based on the number of projects
nx.draw_networkx_edges(G, pos, edgelist=edges, width=[w * 0.8 for w in weights], alpha=0.7)

# Draw the labels for nodes
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

# Add a legend for edge weights
max_weight = max(weights)
min_weight = min(weights)
plt.figtext(0.82, 0.2, f'Max Collaboration: {max_weight} projects', horizontalalignment='right', fontsize=9)
plt.figtext(0.82, 0.16, f'Min Collaboration: {min_weight} projects', horizontalalignment='right', fontsize=9)

# Title and axis configuration
plt.title("Interdisciplinary Research Collaborations\nat Fictional University", fontsize=16, fontweight='bold', pad=20)
plt.axis('off')  # Hide the axis for a cleaner look

# Automatically adjust layout to prevent overlaps
plt.tight_layout()

# Show the plot
plt.show()