import matplotlib.pyplot as plt

# Data for Greenfield City's energy mix in 2023
energy_sources = ['Solar Power', 'Wind Energy', 'Hydroelectricity', 'Biomass', 'Natural Gas', 'Nuclear Energy', 'Coal']
energy_distribution_2023 = [18, 22, 15, 10, 20, 10, 5]

# Historical energy mix data for comparison
years = ['2019', '2020', '2021', '2022', '2023']
historical_data = {
    'Solar Power': [10, 12, 15, 16, 18],
    'Wind Energy': [18, 20, 21, 21, 22],
    'Hydroelectricity': [20, 18, 17, 16, 15],
    'Biomass': [10, 11, 12, 12, 10],
    'Natural Gas': [22, 21, 20, 20, 20],
    'Nuclear Energy': [15, 14, 13, 12, 10],
    'Coal': [5, 4, 2, 3, 5]
}

# Colors corresponding to the energy sources
colors = ['#ffcc00', '#99ccff', '#66ff66', '#ff9966', '#ff6666', '#66ccff', '#cccccc']

# Set up a 1x2 subplot layout
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# Pie chart for 2023 energy mix
axs[0].pie(
    energy_distribution_2023, 
    labels=energy_sources, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    explode=(0, 0, 0, 0, 0, 0, 0.1), 
    shadow=True
)
axs[0].set_title("Greenfield City's Energy Mix 2023:\nA Step Towards Sustainability", fontsize=14, fontweight='bold')

# Stacked bar chart for historical data
bottom = [0] * len(years)
for i, source in enumerate(energy_sources):
    axs[1].bar(years, historical_data[source], bottom=bottom, color=colors[i], label=source)
    bottom = [sum(x) for x in zip(bottom, historical_data[source])]

axs[1].set_title("Historical Energy Mix (2019-2023)", fontsize=14, fontweight='bold')
axs[1].set_xlabel("Year")
axs[1].set_ylabel("Percentage (%)")
axs[1].legend(title="Energy Sources", bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust layout
plt.tight_layout()

# Display the chart
plt.show()