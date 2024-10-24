import matplotlib.pyplot as plt

# Define energy sources and their corresponding capacity percentages
energy_sources = ["Solar", "Wind", "Hydropower", "Biomass", "Geothermal", "Others"]
capacity_percentages = [30, 25, 20, 15, 5, 5]

# Define colors for each segment of the ring chart
colors = ['#FFD700', '#87CEEB', '#6B8E23', '#FF8C00', '#8A2BE2', '#FF69B4']

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Create the ring chart using 'pie' with a defined width for the ring
wedges, texts, autotexts = ax.pie(capacity_percentages, labels=energy_sources, autopct='%1.1f%%', startangle=140,
                                  colors=colors, pctdistance=0.85, wedgeprops=dict(width=0.3, edgecolor='w'))

# Draw a white circle at the center to make it a ring chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that the pie chart is circular
ax.axis('equal')  

# Customize the chart title
plt.title('Global Renewable Energy Capacity Distribution\nin 2023', fontsize=16, fontweight='bold', pad=20)

# Customize autotexts for clarity
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

# Add a legend outside the chart for clarification
plt.legend(wedges, energy_sources, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()