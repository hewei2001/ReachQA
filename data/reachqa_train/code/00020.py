import matplotlib.pyplot as plt
import numpy as np

# Years from 2000 to 2020
years = np.arange(2000, 2021)

# Popularity data for each trend over the years
minimalism = [20, 22, 25, 30, 35, 45, 55, 60, 50, 40, 45, 50, 65, 70, 68, 60, 58, 55, 53, 50, 45]
athleisure = [10, 12, 15, 18, 22, 30, 35, 40, 60, 70, 80, 85, 80, 75, 70, 68, 65, 62, 60, 58, 55]
bohemian = [30, 32, 35, 38, 42, 50, 45, 42, 40, 38, 35, 33, 30, 28, 25, 23, 20, 18, 16, 15, 12]
vintage = [15, 20, 25, 28, 35, 40, 48, 55, 58, 60, 62, 65, 70, 73, 75, 72, 68, 66, 65, 64, 63]
futurism = [5, 8, 12, 15, 18, 25, 30, 32, 34, 36, 38, 40, 45, 48, 52, 55, 60, 68, 75, 78, 80]

# Initialize the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the area chart with stackplot
ax.stackplot(years, minimalism, athleisure, bohemian, vintage, futurism,
             labels=['Minimalism', 'Athleisure', 'Bohemian', 'Vintage', 'Futurism'],
             colors=['#FF6347', '#FFD700', '#32CD32', '#1E90FF', '#9400D3'], alpha=0.8)

# Add title and labels
ax.set_title('The Rise and Fall of Fashion Trends\nin the 21st Century', fontsize=16)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Trend Popularity', fontsize=12)

# Add legend and grid
ax.legend(loc='upper left', fontsize=10)
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Customize the appearance of the x-axis labels
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 101, 10))

# Ensure the layout fits well
plt.tight_layout()

# Display the plot
plt.show()