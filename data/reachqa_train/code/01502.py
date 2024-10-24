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

# Extract the country labels and corresponding data
country_labels = list(renewable_share.keys())
data = np.array(list(renewable_share.values()))

# Initialize the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Assign colors for better differentiation
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

# Plot stacked area chart
ax.stackplot(years, data, labels=country_labels, colors=colors, alpha=0.8)

# Title and labels
ax.set_title("Global Transition to Renewable Energy:\nShare of Total Energy Consumption (2015-2025)",
             fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Renewable Energy Share (%)", fontsize=12)

# Add a legend to the plot
ax.legend(title="Countries", loc='upper left', bbox_to_anchor=(1, 1), fontsize='small')

# Add gridlines to improve readability
ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Rotate x-tick labels for better visibility
plt.xticks(years, rotation=45)

# Automatically adjust layout for clarity and fit
plt.tight_layout()

# Show the plot
plt.show()