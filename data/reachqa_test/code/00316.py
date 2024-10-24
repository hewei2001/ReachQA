import matplotlib.pyplot as plt
import numpy as np

# Years considered
years = np.arange(2015, 2026)

# Popularity scores for each fabric type with associated error (confidence interval)
cotton_popularity = np.array([60, 62, 63, 64, 66, 67, 65, 66, 67, 68, 69])
cotton_error = np.array([5, 4, 5, 3, 4, 5, 3, 4, 2, 3, 4])

wool_popularity = np.array([45, 47, 48, 50, 49, 51, 53, 52, 54, 55, 56])
wool_error = np.array([4, 3, 4, 4, 3, 4, 2, 3, 4, 3, 4])

silk_popularity = np.array([30, 32, 33, 35, 36, 37, 36, 38, 39, 40, 42])
silk_error = np.array([3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3])

linen_popularity = np.array([25, 27, 28, 29, 30, 31, 29, 30, 31, 32, 33])
linen_error = np.array([3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3])

# Calculate growth over the period
cotton_growth = cotton_popularity[-1] - cotton_popularity[0]
wool_growth = wool_popularity[-1] - wool_popularity[0]
silk_growth = silk_popularity[-1] - silk_popularity[0]
linen_growth = linen_popularity[-1] - linen_popularity[0]

growth = [cotton_growth, wool_growth, silk_growth, linen_growth]
fabrics = ['Cotton', 'Wool', 'Silk', 'Linen']
colors = ['teal', 'maroon', 'gold', 'peru']

# Create the subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

# Line chart with error bars
ax1.errorbar(years, cotton_popularity, yerr=cotton_error, label='Cotton', fmt='-o', capsize=5, color='teal', alpha=0.8)
ax1.errorbar(years, wool_popularity, yerr=wool_error, label='Wool', fmt='-s', capsize=5, color='maroon', alpha=0.8)
ax1.errorbar(years, silk_popularity, yerr=silk_error, label='Silk', fmt='-d', capsize=5, color='gold', alpha=0.8)
ax1.errorbar(years, linen_popularity, yerr=linen_error, label='Linen', fmt='-^', capsize=5, color='peru', alpha=0.8)

ax1.set_title("Trends in Fabric Popularity\nin the Fashion Industry (2015-2025)", fontsize=14, fontweight='bold')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Popularity Score", fontsize=12)
ax1.legend(title="Fabric Type", fontsize=10, title_fontsize='11', loc='upper left')
ax1.grid(linestyle='--', alpha=0.7)
ax1.set_xticks(years)
ax1.tick_params(axis='x', rotation=45)

# Bar chart for growth in popularity
ax2.bar(fabrics, growth, color=colors, alpha=0.7)
ax2.set_title("Total Growth in Popularity (2015-2025)", fontsize=14, fontweight='bold')
ax2.set_ylabel("Growth in Popularity Score", fontsize=12)

# Adjust layout
plt.tight_layout()

# Display the chart
plt.show()