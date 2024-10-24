import matplotlib.pyplot as plt
import numpy as np

# Define chocolate types and their consumption in metric tons
chocolate_types = ['Dark Chocolate', 'Milk Chocolate', 'White Chocolate', 
                   'Ruby Chocolate', 'Bittersweet Chocolate']
consumption = [450000, 700000, 150000, 75000, 300000]

# Define distinct colors and explode for emphasis
colors = ['#4B0082', '#FFD700', '#F0E68C', '#FF6347', '#5D3A00']  # Modified for better distinction
explode = (0.1, 0, 0, 0, 0)

# Create the figure with subplots (1 row, 2 columns)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# ----------------- Donut Chart -----------------
# Create the pie chart
wedges, texts, autotexts = ax1.pie(
    consumption, 
    labels=chocolate_types, 
    colors=colors, 
    autopct='%1.1f%%', 
    startangle=140,
    explode=explode,
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w', linewidth=2)
)

# Customize text properties
for text in texts:
    text.set_size(12)
    text.set_color('black')

for autotext in autotexts:
    autotext.set_size(12)
    autotext.set_color('black')  # Changed for better visibility on light colors

# Add a center circle for the donut chart
centre_circle = plt.Circle((0, 0), 0.60, fc='white')
ax1.add_artist(centre_circle)

# Add a title to the donut chart
ax1.set_title(
    "Global Chocolate Consumption (2022)\nby Type",
    fontsize=16,
    fontweight='bold',
    color='#8B4513',
    pad=20
)

# Add a legend with icons
ax1.legend(wedges, chocolate_types, title="Chocolate Types", loc='center left', 
           bbox_to_anchor=(1, 0, 0.5, 1), title_fontsize='13', fontsize='12')

# Adding annotations for interesting facts
facts = [
    "Dark Chocolate is rich in antioxidants.",
    "Milk Chocolate is the most popular type globally.",
    "White Chocolate contains no cocoa solids.",
    "Ruby Chocolate was introduced in 2017.",
    "Bittersweet Chocolate is ideal for baking."
]
for i, fact in enumerate(facts):
    ax1.annotate(fact, xy=(1.2, 0.5 - i * 0.1), fontsize=10, color='#8B4513')

# Ensure pie chart is a perfect circle
ax1.axis('equal')

# ----------------- Bar Chart -----------------
# Data for historical consumption over the last five years
years = ['2018', '2019', '2020', '2021', '2022']
historical_consumption = [
    [400000, 650000, 120000, 50000, 250000],  # 2018
    [410000, 670000, 130000, 60000, 260000],  # 2019
    [420000, 690000, 140000, 65000, 270000],  # 2020
    [430000, 710000, 145000, 70000, 290000],  # 2021
    consumption  # 2022
]

# Bar width and positions
bar_width = 0.15
positions = np.arange(len(chocolate_types))

# Plot the data for each year
for i, year in enumerate(years):
    ax2.bar(positions + i * bar_width, historical_consumption[i], 
            width=bar_width, label=year)

# Customize the bar chart
ax2.set_title("Historical Chocolate Consumption by Type (2018-2022)", fontsize=16)
ax2.set_xlabel("Chocolate Types", fontsize=12)
ax2.set_ylabel("Consumption (Metric Tons)", fontsize=12)
ax2.set_xticks(positions + bar_width * (len(years) - 1) / 2)
ax2.set_xticklabels(chocolate_types, rotation=45, ha='right')  # Rotated for better readability
ax2.legend(title="Year")

# Adjust layout
plt.tight_layout(rect=[0, 0, 0.95, 0.95])

# Show the combined plots
plt.show()