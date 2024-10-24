import matplotlib.pyplot as plt
import squarify

# Define research categories with their subcategories and respective funding
data = {
    "Exoplanet Studies": 12.5,
    "Black Hole Research": 14.2,
    "Space Exploration Tech": 17.8,
    "Astrobiology": 9.3,
    "Cosmic Microwave Background": 8.7,
    "Galaxy Formation": 12.1,
    "Dark Matter & Dark Energy": 11.4,
    "Stellar Evolution": 6.8,
    "Planetary Defense": 5.5,
    "Space Habitat Construction": 7.0,
    # Additional categories
    "Artificial Gravity Development": 4.9,
    "Interstellar Communication": 5.8,
    "Quantum Astronomy": 3.7,
    "Nano-satellites R&D": 4.4,
    "Astrophysics Instrumentation": 6.6
}

# Colors for each category
colors = [
    "#ff9999", "#66b3ff", "#99ff99", "#ffcc99", 
    "#c2c2f0", "#ffb3e6", "#ff6666", "#c2f0c2", 
    "#e6e6e6", "#ffb366", "#ffad99", "#99bfff", 
    "#b3ffb3", "#ffd699", "#d9d9f0"
]

# Calculate total funding and highlight a sum requirement
total_funding = sum(data.values())
required_funding = 125  # Hypothetical budget constraint

# Generate the treemap plot
plt.figure(figsize=(16, 10))
squarify.plot(
    sizes=data.values(), 
    label=[f"{category}\n${amount:.1f}B" for category, amount in data.items()], 
    color=colors, 
    alpha=0.85, 
    pad=True, 
    text_kwargs={'fontsize': 9}
)

# Add dynamic title with funding analysis
plt.title(
    "Global Astronomy and Space Science Research Funding Allocation: 2050\n"
    f"Total Funding: ${total_funding:.1f}B | Required Funding: ${required_funding}B",
    fontsize=15, 
    fontweight='bold'
)

# Remove axis for clarity and adjust layout
plt.axis('off')
plt.tight_layout()

# Display the plot
plt.show()