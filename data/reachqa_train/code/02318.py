import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2022
years = np.arange(2010, 2023)

# Adoption rate data for each programming language (in percentage)
python = [30, 33, 36, 40, 45, 50, 55, 60, 65, 70, 75, 78, 80]
r = [25, 28, 30, 35, 36, 38, 40, 42, 43, 45, 46, 47, 48]
julia = [0, 0, 2, 4, 6, 8, 12, 15, 18, 22, 26, 30, 35]
java = [20, 22, 24, 26, 27, 28, 27, 26, 25, 24, 23, 22, 20]
cpp = [25, 22, 20, 18, 16, 14, 12, 11, 10, 9, 8, 7, 6]

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot line charts for each programming language
ax.plot(years, python, marker='o', linestyle='-', linewidth=2, label='Python', color='#1f77b4')
ax.plot(years, r, marker='s', linestyle='--', linewidth=2, label='R', color='#ff7f0e')
ax.plot(years, julia, marker='^', linestyle='-.', linewidth=2, label='Julia', color='#2ca02c')
ax.plot(years, java, marker='d', linestyle=':', linewidth=2, label='Java', color='#d62728')
ax.plot(years, cpp, marker='x', linestyle='-', linewidth=2, label='C++', color='#9467bd')

# Title and labels
ax.set_title('Rise of AI Programming Languages: 2010-2022\nTrends in Adoption Rates', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Adoption Rate (%)', fontsize=14)

# Legend and grid
ax.legend(title='Programming Language', fontsize=12, loc='upper left', frameon=True)
ax.grid(True, linestyle='--', alpha=0.6)

# Customizing ticks
ax.set_xticks(years)
ax.tick_params(axis='x', rotation=45)

# Automatically adjust layout
plt.tight_layout()

# Show plot
plt.show()