import matplotlib.pyplot as plt
import numpy as np

# Years for the x-axis
years = np.arange(2010, 2020)

# Average annual visitor numbers for five cultural heritage sites
site_A_visitors = np.array([150000, 153000, 157000, 160000, 165000, 170000, 175000, 180000, 185000, 190000])
site_B_visitors = np.array([220000, 225000, 230000, 235000, 240000, 245000, 250000, 255000, 260000, 265000])
site_C_visitors = np.array([90000, 92000, 95000, 98000, 101000, 105000, 109000, 113000, 117000, 120000])
site_D_visitors = np.array([50000, 52000, 54000, 56000, 58000, 60000, 62000, 64000, 66000, 68000])
site_E_visitors = np.array([130000, 135000, 140000, 145000, 150000, 155000, 160000, 165000, 170000, 175000])

# Errors corresponding to each site's data, representing the uncertainty in records
site_A_error = np.array([5000, 4800, 4700, 4500, 4700, 5000, 5200, 5000, 4900, 5100])
site_B_error = np.array([8000, 8200, 8500, 8700, 9000, 9200, 9400, 9600, 9800, 10000])
site_C_error = np.array([3000, 3200, 3500, 3600, 3800, 4000, 4200, 4300, 4500, 4600])
site_D_error = np.array([2000, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000])
site_E_error = np.array([6000, 6200, 6400, 6600, 6800, 7000, 7200, 7400, 7600, 7800])

# Plotting the line chart with error bars
plt.figure(figsize=(12, 7))

# Plotting each site with distinct colors and markers
plt.errorbar(years, site_A_visitors, yerr=site_A_error, label='Site A', fmt='o-', capsize=5, color='#1f77b4', alpha=0.8)
plt.errorbar(years, site_B_visitors, yerr=site_B_error, label='Site B', fmt='s-', capsize=5, color='#ff7f0e', alpha=0.8)
plt.errorbar(years, site_C_visitors, yerr=site_C_error, label='Site C', fmt='^-', capsize=5, color='#2ca02c', alpha=0.8)
plt.errorbar(years, site_D_visitors, yerr=site_D_error, label='Site D', fmt='*-', capsize=5, color='#d62728', alpha=0.8)
plt.errorbar(years, site_E_visitors, yerr=site_E_error, label='Site E', fmt='d-', capsize=5, color='#9467bd', alpha=0.8)

# Title and labels
plt.title('Cultural Heritage Site Visitor Trends\n2010-2019', fontsize=16, weight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Annual Visitors', fontsize=12)

# Adding legend
plt.legend(title='Heritage Sites', loc='upper left', fontsize=10)

# Customize grid
plt.grid(True, linestyle='--', alpha=0.7)

# Set y-axis limits
plt.ylim(40000, 280000)

# Automatically adjust layout for better fit
plt.tight_layout()

# Display the plot
plt.show()