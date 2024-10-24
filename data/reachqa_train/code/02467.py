import matplotlib.pyplot as plt

# Data for the pie chart
regions = ['North America', 'Europe', 'Asia-Pacific', 'Latin America', 'Middle East & Africa']
market_shares = [30, 25, 28, 10, 7]

# Colors for each region
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Explode the slice for North America to highlight it
explode = (0.1, 0, 0, 0, 0)  # Only explode the first slice (North America)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    market_shares, 
    labels=regions, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    explode=explode,
    pctdistance=0.85,
    textprops={'fontsize': 12},
    shadow=True
)

# Draw a circle in the center of the pie chart to create a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that the pie chart is drawn as a circle
ax.axis('equal')  

# Add a title
plt.title('2023 Global Virtual Reality Market Share\nby Region', fontsize=16, fontweight='bold')

# Position legend to the right
plt.legend(wedges, regions, title="Regions", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Improve layout
plt.tight_layout()

# Display the chart
plt.show()