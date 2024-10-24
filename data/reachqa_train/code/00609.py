import matplotlib.pyplot as plt
import numpy as np

# Define the years and the internet usage data for different age groups
years = np.array([2010, 2012, 2014, 2016, 2018, 2020])
usage_0_18 = np.array([10, 15, 25, 35, 45, 60])
usage_19_35 = np.array([40, 50, 65, 75, 85, 90])
usage_36_50 = np.array([25, 30, 35, 45, 55, 65])
usage_51_65 = np.array([10, 15, 20, 25, 30, 35])
usage_66_plus = np.array([5, 7, 10, 13, 17, 20])

# Stack the data for a stacked area plot
data = np.vstack([usage_0_18, usage_19_35, usage_36_50, usage_51_65, usage_66_plus])

# Define labels and colors for each age group
age_groups = ['0-18', '19-35', '36-50', '51-65', '66+']
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Plot the stacked area chart
plt.figure(figsize=(12, 8))
plt.stackplot(years, data, labels=age_groups, colors=colors, alpha=0.8)

# Add title and labels
plt.title('Evolution of Global Internet Usage\nA Decadal Analysis by Age Group', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Internet Usage (% of Population)', fontsize=12)

# Add a legend with title, positioned outside the plot area to avoid overlap
plt.legend(title='Age Group', fontsize=10, loc='upper left', bbox_to_anchor=(1.05, 1))

# Grid and layout adjustments
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout(rect=[0, 0, 0.85, 1])  # Adjust layout to accommodate legend

# Display the plot
plt.show()