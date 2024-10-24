import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Data: Coffee consumption per capita (kg) and Happiness Index
countries = ['Finland', 'Norway', 'Iceland', 'Denmark', 'Netherlands', 'Sweden', 'Switzerland', 'Austria', 'New Zealand', 'Canada']
coffee_consumption = [12.0, 9.9, 9.0, 8.7, 8.4, 7.9, 7.5, 7.0, 6.8, 6.5]
happiness_index = [7.8, 7.7, 7.5, 7.6, 7.4, 7.3, 7.6, 7.0, 7.1, 6.9]

# Additional data: GDP per capita in thousands USD (for illustration)
gdp_per_capita = [55, 75, 73, 68, 58, 54, 81, 50, 42, 46]

# Sort the data by coffee consumption for spline interpolation
sorted_indices = np.argsort(coffee_consumption)
sorted_coffee_consumption = np.array(coffee_consumption)[sorted_indices]
sorted_happiness_index = np.array(happiness_index)[sorted_indices]

fig, ax1 = plt.subplots(figsize=(14, 8))

# Scatter plot for coffee consumption vs. happiness
scatter = ax1.scatter(coffee_consumption, happiness_index, c=range(len(countries)), cmap='tab10', s=100, edgecolor='black', alpha=0.8)
xnew = np.linspace(min(sorted_coffee_consumption), max(sorted_coffee_consumption), 300)
spl = make_interp_spline(sorted_coffee_consumption, sorted_happiness_index, k=3)
ynew = spl(xnew)
ax1.plot(xnew, ynew, color='orange', linewidth=2.5, linestyle='--', label='Smooth Fit')

# Title and labels
ax1.set_title("Global Coffee Consumption vs. Happiness Index & GDP:\nBrewing Joy with Economic Insight", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Coffee Consumption (kg per capita)', fontsize=12)
ax1.set_ylabel('Happiness Index (1-10)', fontsize=12, color='tab:blue')

# Annotate each country
for i, country in enumerate(countries):
    ax1.annotate(country, (coffee_consumption[i], happiness_index[i]), fontsize=9, xytext=(-10, 10), textcoords='offset points', ha='right', arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))

# Second y-axis for GDP per capita
ax2 = ax1.twinx()
ax2.set_ylabel('GDP per Capita (thousands USD)', fontsize=12, color='tab:green')
ax2.plot(coffee_consumption, gdp_per_capita, color='green', linewidth=2, linestyle='-', marker='o', markersize=8, label='GDP per Capita')

# Adding legend
fig.legend(loc='upper right', fontsize=10, title_fontsize=11)

# Color bar for scatter plot
cbar = fig.colorbar(scatter, ax=ax1, orientation='vertical')
cbar.set_label('Country Index', rotation=270, labelpad=15)

# Grid and layout
ax1.grid(True, linestyle='--', alpha=0.7)
plt.xlim(6, 13)
ax1.set_ylim(6.5, 8.0)
ax2.set_ylim(40, 85)

plt.tight_layout()
plt.show()