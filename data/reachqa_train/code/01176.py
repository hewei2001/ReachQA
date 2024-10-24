import matplotlib.pyplot as plt
import numpy as np

# Define quarters over the next two years
quarters = np.array([
    'Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024',
    'Q1 2025', 'Q2 2025', 'Q3 2025', 'Q4 2025'
])

# Projected revenues in millions of dollars
projected_revenues = np.array([150, 160, 170, 180, 192, 205, 215, 230])

# Error margins (confidence intervals) for each quarter
errors = np.array([5, 6, 8, 10, 9, 11, 12, 15])

# Calculate quarterly revenue growth rates (as percentage)
growth_rates = np.array([(projected_revenues[i] - projected_revenues[i-1]) / projected_revenues[i-1] * 100 
                         for i in range(1, len(projected_revenues))])

# Initialize the plot with two subplots
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Subplot 1: Line chart with error bars
ax[0].errorbar(quarters, projected_revenues, yerr=errors, fmt='-o', ecolor='gray', capsize=5, elinewidth=2, markeredgewidth=2, color='#1f77b4', label='Projected Revenue')
ax[0].set_title('Quarterly Revenue Forecast\nwith Confidence Intervals in the Tech Industry', fontsize=14)
ax[0].set_xlabel('Quarter', fontsize=12)
ax[0].set_ylabel('Revenue (Million $)', fontsize=12)
ax[0].set_xticks(quarters)
ax[0].set_xticklabels(quarters, rotation=45, ha='right')
ax[0].grid(True, linestyle='--', alpha=0.5)
ax[0].legend(loc='upper left', fontsize=10)
ax[0].annotate('Projected Peak', xy=('Q4 2025', 230), xytext=('Q2 2025', 240), arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')

# Subplot 2: Bar chart for growth rates
growth_quarters = quarters[1:]  # Excluding the first quarter for growth rate comparison
ax[1].bar(growth_quarters, growth_rates, color='#ff7f0e', alpha=0.7, label='Growth Rate (%)')
ax[1].set_title('Quarterly Revenue Growth Rates', fontsize=14)
ax[1].set_xlabel('Quarter', fontsize=12)
ax[1].set_ylabel('Growth Rate (%)', fontsize=12)
ax[1].set_xticks(growth_quarters)
ax[1].set_xticklabels(growth_quarters, rotation=45, ha='right')
ax[1].axhline(0, color='grey', linewidth=0.8)
ax[1].grid(True, linestyle='--', alpha=0.5)
ax[1].legend(loc='upper left', fontsize=10)
for i, v in enumerate(growth_rates):
    ax[1].text(i, v + 0.5, f"{v:.1f}%", ha='center', va='bottom', fontsize=9)

# Adjust layout to ensure everything fits well
plt.tight_layout()
plt.show()