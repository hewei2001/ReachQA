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

# Calculate cumulative growth percentage over the decade
def compute_growth(start, values):
    return ((values - start) / start) * 100

residential_growth = compute_growth(residential_speed[0], residential_speed)
business_growth = compute_growth(business_speed[0], business_speed)
education_growth = compute_growth(education_speed[0], education_speed)

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 9))

# Plot data with error bars for each sector
ax1.errorbar(years, residential_speed, yerr=residential_variability, fmt='-o', color='teal', 
             capsize=5, alpha=0.8, label='Residential')
ax1.errorbar(years, business_speed, yerr=business_variability, fmt='-s', color='darkorange', 
             capsize=5, alpha=0.8, label='Business')
ax1.errorbar(years, education_speed, yerr=education_variability, fmt='-d', color='forestgreen', 
             capsize=5, alpha=0.8, label='Education')

# Add secondary Y-axis for growth percentages
ax2 = ax1.twinx()
width = 0.3  # Bar width
ax2.bar(years - width, residential_growth, width=width, color='lightblue', alpha=0.6, label='Residential Growth (%)')
ax2.bar(years, business_growth, width=width, color='navajowhite', alpha=0.6, label='Business Growth (%)')
ax2.bar(years + width, education_growth, width=width, color='lightgreen', alpha=0.6, label='Education Growth (%)')

# Set titles and labels
ax1.set_title('Internet Speed Evolution and Variability in Cybercity\n(2010-2020)\nwith Cumulative Growth Percentage Overlay', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Average Internet Speed (Mbps)', fontsize=14)
ax2.set_ylabel('Cumulative Growth Percentage (%)', fontsize=14)

# Set ticks
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)
ax1.set_yticks(np.arange(0, 81, 10))
ax2.set_yticks(np.arange(0, 901, 100))

# Add grid and legend
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend(loc='upper left', fontsize=12)
ax2.legend(loc='upper right', fontsize=12)

# Automatically adjust layout
fig.tight_layout()

# Display the plot
plt.show()