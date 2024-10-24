import matplotlib.pyplot as plt
import squarify
import numpy as np

# Define categories and their market shares by continent
categories = ["Electronics", "Fashion", "Home & Kitchen", "Health & Beauty", "Sports & Outdoors"]

market_share_data = {
    'North America': [35, 25, 15, 10, 15],
    'Europe': [30, 20, 20, 15, 15],
    'Asia': [50, 20, 10, 10, 10],
    'South America': [25, 30, 20, 15, 10],
    'Africa': [20, 25, 25, 15, 15]
}

# Create an additional dataset for annual growth rates by continent
growth_rate_data = {
    'Electronics': [3.5, 2.8, 5.0, 3.0, 2.5],
    'Fashion': [2.0, 2.5, 3.0, 2.8, 2.2],
    'Home & Kitchen': [1.5, 2.0, 1.8, 1.5, 2.0],
    'Health & Beauty': [2.8, 3.0, 2.5, 3.2, 2.0],
    'Sports & Outdoors': [2.5, 2.2, 2.8, 2.5, 2.3]
}

# Set up the figure with two rows: one for tree maps and one for the bar chart
fig, axs = plt.subplots(2, 1, figsize=(18, 16))

# Use a colormap to automatically select distinct colors
colors = plt.cm.Set3.colors[:len(categories)]

# Plot Tree Maps for each continent
for i, (continent, shares) in enumerate(market_share_data.items()):
    ax = plt.subplot(2, len(market_share_data), i + 1)
    labels = [f"{cat}\n{share}%" for cat, share in zip(categories, shares)]
    squarify.plot(sizes=shares, label=labels, color=colors, alpha=0.7, ax=ax, pad=True, edgecolor="black", linewidth=0.5)
    plt.title(continent, fontsize=14, weight='bold')
    plt.axis('off')

# Prepare data for the bar chart
bar_data = np.array([growth_rate_data[cat] for cat in categories])
continent_indices = np.arange(len(market_share_data))
bar_width = 0.15

# Plot Bar Chart for growth rates
for idx, cat_data in enumerate(bar_data):
    axs[1].bar(continent_indices + idx * bar_width, cat_data, bar_width, color=colors[idx], label=categories[idx])

axs[1].set_title("Annual Growth Rate of Product Categories across Continents", fontsize=18, weight='bold')
axs[1].set_xticks(continent_indices + (bar_width * (len(categories) - 1)) / 2)
axs[1].set_xticklabels(market_share_data.keys(), fontsize=12)
axs[1].set_ylabel("Growth Rate (%)", fontsize=12)
axs[1].legend(title="Categories", fontsize=10, title_fontsize='13')
axs[1].grid(True, linestyle='--', alpha=0.6)

# Set a global title and adjust layout
plt.suptitle("Global E-Commerce Market Share and Growth by Product Category\nacross Continents in 2025", fontsize=22, weight='bold', y=1.02)
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Show the plot
plt.show()