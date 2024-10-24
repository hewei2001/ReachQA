import matplotlib.pyplot as plt
import numpy as np

# Define the age groups and smartphone adoption rates
age_groups = ['18-24', '25-34', '35-44', '45-54', '55+']
adoption_data = np.array([
    [85, 75, 65, 55, 30],  # 2019
    [87, 78, 68, 57, 35],  # 2020
    [90, 82, 70, 60, 40],  # 2021
    [92, 85, 73, 62, 45],  # 2022
    [95, 88, 75, 65, 50],  # 2023
])

# Define years for x-axis
years = np.array([2019, 2020, 2021, 2022, 2023])

# Set up the plot
plt.figure(figsize=(12, 8))

# Create area plots for each age group
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
for i, age_group in enumerate(age_groups):
    plt.fill_between(years, adoption_data[:, i], color=colors[i], alpha=0.2)
    plt.plot(years, adoption_data[:, i], marker='o', label=age_group, 
             linestyle='-', linewidth=2, color=colors[i])

    # Annotate each data point with percentage and increase from previous year
    for year_idx, year in enumerate(years):
        if year_idx > 0:
            increase = adoption_data[year_idx, i] - adoption_data[year_idx - 1, i]
            plt.annotate(f"{adoption_data[year_idx, i]}%\n(+{increase}%)", 
                         (year, adoption_data[year_idx, i]), 
                         textcoords="offset points", 
                         xytext=(0, 10), 
                         ha='center', fontsize=9)

# Add titles and labels
plt.title("Evolution of Smartphone Adoption Rates\nby Age Group (2019-2023)", 
          fontsize=16, fontweight='bold', loc='center', pad=20)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Smartphone Adoption Rate (%)", fontsize=14)
plt.xticks(years)
plt.yticks(np.arange(0, 101, 10))
plt.ylim(0, 100)

# Add grid
plt.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Add legend with a semi-transparent background
plt.legend(title="Age Groups", loc='lower right', fontsize=10, framealpha=0.7)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()