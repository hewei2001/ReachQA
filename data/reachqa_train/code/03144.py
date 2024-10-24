import matplotlib.pyplot as plt
import squarify

# Define mineral resources and their quantities in megatons
mineral_resources = {
    'Tritanium': 550,    # Planet Aegis
    'Unobtanium': 400,   # Moon Callisto
    'Phlebotinum': 300,  # Planet Zenith
    'Xenonium': 450,     # Moon Chiron
    'Adamantite': 250,   # Planet Arda
    'Vibranium': 600,    # Planet Nexus
    'Dilithium': 500,    # Moon Talos
}

# Define colors for each mineral
colors = [
    '#e74c3c',  # Tritanium
    '#3498db',  # Unobtanium
    '#9b59b6',  # Phlebotinum
    '#1abc9c',  # Xenonium
    '#f1c40f',  # Adamantite
    '#e67e22',  # Vibranium
    '#2ecc71'   # Dilithium
]

# Define the labels for the treemap, including mineral name and quantity
labels = [f'{key}\n{value} MT' for key, value in mineral_resources.items()]

# Create the figure
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the treemap
squarify.plot(
    sizes=mineral_resources.values(), 
    label=labels, 
    color=colors, 
    alpha=0.8, 
    ax=ax,
    text_kwargs={'fontsize': 12, 'weight': 'bold', 'color': 'white'}
)

# Add a title and remove axes
plt.title('Resource Distribution in Proxima Centauri\nIntergalactic Mining Overview', fontsize=16, fontweight='bold', pad=20)
plt.axis('off')

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the treemap chart
plt.show()