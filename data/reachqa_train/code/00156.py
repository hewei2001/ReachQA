import matplotlib.pyplot as plt
import networkx as nx

# Define the departments as nodes
departments = ['IT', 'Finance', 'Marketing', 'HR', 'Customer Support']

# Define directed edges with weights indicating data transfer volume
data_flow = [
    ('IT', 'Finance', 350),
    ('IT', 'Marketing', 300),
    ('IT', 'HR', 250),
    ('IT', 'Customer Support', 450),
    ('Finance', 'IT', 200),
    ('Marketing', 'IT', 180),
    ('HR', 'IT', 150),
    ('Customer Support', 'IT', 220),
    ('Marketing', 'Customer Support', 75),
    ('Finance', 'HR', 90)
]

# Compute total data handled by each department
total_data_handled = {dept: 0 for dept in departments}
for source, target, weight in data_flow:
    total_data_handled[source] += weight
    total_data_handled[target] += weight

# Create a directed graph
G = nx.DiGraph()
G.add_nodes_from(departments)
G.add_weighted_edges_from(data_flow)

# Create a subplot with 1 row and 2 columns
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))

# First Subplot: Network Flow Diagram
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx_nodes(G, pos, node_size=2500, node_color='skyblue', edgecolors='black', ax=axes[0])
nx.draw_networkx_edges(G, pos, edgelist=data_flow, arrowstyle='-|>', arrowsize=20, edge_color='grey', ax=axes[0])
nx.draw_networkx_labels(G, pos, font_size=10, font_color='black', ax=axes[0])
edge_labels = {(source, target): f"{weight} units" for source, target, weight in data_flow}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, font_color='red', ax=axes[0])
axes[0].set_title('Network Flow in IT Environment', fontsize=14, pad=20)
axes[0].axis('off')

# Second Subplot: Bar Chart of Total Data Handled
departments_sorted = sorted(departments, key=lambda d: total_data_handled[d], reverse=True)
values = [total_data_handled[dept] for dept in departments_sorted]
axes[1].bar(departments_sorted, values, color='skyblue', edgecolor='black')
axes[1].set_title('Total Data Handled per Department', fontsize=14, pad=20)
axes[1].set_xlabel('Department')
axes[1].set_ylabel('Total Data (Units)')
for i, v in enumerate(values):
    axes[1].text(i, v + 10, str(v), ha='center', fontsize=10)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()