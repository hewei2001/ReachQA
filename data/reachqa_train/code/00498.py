import matplotlib.pyplot as plt

# Define energy sources and their shares in global consumption for 2025
energy_sources = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass']
shares = [35, 30, 25, 5, 5]

# Define distinct colors for each sector
colors = ['#FFD700', '#1E90FF', '#32CD32', '#8B4513', '#FF6347']

# Create a pie chart with additional visual enhancements
plt.figure(figsize=(8, 8))
wedges, texts, autotexts = plt.pie(
    shares, labels=energy_sources, colors=colors,
    autopct='%1.1f%%', startangle=140, pctdistance=0.85,
    explode=(0.1, 0, 0, 0, 0)  # Highlight the Solar sector
)

# Customize the appearance of text inside the pie chart
for text in texts:
    text.set_fontsize(12)
    text.set_fontweight('bold')

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

# Draw a circle at the center of pie chart for a donut style
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Set the aspect ratio of the chart to be equal
plt.axis('equal')  

# Add a title with line breaks for clarity
plt.title('Global Renewable Energy Sources\nDistribution in 2025', fontsize=14, fontweight='bold', ha='center')

# Place the legend outside the pie chart
plt.legend(wedges, energy_sources, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust subplot parameters for a neat layout
plt.tight_layout()

# Display the chart
plt.show()