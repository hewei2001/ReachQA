import matplotlib.pyplot as plt
import numpy as np

# Define years from 2010 to 2020
years = np.arange(2010, 2021)

# Artificial data representing percentage of time spent on different devices
desktops = np.array([50, 48, 45, 42, 38, 35, 32, 30, 28, 26, 24])
laptops = np.array([30, 32, 35, 38, 41, 43, 45, 46, 47, 48, 49])
tablets = np.array([5, 5, 5, 6, 7, 8, 10, 11, 12, 13, 14])
smartphones = 100 - (desktops + laptops + tablets)  # Ensure the total adds up to 100%

# Set up the plot
plt.figure(figsize=(12, 7))

# Stack the data for plotting
plt.stackplot(years, desktops, laptops, tablets, smartphones, labels=['Desktops', 'Laptops', 'Tablets', 'Smartphones'],
              colors=['#FF6347', '#4682B4', '#32CD32', '#FFDEAD'], alpha=0.85)

# Add title and labels with adjustments for readability
plt.title('Evolution of Device Usage in Remote Work Environments\n(2010-2020)', fontsize=14, weight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Percentage of Time Spent', fontsize=12)

# Add a legend
plt.legend(loc='upper left', title='Devices', fontsize=10)

# Enhance grid readability
plt.grid(alpha=0.3)

# Improve layout to avoid overlapping elements
plt.tight_layout()

# Display the plot
plt.show()