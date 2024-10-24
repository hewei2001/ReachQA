import matplotlib.pyplot as plt
import numpy as np

# Data: Renewable energy adoption rates by continent in 2025 (%)
continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']
adoption_rates_2025 = [
    [12, 15, 14, 18, 20, 11, 22, 21, 19, 17],  # Africa
    [35, 38, 37, 40, 42, 36, 43, 41, 39, 34],  # Asia
    [60, 62, 65, 64, 67, 61, 63, 66, 68, 69],  # Europe
    [45, 47, 49, 48, 50, 46, 44, 51, 53, 52],  # North America
    [55, 58, 57, 59, 56, 54, 60, 61, 62, 63],  # South America
    [70, 72, 71, 73, 74, 75, 76, 77, 78, 79]   # Oceania
]

# Simulated average annual growth rates (%)
growth_rates = [1.5, 2.0, 1.8, 1.7, 2.2, 2.5]  # Hypothetical values

# Create figure and subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 8), gridspec_kw={'width_ratios': [2, 1]})

# First subplot: Horizontal box plot
axs[0].boxplot(adoption_rates_2025, vert=False, patch_artist=True, notch=True, labels=continents)
colors = ['#8dd3c7', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69']
for patch, color in zip(axs[0].artists, colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.75)

# Customize whiskers, caps, and medians
for whisker, cap in zip(axs[0].lines[0::2], axs[0].lines[1::2]):
    whisker.set(color='#7570b3', linewidth=1.5)
    cap.set(color='#7570b3', linewidth=1.5)

for median in axs[0].lines[6::7]:
    median.set(color='#d95f02', linewidth=2)

axs[0].set_title('Renewable Energy Adoption Rates by Continent in 2025', fontsize=14, pad=20)
axs[0].set_xlabel('Adoption Rate (%)', fontsize=12)
axs[0].set_ylabel('Continent', fontsize=12)
axs[0].grid(axis='x', linestyle='--', alpha=0.7)

# Legend for the first plot
legend_elements = [plt.Line2D([0], [0], color=color, lw=4, label=continent) for color, continent in zip(colors, continents)]
axs[0].legend(handles=legend_elements, title='Continents', loc='lower right', fontsize=10)

# Second subplot: Bar chart of growth rates
axs[1].barh(continents, growth_rates, color=colors, alpha=0.75)
axs[1].set_title('Projected Annual Growth Rates in Renewable Energy', fontsize=14, pad=20)
axs[1].set_xlabel('Growth Rate (%)', fontsize=12)
axs[1].invert_yaxis()  # To align with box plot

# Tight layout for readability
plt.tight_layout()

# Display the plot
plt.show()