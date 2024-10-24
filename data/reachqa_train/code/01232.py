import matplotlib.pyplot as plt
import numpy as np

# Hypothetical monthly sales data (in thousands of units) for each console
game_sphere_x_sales = [40, 42, 38, 50, 46, 49, 53, 45, 44, 47, 50, 49]
nexgen_play_sales = [35, 37, 33, 34, 32, 36, 40, 39, 38, 34, 30, 31]
ultimate_box_sales = [30, 32, 31, 29, 28, 27, 30, 35, 37, 34, 36, 38]

# Assemble data into a list for the boxplot
sales_data = [game_sphere_x_sales, nexgen_play_sales, ultimate_box_sales]

# Names of the gaming consoles
console_names = ['GameSphere X', 'NexGen Play', 'Ultimate Box']

# Create horizontal box plot
plt.figure(figsize=(12, 8))
box = plt.boxplot(sales_data, vert=False, patch_artist=True, labels=console_names, 
                  meanline=True, showmeans=True, notch=True)

# Customizing boxplot colors
colors = ['#FF9999', '#66B2FF', '#99FF99']

for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Adding title and labels
plt.title('Monthly Sales Distribution\nof Top Gaming Consoles - Last Year', fontsize=16, fontweight='bold')
plt.xlabel('Monthly Sales (thousands of units)', fontsize=14)
plt.ylabel('Gaming Consoles', fontsize=14)

# Annotating significant observations
plt.annotate('High Demand', xy=(53, 1), xytext=(60, 1),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
plt.annotate('Steady Sales', xy=(35, 2), xytext=(40, 2.5),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
plt.annotate('Growth Trend', xy=(38, 3), xytext=(45, 3),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Adding grid for readability
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Automatically adjust layout for readability and to prevent overlap
plt.tight_layout()

# Display plot
plt.show()