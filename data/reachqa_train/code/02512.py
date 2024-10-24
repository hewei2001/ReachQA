import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

# Define the years of interest
years = np.array([2000, 2005, 2010, 2015, 2020, 2025, 2030])

# Data representing the percentage of renewable energy adoption for each continent
north_america = {
    'solar': [2, 3, 5, 10, 15, 18, 20],
    'wind': [3, 5, 10, 15, 20, 25, 28],
    'hydro': [15, 16, 17, 18, 19, 20, 21],
    'other': [1, 2, 3, 5, 7, 9, 10],
    'growth': [1, 2, 2, 4, 3, 2, 2]  # Made-up growth data
}

south_america = {
    'solar': [1, 2, 4, 8, 12, 15, 18],
    'wind': [2, 3, 5, 7, 10, 13, 15],
    'hydro': [20, 22, 23, 24, 25, 26, 27],
    'other': [2, 3, 5, 6, 7, 8, 9],
    'growth': [2, 3, 4, 2, 3, 3, 3]  # Made-up growth data
}

europe = {
    'solar': [5, 10, 15, 20, 25, 30, 35],
    'wind': [5, 10, 15, 20, 25, 30, 35],
    'hydro': [10, 12, 14, 16, 18, 20, 22],
    'other': [2, 3, 4, 5, 6, 7, 8],
    'growth': [3, 4, 5, 5, 5, 5, 5]  # Made-up growth data
}

asia = {
    'solar': [1, 2, 3, 7, 11, 14, 18],
    'wind': [1, 3, 5, 9, 14, 18, 22],
    'hydro': [10, 11, 13, 15, 16, 18, 20],
    'other': [1, 2, 3, 5, 7, 9, 11],
    'growth': [2, 3, 4, 4, 4, 4, 4]  # Made-up growth data
}

africa = {
    'solar': [2, 4, 7, 12, 18, 25, 30],
    'wind': [1, 2, 4, 6, 9, 12, 15],
    'hydro': [5, 6, 7, 8, 9, 10, 11],
    'other': [2, 3, 4, 5, 6, 7, 8],
    'growth': [1, 1, 2, 2, 2, 2, 3]  # Made-up growth data
}

def plot_renewable_energy_adoption(years, continent_data, continent_name):
    fig = plt.figure(figsize=(14, 6))
    gs = GridSpec(1, 2, width_ratios=[3, 1])

    # Extract data for different renewable sources
    solar = continent_data['solar']
    wind = continent_data['wind']
    hydro = continent_data['hydro']
    other = continent_data['other']
    growth = continent_data['growth']

    # Stackplot for cumulative data visualization
    ax1 = fig.add_subplot(gs[0])
    ax1.stackplot(years, solar, wind, hydro, other,
                  labels=['Solar', 'Wind', 'Hydroelectric', 'Other Renewables'],
                  colors=['#f9c74f', '#90be6d', '#43aa8b', '#577590'],
                  alpha=0.8)

    ax1.set_title(f'Renewable Energy Adoption in {continent_name}\n(2000-2030)', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Year', fontsize=10)
    ax1.set_ylabel('Percentage of Total Energy Consumption', fontsize=10)
    ax1.set_xticks(years)
    ax1.set_xticklabels(years, rotation=45)
    ax1.set_ylim(0, 100)
    ax1.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=8)

    # Bar chart for growth comparison
    ax2 = fig.add_subplot(gs[1])
    energy_sources = ['Solar', 'Wind', 'Hydro', 'Other']
    ax2.bar(energy_sources, growth[:4], color=['#f9c74f', '#90be6d', '#43aa8b', '#577590'], alpha=0.8)
    ax2.set_title('Growth Contribution', fontsize=12)
    ax2.set_ylabel('Growth Units', fontsize=10)

    plt.tight_layout()
    plt.show()

# Generate the plots for each continent
plot_renewable_energy_adoption(years, north_america, "North America")
plot_renewable_energy_adoption(years, south_america, "South America")
plot_renewable_energy_adoption(years, europe, "Europe")
plot_renewable_energy_adoption(years, asia, "Asia")
plot_renewable_energy_adoption(years, africa, "Africa")