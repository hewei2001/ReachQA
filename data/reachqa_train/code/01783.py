import matplotlib.pyplot as plt
import squarify  # For creating treemaps

# Define research categories and their respective funding in billions
categories = [
    "Exoplanet Studies", "Black Hole Research", "Space Exploration Tech",
    "Astrobiology", "Cosmic Microwave Background", "Galaxy Formation",
    "Dark Matter & Dark Energy", "Stellar Evolution", "Planetary Defense", 
    "Space Habitat Construction"
]

# Funding amounts, creatively constructed
funding = [8, 10, 12, 6, 7, 8, 9, 5, 4, 6]  # Funding in billions

# Colors for each category
colors = [
    "#ff9999", "#66b3ff", "#99ff99", "#ffcc99", 
    "#c2c2f0", "#ffb3e6", "#ff6666", "#c2f0c2", 
    "#e6e6e6", "#ffb366"
]

# Create the treemap plot
plt.figure(figsize=(14, 8))
squarify.plot(
    sizes=funding, 
    label=[f"{cat}\n${amt}B" for cat, amt in zip(categories, funding)], 
    color=colors, 
    alpha=0.8, 
    pad=True, 
    text_kwargs={'fontsize':10}
)

# Title with line break for readability
plt.title(
    "Global Astronomy and Space Science Research Funding Allocation: 2050", 
    fontsize=16, 
    fontweight='bold'
)

# Remove axis for clarity
plt.axis('off')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()