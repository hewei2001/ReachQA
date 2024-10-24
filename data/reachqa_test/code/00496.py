import matplotlib.pyplot as plt
import numpy as np

# Define the cities and their access to legal representation data
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami']
access_data = [
    [45, 50, 55, 60, 70],  # New York
    [35, 40, 45, 55, 60],  # Los Angeles
    [40, 45, 50, 52, 58],  # Chicago
    [30, 35, 40, 45, 50],  # Houston
    [55, 60, 65, 70, 75],  # Miami
]

# Define trend data for a new subplot
years = np.array([2018, 2019, 2020, 2021, 2022])
trend_data = {
    'New York': [40, 45, 50, 55, 70],
    'Los Angeles': [30, 32, 35, 40, 60],
    'Chicago': [35, 38, 42, 45, 58],
    'Houston': [25, 28, 32, 35, 50],
    'Miami': [50, 55, 60, 65, 75],
}

# Create the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Create a horizontal box plot with notches and colors
box = ax1.boxplot(access_data, vert=False, patch_artist=True, notch=True,
                  boxprops=dict(facecolor='lightblue', color='blue'),
                  whiskerprops=dict(color='blue'), capprops=dict(color='blue'), 
                  medianprops=dict(color='red'))

# Set unique colors for each box
colors = ['#AEDFF7', '#F4B400', '#4285F4', '#DB4437', '#0F9D58']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Customize the first subplot
ax1.set_yticks(range(1, len(cities) + 1))
ax1.set_yticklabels(cities, fontsize=12)
ax1.set_xlabel('Percentage of Residents with Access to Legal Representation', fontsize=12)
ax1.set_title('Access to Legal Representation in Major US Cities\nA Comparative Analysis', fontsize=14, pad=20)
ax1.grid(axis='x', linestyle='--', alpha=0.7)

# Create a line plot for trend data in the second subplot
for city, data in trend_data.items():
    ax2.plot(years, data, marker='o', label=city)

# Customize the second subplot
ax2.set_title('Trend of Access to Legal Representation Over Years', fontsize=14)
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Percentage of Residents with Access', fontsize=12)
ax2.set_xticks(years)
ax2.legend(title='Cities', fontsize=10)
ax2.grid(True)

# Adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()