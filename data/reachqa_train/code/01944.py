import matplotlib.pyplot as plt
import numpy as np

# Original data for donut chart
coffee_types = ['Espresso', 'Latte', 'Cappuccino', 'Americano', 'Cold Brew']
consumption_percentages = [30, 25, 20, 15, 10]
colors = ['#e73030', '#f5c46b', '#a87f32', '#b5b5b5', '#35647f']

# New data for the line chart showing trends over 5 years
years = np.arange(2019, 2024)
trends = {
    'Espresso': [28, 29, 30, 32, 30],
    'Latte': [20, 22, 23, 24, 25],
    'Cappuccino': [18, 19, 20, 21, 20],
    'Americano': [15, 16, 16, 15, 15],
    'Cold Brew': [8, 9, 10, 10, 10]
}

# Initialize a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Donut chart
wedges, texts, autotexts = ax1.pie(
    consumption_percentages, labels=coffee_types, colors=colors,
    autopct='%1.1f%%', startangle=90, pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w'), explode=(0.1, 0, 0, 0, 0),
    shadow=True
)
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax1.add_artist(centre_circle)
ax1.set_title('Global Coffee Consumption by Type\nin 2023', fontsize=16, fontweight='bold', pad=20)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(12)
    autotext.set_fontweight('bold')

ax1.legend(wedges, coffee_types, title="Coffee Types", loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10, title_fontsize='12')
ax1.axis('equal')

# Line chart
for coffee_type, trend_data in trends.items():
    ax2.plot(years, trend_data, marker='o', label=coffee_type)

ax2.set_title('Coffee Consumption Trends (2019-2023)', fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Consumption (%)', fontsize=12)
ax2.grid(True, which='both', linestyle='--', linewidth=0.5)
ax2.set_xticks(years)
ax2.legend(loc='upper left', fontsize=10)

# Improve layout
plt.tight_layout()

# Show the plots
plt.show()