import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2013, 2023)

# Plant-based food sales data (in millions of dollars)
meat_substitutes_sales = [200, 220, 245, 280, 310, 340, 390, 450, 500, 550]
dairy_alternatives_sales = [150, 160, 175, 200, 230, 270, 300, 350, 400, 450]
plant_snacks_sales = [50, 55, 60, 75, 85, 95, 115, 130, 150, 170]

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot lines for each category
ax.plot(years, meat_substitutes_sales, label='Meat Substitutes', marker='o', linestyle='-', linewidth=2, color='forestgreen')
ax.plot(years, dairy_alternatives_sales, label='Dairy Alternatives', marker='s', linestyle='-', linewidth=2, color='royalblue')
ax.plot(years, plant_snacks_sales, label='Plant-Based Snacks', marker='^', linestyle='-', linewidth=2, color='firebrick')

# Set chart title and labels
ax.set_title('The Evolution of Plant-Based Food Sales (2013-2022)', fontsize=16, pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Sales (Millions of Dollars)', fontsize=12)
ax.set_xticks(years)
ax.set_ylim(0, 600)
ax.set_xlim(2012, 2023)

# Add gridlines
ax.grid(True, linestyle='--', alpha=0.5)

# Add legend
ax.legend(title='Product Categories', loc='upper left')

# Annotate significant trends
ax.annotate('Rapid Growth in Meat Substitutes', xy=(2020, 450), xytext=(2016, 500),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
ax.annotate('Emerging Popularity of Snacks', xy=(2019, 130), xytext=(2015, 200),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()