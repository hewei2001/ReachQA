import matplotlib.pyplot as plt
import numpy as np

# Define the years and sales data
years = np.arange(2015, 2025)
north_america = np.array([200, 210, 220, 230, 250, 280, 310, 340, 370, 400])
europe = np.array([180, 190, 200, 210, 230, 260, 290, 320, 350, 380])
asia = np.array([150, 160, 170, 190, 210, 230, 260, 290, 320, 350])
south_america = np.array([100, 105, 110, 120, 135, 150, 170, 190, 210, 230])
oceania = np.array([80, 85, 90, 95, 110, 125, 140, 160, 180, 200])

# Calculate year-over-year growth rate for each region
def calculate_growth_rate(data):
    return np.round(100 * (data[1:] - data[:-1]) / data[:-1], 1)

growth_na = calculate_growth_rate(north_america)
growth_eu = calculate_growth_rate(europe)
growth_as = calculate_growth_rate(asia)
growth_sa = calculate_growth_rate(south_america)
growth_oc = calculate_growth_rate(oceania)

# Define bar width and index for plotting
bar_width = 0.15
index = np.arange(len(years))

# Set up colors for each region
colors = ['#FFD700', '#B22222', '#32CD32', '#1E90FF', '#FF69B4']

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Plot 1: Bar chart for sales data
bars_na = ax1.bar(index, north_america, bar_width, label='North America', color=colors[0])
bars_eu = ax1.bar(index + bar_width, europe, bar_width, label='Europe', color=colors[1])
bars_as = ax1.bar(index + 2 * bar_width, asia, bar_width, label='Asia', color=colors[2])
bars_sa = ax1.bar(index + 3 * bar_width, south_america, bar_width, label='South America', color=colors[3])
bars_oc = ax1.bar(index + 4 * bar_width, oceania, bar_width, label='Oceania', color=colors[4])

# Add data annotations for each bar
for bars in [bars_na, bars_eu, bars_as, bars_sa, bars_oc]:
    for bar in bars:
        height = bar.get_height()
        ax1.annotate(f'{height}',
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3),
                     textcoords="offset points",
                     ha='center', va='bottom', fontsize=9)

# Customize the bar chart
ax1.set_title('The Renaissance of Artisan Bread:\nA Decade of Rising Artisan Bakery Sales (2015-2024)',
              fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Sales Volume (Thousands of Units)', fontsize=12)
ax1.set_xticks(index + 2 * bar_width)
ax1.set_xticklabels(years, rotation=45)
ax1.legend(title='Regions', fontsize=10, title_fontsize=11)
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Plot 2: Line chart for year-over-year growth rate
growth_years = years[1:]  # Growth rates start from the second year
ax2.plot(growth_years, growth_na, marker='o', label='North America', color=colors[0])
ax2.plot(growth_years, growth_eu, marker='o', label='Europe', color=colors[1])
ax2.plot(growth_years, growth_as, marker='o', label='Asia', color=colors[2])
ax2.plot(growth_years, growth_sa, marker='o', label='South America', color=colors[3])
ax2.plot(growth_years, growth_oc, marker='o', label='Oceania', color=colors[4])

# Customize the line chart
ax2.set_title('Year-over-Year Growth Rate of Artisan Bakery Sales', fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Growth Rate (%)', fontsize=12)
ax2.set_xticks(growth_years)
ax2.set_xticklabels(growth_years, rotation=45)
ax2.legend(title='Regions', fontsize=10, title_fontsize=11)
ax2.grid(True, linestyle='--', alpha=0.7)

# Optimize layout and display the charts
plt.tight_layout()
plt.show()