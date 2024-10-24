import matplotlib.pyplot as plt
import squarify

# Market share data for renewable energy sources
energy_types = ['Solar', 'Wind', 'Hydropower', 'Geothermal', 'Biomass']
market_shares = [320, 280, 230, 90, 70]  # Market shares in hypothetical units
growth_rates = [10, 8, 6, 3, 2]  # Annual growth rates as percentages

# Define colors for each energy source
colors = ['#FFD700', '#87CEEB', '#32CD32', '#FF8C00', '#8B4513']

# Create the figure and subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 8))
fig.suptitle('Renewable Energy Sources: Market Share & Growth in 2023', fontsize=18, weight='bold')

# Subplot 1: Tree Map
axs[0].set_title('Market Share', fontsize=14, pad=10)
squarify.plot(
    sizes=market_shares,
    label=[f"{energy}\n{share} units" for energy, share in zip(energy_types, market_shares)],
    color=colors, alpha=0.75, edgecolor="white", linewidth=2,
    text_kwargs={'fontsize': 10, 'weight': 'bold'},
    ax=axs[0]
)
axs[0].axis('off')

# Subplot 2: Bar Chart for Growth Rates
axs[1].set_title('Annual Growth Rates', fontsize=14, pad=10)
bars = axs[1].bar(energy_types, growth_rates, color=colors, alpha=0.85, edgecolor='black')
axs[1].set_ylabel('Growth Rate (%)', fontsize=12, weight='bold')
axs[1].set_ylim(0, max(growth_rates) + 2)

# Add value annotations on each bar
for bar in bars:
    height = bar.get_height()
    axs[1].annotate(
        f'{height}%', xy=(bar.get_x() + bar.get_width() / 2, height),
        xytext=(0, 3),  # 3 points vertical offset
        textcoords='offset points',
        ha='center', va='bottom', fontsize=10, weight='bold'
    )

# Automatically adjust layout to avoid overlap
plt.tight_layout(rect=[0, 0, 1, 0.95])  # Adjust the tight_layout to consider the main title

# Display the plot
plt.show()