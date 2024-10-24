import matplotlib.pyplot as plt
import numpy as np

# Years from 2000 to 2020
years = np.arange(2000, 2021)

# Proportion of robotics utilization in each sector over the years
manufacturing = np.array([10, 15, 20, 28, 35, 45, 55, 65, 75, 85, 100, 115, 130, 145, 160, 175, 190, 210, 230, 250, 270])
healthcare = np.array([5, 7, 10, 13, 18, 23, 30, 38, 45, 55, 65, 75, 88, 100, 115, 130, 145, 160, 175, 190, 205])
retail = np.array([3, 5, 7, 10, 13, 17, 22, 28, 35, 42, 50, 58, 67, 77, 88, 100, 113, 126, 140, 155, 170])
agriculture = np.array([2, 3, 4, 6, 8, 10, 13, 17, 21, 26, 32, 39, 47, 56, 66, 77, 89, 102, 116, 131, 147])

# Plotting the area chart
plt.figure(figsize=(14, 8))
plt.stackplot(years, manufacturing, healthcare, retail, agriculture,
              labels=['Manufacturing', 'Healthcare', 'Retail', 'Agriculture'],
              colors=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99'], alpha=0.7)

# Title and labels
plt.title("The Evolution of Robotics in Industry\nfrom 2000 to 2020", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Robotics Utilization (Arbitrary Units)", fontsize=12)

# Legend
plt.legend(loc='upper left', fontsize=10, title="Industry Sectors")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Grid lines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Display the chart
plt.show()