import matplotlib.pyplot as plt
import numpy as np

# Years from 2012 to 2022
years = np.arange(2012, 2023)

# Streaming service hours watched per month (in millions)
netflix = [15, 22, 30, 40, 52, 65, 78, 90, 100, 115, 130]
hulu = [10, 12, 15, 18, 21, 25, 29, 34, 38, 43, 48]
disney_plus = [0, 0, 0, 0, 5, 15, 25, 35, 47, 60, 72]
amazon_prime = [5, 8, 12, 17, 23, 30, 38, 47, 55, 63, 70]
hbo_max = [0, 0, 0, 5, 10, 18, 27, 35, 40, 50, 60]

# Combine data into a stacked format
data = np.array([netflix, hulu, disney_plus, amazon_prime, hbo_max])

# Color map for the areas
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FF9966']

# Plotting the Stacked Area Chart
fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(years, data, labels=['Netflix', 'Hulu', 'Disney+', 'Amazon Prime', 'HBO Max'], colors=colors, alpha=0.8)

# Title and labels
plt.title('Streaming Services Usage Trends\nHours Watched Per Month (2012 - 2022)', fontsize=16, weight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Monthly Hours Watched (Millions)', fontsize=12)
plt.legend(loc='upper left', fontsize=10, title='Streaming Services')

# Annotate significant milestones
ax.annotate('Disney+ Launch', xy=(2019, 5), xytext=(2017, 30),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
             fontsize=10, color='darkgreen', ha='right')

ax.annotate('HBO Max Launch', xy=(2016, 10), xytext=(2014, 45),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
             fontsize=10, color='purple', ha='right')

# Enhancing gridlines and layout
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()