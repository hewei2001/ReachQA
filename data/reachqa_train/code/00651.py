import matplotlib.pyplot as plt
import numpy as np

# Define the years and internet usage data for different age groups
years = np.array(range(2010, 2020))

# Internet usage percentages for each age group
usage_5_14 = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55])
usage_15_24 = np.array([40, 50, 60, 65, 70, 75, 80, 82, 85, 88])
usage_25_34 = np.array([50, 55, 60, 65, 70, 72, 75, 78, 80, 85])
usage_35_44 = np.array([30, 35, 40, 45, 50, 55, 58, 60, 62, 65])
usage_45_plus = np.array([20, 25, 30, 35, 40, 45, 48, 50, 52, 55])

# Stack the usage data
usage_data = np.vstack([usage_5_14, usage_15_24, usage_25_34, usage_35_44, usage_45_plus])

# Create the area chart
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each age group's internet usage using stackplot
ax.stackplot(years, usage_data, labels=[
    'Age 5-14', 'Age 15-24', 'Age 25-34', 'Age 35-44', 'Age 45+'],
    colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0'], alpha=0.8)

# Add title and labels
ax.set_title("Internet Usage Trends Across Age Groups\nFrom 2010 to 2019", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Internet Usage (%)", fontsize=12)

# Add a legend
ax.legend(loc='upper left', fontsize=12)

# Enhance readability with a grid
ax.grid(True, linestyle='--', alpha=0.5)

# Rotate x-axis labels to avoid overlap
plt.xticks(rotation=45)

# Adjust the layout to make all elements visible
plt.tight_layout()

# Display the chart
plt.show()