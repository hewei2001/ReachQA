import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2020
years = np.arange(2010, 2021)

# Renewable energy consumption (in exajoules) for each sector
residential_consumption = [2, 2.5, 3, 3.5, 4, 4.5, 5, 5.8, 6.5, 7.5, 8]
industrial_consumption = [1, 1.5, 2, 2.8, 3.5, 4.2, 5.1, 6, 7.2, 8.6, 9.5]
transportation_consumption = [0.5, 0.6, 0.8, 1, 1.5, 2, 2.8, 3.5, 4.5, 5.7, 7]

# Cumulative consumption data for stacked plotting
consumptions = np.vstack([residential_consumption, industrial_consumption, transportation_consumption])

# Total renewable energy production (related data, in exajoules)
total_production = [3, 4, 5.2, 6.3, 8, 9.5, 11.5, 14, 16.5, 19.8, 24]

# Set up the plot
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plotting the stacked area chart
ax1.stackplot(years, consumptions, labels=['Residential', 'Industrial', 'Transportation'],
              colors=['#ff9999', '#66b3ff', '#99ff99'], alpha=0.7)

# Primary Y-Axis labels
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Energy Consumption (Exajoules)", fontsize=12)

# Titles
plt.title("The Rise of Renewable Energy\nConsumption and Production (2010-2020)",
          fontsize=16, fontweight='bold', pad=20)

# Adding a legend
ax1.legend(loc='upper left', title="Sectors")

# Customizing grid and style
ax1.grid(linestyle='--', linewidth=0.5, alpha=0.7)

# Annotations for significant trends in consumption
ax1.annotate('Residential solar growth', xy=(2019, 16), xytext=(2016, 17),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkred')

ax1.annotate('Electric vehicles boom', xy=(2020, 22.5), xytext=(2018, 20.5),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='green')

# Rotating x-axis labels for better readability
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

# Secondary axis for the overlay plot
ax2 = ax1.twinx()
ax2.plot(years, total_production, color='orange', marker='o', linestyle='-', linewidth=2,
         label='Total Renewable Production')
ax2.set_ylabel("Energy Production (Exajoules)", fontsize=12, color='orange')

# Annotating the overlay line plot
ax2.annotate('Production milestones', xy=(2020, 24), xytext=(2017, 23),
             arrowprops=dict(facecolor='orange', arrowstyle='->'), fontsize=10, color='orange')

# Adding a legend for the overlay plot
ax2.legend(loc='upper right', title="Production")

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()