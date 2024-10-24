import matplotlib.pyplot as plt
import numpy as np

# Define the countries and renewable energy percentages for 2023
countries = ['Germany', 'France', 'Spain', 'Sweden', 'Italy']
wind = [40, 30, 35, 50, 25]
solar = [25, 30, 40, 10, 35]
hydro = [20, 25, 10, 30, 25]
biomass = [15, 15, 15, 10, 15]

# Simulate renewable energy growth rates over the years for each country
years = ['2019', '2020', '2021', '2022', '2023']
growth_data = {
    'Germany': [60, 63, 67, 72, 75],
    'France': [55, 58, 60, 62, 65],
    'Spain': [50, 52, 55, 58, 60],
    'Sweden': [80, 83, 85, 90, 95],
    'Italy': [40, 42, 45, 48, 50],
}

# Create the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# --- Stacked Bar Chart ---
# Calculate the cumulative percentages for stacking
cumulative_wind = np.array(wind)
cumulative_solar = cumulative_wind + np.array(solar)
cumulative_hydro = cumulative_solar + np.array(hydro)

# Plot each renewable energy source on top of each other
ax1.bar(countries, wind, label='Wind', color='#66c2a5')
ax1.bar(countries, solar, bottom=cumulative_wind, label='Solar', color='#fc8d62')
ax1.bar(countries, hydro, bottom=cumulative_solar, label='Hydro', color='#8da0cb')
ax1.bar(countries, biomass, bottom=cumulative_hydro, label='Biomass', color='#e78ac3')

# Add labels and title
ax1.set_title('Renewable Energy Adoption\nin European Countries (2023)', fontsize=14, fontweight='bold')
ax1.set_ylabel('Percentage (%)')
ax1.set_xlabel('Countries')
ax1.set_ylim(0, 100)
ax1.legend(title='Energy Source', bbox_to_anchor=(1.05, 1), loc='upper left')

# Add percentage labels
for i, country in enumerate(countries):
    ax1.text(i, cumulative_wind[i] - wind[i] / 2, f'{wind[i]}%', ha='center', va='center', color='white', fontweight='bold')
    ax1.text(i, cumulative_solar[i] - solar[i] / 2, f'{solar[i]}%', ha='center', va='center', color='white', fontweight='bold')
    ax1.text(i, cumulative_hydro[i] - hydro[i] / 2, f'{hydro[i]}%', ha='center', va='center', color='white', fontweight='bold')
    ax1.text(i, cumulative_hydro[i] + biomass[i] / 2, f'{biomass[i]}%', ha='center', va='center', color='white', fontweight='bold')

# --- Line Chart for Growth Rates ---
# Plot the renewable energy growth for each country
for country in countries:
    ax2.plot(years, growth_data[country], marker='o', label=country)

# Add labels and title
ax2.set_title('Renewable Energy Growth Over Years', fontsize=14, fontweight='bold')
ax2.set_ylabel('Renewable Energy Percentage (%)')
ax2.set_xlabel('Year')
ax2.set_ylim(30, 100)
ax2.legend(title='Country')

# Adjust layout
plt.tight_layout()

# Display the charts
plt.show()