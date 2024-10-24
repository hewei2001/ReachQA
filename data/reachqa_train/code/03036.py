import matplotlib.pyplot as plt
import numpy as np

# Renewable energy technologies and their installation rates in 2023 (in gigawatts)
technologies = ['Solar Power', 'Wind Power', 'Hydropower', 'Biomass']
installation_rates = [180, 140, 90, 60]

# Historical growth rates data (percentages from 2018 to 2023)
years = np.arange(2018, 2024)
growth_rates = {
    'Solar Power': [10, 12, 15, 20, 18, 22],
    'Wind Power': [8, 9, 12, 14, 15, 17],
    'Hydropower': [3, 4, 4, 5, 6, 7],
    'Biomass': [2, 3, 3, 4, 4, 5]
}

colors = ['#FFD700', '#1E90FF', '#32CD32', '#8B4513']

# Create the figure and the subplots
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(12, 10))

# Bar chart: Installation rates
x_positions = np.arange(len(technologies))
bars = ax1.bar(x_positions, installation_rates, color=colors, width=0.6)

# Annotate bars with installation rates
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height} GW',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 5),
                 textcoords="offset points",
                 ha='center', va='bottom', fontsize=10, color='black', weight='bold')

ax1.set_title('The Rise of Renewable Energy Technologies\nGlobal Installation Rates in 2023', fontsize=14, weight='bold')
ax1.set_xlabel('Renewable Energy Technologies', fontsize=12)
ax1.set_ylabel('Installation Rates (GW)', fontsize=12)
ax1.set_xticks(x_positions)
ax1.set_xticklabels(technologies, fontsize=11)
ax1.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Line plot: Historical growth trends
for i, tech in enumerate(technologies):
    ax2.plot(years, growth_rates[tech], label=tech, color=colors[i], marker='o', linewidth=2)

ax2.set_title('Historical Growth Trends of Renewable Energy Installations (2018-2023)', fontsize=14, weight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Growth Rate (%)', fontsize=12)
ax2.legend(title='Technology', loc='upper left', fontsize=10)
ax2.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()