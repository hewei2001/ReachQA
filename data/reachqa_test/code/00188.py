import matplotlib.pyplot as plt
import numpy as np

# Data for solar power installations by continent
continents = ['Asia', 'Europe', 'North America', 'South America', 'Africa', 'Australia']
installations_percent = [35, 25, 20, 8, 7, 5]

# Growth rate data for solar installations (made-up data for illustration)
years = np.array([2019, 2020, 2021, 2022, 2023])
growth_rates = {
    'Asia': [20, 22, 28, 30, 35],
    'Europe': [15, 18, 22, 23, 25],
    'North America': [12, 15, 18, 19, 20],
    'South America': [5, 6, 7, 7.5, 8],
    'Africa': [3, 4, 5, 6, 7],
    'Australia': [2, 3, 4, 4.5, 5]
}

# Colors for the chart
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF2', '#FFC133']

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# Plot the donut pie chart
wedges, texts, autotexts = axs[0].pie(
    installations_percent, 
    colors=colors, 
    labels=continents, 
    autopct='%1.1f%%', 
    startangle=90, 
    pctdistance=0.85, 
    textprops=dict(color="black", fontsize=10), 
    wedgeprops=dict(width=0.3, edgecolor='w'), 
    explode=(0.1, 0, 0, 0, 0, 0)
)
centre_circle = plt.Circle((0, 0), 0.60, fc='white')
axs[0].add_artist(centre_circle)
axs[0].set_title(
    "Harnessing Solar Power:\nThe Rise of Green Tech Across Continents in 2023", 
    fontsize=14, 
    weight='bold'
)
axs[0].legend(wedges, continents, title="Continents", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
axs[0].axis('equal')

# Plot the line chart
for continent, growth in growth_rates.items():
    axs[1].plot(years, growth, marker='o', label=continent, color=colors[continents.index(continent)])

axs[1].set_title("Growth Trends of Solar Installations (2019-2023)", fontsize=14, weight='bold')
axs[1].set_xlabel("Year", fontsize=12)
axs[1].set_ylabel("Installations (%)", fontsize=12)
axs[1].legend(title="Continents", loc="upper left")
axs[1].grid(True)
axs[1].set_xlim(years[0], years[-1])
axs[1].set_ylim(0, 40)

# Adjust layout for better fit
plt.tight_layout()

# Display the chart
plt.show()