import matplotlib.pyplot as plt
import networkx as nx

# Define the nodes (creatures) and their edges (relationships)
creatures = [
    "Unicorn", "Dragon", "Fairy", "Elf", "Dwarf", 
    "Griffin", "Phoenix", "Mermaid"
]

# Define relationships (edges) between creatures
relationships = [
    ("Unicorn", "Fairy"),
    ("Unicorn", "Elf"),
    ("Fairy", "Elf"),
    ("Fairy", "Mermaid"),
    ("Elf", "Dwarf"),
    ("Dwarf", "Griffin"),
    ("Griffin", "Dragon"),
    ("Dragon", "Phoenix"),
    ("Phoenix", "Mermaid")
]

# Create a graph using NetworkX
G = nx.Graph()
G.add_nodes_from(creatures)
G.add_edges_from(relationships)

# Define a layout for the graph
pos = nx.spring_layout(G, seed=42)  # Positions nodes using a force-directed algorithm

# Customize node properties
node_colors = ['skyblue', 'orange', 'green', 'purple', 'brown', 'gold', 'red', 'aqua']
node_sizes = [2500 for _ in creatures]

# Plot the graph
plt.figure(figsize=(12, 10))
nx.draw(G, pos, with_labels=True, node_size=node_sizes, node_color=node_colors, font_size=12, font_weight='bold', edge_color="gray", linewidths=2, alpha=0.8)

# Add a descriptive title
plt.title("Network of Mythical Creatures\nin Enchanted Forests", fontsize=16, fontweight='bold')

# Annotate nodes with interesting facts
creature_facts = {
    "Unicorn": "Guardian of Innocence",
    "Dragon": "Master of Elements",
    "Fairy": "Harbinger of Magic",
    "Elf": "Keeper of Knowledge",
    "Dwarf": "Forgemaster",
    "Griffin": "Protector of Treasures",
    "Phoenix": "Symbol of Rebirth",
    "Mermaid": "Siren of the Seas"
}

for creature, position in pos.items():
    plt.text(position[0], position[1] + 0.1, s=creature_facts[creature], fontsize=9, ha='center', color='darkblue', alpha=0.7)

# Remove axis
plt.axis('off')

# Use tight layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()