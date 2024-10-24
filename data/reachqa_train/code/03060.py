import matplotlib.pyplot as plt
import numpy as np

# Data representing the projected percentage share of global food sources in 2050
food_sources = ["Plant-based Foods", "Lab-grown Meat", "Insects", "Algae", "Traditional Meat", "Dairy Alternatives"]
percentages = np.array([40, 25, 15, 10, 5, 5])

# Colors for each food source segment
colors = ['#76B041', '#D12B2B', '#FFDD44', '#2EABBF', '#8D674B', '#F2C14E']

# Create the donut pie chart
fig, ax = plt.subplots(figsize=(9, 9))

# Creating pie chart with a donut shape by adding width to wedgeprops
wedges, texts, autotexts = ax.pie(
    percentages, 
    labels=food_sources,
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors, 
    wedgeprops=dict(width=0.4, edgecolor='w'), # Adjusting the donut thickness
    pctdistance=0.75)  # Position the percentage labels to avoid overlap

# Adding a central circle to transform the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.60, fc='white')
fig.gca().add_artist(centre_circle)

# Ensure equal aspect ratio
ax.axis('equal')  

# Enhance the percentage labels
plt.setp(autotexts, size=12, weight="bold", color='black')

# Add a title with line breaks for readability
ax.set_title('Global Food Sources Distribution in 2050\nFocus on Sustainability', fontsize=15, weight='bold', pad=20)

# Add a legend outside the chart for clarity
ax.legend(wedges, food_sources, title="Food Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=11)

# Annotate key insights in the center of the chart
ax.annotate('Sustainable\nChoices', xy=(0, 0), fontsize=13, color='grey', weight='bold', ha='center', va='center')

# Adjust the layout to prevent overlapping and to ensure readability
plt.tight_layout()

# Display the chart
plt.show()