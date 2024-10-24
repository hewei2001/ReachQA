import matplotlib.pyplot as plt
import squarify

# Define data for renewable energy investments (in billions of dollars)
energy_sources = ['Solar Energy', 'Wind Energy', 'Hydropower', 'Biomass', 'Geothermal']
investments = [160, 140, 110, 60, 30]  # Updated hypothetical investment figures for balance

# Calculate the total investment for percentage calculations
total_investment = sum(investments)

# Create labels with investment values and percentages
labels = [f"{source}\n${value}B\n({value / total_investment * 100:.1f}%)"
          for source, value in zip(energy_sources, investments)]

# Color palette for visual distinction
colors = ['#FDD835', '#29B6F6', '#66BB6A', '#AB47BC', '#FF7043']

# Plotting the treemap
fig, ax = plt.subplots(figsize=(12, 8))
squarify.plot(sizes=investments, label=labels, color=colors, alpha=0.8, ax=ax, text_kwargs={'fontsize': 10, 'weight': 'bold'})

# Set title with proper wrapping for clarity
plt.title('Global Investment in Renewable Energy Sources\nDistribution Across Major Sectors', fontsize=18, fontweight='bold')

# Remove axes for visual clarity
plt.axis('off')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()