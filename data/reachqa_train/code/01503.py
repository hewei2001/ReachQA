import matplotlib.pyplot as plt
import numpy as np

# Define the years for the dataset
years = np.arange(2015, 2026)

# Define the percentage of renewable energy share for each country
renewable_share = {
    "Country A": [15, 18, 22, 28, 35, 40, 45, 50, 58, 60, 65],
    "Country B": [10, 12, 15, 20, 25, 30, 35, 40, 45, 48, 50],
    "Country C": [8, 10, 12, 16, 22, 28, 33, 38, 43, 47, 50],
    "Country D": [5, 7, 10, 15, 20, 25, 30, 35, 40, 45, 48],
    "Country E": [3, 5, 8, 12, 18, 24, 29, 34, 39, 42, 45],
}

# Define a new dataset for cumulative renewable energy growth rates
growth_rates = {
    "Country A": np.diff(renewable_share["Country A"], prepend=0),
    "Country B": np.diff(renewable_share["Country B"], prepend=0),
    "Country C": np.diff(renewable_share["Country C"], prepend=0),
    "Country D": np.diff(renewable_share["Country D"], prepend=0),
    "Country E": np.diff(renewable_share["Country E"], prepend=0),
}

# Extract labels and data arrays
country_labels = list(renewable_share.keys())
renewable_data = np.array(list(renewable_share.values()))
growth_data = np.array(list(growth_rates.values()))

# Initialize the subplot layout
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Colors for different countries
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Plot the stacked area chart
ax1.stackplot(years, renewable_data, labels=country_labels, colors=colors, alpha=0.8)
ax1.set_title("Global Transition to Renewable Energy:\nShare of Total Energy Consumption (2015-2025)",
              fontsize=14, weight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Renewable Energy Share (%)", fontsize=12)
ax1.legend(title="Countries", loc='upper left', bbox_to_anchor=(1, 1), fontsize='small')
ax1.xaxis.grid(True, linestyle='--', color='grey', alpha=0.7)
ax1.yaxis.grid(True, linestyle='--', color='grey', alpha=0.7)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

# Plot the line chart for growth rates
for i, country in enumerate(country_labels):
    ax2.plot(years, growth_data[i], label=country, color=colors[i], marker='o', linestyle='-', linewidth=2)

ax2.set_title("Annual Growth in Renewable Energy Share (2015-2025)", fontsize=14, weight='bold', pad=20)
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Annual Growth (%)", fontsize=12)
ax2.legend(title="Countries", loc='upper left', bbox_to_anchor=(1, 1), fontsize='small')
ax2.xaxis.grid(True, linestyle='--', color='grey', alpha=0.7)
ax2.yaxis.grid(True, linestyle='--', color='grey', alpha=0.7)
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45)

# Automatically adjust layout for clarity and fit
plt.tight_layout()

# Display the plot
plt.show()