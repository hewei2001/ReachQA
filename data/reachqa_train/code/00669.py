import matplotlib.pyplot as plt
import squarify  # Used for creating tree maps

# Define the data: energy sources and their market share
energy_sources = ['Solar Power', 'Wind Power', 'Hydropower', 'Geothermal', 'Biomass']
market_share = [35, 25, 20, 10, 10]  # Market share in percentage
colors = ['#ffd700', '#1e90ff', '#32cd32', '#ff8c00', '#8a2be2']  # Unique colors for each category

# Prepare labels that include energy sources and their market share
labels = [f'{source}\n{share}%' for source, share in zip(energy_sources, market_share)]

# Create the plot
plt.figure(figsize=(12, 8))
squarify.plot(sizes=market_share, label=labels, color=colors, alpha=0.8, text_kwargs={'fontsize': 14})

# Customize plot appearance
plt.title('The Transition to Renewable Energy\nMarket Share of Various Sources in 2023', fontsize=18, fontweight='bold', pad=20)
plt.axis('off')  # Disable axes for clarity

# Adjust layout to avoid overlapping
plt.tight_layout()

# Display the plot
plt.show()