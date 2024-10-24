import matplotlib.pyplot as plt
import squarify

# Define the districts and their focus areas for urban agriculture
districts = [
    'Hydroponics', 'Vertical\nFarming', 'Rooftop\nGardens',
    'Greenhouses', 'Community\nGardens'
]

# Production values for each focus area in thousands of tons
production_values = [30, 50, 20, 40, 10]

# Hypothetical growth rates for each focus area
growth_rates = [12, 25, 8, 18, 5]  # in percentage

# Define colors for each category
colors = ['#64b5f6', '#81c784', '#ffb74d', '#ba68c8', '#e57373']

# Create a subplot layout
fig, ax = plt.subplots(1, 2, figsize=(16, 8))

# Treemap
squarify.plot(
    ax=ax[0],
    sizes=production_values,
    label=[f"{districts[i]}\n{production_values[i]}k tons" for i in range(len(districts))],
    color=colors,
    alpha=0.8,
    text_kwargs={'fontsize': 10, 'weight': 'bold', 'color': 'white'},
    bar_kwargs={'linewidth': 2, 'edgecolor': 'white'}
)
ax[0].set_title(
    "Urban Agriculture Production\nCity of New Harmonia, 2150",
    fontsize=14, weight='bold', color='darkgreen'
)
ax[0].axis('off')

# Bar chart for growth rates
ax[1].bar(districts, growth_rates, color=colors, edgecolor='black', alpha=0.9)
ax[1].set_title(
    "Projected Growth Rates\nUrban Agriculture Techniques",
    fontsize=14, weight='bold', color='darkgreen'
)
ax[1].set_ylabel('Growth Rate (%)', fontsize=12)
ax[1].set_xlabel('Focus Areas', fontsize=12)
ax[1].set_xticklabels(districts, fontsize=10, rotation=45, ha='right')

# Adjust layout to prevent label overlap
plt.tight_layout()

# Display the plot
plt.show()