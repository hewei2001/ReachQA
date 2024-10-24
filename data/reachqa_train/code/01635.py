import matplotlib.pyplot as plt
import numpy as np

# Define years
years = np.arange(2013, 2023)

# Define adoption data for each technology
ai_adoption = np.array([5, 10, 20, 30, 40, 50, 55, 60, 70, 75])
blockchain_adoption = np.array([2, 8, 15, 22, 30, 28, 26, 24, 22, 20])
iot_adoption = np.array([10, 15, 25, 35, 45, 55, 53, 51, 50, 48])
ar_adoption = np.array([3, 7, 10, 15, 18, 20, 22, 20, 18, 17])

# Sum up all tech adoptions per year
total_adoption = ai_adoption + blockchain_adoption + iot_adoption + ar_adoption

# Normalize to percentage of total adoption each year
ai_adoption_percentage = (ai_adoption / total_adoption) * 100
blockchain_adoption_percentage = (blockchain_adoption / total_adoption) * 100
iot_adoption_percentage = (iot_adoption / total_adoption) * 100
ar_adoption_percentage = (ar_adoption / total_adoption) * 100

# Stack the data for plotting
adoption_data = np.vstack([ai_adoption_percentage, blockchain_adoption_percentage, iot_adoption_percentage, ar_adoption_percentage])

# Plotting the stacked area chart
plt.figure(figsize=(12, 7))

# Set colors for each technology trend
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Create stacked area plot
plt.stackplot(years, adoption_data, labels=['AI', 'Blockchain', 'IoT', 'AR'], colors=colors, alpha=0.8)

# Adding title and labels
plt.title('Decade of Tech Evolution: Trends and Adoption (2013-2022)', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('User Adoption (%)', fontsize=12)

# Adjust x-axis labels to prevent overlap
plt.xticks(years, rotation=45)

# Adding legend outside the main plot area
plt.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 1))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()