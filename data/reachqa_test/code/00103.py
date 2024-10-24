import matplotlib.pyplot as plt
import numpy as np

# Original Data for sectors
sectors = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon', 'Zeta', 'Eta', 'Theta', 'Iota', 'Kappa']
star_density = [45, 60, 80, 35, 50, 75, 30, 55, 65, 70]
exploration_challenge = [4, 7, 8, 3, 5, 9, 2, 6, 7, 8]
discovery_potential = [70, 80, 95, 60, 75, 90, 50, 85, 90, 93]

# Convert discovery potential to a scale for bubble size
bubble_size = [potential * 10 for potential in discovery_potential]

# Additional Data: Average Star Density grouped by Exploration Challenge levels
# Constructed so each challenge level is averaged over non-overlapping groups
unique_challenges = sorted(set(exploration_challenge))
avg_star_density_per_challenge = [np.mean([star_density[i] for i in range(len(star_density)) if exploration_challenge[i] == level]) 
                                  for level in unique_challenges]

# Create subplots
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(18, 8))

# Scatter Plot (Original)
scatter = axs[0].scatter(star_density, exploration_challenge, s=bubble_size, c=discovery_potential, cmap='plasma', alpha=0.75, edgecolor='black', linewidth=0.5)
axs[0].set_xlabel("Star Density (stars/light-year)", fontsize=12)
axs[0].set_ylabel("Exploration Challenge\n(Scale 1-10)", fontsize=12)
axs[0].set_title("Galactic Traveler's Guide:\nStar Density vs. Exploration Challenge", fontsize=14, fontweight='bold')
for i, sector in enumerate(sectors):
    axs[0].text(star_density[i] + 0.5, exploration_challenge[i], sector, fontsize=9, ha='left', va='bottom')
cbar = fig.colorbar(scatter, ax=axs[0])
cbar.set_label('Discovery Potential', rotation=270, labelpad=15)
axs[0].grid(True, linestyle='--', alpha=0.6)

# Bar Plot (New)
axs[1].bar(unique_challenges, avg_star_density_per_challenge, color='skyblue', edgecolor='black')
axs[1].set_xlabel("Exploration Challenge (Scale 1-10)", fontsize=12)
axs[1].set_ylabel("Average Star Density\n(stars/light-year)", fontsize=12)
axs[1].set_title("Average Star Density\nper Exploration Challenge Level", fontsize=14, fontweight='bold')
axs[1].set_xticks(unique_challenges)
axs[1].grid(axis='y', linestyle='--', alpha=0.6)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()