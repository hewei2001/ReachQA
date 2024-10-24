import matplotlib.pyplot as plt
import squarify

# Define the data
labels = ['Fashion', 'Electronics', 'Health & Beauty', 'Home & Garden', 
          'Toys & Games', 'Sports & Outdoors', 'Automotive']
sizes = [30, 25, 15, 10, 10, 5, 5]  # Market share percentages
growth_rates = [12, 8, 20, 5, 15, 10, 7]  # Growth rates

# Normalize the growth rates for coloring
colors = plt.cm.viridis([(rate - min(growth_rates)) / (max(growth_rates) - min(growth_rates)) for rate in growth_rates])

# Create a new figure with 1x2 subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 8))

# Create the treemap on the first subplot
squarify.plot(sizes=sizes, label=[f"{label}\n{size}%" for label, size in zip(labels, sizes)], 
              color=colors, alpha=0.8, edgecolor='white', ax=axs[0])
axs[0].set_title('The Digital Jungle: E-Commerce Growth by Industry\nMarket Share and Growth Rates (2023)', 
                 fontsize=16, fontweight='bold')
axs[0].axis('off')  # Hide axes

# Prepare data for the bar chart
bar_width = 0.35
x_indices = range(len(labels))

# Create the bar chart on the second subplot
market_share_bar = axs[1].bar(x_indices, sizes, width=bar_width, color='skyblue', label='Market Share (%)')
growth_rate_bar = axs[1].bar([x + bar_width for x in x_indices], growth_rates, width=bar_width, color='lightgreen', label='Growth Rate (%)')

axs[1].set_title('Market Share vs Growth Rate by Industry', fontsize=16, fontweight='bold')
axs[1].set_xticks([x + bar_width / 2 for x in x_indices])
axs[1].set_xticklabels(labels, rotation=15, ha='right')
axs[1].set_ylabel('Percentage (%)')
axs[1].legend()
axs[1].grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()