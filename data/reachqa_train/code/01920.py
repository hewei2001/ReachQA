import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

# Data
years = np.arange(2014, 2024)
north_america = [5, 8, 12, 18, 26, 35, 47, 60, 74, 90]
europe = [4, 7, 11, 17, 25, 34, 44, 55, 68, 83]
asia = [6, 10, 15, 23, 33, 45, 58, 72, 87, 105]
latin_america = [1, 3, 5, 8, 12, 17, 23, 30, 38, 47]
africa = [0.5, 1, 2, 4, 7, 11, 16, 22, 29, 37]

# Plot setup
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each region with enhanced styles
ax.plot(years, north_america, label='North America', marker='o', linestyle='-', linewidth=2, color='#1f77b4', alpha=0.8)
ax.plot(years, europe, label='Europe', marker='s', linestyle='--', linewidth=2, color='#ff7f0e', alpha=0.8)
ax.plot(years, asia, label='Asia', marker='^', linestyle='-', linewidth=2, color='#2ca02c', alpha=0.8)
ax.plot(years, latin_america, label='Latin America', marker='D', linestyle=':', linewidth=2, color='#d62728', alpha=0.8)
ax.plot(years, africa, label='Africa', marker='x', linestyle='-.', linewidth=2, color='#9467bd', alpha=0.8)

# Title and labels
plt.title('Decade of Connectivity: Growth of High-Speed Internet Users\n(2014-2023)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Users with Gbps Internet (Millions)', fontsize=12)

# Highlight annotations for specific points
max_yr_na = max(north_america)
ax.annotate(f'Max: {max_yr_na}', xy=(2023, max_yr_na), xytext=(2021, max_yr_na+10),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Legend and Grid
plt.legend(title='Region', loc='upper left', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)

# Improved axis ticks
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.set_yticks(np.arange(0, 120, 10))

# Highlight significant years
for year in [2016, 2020]:
    ax.axvline(x=year, color='gray', linestyle='--', linewidth=0.8, alpha=0.5)

# Background for every 5 years
ax.axvspan(2014, 2015, color='yellow', alpha=0.1)
ax.axvspan(2019, 2020, color='yellow', alpha=0.1)

# Adjust layout for clarity
plt.xticks(years, rotation=45)
plt.tight_layout()

# Show the plot
plt.show()