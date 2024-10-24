import matplotlib.pyplot as plt

# Data for renewable energy production in 2023
energy_sources = ['Solar', 'Wind', 'Hydropower', 'Biomass', 'Geothermal', 'Tidal', 'Other']
energy_share = [33, 25, 20, 12, 5, 3, 2]

# Colors for the pie chart segments
colors = ['#ffcc00', '#1f77b4', '#aec7e8', '#2ca02c', '#ff7f0e', '#9467bd', '#8c564b']

# Explode the Solar section to highlight it
explode = (0.1, 0, 0, 0, 0, 0, 0)

# Plotting the pie chart
plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(
    energy_share, 
    explode=explode, 
    labels=energy_sources, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    pctdistance=0.85, 
    wedgeprops={'edgecolor': 'black'}, 
    shadow=True
)

# Customize the font size and style of labels and percentages
for text in texts:
    text.set_fontsize(10)
for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_color('white')
    autotext.set_fontweight('bold')

# Draw a circle at the center of pie to convert it into a doughnut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Add a title with proper styling
plt.title('Global Renewable Energy Production in 2023\nDiverse and Sustainable Power Sources', fontsize=16, fontweight='bold', pad=20)

# Position the legend outside the pie chart
plt.legend(wedges, energy_sources, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()