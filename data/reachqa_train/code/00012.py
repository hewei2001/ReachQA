import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
labels = ['Action', 'Role-playing', 'Shooter', 'Adventure', 'Simulation', 'Strategy', 'Sports', 'Other']
sizes = [25, 20, 15, 10, 10, 8, 7, 5]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6', '#c7f0c2', '#f0c2d1']
explode = (0.05, 0.05, 0.05, 0, 0, 0, 0, 0)  # slightly pull out the top genres for emphasis

# Create the donut pie chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    sizes, 
    colors=colors, 
    labels=labels, 
    autopct='%1.1f%%', 
    startangle=90, 
    pctdistance=0.85, 
    explode=explode,
    wedgeprops=dict(width=0.3),  # create donut effect
    shadow=True  # add shadow for depth
)

# Set properties for the labels and percentage texts
plt.setp(autotexts, size=10, weight="bold", color='white')
plt.setp(texts, size=10, weight='bold')

# Add legend with appropriate positioning to avoid overlap
ax.legend(wedges, labels, title="Genres", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Title and layout adjustments
ax.set_title("2023 Global Video Game Genre\nPopularity Survey", fontsize=14, weight='bold', pad=20)

# Ensure that everything fits without overlapping
plt.tight_layout()

# Display the plot
plt.show()