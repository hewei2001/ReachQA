import matplotlib.pyplot as plt
import numpy as np

# Define the food categories and their popularity percentages
food_categories = [
    "Cosmic Confections", 
    "Astro Appetizers", 
    "Galactic Grains", 
    "Nebula Noodles", 
    "Stellar Sweets"
]

# Fictional survey results (popularity percentages)
popularity_percentages = [20, 25, 15, 30, 10]

# Colors for each food category
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create a ring chart
fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(aspect="equal"))

# Create the ring chart with the wedgeprops parameter set for ring width
wedges, texts, autotexts = ax.pie(
    popularity_percentages, 
    labels=food_categories, 
    autopct='%1.1f%%', 
    pctdistance=0.85, 
    colors=colors,
    startangle=140, 
    wedgeprops=dict(width=0.3, edgecolor='w')
)

# Set central title in the ring for context
plt.gcf().text(0.5, 0.5, 'Galactic Culinary Survey', ha='center', va='center', fontsize=14, fontweight='bold', color='gray')

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')  

# Add a title and adjust text properties
plt.title('Gastronomic Rings:\nThe Culinary Preferences of Galactic Voyagers', size=16, weight='bold', pad=30)
plt.setp(texts, size=10, weight='bold')
plt.setp(autotexts, size=9, weight='bold', color="white")

# Add a legend outside the ring chart
ax.legend(wedges, food_categories, title="Food Categories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()