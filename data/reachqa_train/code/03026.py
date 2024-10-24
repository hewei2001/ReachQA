import matplotlib.pyplot as plt
import numpy as np

# Original data: Years and number of eco-friendly brands
years = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
brands = np.array([50, 65, 80, 95, 120, 140, 180, 220, 280, 350, 420])

# Derived data: Year-on-year growth rate in percentage
growth_rate = np.diff(brands) / brands[:-1] * 100
growth_years = years[1:]

# Initialize the figure and create subplots
fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# First subplot: Line plot of the number of brands
axes[0].plot(years, brands, marker='o', color='seagreen', linewidth=2, linestyle='-')
annotations = {2012: "Material Innovations", 2015: "Climate Agreement", 
               2018: "Ethical Consumerism", 2020: "Sustainability Focus"}

for year, text in annotations.items():
    axes[0].annotate(text,
                     xy=(year, brands[years.tolist().index(year)]),
                     xytext=(year, brands[years.tolist().index(year)] + 40),
                     arrowprops=dict(facecolor='grey', shrink=0.05, width=1, headwidth=8),
                     fontsize=10, color='darkgreen')

for (x, y) in zip(years, brands):
    axes[0].text(x, y + 10, f'{y}', ha='center', va='bottom', fontsize=9, color='darkblue')

axes[0].set_title('Rise of Eco-Friendly Fashion Brands\n(2010-2020)', fontsize=14, fontweight='bold', pad=20)
axes[0].set_xlabel('Year', fontsize=12)
axes[0].set_ylabel('Number of Brands', fontsize=12)
axes[0].legend(['Number of Eco-Friendly Brands'], loc='upper left', fontsize=10)
axes[0].set_xticks(years)
axes[0].set_yticks(np.arange(0, 501, 50))
axes[0].grid(axis='y', linestyle='--', alpha=0.7)

# Second subplot: Bar chart for growth rate
axes[1].bar(growth_years, growth_rate, color='lightcoral', edgecolor='black')
for (x, y) in zip(growth_years, growth_rate):
    axes[1].text(x, y + 0.5, f'{y:.1f}%', ha='center', va='bottom', fontsize=9, color='darkred')

axes[1].set_title('Annual Growth Rate of\nEco-Friendly Brands (%)', fontsize=14, fontweight='bold', pad=20)
axes[1].set_xlabel('Year', fontsize=12)
axes[1].set_ylabel('Growth Rate (%)', fontsize=12)
axes[1].set_xticks(growth_years)
axes[1].set_yticks(np.arange(0, max(growth_rate) + 10, 10))
axes[1].grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Show the plots
plt.show()