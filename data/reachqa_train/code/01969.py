import numpy as np
import matplotlib.pyplot as plt

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Area of land used for each crop (in hectares)
wheat = np.array([30, 35, 37, 40, 45, 50, 55, 60, 65, 67, 70])
corn = np.array([20, 22, 25, 28, 30, 35, 40, 42, 45, 46, 50])
soybeans = np.array([15, 18, 20, 22, 25, 27, 30, 35, 40, 42, 45])
barley = np.array([10, 12, 15, 18, 20, 22, 25, 28, 30, 32, 35])

# Ensure the data represents cumulative totals for the area plot
wheat_cum = wheat
corn_cum = corn + wheat_cum
soybeans_cum = soybeans + corn_cum
barley_cum = barley + soybeans_cum

# Plotting the area chart
plt.figure(figsize=(12, 8))

# Fill between the different produce types
plt.fill_between(years, wheat_cum, label='Wheat', color='#FFD700', alpha=0.7)
plt.fill_between(years, corn_cum, wheat_cum, label='Corn', color='#FF6347', alpha=0.7)
plt.fill_between(years, soybeans_cum, corn_cum, label='Soybeans', color='#4682B4', alpha=0.7)
plt.fill_between(years, barley_cum, soybeans_cum, label='Barley', color='#32CD32', alpha=0.7)

# Customizing the plot
plt.title('Agricultural Produce Growth Trends:\nA Decade of Change in Valley Farms (2010-2020)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Area of Land Used (hectares)', fontsize=12)
plt.xticks(years, fontsize=10, rotation=45)
plt.yticks(fontsize=10)
plt.legend(loc='upper left', fontsize=10)
plt.grid(visible=True, linestyle='--', alpha=0.5)

# Annotation example
plt.annotate('Notable Soybeans Growth', xy=(2017, 140), xytext=(2014, 180),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, color='darkgreen', fontweight='bold')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()