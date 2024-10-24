import matplotlib.pyplot as plt
import numpy as np

# Define years
years = np.arange(2010, 2021)

# Define popularity scores for each shoe style over the years
sneakers = np.array([40, 45, 55, 65, 75, 85, 95, 90, 92, 95, 100])
boots = np.array([60, 65, 60, 55, 50, 60, 70, 80, 75, 80, 82])
sandals = np.array([30, 32, 35, 40, 50, 45, 55, 60, 58, 55, 60])
loafers = np.array([20, 25, 30, 32, 35, 40, 45, 48, 46, 50, 55])
heels = np.array([70, 75, 70, 65, 68, 70, 72, 70, 69, 68, 70])

# Create the plot
plt.figure(figsize=(14, 8), facecolor='whitesmoke')

# Plot each shoe style's popularity over the years with enhanced styling
plt.plot(years, sneakers, marker='o', linestyle='-', color='royalblue', linewidth=2, label='Sneakers')
plt.plot(years, boots, marker='s', linestyle='--', color='orangered', linewidth=2.5, label='Boots')
plt.plot(years, sandals, marker='^', linestyle='-', color='gold', linewidth=1.5, label='Sandals', alpha=0.8)
plt.plot(years, loafers, marker='v', linestyle='-.', color='forestgreen', linewidth=1.8, label='Loafers')
plt.plot(years, heels, marker='d', linestyle=':', color='purple', linewidth=2, label='Heels', alpha=0.7)

# Add annotations for specific points
plt.annotate('Sneakers Peak', xy=(2020, 100), xytext=(2018, 105),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)

plt.annotate('Boots Rise', xy=(2019, 80), xytext=(2016, 85),
             arrowprops=dict(facecolor='gray', shrink=0.05), fontsize=10)

# Add title and labels with improved layout
plt.title("Footwear Trends Over the Decade\nA Style Evolution from 2010 to 2020", fontsize=18, fontweight='bold')
plt.xlabel("Year", fontsize=14)
plt.ylabel("Popularity Score", fontsize=14)

# Customize x and y axis ticks
plt.xticks(years, rotation=45, fontsize=12)
plt.yticks(np.arange(0, 101, 10), fontsize=12)

# Add shaded area under the curve for sneakers
plt.fill_between(years, sneakers, color='royalblue', alpha=0.1)

# Add grid
plt.grid(True, linestyle='--', alpha=0.4)

# Add legend with enhanced formatting
plt.legend(title="Shoe Styles", fontsize=11, loc='upper left', frameon=True, shadow=True)

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Show the plot
plt.show()