import matplotlib.pyplot as plt
import networkx as nx

# Define nodes (planetary systems) and edges (communication links)
planetary_systems = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon', 'Zeta', 'Eta', 'Theta']
edges = [
    ('Alpha', 'Beta'), 
    ('Alpha', 'Gamma'),
    ('Beta', 'Delta'), 
    ('Gamma', 'Delta'), 
    ('Gamma', 'Epsilon'), 
    ('Delta', 'Zeta'), 
    ('Zeta', 'Eta'),
    ('Epsilon', 'Theta'),
    ('Theta', 'Alpha'),
    ('Delta', 'Alpha')  # Additional link to make the network more complex
]

# Create a directed graph
G = nx.DiGraph()
G.add_nodes_from(planetary_systems)
G.add_edges_from(edges)

# Define node categories for differentiation
hub_systems = {'Alpha', 'Gamma', 'Zeta'}  # Major hubs
minor_systems = set(planetary_systems) - hub_systems

# Position nodes using a circular layout
pos = nx.spring_layout(G, seed=42)  # Seed for consistent layout

# Plotting
plt.figure(figsize=(12, 8))

# Draw major hubs with larger and differently colored nodes
nx.draw_networkx_nodes(G, pos, nodelist=hub_systems, node_size=800, node_color='royalblue', edgecolors='black', label='Major Hubs')

# Draw minor systems with smaller and light-colored nodes
nx.draw_networkx_nodes(G, pos, nodelist=minor_systems, node_size=500, node_color='lightgrey', edgecolors='black', label='Minor Systems')

# Draw edges with arrows to indicate direction
nx.draw_networkx_edges(G, pos, edgelist=edges, arrowstyle='-|>', arrowsize=15, edge_color='grey', connectionstyle='arc3,rad=0.1')

# Draw labels for nodes
nx.draw_networkx_labels(G, pos, font_size=12, font_color='black')

# Title and legend
plt.title('Galactic Communication Network\nPlanetary System Interconnections', fontsize=16, pad=20)
plt.legend(scatterpoints=1, fontsize=12, loc='upper left', bbox_to_anchor=(1, 1))

# Remove axes and apply tight layout to prevent overlap
plt.axis('off')
plt.tight_layout()

# Show plot
plt.show()