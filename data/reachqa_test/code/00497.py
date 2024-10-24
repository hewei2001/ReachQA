import matplotlib.pyplot as plt
import squarify
import matplotlib.colors as mcolors

# Define categories and corresponding revenue data
categories = ['Clothing', 'Footwear', 'Accessories', 'Luxury', 'Activewear', 'Fast Fashion']
revenues = [600, 300, 150, 200, 250, 350]  # in billion USD

# Define corresponding growth rates for a new subplot
growth_rates = [8, 10, 5, 6, 12, 9]  # in percentage

# Set a distinct color palette
colors = mcolors.TABLEAU_COLORS

# Create a figure with a defined size
fig, axs = plt.subplots(1, 2, figsize=(14, 8))

# Create the treemap
squarify.plot(sizes=revenues, 
              label=[f"{cat}\n${rev}B" for cat, rev in zip(categories, revenues)],
              color=list(colors.values())[:len(categories)], 
              alpha=0.8, edgecolor='white', ax=axs[0])

# Title for the treemap
axs[0].set_title("Global Fashion Market Revenue Distribution\nby Category (2022)", 
                 fontsize=16, fontweight='bold', pad=15)
axs[0].axis('off')

# Create the bar chart for growth rates
axs[1].bar(categories, growth_rates, color=list(colors.values())[:len(categories)])
axs[1].set_title("Year-Over-Year Growth Rate by Category\n(2022)", fontsize=16, fontweight='bold', pad=15)
axs[1].set_ylabel("Growth Rate (%)", fontsize=12)
axs[1].set_xlabel("Categories", fontsize=12)
axs[1].set_ylim(0, max(growth_rates) + 5)  # Add some space above the highest bar

# Annotate bars with growth rates
for i, v in enumerate(growth_rates):
    axs[1].text(i, v + 0.2, f"{v}%", ha='center', fontsize=10, fontweight='bold')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plots
plt.show()