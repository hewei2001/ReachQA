import matplotlib.pyplot as plt
import numpy as np

# Define the countries and renewable energy percentages
countries = ['Germany', 'France', 'Spain', 'Sweden', 'Italy']
wind = [40, 30, 35, 50, 25]
solar = [25, 30, 40, 10, 35]
hydro = [20, 25, 10, 30, 25]
biomass = [15, 15, 15, 10, 15]

# Set figure size and create a bar chart
fig, ax = plt.subplots(figsize=(10, 7))

# Calculate the cumulative percentage positions for stacking
cumulative_wind = np.array(wind)
cumulative_solar = cumulative_wind + np.array(solar)
cumulative_hydro = cumulative_solar + np.array(hydro)

# Plot each renewable energy source on top of each other
ax.bar(countries, wind, label='Wind', color='#66c2a5')
ax.bar(countries, solar, bottom=cumulative_wind, label='Solar', color='#fc8d62')
ax.bar(countries, hydro, bottom=cumulative_solar, label='Hydro', color='#8da0cb')
ax.bar(countries, biomass, bottom=cumulative_hydro, label='Biomass', color='#e78ac3')

# Add title and labels
ax.set_title('Renewable Energy Adoption in European Countries\n2023', fontsize=16, fontweight='bold')
ax.set_ylabel('Percentage (%)', fontsize=12)
ax.set_xlabel('Countries', fontsize=12)
ax.set_ylim(0, 100)

# Add a legend
ax.legend(title='Energy Source', bbox_to_anchor=(1.05, 1), loc='upper left')

# Add percentage labels to each section of the bars
for i, country in enumerate(countries):
    ax.text(i, cumulative_wind[i] - wind[i] / 2, f'{wind[i]}%', ha='center', va='center', color='white', fontweight='bold')
    ax.text(i, cumulative_solar[i] - solar[i] / 2, f'{solar[i]}%', ha='center', va='center', color='white', fontweight='bold')
    ax.text(i, cumulative_hydro[i] - hydro[i] / 2, f'{hydro[i]}%', ha='center', va='center', color='white', fontweight='bold')
    ax.text(i, cumulative_hydro[i] + biomass[i] / 2, f'{biomass[i]}%', ha='center', va='center', color='white', fontweight='bold')

# Adjust layout to prevent overlap and ensure clarity
plt.tight_layout()

# Display the chart
plt.show()