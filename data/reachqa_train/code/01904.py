import matplotlib.pyplot as plt
import numpy as np

# Years for the data
years = np.arange(2020, 2031)

# Funding allocation for each category (in billions)
planetary_science = [2, 2.2, 2.4, 2.7, 3.0, 3.2, 3.3, 3.5, 3.8, 4.0, 4.2]
space_telescopes = [1.5, 1.6, 1.7, 1.8, 2.0, 2.2, 2.3, 2.5, 2.6, 2.8, 3.0]
human_spaceflight = [3, 3.1, 3.3, 3.5, 3.7, 4.0, 4.2, 4.5, 4.7, 4.9, 5.2]
astrobiology = [0.5, 0.6, 0.8, 1.0, 1.1, 1.2, 1.4, 1.5, 1.6, 1.8, 2.0]
space_technology = [1, 1.2, 1.3, 1.5, 1.7, 1.8, 2.0, 2.2, 2.5, 2.7, 3.0]

# Stack the funding allocations for plotting
funding_allocation = np.vstack([planetary_science, space_telescopes, human_spaceflight, astrobiology, space_technology])

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the stacked area chart
ax.stackplot(years, funding_allocation, labels=[
    'Planetary Science', 'Space Telescopes', 
    'Human Spaceflight', 'Astrobiology', 
    'Space Technology Development'
], colors=['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854'], alpha=0.8)

# Title and labels
ax.set_title('Space Exploration and Research Funding Allocation\n(2020-2030)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Funding (Billions $)', fontsize=14)

# Legend positioned outside the plot
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), title='Research Categories', fontsize=12)

# Customizing the x-ticks
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()