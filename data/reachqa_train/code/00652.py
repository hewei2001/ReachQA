import matplotlib.pyplot as plt

# Data for solar energy usage by sector
sectors = ["Residential", "Commercial", "Industrial", "Public Transportation", "Miscellaneous"]
energy_usage = [30, 25, 15, 20, 10]

# Colors for each sector in the pie chart
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FF66B3']

# Explode the slice for the public transportation sector to emphasize it
explode = (0, 0, 0, 0.1, 0)

# Create the pie chart
plt.figure(figsize=(10, 7))
plt.pie(
    energy_usage, 
    explode=explode, 
    labels=sectors, 
    colors=colors, 
    autopct='%1.1f%%', 
    shadow=True, 
    startangle=90
)

# Title and layout adjustments
plt.title('Solar Energy Usage Distribution\nin Solis, 2050', fontsize=16, fontweight='bold', pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.
plt.tight_layout()

# Show the plot
plt.show()