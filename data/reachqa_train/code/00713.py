import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2013, 2023)

# Plant-based food sales data (in millions of dollars)
meat_substitutes_sales = [200, 220, 245, 280, 310, 340, 390, 450, 500, 550]
dairy_alternatives_sales = [150, 160, 175, 200, 230, 270, 300, 350, 400, 450]
plant_snacks_sales = [50, 55, 60, 75, 85, 95, 115, 130, 150, 170]
beverage_sales = [80, 85, 95, 105, 120, 145, 160, 190, 220, 250]  # New data

# Set up the figure and primary axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot lines for each category
ax1.plot(years, meat_substitutes_sales, label='Meat Substitutes', marker='o', linestyle='-', linewidth=2, color='forestgreen')
ax1.plot(years, dairy_alternatives_sales, label='Dairy Alternatives', marker='s', linestyle='-', linewidth=2, color='royalblue')
ax1.plot(years, plant_snacks_sales, label='Plant-Based Snacks', marker='^', linestyle='-', linewidth=2, color='firebrick')

# Create a secondary y-axis for the bar chart
ax2 = ax1.twinx()
ax2.bar(years, beverage_sales, label='Beverage Sales', width=0.5, alpha=0.6, color='darkorange')

# Set chart titles and labels
ax1.set_title('Evolution of Plant-Based Food Sales & Beverage Trends\n(2013-2022)', fontsize=16, pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Sales (Millions of Dollars)', fontsize=12, color='dimgray')
ax2.set_ylabel('Beverage Sales (Millions of Dollars)', fontsize=12, color='dimgray')

ax1.set_xticks(years)
ax1.set_ylim(0, 600)
ax2.set_ylim(0, 300)
ax1.set_xlim(2012, 2023)

# Add gridlines
ax1.grid(True, linestyle='--', alpha=0.5)

# Add legends
lines_labels = ax1.get_legend_handles_labels()
bars_labels = ax2.get_legend_handles_labels()
ax1.legend(*lines_labels, title='Product Categories', loc='upper left')
ax2.legend(*bars_labels, loc='upper right')

# Annotate significant trends
ax1.annotate('Rapid Growth in Meat Substitutes', xy=(2020, 450), xytext=(2016, 500),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
ax1.annotate('Emerging Popularity of Snacks', xy=(2019, 130), xytext=(2015, 200),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Highlight regions of interest
ax1.axvspan(2013, 2015, color='lightgray', alpha=0.3)
ax1.text(2013.5, 550, 'Market Entry Phase', rotation=90, verticalalignment='center', color='gray', fontsize=10)

# Adjust layout to prevent overlapping
fig.tight_layout()

# Display the plot
plt.show()