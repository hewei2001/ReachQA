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

# Fictional data for mythical creature popularity
creature_popularity = {
    "Unicorn": 95,
    "Dragon": 90,
    "Fairy": 85,
    "Elf": 80,
    "Dwarf": 75,
    "Griffin": 70,
    "Phoenix": 78,
    "Mermaid": 88
}

# Create a graph using NetworkX
G = nx.Graph()
G.add_nodes_from(creatures)
G.add_edges_from(relationships)

# Layout for the graph
pos = nx.spring_layout(G, seed=42)

# Node properties
node_colors = ['skyblue', 'orange', 'green', 'purple', 'brown', 'gold', 'red', 'aqua']
node_sizes = [2500 for _ in creatures]

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(18, 9))

# First subplot: Network graph
axs[0].set_title("Network of Mythical Creatures\nin Enchanted Forests", fontsize=16, fontweight='bold')
nx.draw(G, pos, ax=axs[0], with_labels=True, node_size=node_sizes, node_color=node_colors,
        font_size=12, font_weight='bold', edge_color="gray", linewidths=2, alpha=0.8)

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
    axs[0].text(position[0], position[1] + 0.1, s=creature_facts[creature], fontsize=9, ha='center',
                color='darkblue', alpha=0.7)

# Second subplot: Bar chart for creature popularity
axs[1].bar(creature_popularity.keys(), creature_popularity.values(), color=node_colors)
axs[1].set_title("Mythical Creature Popularity", fontsize=16, fontweight='bold')
axs[1].set_ylabel("Popularity Score")
axs[1].set_xlabel("Creature")
axs[1].tick_params(axis='x', rotation=45)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plots
plt.show()