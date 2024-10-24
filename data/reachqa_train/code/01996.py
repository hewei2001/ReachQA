import matplotlib.pyplot as plt
import networkx as nx

# Define the nodes representing countries and organizations
nodes = [
    'US-CERT', 'European Union Agency', 'Japan CERT',
    'Australian Cyber Security Centre', 'Interpol',
    'Cyber Security Alliance'
]

# Define the directed edges representing the flow of intelligence
edges = [
    ('US-CERT', 'European Union Agency'),
    ('US-CERT', 'Japan CERT'),
    ('European Union Agency', 'Interpol'),
    ('Japan CERT', 'Australian Cyber Security Centre'),
    ('Australian Cyber Security Centre', 'Interpol'),
    ('Interpol', 'Cyber Security Alliance'),
    ('Cyber Security Alliance', 'US-CERT'),  # Circular collaboration back to US-CERT
    ('Interpol', 'US-CERT'),  # Alternative path for intelligence sharing
    ('Cyber Security Alliance', 'European Union Agency')  # Another collaboration loop
]

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Choose a layout for the nodes
pos = nx.spring_layout(G, seed=42)  # Spring layout for better visual spacing

# Initialize the plot
plt.figure(figsize=(14, 10))

# Draw the nodes with specific options
nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='lightseagreen', node_shape='o')

# Draw the edges with arrows
nx.draw_networkx_edges(G, pos, edgelist=edges, arrowstyle='-|>', arrowsize=20, edge_color='darkgray', width=2)

# Draw labels on the nodes
nx.draw_networkx_labels(G, pos, font_size=11, font_weight='bold', verticalalignment='center')

# Add a multi-line title to the plot
plt.title("Global Cybersecurity Threats and Collaborations:\n"
          "Flow of Intelligence within the Global Cybersecurity Alliance (GCA)",
          fontsize=15, fontweight='bold', ha='center')

# Remove axes for a cleaner look
plt.axis('off')

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Display the directed node chart
plt.show()