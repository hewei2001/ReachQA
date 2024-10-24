import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2013 to 2023
years = np.arange(2013, 2024)

# Percentage of new buildings using sustainable materials each year
sustainable_percentage = np.array([5, 8, 12, 18, 26, 35, 42, 50, 60, 70, 80])

# Create the percentage bar chart
plt.figure(figsize=(14, 8))
bars = plt.bar(years, sustainable_percentage, color='#76c7c0', edgecolor='black')

# Chart details
plt.title('Sustainable Architecture: 2013-2023\nPercentage of New Buildings Using Green Materials', fontsize=16, pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Percentage of New Buildings (%)', fontsize=12)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 101, 10))

# Annotate the bars with the percentage values
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{yval}%', ha='center', va='bottom', fontsize=10, fontweight='bold', color='darkgreen')

# Highlight certain milestones in the trend
plt.axhline(y=50, color='gray', linestyle='--', linewidth=1)
plt.text(years[0] - 0.7, 51, '50% Milestone', fontsize=10, color='gray')

plt.axhline(y=75, color='gray', linestyle='--', linewidth=1)
plt.text(years[0] - 0.7, 76, '75% Target', fontsize=10, color='gray')

# Add a legend explaining highlighted milestones
plt.legend(['50% Milestone', '75% Target'], loc='upper left', fontsize=10)

# Layout adjustment to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()