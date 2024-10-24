import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2020
years = np.arange(2010, 2021)

# Solar energy production data for each continent (in gigawatts)
north_america = [20, 25, 30, 40, 50, 65, 80, 100, 120, 140, 160]
europe = [30, 40, 55, 70, 85, 105, 130, 160, 200, 240, 280]
asia = [50, 70, 100, 140, 190, 250, 330, 420, 520, 640, 760]
africa = [5, 8, 12, 18, 25, 35, 45, 60, 75, 95, 120]
south_america = [10, 15, 22, 32, 45, 60, 80, 100, 130, 165, 200]

# Stack the data for the area chart
solar_data = np.vstack([north_america, europe, asia, africa, south_america])

# Set up the plot
plt.figure(figsize=(12, 7))

# Colors for each continent
colors = ['#FFD700', '#FF6347', '#2E8B57', '#4169E1', '#FF69B4']

# Plotting the stacked area chart
plt.stackplot(years, solar_data, labels=['North America', 'Europe', 'Asia', 'Africa', 'South America'], 
              colors=colors, alpha=0.9)

# Overlaying trend lines
for continent, color in zip(solar_data, colors):
    plt.plot(years, continent, color=color, linewidth=1.5, linestyle='--')

# Customize the plot
plt.title("The Solar Transition: A Decade of Solar Energy Production\nGrowth by Continents (2010-2020)", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Solar Energy Production (Gigawatts)", fontsize=12)

# Add grid lines for better readability
plt.grid(linestyle='--', alpha=0.5)

# Rotate x-axis labels to avoid overlap
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 901, 100))

# Highlighting the peak production year for each continent
peak_years = [2010 + np.argmax(continent) for continent in solar_data]
peak_values = [max(continent) for continent in solar_data]

for year, value, label, color in zip(peak_years, peak_values, ['North America', 'Europe', 'Asia', 'Africa', 'South America'], colors):
    plt.annotate(f'{value} GW', xy=(year, value), xytext=(3, 10),
                 textcoords='offset points', fontsize=10,
                 arrowprops=dict(facecolor=color, shrink=0.05),
                 bbox=dict(facecolor='white', edgecolor=color, boxstyle='round,pad=0.3'))

# Custom legend for clarity
custom_legend = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
plt.legend(custom_legend, ['North America', 'Europe', 'Asia', 'Africa', 'South America'], loc='upper left', fontsize=10, title="Continents")

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()