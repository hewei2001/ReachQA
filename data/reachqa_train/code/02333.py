import matplotlib.pyplot as plt

# Define energy sources
energy_sources = ['Solar', 'Wind', 'Hydroelectric', 'Biomass', 'Geothermal']

# Projected percentage distribution of each energy source in 2030
energy_distribution = [35, 30, 20, 10, 5]

# Define colors for each section of the pie chart
colors = ['#FFD700', '#1E90FF', '#32CD32', '#FF8C00', '#8A2BE2']

# Explode the largest segment for emphasis
explode = (0.1, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    energy_distribution, labels=energy_sources, autopct='%1.1f%%',
    startangle=140, colors=colors, explode=explode, shadow=True, textprops={'fontsize': 12}
)

# Customize autotext for better readability
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(12)

# Title for the plot
ax.set_title('Future of Energy:\nProjected Distribution of Renewable Energy Sources by 2030',
             fontsize=15, fontweight='bold', pad=20)

# Enhance legend to separate from the chart
ax.legend(wedges, energy_sources, title='Energy Sources', loc='upper right', bbox_to_anchor=(1.2, 1))

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the pie chart
plt.show()