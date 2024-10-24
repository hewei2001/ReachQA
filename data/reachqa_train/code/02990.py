import matplotlib.pyplot as plt
import squarify

# Market share data for digital entertainment sectors in 2023
sectors = ['Streaming Services', 'Online Gaming', 'Digital Music', 'E-books', 'Virtual Reality']
market_share_2023 = [35, 30, 15, 10, 10]

# Projected growth rates for 2024 (in percentage)
growth_rates_2024 = [5, 8, 3, 2, 10]

# Color palette for sectors
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']

# Create the figure and subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

# Treemap for market share 2023
axes[0].set_title("Market Share in 2023 by Sector", fontsize=16, fontweight='bold', pad=15)
squarify.plot(sizes=market_share_2023, label=[f"{sector}\n{share}%" for sector, share in zip(sectors, market_share_2023)], 
              color=colors, alpha=0.8, text_kwargs={'fontsize': 10, 'weight': 'bold', 'color': 'white'}, ax=axes[0])
axes[0].axis('off')

# Bar chart for projected growth in 2024
axes[1].barh(sectors, growth_rates_2024, color=colors, alpha=0.8)
axes[1].set_title("Projected Growth Rate for 2024", fontsize=16, fontweight='bold', pad=15)
axes[1].set_xlabel("Growth Rate (%)", fontsize=12)
axes[1].set_xlim(0, max(growth_rates_2024) + 5)
for i, v in enumerate(growth_rates_2024):
    axes[1].text(v + 0.5, i, f"{v}%", color='black', va='center', fontweight='bold')

# General layout adjustments
plt.tight_layout()

# Display the plot
plt.show()