import numpy as np
import matplotlib.pyplot as plt

# Define the years and industries
years = np.array([2018, 2019, 2020, 2021, 2022, 2023])
industries = ["Technology", "Healthcare", "Education", "Finance", "Retail"]

# Define remote work adoption rates (in percentage) for each industry over the years
adoption_rates = np.array([
    [20, 30, 50, 65, 70, 75],  # Technology
    [5, 10, 20, 30, 40, 50],   # Healthcare
    [10, 15, 30, 45, 55, 65],  # Education
    [15, 20, 35, 50, 60, 70],  # Finance
    [8, 12, 25, 35, 45, 55]    # Retail
])

# Setup the figure and axes for the line chart
fig, ax = plt.subplots(figsize=(14, 8))

# Define color palette for the lines
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF']

# Plotting each industry's data as a line in the chart
for idx, industry in enumerate(industries):
    ax.plot(years, adoption_rates[idx], marker='o', linestyle='-', linewidth=2, color=colors[idx], label=industry)

    # Annotate data points with the adoption rates
    for x, y in zip(years, adoption_rates[idx]):
        ax.annotate(f'{y}%', xy=(x, y), xytext=(0, 5), textcoords='offset points', fontsize=9, color=colors[idx],
                    ha='center')

# Adding the title and labels
ax.set_title('Digital Nomads: Remote Work Adoption Rates\nAcross Industries (2018-2023)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Adoption Rate (%)', fontsize=12)
ax.set_xticks(years)
ax.set_xticklabels(years)

# Adding the legend to identify the industries
ax.legend(title='Industries', loc='upper left', fontsize=10, frameon=True)

# Adding a grid for better readability
ax.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Optimize layout to ensure nothing is clipped
plt.tight_layout()

# Display the plot
plt.show()