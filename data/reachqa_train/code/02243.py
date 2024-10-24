import matplotlib.pyplot as plt
import numpy as np

# Define the cities, categories, and their tallest building heights over the years
cities = ['New York', 'Dubai', 'Shanghai', 'London', 'Tokyo', 'Kuala Lumpur', 'Sydney', 'Moscow', 'Chicago', 'Hong Kong']
categories = ['Commercial', 'Residential', 'Mixed-use']
years = [2000, 2010, 2020, 2023]

# Heights (in meters) are constructed for illustration, for each city over different categories and years
heights_data = {
    'New York': {
        'Commercial': [410, 420, 430, 450],
        'Residential': [380, 390, 400, 420],
        'Mixed-use': [360, 370, 380, 400]
    },
    'Dubai': {
        'Commercial': [350, 700, 800, 830],
        'Residential': [300, 650, 750, 800],
        'Mixed-use': [320, 680, 770, 820]
    },
    # Add similar data for other cities...
}

# Create a figure with subplots
fig, ax = plt.subplots(figsize=(15, 10))

# Prepare colors for categories
category_colors = {'Commercial': '#1f77b4', 'Residential': '#ff7f0e', 'Mixed-use': '#2ca02c'}

# Calculate and plot data for each city and category
index = np.arange(len(years))
bar_width = 0.2

for idx, city in enumerate(cities):
    for cat_idx, category in enumerate(categories):
        if city in heights_data:
            city_data = heights_data[city][category]
            ax.bar(index + (bar_width * idx) + (cat_idx * bar_width / 3), city_data, 
                   bar_width / 3, label=f'{city} - {category}' if idx == 0 else "", 
                   color=category_colors[category], edgecolor='black')
    
    # Calculate total height and annotate
    if city in heights_data:
        total_heights = [sum(heights) for heights in zip(*heights_data[city].values())]
        for year_idx, total_height in enumerate(total_heights):
            ax.text(year_idx + bar_width * idx + bar_width, total_height + 10, f'{total_height} m', 
                    ha='center', va='bottom', fontsize=8, fontweight='bold', color='black')

# Customize the appearance
ax.set_xlabel('Year', fontsize=12, fontweight='bold')
ax.set_ylabel('Height (m)', fontsize=12, fontweight='bold')
ax.set_title('Evolution of Skyscrapers:\nHeight of Tallest Buildings by City and Category (2000-2023)', fontsize=16, fontweight='bold', ha='center')
ax.set_xticks(index + len(cities) * bar_width / 2)
ax.set_xticklabels(years, fontsize=11, weight='bold')

# Add a legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Improve the layout
plt.tight_layout(rect=[0, 0, 0.85, 1]) # Adjusted for legend outside plot

# Display the plot
plt.show()