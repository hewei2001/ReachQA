import numpy as np
import matplotlib.pyplot as plt

# Define the years
years = np.arange(2015, 2026)

# Average internet speeds (in Gbps)
neon_metropolis_speeds = [0.5, 0.8, 1.2, 1.8, 2.5, 3.5, 4.8, 6.4, 8.5, 10.9, 13.5]
digi_heights_speeds = [0.6, 0.9, 1.3, 1.7, 2.1, 2.6, 3.1, 3.7, 4.4, 5.2, 6.1]
tech_valley_speeds = [0.3, 0.5, 0.7, 1.0, 1.4, 2.0, 3.2, 5.0, 7.5, 11.0, 15.5]

# Infrastructure investment (hypothetical values in billion $)
infrastructure_investment = [1.0, 1.2, 1.4, 1.6, 2.0, 2.4, 3.0, 3.5, 4.0, 4.5, 5.0]

# Initialize the plot
fig, ax1 = plt.subplots(figsize=(14, 8), dpi=100)
ax2 = ax1.twinx()  # Create a secondary y-axis

# Plot line chart for each city
ax1.plot(years, neon_metropolis_speeds, label='Neon Metropolis', marker='o', color='#1E90FF', linewidth=2)
ax1.plot(years, digi_heights_speeds, label='Digi Heights', marker='s', color='#32CD32', linewidth=2, linestyle='--')
ax1.plot(years, tech_valley_speeds, label='Tech Valley', marker='^', color='#FF4500', linewidth=2, linestyle='-.')

# Plot infrastructure investment on the secondary y-axis
ax2.bar(years, infrastructure_investment, alpha=0.3, color='gray', label='Infrastructure Investment ($B)', width=0.6)

# Title and labels
ax1.set_title("The Evolution of Urban Connectivity:\nInternet Speeds and Investment Trends (2015-2025)",
              fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Average Internet Speed (Gbps)', fontsize=12)
ax2.set_ylabel('Investment in Infrastructure ($B)', fontsize=12, color='gray')

# Customizing the x-axis
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

# Add grid for better readability
ax1.grid(True, linestyle='--', alpha=0.5)

# Customize legend
ax1.legend(loc='upper left', title='Cities', fontsize=10)
ax2.legend(loc='upper right', title='Economic Factors', fontsize=10)

# Highlight significant milestones with annotations
ax1.annotate('5G Introduction', xy=(2020, 2), xytext=(2017, 4),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, backgroundcolor='w')

# Automatically adjust the layout for better spacing
plt.tight_layout()

# Display the chart
plt.show()