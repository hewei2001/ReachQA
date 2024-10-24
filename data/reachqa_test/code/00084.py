import matplotlib.pyplot as plt
import numpy as np

# Define energy sources and their hypothetical consumption percentages
energy_sources = ['Solar Power', 'Wind Power', 'Hydroelectric', 'Fossil Fuels', 'Nuclear Power']
consumption_percentages = [25, 20, 15, 30, 10]

# Historical consumption data (last 5 years)
historical_data = {
    'Solar Power': [15, 18, 20, 23, 25],
    'Wind Power': [10, 12, 15, 18, 20],
    'Hydroelectric': [13, 14, 14, 15, 15],
    'Fossil Fuels': [40, 35, 33, 31, 30],
    'Nuclear Power': [22, 18, 15, 12, 10]
}

# Colors for the pie chart and bar chart segments
colors = ['#FFD700', '#00BFFF', '#8A2BE2', '#FF6347', '#3CB371']

# Explode the 'Fossil Fuels' slice to highlight it
explode = (0.1, 0, 0, 0.1, 0)

# Create the figure and axis for the pie chart
fig, ax = plt.subplots(figsize=(10, 10))

# Plot the pie chart
wedges, texts, autotexts = ax.pie(
    consumption_percentages,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode,
    shadow=True,
    textprops=dict(color='black', fontsize=10)
)

# Customize percentage inside slices
for autotext in autotexts:
    autotext.set_weight('bold')
    autotext.set_size(10)

# Create a central circle for a donut chart effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)

# Add a radial bar chart for historical data
num_bars = len(energy_sources)
radii = []
theta = np.linspace(0.15, 2 * np.pi, num_bars, endpoint=False)
for i, source in enumerate(energy_sources):
    radii.extend(historical_data[source])

# Flatten the theta for each year
theta = np.tile(theta, len(historical_data['Solar Power']))
radii = np.array(radii)

# Bar colors matching the pie chart
bar_colors = np.repeat(colors, len(historical_data['Solar Power']))

bars = ax.bar(
    theta, radii,
    width=0.1,
    bottom=20,
    color=bar_colors,
    alpha=0.5,
    edgecolor='black'
)

# Equal aspect ratio
ax.set(aspect="equal")

# Title with multiple lines
plt.title('Energy Consumption in 2023 and Historical Trends\n(Last 5 Years)', fontsize=14, fontweight='bold', pad=40)

# Add legend outside the pie chart
plt.legend(
    wedges, 
    energy_sources, 
    title='Energy Sources', 
    loc='center left', 
    bbox_to_anchor=(1, 0.5),
    frameon=False
)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the chart
plt.show()