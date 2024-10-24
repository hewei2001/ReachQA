import matplotlib.pyplot as plt
import numpy as np

# Expanded time range for the x-axis
years = np.arange(2000, 2025)

# Simulated visitor numbers for five cultural heritage sites with non-linear trends and more data groups
site_A_visitors = np.array([140000 + 10000*np.sin(0.2*y) + 1000*y for y in range(len(years))])
site_B_visitors = np.array([200000 + 15000*np.cos(0.15*y) + 1500*y for y in range(len(years))])
site_C_visitors = np.array([80000 + 5000*np.sin(0.25*y + np.pi/4) + 800*y for y in range(len(years))])
site_D_visitors = np.array([40000 + 7000*np.cos(0.1*y) + 500*y for y in range(len(years))])
site_E_visitors = np.array([120000 + 12000*np.sin(0.18*y + np.pi/6) + 1200*y for y in range(len(years))])

# Additional sites
site_F_visitors = np.array([180000 + 13000*np.sin(0.22*y + np.pi/3) + 900*y for y in range(len(years))])
site_G_visitors = np.array([100000 + 6000*np.cos(0.2*y + np.pi/5) + 700*y for y in range(len(years))])

# Corresponding errors
site_A_error = np.array([4000 + 100*np.sin(0.3*y) for y in range(len(years))])
site_B_error = np.array([7000 + 150*np.cos(0.25*y) for y in range(len(years))])
site_C_error = np.array([2500 + 50*np.sin(0.35*y) for y in range(len(years))])
site_D_error = np.array([1500 + 30*np.cos(0.2*y) for y in range(len(years))])
site_E_error = np.array([5000 + 100*np.sin(0.28*y) for y in range(len(years))])
site_F_error = np.array([6000 + 120*np.cos(0.24*y) for y in range(len(years))])
site_G_error = np.array([3000 + 60*np.sin(0.31*y) for y in range(len(years))])

# Plotting the line chart with error bars
plt.figure(figsize=(14, 8))

# Plotting each site with distinct colors and markers
plt.errorbar(years, site_A_visitors, yerr=site_A_error, label='Site A', fmt='o-', capsize=4, color='#1f77b4', alpha=0.8)
plt.errorbar(years, site_B_visitors, yerr=site_B_error, label='Site B', fmt='s-', capsize=4, color='#ff7f0e', alpha=0.8)
plt.errorbar(years, site_C_visitors, yerr=site_C_error, label='Site C', fmt='^-', capsize=4, color='#2ca02c', alpha=0.8)
plt.errorbar(years, site_D_visitors, yerr=site_D_error, label='Site D', fmt='*-', capsize=4, color='#d62728', alpha=0.8)
plt.errorbar(years, site_E_visitors, yerr=site_E_error, label='Site E', fmt='d-', capsize=4, color='#9467bd', alpha=0.8)
plt.errorbar(years, site_F_visitors, yerr=site_F_error, label='Site F', fmt='x-', capsize=4, color='#8c564b', alpha=0.8)
plt.errorbar(years, site_G_visitors, yerr=site_G_error, label='Site G', fmt='h-', capsize=4, color='#e377c2', alpha=0.8)

# Title and labels
plt.title('Cultural Heritage Site Visitor Trends\n2000-2024', fontsize=16, weight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Annual Visitors', fontsize=12)

# Adding legend
plt.legend(title='Heritage Sites', loc='upper left', fontsize=9)

# Customize grid
plt.grid(True, linestyle='--', alpha=0.6)

# Set y-axis limits to show all data comfortably
plt.ylim(0, 300000)

# Adding a trend line for one of the sites for a higher-level analysis
z = np.polyfit(years, site_A_visitors, 2)
p = np.poly1d(z)
plt.plot(years, p(years), "--", color="#1f77b4", linewidth=1.5, alpha=0.6, label="Trend Line Site A")

# Automatically adjust layout for better fit
plt.tight_layout()

# Display the plot
plt.show()