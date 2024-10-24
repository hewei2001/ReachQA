import matplotlib.pyplot as plt

# Define energy sources and their respective distribution for 2025
energy_sources = ['Solar', 'Wind', 'Hydropower', 'Geothermal', 'Bioenergy']
distribution = [35, 30, 20, 10, 5]

# Colors for each sector
colors = ['#ffcc00', '#99ccff', '#66c2a5', '#ff99c8', '#ffb266']

# Create a figure for the pie chart
fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))

# Plot the pie chart with detailed settings
wedges, texts, autotexts = ax.pie(
    distribution, labels=energy_sources, colors=colors, autopct='%1.1f%%',
    startangle=140, pctdistance=0.85, textprops={'fontsize': 9, 'color': 'black'},
    explode=(0.05, 0.05, 0, 0, 0), shadow=True
)

# Add a circle in the center to convert the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Enhance annotations
for autotext in autotexts:
    autotext.set_weight('bold')

# Add a descriptive title
plt.title("Global Renewable Energy\nUsage Distribution in 2025", fontsize=14, fontweight='bold', pad=20, color='darkgreen')

# Adjust layout to prevent any label overlap
plt.tight_layout()

# Display the pie chart
plt.show()