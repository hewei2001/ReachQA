import matplotlib.pyplot as plt
import numpy as np

# Define the data for the pie chart
continents = ['Africa', 'Antarctica', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']
initiatives_percentage = [15, 10, 25, 20, 18, 8, 4]

# Define colors for each continent
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2C2F0', '#FFB3E6', '#FFD700']

# Additional data for the bar chart
years = ['2018', '2019', '2020', '2021', '2022']
growth_data = {
    'Africa': [12, 14, 16, 15, 15],
    'Antarctica': [9, 10, 11, 11, 10],
    'Asia': [20, 22, 25, 28, 30],
    'Europe': [18, 19, 19, 20, 20],
    'North America': [16, 17, 17, 18, 18],
    'South America': [6, 7, 8, 8, 8],
    'Oceania': [3, 3, 4, 4, 4]
}

# Set up the figure and axis for subplots
fig, ax = plt.subplots(1, 2, figsize=(18, 8))

# Create the pie chart on the first subplot
explode = (0, 0, 0.1, 0, 0, 0, 0)
ax[0].pie(initiatives_percentage, labels=continents, autopct='%1.1f%%', startangle=120, 
          colors=colors, shadow=True, explode=explode)
ax[0].set_title('Global Exploration Initiatives by Continent\n(A Hypothetical Distribution)', 
                fontsize=14, fontweight='bold', pad=20)

# Create a bar chart on the second subplot to show growth over years
width = 0.12
x = np.arange(len(years))
for i, continent in enumerate(continents):
    ax[1].bar(x + i * width, growth_data[continent], width, label=continent, color=colors[i])

ax[1].set_title('Yearly Growth in Exploration Initiatives\n(Hypothetical Data)', fontsize=14, fontweight='bold')
ax[1].set_xlabel('Year', fontsize=12)
ax[1].set_ylabel('Number of Initiatives', fontsize=12)
ax[1].set_xticks(x + width * 3)
ax[1].set_xticklabels(years)
ax[1].legend(title="Continents", loc='upper left', fontsize=10, bbox_to_anchor=(1, 1))

# Ensure layout is adjusted to prevent overlap
plt.tight_layout()

# Display the combined chart
plt.show()