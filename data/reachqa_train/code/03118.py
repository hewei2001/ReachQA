import numpy as np
import matplotlib.pyplot as plt

# Programming languages and regions
languages = ["Python", "JavaScript", "C++", "Java", "Go"]
regions = ["North America", "Europe", "Asia", "Africa", "South America"]

# Adoption rates (example values in %)
adoption_rates = np.array([
    [70, 65, 50, 55, 40],   # North America
    [65, 60, 45, 50, 35],   # Europe
    [60, 70, 60, 60, 50],   # Asia
    [30, 35, 25, 20, 15],   # Africa
    [55, 50, 45, 40, 30]    # South America
])

# Create the heat map
fig, ax = plt.subplots(figsize=(10, 6))
cax = ax.imshow(adoption_rates, cmap='YlGnBu', interpolation='nearest', aspect='auto')

# Add title and labels
plt.title("Tech Revolution:\nGlobal Adoption of Programming Languages (2020-2030)", fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel("Programming Languages", fontsize=12, fontweight='bold')
ax.set_ylabel("Regions", fontsize=12, fontweight='bold')

# Set tick labels
ax.set_xticks(np.arange(len(languages)))
ax.set_xticklabels(languages, fontsize=10, rotation=45, ha='right')
ax.set_yticks(np.arange(len(regions)))
ax.set_yticklabels(regions, fontsize=10)

# Add a color bar
cbar = plt.colorbar(cax, pad=0.02)
cbar.set_label('Adoption Rate (%)', fontsize=12, weight='bold')

# Annotate each cell with the numerical value
for i in range(len(regions)):
    for j in range(len(languages)):
        ax.text(j, i, f"{adoption_rates[i, j]}%", va='center', ha='center', color='black')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()