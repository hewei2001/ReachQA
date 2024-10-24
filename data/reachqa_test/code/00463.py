import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Define the years from 2015 to 2023
years = np.arange(2015, 2024)

# Data: yields (in tons) for different crops
tomatoes = np.array([200, 220, 240, 260, 280, 310, 330, 360, 400])
lettuce = np.array([150, 160, 170, 180, 190, 220, 230, 240, 250])
bell_peppers = np.array([100, 120, 140, 160, 170, 180, 200, 220, 240])
spinach = np.array([80, 90, 100, 110, 120, 130, 140, 160, 180])
strawberries = np.array([60, 70, 80, 90, 95, 110, 125, 130, 140])

# Create the figure and axis for the plot
plt.figure(figsize=(14, 8))

# Plotting with area fills
plt.plot(years, tomatoes, marker='o', label='Tomatoes', color='tomato', linewidth=2, linestyle='-')
plt.fill_between(years, tomatoes, color='tomato', alpha=0.2)

plt.plot(years, lettuce, marker='s', label='Lettuce', color='forestgreen', linewidth=2, linestyle='--')
plt.fill_between(years, lettuce, color='forestgreen', alpha=0.2)

plt.plot(years, bell_peppers, marker='^', label='Bell Peppers', color='gold', linewidth=2, linestyle=':')
plt.fill_between(years, bell_peppers, color='gold', alpha=0.2)

plt.plot(years, spinach, marker='d', label='Spinach', color='mediumseagreen', linewidth=2, linestyle='-')
plt.fill_between(years, spinach, color='mediumseagreen', alpha=0.2)

plt.plot(years, strawberries, marker='*', label='Strawberries', color='deeppink', linewidth=2, linestyle='--')
plt.fill_between(years, strawberries, color='deeppink', alpha=0.2)

# Add annotations for maximum yields
max_yields = [400, 250, 240, 180, 140]
crop_names = ['Tomatoes', 'Lettuce', 'Bell Peppers', 'Spinach', 'Strawberries']
for i, max_yield in enumerate(max_yields):
    plt.annotate(f'Max: {max_yield}', xy=(years[-1], max_yield), 
                 xytext=(years[-1]-1, max_yield + 15),
                 arrowprops=dict(facecolor='black', shrink=0.05),
                 fontsize=9, color='black')

# Set the title and labels with line breaks
plt.title("Urban Agriculture Yield Trends\n2015 - 2023", fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Crop Yield (tons)', fontsize=12)

# Add a legend to the plot
plt.legend(loc='upper left', title='Crops', fontsize=10, frameon=True)

# Enable grid for better readability with customized styling
plt.grid(True, linestyle='--', alpha=0.6)

# Adjust x-axis ticks for clarity
plt.xticks(years, rotation=45)

# Set y-axis limits for better focus
plt.ylim(0, 420)

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()