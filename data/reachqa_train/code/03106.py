import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2025
years = np.arange(2010, 2026)

# Renewable energy consumption in terawatt-hours (TWh) for each country
# The data reflects an upward trend with different growth patterns
country_a_consumption = [50, 55, 61, 68, 76, 85, 95, 106, 118, 131, 145, 160, 176, 193, 211, 230]
country_b_consumption = [40, 45, 51, 58, 66, 75, 85, 96, 108, 121, 135, 150, 166, 183, 201, 220]
country_c_consumption = [30, 33, 37, 42, 48, 55, 63, 72, 82, 93, 105, 118, 132, 147, 163, 180]
country_d_consumption = [60, 65, 71, 78, 86, 95, 105, 116, 128, 141, 155, 170, 186, 203, 221, 240]
country_e_consumption = [20, 24, 29, 35, 42, 50, 59, 69, 80, 92, 105, 119, 134, 150, 167, 185]

# Plot the data
plt.figure(figsize=(14, 8))

plt.plot(years, country_a_consumption, label='Country A', color='#1f77b4', marker='o', linewidth=2)
plt.plot(years, country_b_consumption, label='Country B', color='#ff7f0e', marker='^', linewidth=2, linestyle='--')
plt.plot(years, country_c_consumption, label='Country C', color='#2ca02c', marker='s', linewidth=2, linestyle='-.')
plt.plot(years, country_d_consumption, label='Country D', color='#d62728', marker='x', linewidth=2, linestyle=':')
plt.plot(years, country_e_consumption, label='Country E', color='#9467bd', marker='d', linewidth=2)

# Titles and labels
plt.title('Renewable Energy Revolution:\nA Global Perspective (2010-2025)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Energy Consumption (TWh)', fontsize=12)

# Legend and grid
plt.legend(loc='upper left', title='Countries', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)

# Customize ticks
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 261, 20))

# Highlight significant trends
plt.axvline(x=2020, color='gray', linestyle='--', linewidth=0.8, label='Pandemic Year')

# Annotate notable events
plt.annotate('Policy Shift', xy=(2015, country_a_consumption[5]), xytext=(2013, 100),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Adjust layout for clarity
plt.tight_layout()

# Show the plot
plt.show()