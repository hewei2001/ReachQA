import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Define countries and their investment distributions in millions of dollars
countries = ['Country A', 'Country B', 'Country C', 'Country D', 'Country E']
solar_investment = [250, 300, 200, 400, 350]
wind_investment = [300, 250, 300, 200, 150]
hydro_investment = [150, 200, 250, 100, 200]

# Calculate the total investment for each country
total_investment = np.array(solar_investment) + np.array(wind_investment) + np.array(hydro_investment)

# Calculate the percentage for each energy source per country
percent_solar = (np.array(solar_investment) / total_investment) * 100
percent_wind = (np.array(wind_investment) / total_investment) * 100
percent_hydro = (np.array(hydro_investment) / total_investment) * 100

# Plotting the stacked bar chart
fig, ax = plt.subplots(figsize=(14, 9))
width = 0.6

# Adding a color gradient to each type of investment
solar_colors = cm.YlOrRd(np.linspace(0.3, 0.7, len(countries)))
wind_colors = cm.Blues(np.linspace(0.4, 0.8, len(countries)))
hydro_colors = cm.Greens(np.linspace(0.5, 0.9, len(countries)))

# Plot bars with gradients
bars_solar = ax.bar(countries, solar_investment, label='Solar', color=solar_colors, width=width)
bars_wind = ax.bar(countries, wind_investment, bottom=solar_investment, label='Wind', color=wind_colors, width=width)
bars_hydro = ax.bar(countries, hydro_investment, bottom=np.array(solar_investment) + np.array(wind_investment), label='Hydroelectric', color=hydro_colors, width=width)

# Titles and labels
ax.set_title("Renewable Energy Investment by Country in 2023\nSolar, Wind, and Hydroelectric Sectors", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel("Countries", fontsize=14)
ax.set_ylabel("Investment in Millions of USD", fontsize=14)
ax.set_ylim(0, max(total_investment) + 150)
ax.legend(title="Energy Sector", loc='upper right')

# Add text annotations on bars
for idx, (country, total, solar, wind, hydro) in enumerate(zip(countries, total_investment, percent_solar, percent_wind, percent_hydro)):
    ax.text(idx, total + 5, f"{total}M", ha='center', va='bottom', fontsize=10, fontweight='bold')
    ax.text(idx, solar_investment[idx] / 2, f"{solar:.1f}%", ha='center', va='center', color='black', fontsize=10)
    ax.text(idx, solar_investment[idx] + wind_investment[idx] / 2, f"{wind:.1f}%", ha='center', va='center', color='black', fontsize=10)
    ax.text(idx, total - hydro_investment[idx] / 2, f"{hydro:.1f}%", ha='center', va='center', color='white', fontsize=10)

# Rotate x-tick labels
plt.xticks(rotation=45, ha='right')

# Grid for readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Add a subtle background
ax.set_facecolor('#f0f0f5')

# Highlight the country with the maximum investment
max_idx = np.argmax(total_investment)
ax.bar(countries[max_idx], total_investment[max_idx], color='gold', alpha=0.5, width=width, edgecolor='black')

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()