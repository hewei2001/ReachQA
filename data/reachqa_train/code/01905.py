import matplotlib.pyplot as plt
import numpy as np

# Quarterly data from 2020 to 2030
quarters = np.arange(2020, 2031, 0.25)

# Funding allocation for each category (in billions), using more intricate patterns
planetary_science = 2 + 0.2 * np.sin(0.5 * np.pi * (quarters - 2020)) + 0.05 * (quarters - 2020)
space_telescopes = 1.5 + 0.05 * (quarters - 2020)**1.1
human_spaceflight = 3 + 0.4 * np.cos(0.3 * np.pi * (quarters - 2020)) + 0.1 * (quarters - 2020)
astrobiology = 0.5 + 0.02 * (quarters - 2020)**1.2
space_technology = 1 + 0.1 * np.exp(0.05 * (quarters - 2020))
robotic_missions = 0.7 + 0.15 * np.log1p((quarters - 2020) * 2)

# Combine funding allocations
funding_allocation = np.vstack([
    planetary_science, space_telescopes, human_spaceflight,
    astrobiology, space_technology, robotic_missions
])

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(16, 9))

# Plot the stacked area chart
ax.stackplot(quarters, funding_allocation, labels=[
    'Planetary Science', 'Space Telescopes', 
    'Human Spaceflight', 'Astrobiology', 
    'Space Technology', 'Robotic Missions'
], colors=['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f'], alpha=0.85)

# Title and labels
ax.set_title('Quarterly Space Exploration and Research Funding Allocation\nfrom 2020 to 2030', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Funding (Billions $)', fontsize=14)

# Legend positioned outside the plot
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), title='Research Categories', fontsize=12)

# Customizing the x-ticks
ax.set_xticks(np.arange(2020, 2031, 1))
ax.set_xticklabels([f"{int(year)}" for year in np.arange(2020, 2031, 1)], rotation=45)

# Adding a secondary plot overlay: Total funding as a line plot
total_funding = np.sum(funding_allocation, axis=0)
ax.plot(quarters, total_funding, color='black', linewidth=2, label='Total Funding')
ax.text(2030, total_funding[-1], f'{total_funding[-1]:.1f}', fontsize=10, color='black', ha='right')

# Grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()