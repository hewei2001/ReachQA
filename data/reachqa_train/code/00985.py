import matplotlib.pyplot as plt

# Data for vacation destinations
regions = ['Europe', 'Asia', 'North America', 'South America', 'Africa', 'Oceania']
tourist_percentages = [30, 25, 20, 10, 10, 5]

# Colors for each region
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize=(10, 7))

# Plot a donut pie chart
wedges, texts, autotexts = ax.pie(
    tourist_percentages, 
    labels=regions, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    explode=(0.05, 0.05, 0.05, 0.05, 0.05, 0.05),
    shadow=True
)

# Customize the text properties
plt.setp(autotexts, size=10, weight='bold', color='black')
plt.setp(texts, size=12)

# Title and legend configuration
ax.set_title('Global Travel Resurgence in 2023:\nPopular Vacation Destinations', fontsize=14, fontweight='bold', pad=20)
ax.legend(wedges, regions, title="Regions", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Adding a central circle for the donut appearance
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')

# Automatically adjust subplot params for better layout
plt.tight_layout()

# Display the plot
plt.show()