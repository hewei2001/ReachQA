import matplotlib.pyplot as plt

# Data: Proportion of renewable energy sources in 2023
energy_sources = ['Solar Energy', 'Wind Energy', 'Hydropower', 'Biomass', 'Geothermal']
percentages = [35, 30, 20, 10, 5]

# Sub-categories for each energy source
sub_categories = {
    'Solar Energy': [20, 15],      # Photovoltaic, Thermal
    'Wind Energy': [15, 15],       # Onshore, Offshore
    'Hydropower': [12, 8],         # Large, Small
    'Biomass': [5, 5],             # Solid, Gas
    'Geothermal': [3, 2]           # Electric, Direct Use
}

# Main color palette for the pie chart
colors = ['#f4a261', '#2a9d8f', '#264653', '#e9c46a', '#e76f51']
sub_colors = ['#e9c46a', '#f4a261', '#e76f51', '#2a9d8f', '#264653']  # Just an example palette

# Explode the Solar and Wind sectors slightly for emphasis
explode = (0.1, 0.1, 0, 0, 0)

# Create the main pie chart
fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    percentages, labels=energy_sources, autopct='%1.1f%%', startangle=90,
    colors=colors, pctdistance=0.85, wedgeprops=dict(edgecolor='w', linewidth=1.5), explode=explode
)

# Sub-category pie chart on the inner ring
size = 0.35
inner_sizes = [sum(sub) for sub in sub_categories.values()]
inner_colors = [sub_colors[i % len(sub_colors)] for i, sub in enumerate(sub_categories.values()) for _ in sub]

ax.pie(
    [value for sublist in sub_categories.values() for value in sublist], radius=1-size, colors=inner_colors,
    startangle=90, wedgeprops=dict(width=size, edgecolor='w', linewidth=1.5)
)

# Enhance aesthetics with bold text
plt.setp(autotexts, size=10, weight="bold", color="white")
for text in texts:
    text.set_fontsize(12)

# Add a center circle for a doughnut chart look
centre_circle = plt.Circle((0, 0), 1-size, fc='white')
ax.add_artist(centre_circle)

# Title and subtitle
plt.title('Global Renewable Energy Mix in 2023\nSub-categories included for detailed insights',
          fontsize=15, fontweight='bold', pad=20)

# Add legend outside the pie chart
ax.legend(wedges, energy_sources, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()