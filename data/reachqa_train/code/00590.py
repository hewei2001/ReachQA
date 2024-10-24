import matplotlib.pyplot as plt
import numpy as np

# Define the countries and years
countries = ["Country A", "Country B", "Country C", "Country D"]
years = np.arange(2010, 2021)

# Define the artificial data for each energy source
data_solar = {
    "Country A": [1, 3, 5, 7, 11, 15, 20, 25, 30, 35, 40],
    "Country B": [2, 4, 6, 9, 13, 18, 24, 30, 36, 43, 50],
    "Country C": [1, 2, 3, 5, 8, 12, 17, 23, 30, 38, 45],
    "Country D": [2, 5, 8, 12, 17, 23, 30, 38, 47, 57, 68]
}

data_wind = {
    "Country A": [2, 4, 7, 10, 13, 17, 22, 27, 33, 40, 48],
    "Country B": [3, 5, 8, 12, 16, 21, 27, 34, 41, 49, 58],
    "Country C": [2, 4, 7, 10, 14, 19, 25, 32, 40, 49, 59],
    "Country D": [4, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78]
}

data_hydro = {
    "Country A": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    "Country B": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    "Country C": [5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10],
    "Country D": [4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9]
}

data_biomass = {
    "Country A": [1, 2, 3, 4, 5, 6, 7, 9, 10, 12, 14],
    "Country B": [1, 2, 2, 3, 4, 5, 7, 9, 12, 15, 19],
    "Country C": [1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8],
    "Country D": [0, 1, 1, 1, 2, 2, 3, 4, 5, 6, 7]
}

# Function to plot stacked area chart for a given country
def plot_renewable_energy(country, solar, wind, hydro, biomass):
    plt.figure(figsize=(12, 6))
    plt.stackplot(years, solar, wind, hydro, biomass, labels=['Solar', 'Wind', 'Hydro', 'Biomass'],
                  colors=['gold', 'skyblue', 'lightgreen', 'sandybrown'], alpha=0.8)

    # Setting titles and labels
    plt.title(f"Renewable Energy Production Trends in {country}\n(2010-2020)", fontsize=14, fontweight='bold')
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Energy Production (TWh)", fontsize=12)
    plt.legend(loc='upper left', fontsize=10, title='Energy Sources')
    
    # Set axis limits and grid
    plt.xlim(years[0], years[-1])
    plt.grid(visible=True, linestyle='--', alpha=0.5)
    
    # Improve layout
    plt.xticks(years, rotation=45)
    plt.tight_layout()

    # Display the plot
    plt.show()

# Plot the stacked area chart for each country
for country in countries:
    plot_renewable_energy(country, 
                          data_solar[country], 
                          data_wind[country], 
                          data_hydro[country], 
                          data_biomass[country])