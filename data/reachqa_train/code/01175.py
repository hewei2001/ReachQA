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

# Initialize the plot
plt.figure(figsize=(12, 6))

# Plotting the line chart with error bars
plt.errorbar(
    quarters, projected_revenues, yerr=errors, fmt='-o',
    ecolor='gray', capsize=5, elinewidth=2, markeredgewidth=2,
    color='#1f77b4', label='Projected Revenue'
)

# Add title and labels
plt.title('Quarterly Revenue Forecast with Confidence Intervals\nin the Tech Industry', fontsize=16)
plt.xlabel('Quarter', fontsize=12)
plt.ylabel('Revenue (Million $)', fontsize=12)

# Customize x-ticks and rotation for clarity
plt.xticks(rotation=45)

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.5)

# Add legend
plt.legend(loc='upper left', fontsize=10)

# Adding annotation for significant revenue change
plt.annotate('Projected Peak', xy=('Q4 2025', 230), xytext=('Q2 2025', 240),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')

# Ensure the layout fits well without overlap
plt.tight_layout()

# Show plot
plt.show()