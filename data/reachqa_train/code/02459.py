import matplotlib.pyplot as plt
import numpy as np

# Define years
years = np.arange(2010, 2021)

# Define average internet speeds (Mbps) for each sector
residential_speed = np.array([4, 5, 6, 8, 10, 15, 20, 25, 35, 40, 45])
business_speed = np.array([10, 12, 15, 18, 24, 30, 35, 40, 50, 60, 70])
education_speed = np.array([6, 7, 9, 11, 14, 17, 22, 28, 34, 38, 42])

# Define variability (standard deviation) for each sector
residential_variability = np.array([1, 1.2, 1.1, 1.5, 1.8, 2, 2.5, 3, 3.5, 4, 4.5])
business_variability = np.array([1.5, 1.6, 1.8, 2, 2.2, 2.4, 3, 3.5, 4, 4.5, 5])
education_variability = np.array([1.2, 1.3, 1.5, 1.7, 2, 2.2, 2.8, 3.2, 3.5, 4, 4.2])

# Create the plot
plt.figure(figsize=(12, 8))

# Plot data with error bars for each sector
plt.errorbar(years, residential_speed, yerr=residential_variability, fmt='-o', color='teal', 
             capsize=5, alpha=0.8, label='Residential', ecolor='lightgray')
plt.errorbar(years, business_speed, yerr=business_variability, fmt='-s', color='darkorange', 
             capsize=5, alpha=0.8, label='Business', ecolor='lightgray')
plt.errorbar(years, education_speed, yerr=education_variability, fmt='-d', color='forestgreen', 
             capsize=5, alpha=0.8, label='Education', ecolor='lightgray')

# Add labels and title
plt.title('Internet Speed Evolution and Variability in Cybercity\n(2010-2020)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Average Internet Speed (Mbps)', fontsize=14)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 81, 10))

# Add grid
plt.grid(True, linestyle='--', alpha=0.7)

# Add legend
plt.legend(title='Sector', fontsize=12, title_fontsize=14, loc='upper left')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()