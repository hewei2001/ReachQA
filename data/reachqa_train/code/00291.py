import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2020
years = np.arange(2010, 2021)

# Artificial data for internet usage growth (% of population using internet)
africa_internet = [10, 13, 17, 22, 28, 33, 39, 45, 52, 59, 65]
asia_internet = [20, 25, 30, 37, 44, 50, 58, 65, 72, 78, 84]
europe_internet = [60, 63, 66, 69, 72, 76, 79, 83, 86, 88, 91]
north_america_internet = [70, 73, 75, 78, 80, 82, 84, 86, 88, 89, 90]
south_america_internet = [40, 44, 48, 53, 59, 64, 68, 73, 78, 82, 86]

# Related data for the second plot: CAGR from 2010 to 2020
cagr = [
    (africa_internet[-1]/africa_internet[0])**(1/10) - 1,
    (asia_internet[-1]/asia_internet[0])**(1/10) - 1,
    (europe_internet[-1]/europe_internet[0])**(1/10) - 1,
    (north_america_internet[-1]/north_america_internet[0])**(1/10) - 1,
    (south_america_internet[-1]/south_america_internet[0])**(1/10) - 1
]
continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America']

# Create figure and axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), gridspec_kw={'width_ratios': [3, 1]})

# Stacked area chart
ax1.stackplot(years, africa_internet, asia_internet, europe_internet, north_america_internet, south_america_internet, 
              labels=continents, colors=['gold', 'lightcoral', 'lightblue', 'lightgreen', 'thistle'], alpha=0.8)
ax1.set_title("Decade of Digital Growth:\nInternet Adoption Across Continents (2010-2020)", fontsize=14, fontweight='bold')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Internet Users (% of Population)", fontsize=12)
ax1.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Continents')
ax1.grid(alpha=0.3)
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)

# Bar chart for CAGR
ax2.barh(continents, [c * 100 for c in cagr], color=['gold', 'lightcoral', 'lightblue', 'lightgreen', 'thistle'])
ax2.set_title("CAGR of Internet Usage\n2010-2020 (%)", fontsize=14, fontweight='bold')
ax2.set_xlabel("CAGR (%)", fontsize=12)
ax2.set_yticks(range(len(continents)))
ax2.set_yticklabels(continents)

# Adjust layout to ensure no overlapping and clear visual presentation
plt.tight_layout()

# Display the plots
plt.show()