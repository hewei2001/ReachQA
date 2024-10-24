import matplotlib.pyplot as plt
import numpy as np

# Define global popularity percentages for cuisines
cuisines = ['Italian', 'Chinese', 'Mexican', 'Indian', 'Japanese', 'Mediterranean', 'Others']
global_popularity = [18, 15, 12, 14, 10, 8, 23]  # Global percentages

# Define regional popularity percentages (fictional)
regions = ['North America', 'Europe', 'Asia']
regional_popularity = {
    'Italian': [25, 30, 5],
    'Chinese': [10, 15, 25],
    'Mexican': [20, 10, 5],
    'Indian': [5, 10, 25],
    'Japanese': [10, 5, 20],
    'Mediterranean': [10, 15, 5],
    'Others': [20, 15, 15]
}

# Colors for the chart
colors = ['#FF5733', '#33FFBD', '#FFD700', '#FF33A6', '#33A1FF', '#95FF33', '#D3D3D3']

# Explode the largest category for the pie chart
explode = (0.1, 0, 0, 0, 0, 0, 0)  # Exploding the 'Italian' category

# Create a 1x2 grid of subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Pie chart
wedges, texts, autotexts = ax1.pie(global_popularity, labels=cuisines, autopct='%1.1f%%', startangle=140,
                                   colors=colors, explode=explode, shadow=True, textprops={'fontsize': 11, 'weight': 'bold'})
ax1.set_title("Global Culinary Trends in 2023:\nA Taste of Diversity", fontsize=14, weight='bold', pad=20)
ax1.legend(wedges, cuisines, title='Cuisines', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Bar chart for regional comparison
x = np.arange(len(regions))
width = 0.1  # Width of bars

for i, cuisine in enumerate(cuisines):
    ax2.bar(x + i*width, regional_popularity[cuisine], width, label=cuisine, color=colors[i])

# Customize bar chart
ax2.set_xticks(x + width*(len(cuisines)/2))
ax2.set_xticklabels(regions)
ax2.set_ylabel('Popularity (%)')
ax2.set_title('Regional Culinary Popularity in 2023', fontsize=14, weight='bold', pad=20)
ax2.legend(title='Cuisines')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()