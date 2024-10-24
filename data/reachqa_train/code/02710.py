import matplotlib.pyplot as plt

# Define the data for global internet users by region
regions = ['Asia', 'Europe', 'Africa', 'North America', 'Latin America & Caribbean', 'Oceania']
usage_percentages = [53, 15, 12, 10, 7, 3]

# Colors for each segment
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700', '#FF6347']

# Explode the largest slice for emphasis (Asia)
explode = (0.1, 0, 0, 0, 0, 0)

# Create the pie chart
plt.figure(figsize=(10, 7))
plt.pie(usage_percentages, labels=regions, autopct='%1.1f%%', startangle=90, colors=colors, 
        explode=explode, pctdistance=0.85, shadow=True)

# Draw a circle in the center to make it a donut chart for aesthetic reasons
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Title and formatting
plt.title('Global Internet Users\nDistribution by Region (2023)', fontsize=16, fontweight='bold')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()