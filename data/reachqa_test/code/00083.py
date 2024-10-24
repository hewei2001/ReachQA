import matplotlib.pyplot as plt
import numpy as np

# Define years and technologies
years = ['2000', '2010', '2020']
projected_year = '2030'
technologies = ['Postal Mail', 'Email', 'SMS', 'Social Media', 'Video Conferencing']

# Usage percentages for each technology over the years
usage_percentages = np.array([
    [50, 30, 15, 5, 0],   # Year 2000
    [20, 40, 25, 10, 5],  # Year 2010
    [5, 25, 15, 30, 25]   # Year 2020
])

# Projected usage percentages for 2030
projected_usage = np.array([1, 20, 10, 35, 34])

# Define colors for each technology
colors = ['#FFD700', '#FF4500', '#32CD32', '#4682B4', '#8A2BE2']

# Create a figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Plot the stacked percentage bar chart on the first subplot
for i, tech in enumerate(technologies):
    axes[0].bar(years, usage_percentages[:, i], color=colors[i], 
                bottom=usage_percentages[:, :i].sum(axis=1), label=tech)

# Original Chart: Titles, labels, and legend
axes[0].set_title('Evolution of Communication Technologies\nin Techville (2000-2020)', fontsize=12)
axes[0].set_xlabel('Year', fontsize=10)
axes[0].set_ylabel('Percentage Usage (%)', fontsize=10)
axes[0].set_ylim(0, 100)
axes[0].tick_params(axis='x', labelsize=8)
axes[0].tick_params(axis='y', labelsize=8)

for year_idx, year in enumerate(years):
    bottom_value = 0
    for tech_idx, tech in enumerate(technologies):
        percentage_value = usage_percentages[year_idx, tech_idx]
        if percentage_value > 0:
            axes[0].text(year, bottom_value + percentage_value / 2, f'{percentage_value}%', 
                         ha='center', va='center', fontsize=8, color='white')
        bottom_value += percentage_value

axes[0].legend(title='Technologies', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)

# Plot the line chart for projected usage on the second subplot
axes[1].plot(technologies, projected_usage, marker='o', color='b')

# New Subplot: Titles, labels, and aesthetics
axes[1].set_title('Projected Communication Technology\nUsage for 2030', fontsize=12)
axes[1].set_xlabel('Technology', fontsize=10)
axes[1].set_ylabel('Projected Usage (%)', fontsize=10)
axes[1].set_ylim(0, 100)
axes[1].tick_params(axis='x', labelsize=8, rotation=45)
axes[1].tick_params(axis='y', labelsize=8)

# Adding value labels on the line chart
for i, tech in enumerate(technologies):
    axes[1].text(tech, projected_usage[i] + 1, f'{projected_usage[i]}%', 
                 ha='center', va='bottom', fontsize=8)

# Adjust layout for better fitting
plt.tight_layout()
plt.show()