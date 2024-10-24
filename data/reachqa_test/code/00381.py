import matplotlib.pyplot as plt
import numpy as np

# Define the countries
countries = ['Germany', 'France', 'UK', 'Italy', 'Spain', 'Poland', 'Sweden', 'Norway', 'Denmark', 'Netherlands']

# Define the average annual household spending on eco-friendly products
spending = np.array([850, 750, 900, 650, 700, 550, 800, 950, 600, 750])

# Define the percentage increase in spending from the previous year
increase_percentages = [10, 8, 12, 5, 7, 3, 11, 15, 4, 9]

# Define the population (in millions) of each country
population = np.array([83, 67, 67, 60, 46, 38, 10, 5, 6, 17])

# Calculate the total annual household spending on eco-friendly products in each country
total_spending = spending * population

# Create the figure and axis
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), gridspec_kw={'width_ratios': [4, 3]})

# Plot the bar chart
bar_positions = np.arange(len(spending))
bar_width = 0.8
ax1.bar(bar_positions, spending, width=bar_width, color='skyblue')
ax1.set_title("Average Annual Household Spending on Eco-Friendly Products\nin European Countries (€)", fontsize=14)
ax1.set_xticks(bar_positions)
ax1.set_xticklabels(countries, rotation=45, ha='right')
ax1.set_ylabel('Average Spending (€)')
ax1.grid(axis='y', linestyle='--')
for i, (spend, increase) in enumerate(zip(spending, increase_percentages)):
    ax1.text(bar_positions[i], spend + 20, f"€{spend}\n(+{increase}%)", ha='center', va='bottom')

# Plot the line chart
ax2.plot(countries, total_spending, marker='o', linestyle='-', color='coral', label='Country Spending')
ax2.axhline(y=np.mean(total_spending), color='green', linestyle='--', label='European Average')
ax2.set_title("Total Annual Household Spending on Eco-Friendly Products\nin European Countries", fontsize=14)
ax2.set_xlabel('Country')
ax2.set_ylabel('Total Spending (€ million)')
ax2.legend()
ax2.grid(axis='y', linestyle='--')
ax2.set_xticklabels(countries, rotation=45, ha='right')

# Automatically adjust layout to avoid occlusion
fig.tight_layout()

# Show the plot
plt.show()