import matplotlib.pyplot as plt
import numpy as np

# Define the years for the projections
years = np.arange(2020, 2031)

# Budget projections for each mission type (in Billion USD)
lunar_budget = np.array([1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5])
mars_budget = np.array([2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0])
asteroid_budget = np.array([1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0])
deep_space_budget = np.array([2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5])

# Budget variability (standard deviation) due to uncertainties
lunar_variability = np.array([0.2] * 11)
mars_variability = np.array([0.25] * 11)
asteroid_variability = np.array([0.15] * 11)
deep_space_variability = np.array([0.3] * 11)

# Cumulative budget for the bar chart
total_lunar = lunar_budget.sum()
total_mars = mars_budget.sum()
total_asteroid = asteroid_budget.sum()
total_deep_space = deep_space_budget.sum()

# Setting up the figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# Plotting the line chart with error bars in the first subplot
axes[0].errorbar(years, lunar_budget, yerr=lunar_variability, fmt='-o', label='Lunar Missions',
                 capsize=4, color='grey', alpha=0.8)
axes[0].errorbar(years, mars_budget, yerr=mars_variability, fmt='-s', label='Mars Missions',
                 capsize=4, color='tomato', alpha=0.8)
axes[0].errorbar(years, asteroid_budget, yerr=asteroid_variability, fmt='-^', label='Asteroid Exploration',
                 capsize=4, color='skyblue', alpha=0.8)
axes[0].errorbar(years, deep_space_budget, yerr=deep_space_variability, fmt='-D', label='Deep Space Probes',
                 capsize=4, color='forestgreen', alpha=0.8)

# Adding titles and labels to the line chart
axes[0].set_title('Space Exploration Budget Projections with Variability\n(2020-2030)', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Year', fontsize=12)
axes[0].set_ylabel('Budget (Billion USD)', fontsize=12)
axes[0].legend(loc='upper left', fontsize=10, frameon=False)
axes[0].grid(alpha=0.3, linestyle='--', linewidth=0.7)
axes[0].tick_params(axis='x', rotation=45)

# Plotting the bar chart in the second subplot
categories = ['Lunar', 'Mars', 'Asteroid', 'Deep Space']
totals = [total_lunar, total_mars, total_asteroid, total_deep_space]
colors = ['grey', 'tomato', 'skyblue', 'forestgreen']

axes[1].bar(categories, totals, color=colors, alpha=0.8)
axes[1].set_title('Total Budget Allocation by Mission Type\n(2020-2030)', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Mission Type', fontsize=12)
axes[1].set_ylabel('Total Budget (Billion USD)', fontsize=12)

# Adding text labels above the bars
for i, total in enumerate(totals):
    axes[1].text(i, total + 0.2, f'{total:.1f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Adjust layout to ensure no overlap and consistent appearance
plt.tight_layout()

# Display the plots
plt.show()