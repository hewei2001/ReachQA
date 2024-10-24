import matplotlib.pyplot as plt

# Define the energy sources and their proportions
energy_sources = ['Solar', 'Wind', 'Hydroelectric', 'Biomass', 'Geothermal']
energy_proportions = [35, 30, 20, 10, 5]

# Define historical growth rates (%) for each energy source over 5 years
growth_rates = [5, 10, 3, 7, 2]  # Hypothetical annual growth rates

# Define colors for each sector to ensure consistency across plots
colors = ['#FFD700', '#87CEEB', '#32CD32', '#FF8C00', '#8A2BE2']

# Explode the 'Solar' sector to highlight it in the pie chart
explode = (0.1, 0, 0, 0, 0)

# Create a figure and axes for two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

# Plot the pie chart
wedges, texts, autotexts = ax1.pie(energy_proportions, labels=energy_sources, autopct='%1.1f%%',
                                   startangle=140, colors=colors, explode=explode,
                                   wedgeprops={'edgecolor': 'black', 'linewidth': 1})

# Style text for the pie chart
for text in texts:
    text.set_fontsize(12)
for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_color('white')

# Set the title for the pie chart
ax1.set_title('EcoLandia\'s 2023\nSustainable Energy Mix', fontsize=14, fontweight='bold')

# Plot the bar chart for growth rates
bars = ax2.bar(energy_sources, growth_rates, color=colors, edgecolor='black', linewidth=1)

# Annotate each bar with its growth rate value
for bar, rate in zip(bars, growth_rates):
    height = bar.get_height()
    ax2.annotate(f'{rate}%', xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10)

# Set titles and labels for the bar chart
ax2.set_title('Annual Growth Rates of\nSustainable Energy Sources (2018-2023)', fontsize=14, fontweight='bold')
ax2.set_ylabel('Growth Rate (%)', fontsize=12)

# Add a legend for the bar chart
ax2.legend(bars, energy_sources, title="Energy Sources", loc="upper right", fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout(pad=3)

# Add a comprehensive footer for context
plt.figtext(0.5, 0.01, "EcoLandia is at the forefront of the clean energy revolution, showing consistent growth and diversification.",
            ha="center", fontsize=10, fontstyle='italic')

# Show the plot
plt.show()