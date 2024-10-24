import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Introduction years of space tour packages
introduction_years = np.array([2030, 2032, 2035, 2038, 2040, 2042, 2044, 2046, 2048, 2050])

# Sales figures in thousands (hypothetical growth data)
sales_figures = np.array([12, 18, 30, 50, 72, 95, 125, 160, 210, 260])

# Hypothetical data: Number of companies entering space tourism market
companies_entering = np.array([1, 2, 3, 4, 5, 7, 9, 12, 15, 18])

# Define an exponential growth function for fitting the data
def exponential_growth(x, a, b, c):
    return a * np.exp(b * (x - 2030)) + c

# Fit the exponential curve to the data
params, _ = curve_fit(exponential_growth, introduction_years, sales_figures)

# Generate years for a smooth curve
years_fit = np.linspace(2030, 2050, 100)
sales_fit = exponential_growth(years_fit, *params)

# Create the scatter plot and smooth fitting line
fig, ax1 = plt.subplots(figsize=(12, 7))

# Scatter plot for actual data points
ax1.scatter(introduction_years, sales_figures, color='indianred', s=100, edgecolor='black', label='Actual Sales Data')

# Smooth fitting line
ax1.plot(years_fit, sales_fit, color='navy', linestyle='-', linewidth=2, label='Exponential Growth Fit')

# Add labels, title, and legend
ax1.set_xlabel('Year of Package Introduction', fontsize=12)
ax1.set_ylabel('Sales in Thousands', fontsize=12)
ax1.set_title('Stellar Sales:\nThe Trajectory of Space Tourism Packages', fontsize=16, fontweight='bold', pad=20)
ax1.legend(loc='upper left', fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.set_xlim(2029, 2051)
ax1.set_ylim(0, 300)

# Secondary axis for the number of companies
ax2 = ax1.twinx()
ax2.bar(introduction_years, companies_entering, color='skyblue', width=0.6, alpha=0.6, label='Companies Entering')

# Add label and legend for the secondary axis
ax2.set_ylabel('Number of Companies', fontsize=12)
ax2.legend(loc='upper right', fontsize=10)

# Ensure layout is adjusted properly
plt.tight_layout()

# Show the final plot
plt.show()