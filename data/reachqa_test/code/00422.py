import matplotlib.pyplot as plt
import numpy as np

# Constructing historical migration data (in thousands)
years = np.array([1850, 1860, 1870, 1880, 1890, 1900, 1910, 1920, 1930, 1940,
                  1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020])

# Asia, Europe, Africa, South America, Oceania
asia_migration = np.array([5, 10, 20, 30, 40, 80, 90, 100, 110, 120, 130, 140, 150, 170, 200, 220, 240, 250])
europe_migration = np.array([20, 25, 30, 45, 50, 80, 70, 60, 55, 40, 75, 90, 100, 110, 130, 150, 170, 190])
africa_migration = np.array([5, 5, 5, 5, 5, 5, 5, 10, 15, 15, 20, 25, 30, 40, 55, 70, 85, 95])
south_america_migration = np.array([10, 10, 10, 20, 20, 30, 30, 35, 40, 40, 45, 50, 55, 70, 90, 105, 120, 130])
oceania_migration = np.array([2, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85])

# Calculate total migration for each year
total_migration = asia_migration + europe_migration + africa_migration + south_america_migration + oceania_migration

# Calculate the percentage contribution for each continent
asia_percent = (asia_migration / total_migration) * 100
europe_percent = (europe_migration / total_migration) * 100
africa_percent = (africa_migration / total_migration) * 100
south_america_percent = (south_america_migration / total_migration) * 100
oceania_percent = (oceania_migration / total_migration) * 100

# Plotting the enhanced figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12))

# Original line chart with enhanced styles
ax1.plot(years, asia_migration, label='Asia', color='red', marker='o', linestyle='-', linewidth=2)
ax1.plot(years, europe_migration, label='Europe', color='blue', marker='s', linestyle=':', linewidth=2)
ax1.plot(years, africa_migration, label='Africa', color='green', marker='^', linestyle='--', linewidth=2)
ax1.plot(years, south_america_migration, label='South America', color='purple', marker='v', linestyle='-.', linewidth=2)
ax1.plot(years, oceania_migration, label='Oceania', color='orange', marker='D', linestyle='-', linewidth=2)

# Customizing the main plot
ax1.set_title('Historical Migration Patterns\nA Journey Through Time')
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Immigrants (in Thousands)')
ax1.legend(title='Continent', loc='upper left')

# Adjust the x-axis tick frequency and formatting for year labels
ax1.set_xticks(range(1850, 2030, 50))
ax1.tick_params(axis='x', rotation=45, labelsize=10)

# Enhance readability with grid
ax1.grid(True, which='both', linestyle='--', linewidth=0.5)

# Stacked bar chart for percentage contribution
bottom_stack = np.zeros(len(years))
continents = ['Asia', 'Europe', 'Africa', 'South America', 'Oceania']
colors = ['red', 'blue', 'green', 'purple', 'orange']

for continent, percent, color in zip(continents, [asia_percent, europe_percent, africa_percent, south_america_percent, oceania_percent], colors):
    ax2.bar(years, percent, bottom=bottom_stack, label=continent, color=color)
    bottom_stack += percent

# Customizing the stacked bar chart
ax2.set_title('Continent Contribution to Migration\n(Percentages)')
ax2.set_xlabel('Year')
ax2.set_ylabel('Percentage (%)')
ax2.set_ylim(0, 100)
ax2.legend(title='Continent', loc='upper left')

# Adjust the layout to prevent any overlapping
plt.tight_layout()

# Show the charts
plt.show()