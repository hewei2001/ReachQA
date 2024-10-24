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

# Define related productivity growth rates for each industry over the years
productivity_rates = np.array([
    [1.0, 2.0, 3.5, 4.5, 4.8, 5.0],  # Technology
    [0.5, 0.8, 1.2, 2.0, 2.5, 3.0],  # Healthcare
    [0.7, 1.0, 1.5, 2.3, 2.8, 3.4],  # Education
    [0.8, 1.1, 1.8, 2.6, 3.0, 3.6],  # Finance
    [0.6, 0.9, 1.3, 1.8, 2.2, 2.7]   # Retail
])

# Setup the figure and axes for the combined chart
fig, ax1 = plt.subplots(figsize=(14, 8))

# Define color palette for the lines
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF']

# Plotting each industry's data as a line in the chart
for idx, industry in enumerate(industries):
    ax1.plot(years, adoption_rates[idx], marker='o', linestyle='-', linewidth=2, color=colors[idx], label=industry)
    for x, y in zip(years, adoption_rates[idx]):
        ax1.annotate(f'{y}%', xy=(x, y), xytext=(0, 5), textcoords='offset points', fontsize=9, color=colors[idx], ha='center')

# Adding the title and labels
ax1.set_title('Digital Nomads: Remote Work Adoption Rates\nand Productivity Growth Across Industries (2018-2023)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Adoption Rate (%)', fontsize=12)
ax1.set_xticks(years)
ax1.set_xticklabels(years)

# Adding a second y-axis for productivity rates
ax2 = ax1.twinx()
ax2.set_ylabel('Productivity Growth (in index)', fontsize=12)
for idx, industry in enumerate(industries):
    ax2.bar(years + idx*0.15, productivity_rates[idx], width=0.1, color=colors[idx], alpha=0.3, label=f"{industry} Productivity" if idx == 0 else "")

# Combine legends for both line and bar plots
lines, labels = ax1.get_legend_handles_labels()
bars, bar_labels = ax2.get_legend_handles_labels()
ax1.legend(lines + bars, labels + bar_labels, title='Industries and Productivity', loc='upper left', fontsize=10, frameon=True)

# Adding a grid for better readability
ax1.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Optimize layout to ensure nothing is clipped
plt.tight_layout()

# Display the plot
plt.show()