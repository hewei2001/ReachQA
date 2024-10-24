import matplotlib.pyplot as plt
import numpy as np

# Years from 2013 to 2022
years = np.arange(2013, 2023)

# Data: Number of residential solar installations (in thousands)
san_francisco = [10, 13, 17, 22, 29, 37, 46, 58, 72, 90]
austin = [8, 12, 16, 21, 26, 33, 41, 52, 66, 83]
munich = [5, 8, 11, 16, 22, 29, 38, 49, 62, 77]
bangalore = [7, 10, 14, 19, 25, 33, 42, 54, 68, 85]
tokyo = [9, 14, 19, 25, 32, 41, 52, 66, 83, 102]

# Calculate percentage growth year-over-year for Tokyo
tokyo_growth = [((tokyo[i] - tokyo[i - 1]) / tokyo[i - 1]) * 100 if i != 0 else 0 for i in range(len(tokyo))]

# Create a subplot structure
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(18, 8))

# Line Plot for Number of Installations
axs[0].plot(years, san_francisco, marker='o', linestyle='-', linewidth=2, label='San Francisco', color='#1f77b4')
axs[0].plot(years, austin, marker='s', linestyle='--', linewidth=2, label='Austin', color='#ff7f0e')
axs[0].plot(years, munich, marker='^', linestyle='-.', linewidth=2, label='Munich', color='#2ca02c')
axs[0].plot(years, bangalore, marker='d', linestyle=':', linewidth=2, label='Bangalore', color='#d62728')
axs[0].plot(years, tokyo, marker='p', linestyle='-', linewidth=2, label='Tokyo', color='#9467bd')

# Title and Labels
axs[0].set_title('Growth of Residential Solar Installations\n(2013-2022)', fontsize=16, fontweight='bold')
axs[0].set_xlabel('Year', fontsize=14)
axs[0].set_ylabel('Number of Installations (Thousands)', fontsize=14)
axs[0].legend(title='City', fontsize=12, loc='upper left', frameon=True)
axs[0].grid(True, linestyle='--', alpha=0.6)
axs[0].set_xticks(years)
axs[0].tick_params(axis='x', rotation=45)

# Bar Chart for Year-over-Year Growth for Tokyo
axs[1].bar(years, tokyo_growth, color='#9467bd', alpha=0.7)
axs[1].set_title('Year-over-Year Growth for Tokyo\nResidential Solar Installations', fontsize=16, fontweight='bold')
axs[1].set_xlabel('Year', fontsize=14)
axs[1].set_ylabel('Growth Rate (%)', fontsize=14)
axs[1].grid(True, linestyle='--', alpha=0.6)
axs[1].set_xticks(years)
axs[1].tick_params(axis='x', rotation=45)

# Tight layout to ensure no overlap
plt.tight_layout()

# Display the plots
plt.show()