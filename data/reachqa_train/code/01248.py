import numpy as np
import matplotlib.pyplot as plt

# Years from 2050 to 2060
years = np.arange(2050, 2061)

# Internet users (in thousands) for each colony
internet_users_mars = np.array([50, 70, 95, 120, 160, 210, 280, 360, 460, 580, 720])
internet_users_europa = np.array([10, 15, 22, 30, 45, 65, 90, 120, 160, 210, 280])
internet_users_titan = np.array([5, 8, 12, 20, 30, 45, 65, 85, 110, 140, 180])

# Plot the area chart
plt.figure(figsize=(14, 8))

# Using stackplot for cumulative area chart
plt.stackplot(years, internet_users_mars, internet_users_europa, internet_users_titan, 
              labels=['Mars', 'Europa', 'Titan'], 
              colors=['crimson', 'royalblue', 'darkorange'], alpha=0.7)

# Title and labels
plt.title("Internet Usage Trends in Galactic Colonies (2050-2060)", fontsize=16, fontweight='bold')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Internet Users (in thousands)", fontsize=12)

# Add a legend
plt.legend(title="Colonies", title_fontsize='13', fontsize='11', loc='upper left', frameon=True)

# Grid lines
plt.grid(True, linestyle='--', alpha=0.5)

# Annotations for significant events
plt.annotate('Mars: Rapid Growth Begins', xy=(2055, 210), xytext=(2052, 500),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='crimson')

plt.annotate('Titan: Infrastructure Boom', xy=(2058, 110), xytext=(2056, 300),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkorange')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()