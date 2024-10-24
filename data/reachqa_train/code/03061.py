import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Wedge

# Data representing the projected percentage share of global food sources in 2050
food_sources = ["Plant-based Foods", "Lab-grown Meat", "Insects", "Algae", "Traditional Meat", "Dairy Alternatives"]
percentages = np.array([40, 25, 15, 10, 5, 5])

# Secondary data layer for additional insight: hypothetical growth rates in percentage
growth_rates = np.array([3, 5, 7, 6, 2, 4])

# Colors and patterns for each food source segment
colors = ['#8DD35F', '#E57F80', '#FFD966', '#A0E7E5', '#BB8B63', '#F7C843']
hatches = ['/', '\\', '|', '-', '+', 'x']

# Create the donut pie chart
fig, ax = plt.subplots(figsize=(10, 10))

# Creating pie chart with a donut shape and a radial gradient-like pattern
wedges, texts, autotexts = ax.pie(
    percentages,
    labels=food_sources,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    wedgeprops=dict(width=0.3, edgecolor='w', hatch=None),  # Adjusting the donut thickness
    pctdistance=0.7)  # Position the percentage labels

# Add an inner ring to represent growth rates
inner_wedges = [Wedge((0, 0), 0.3, w.theta1, w.theta2, width=0.15, facecolor=colors[i], edgecolor='w', hatch=hatches[i]) for i, w in enumerate(wedges)]
for inner_wedge in inner_wedges:
    ax.add_patch(inner_wedge)

# Central circle to enhance donut chart appearance
centre_circle = plt.Circle((0, 0), 0.45, fc='white')
fig.gca().add_artist(centre_circle)

# Ensure equal aspect ratio
ax.axis('equal')

# Enhance the percentage labels
plt.setp(autotexts, size=12, weight="bold", color='black')

# Add a title with line breaks for readability
ax.set_title('Global Food Sources Distribution in 2050\nand Predicted Growth Rates', fontsize=14, weight='bold', pad=20)

# Add a legend outside the chart for clarity
ax.legend(wedges, food_sources, title="Food Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=11)

# Annotate key insights and add a symbol in the center of the chart
ax.annotate('Sustainable\nChoices 🌱', xy=(0, 0), fontsize=14, color='grey', weight='bold', ha='center', va='center')

# Adjust layout for better fit
plt.tight_layout()

# Display the chart
plt.show()