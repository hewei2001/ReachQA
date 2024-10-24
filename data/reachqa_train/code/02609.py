import matplotlib.pyplot as plt
import numpy as np

# Define the years and renewable energy data for each country
years = np.arange(2010, 2021)
renewable_usa = [250, 300, 360, 430, 510, 600, 700, 800, 900, 1050, 1200]
renewable_germany = [200, 240, 290, 350, 420, 480, 550, 620, 710, 800, 890]
renewable_india = [50, 60, 75, 100, 150, 250, 400, 500, 630, 780, 920]
renewable_china = [100, 150, 220, 310, 420, 560, 720, 900, 1050, 1250, 1500]

# Plotting the line chart
plt.figure(figsize=(12, 8))
plt.plot(years, renewable_usa, marker='o', linestyle='-', linewidth=2, color='blue', label='USA')
plt.plot(years, renewable_germany, marker='o', linestyle='-', linewidth=2, color='green', label='Germany')
plt.plot(years, renewable_india, marker='o', linestyle='-', linewidth=2, color='orange', label='India')
plt.plot(years, renewable_china, marker='o', linestyle='-', linewidth=2, color='red', label='China')

# Adding title and labels
plt.title('Renewable Energy Generation (2010-2020)\nA Decade of Growth and Innovation', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Renewable Energy Generation (TWh)', fontsize=14)

# Adding a legend
plt.legend(title='Countries', fontsize=12, loc='upper left')

# Annotate significant milestones
annotations = {
    "USA": [(2015, 600, 'Ramped up solar installations')],
    "Germany": [(2018, 620, 'Exceeded 50% of energy from renewables')],
    "India": [(2017, 400, 'Massive investments in solar parks')],
    "China": [(2020, 1500, 'World leader in renewable energy')]
}

# Annotate each significant point
for country, points in annotations.items():
    for year, value, text in points:
        plt.annotate(
            text, xy=(year, value), xytext=(year+0.5, value+50),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=10, color='black', ha='left'
        )

# Adding grid lines
plt.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()