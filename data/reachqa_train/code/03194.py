import numpy as np
import matplotlib.pyplot as plt

# Define countries and their investment distributions in millions of dollars
countries = ['Country A', 'Country B', 'Country C', 'Country D', 'Country E']
solar_investment = [250, 300, 200, 400, 350]
wind_investment = [300, 250, 300, 200, 150]
hydro_investment = [150, 200, 250, 100, 200]

# Calculate the total investment for each country
total_investment = np.array(solar_investment) + np.array(wind_investment) + np.array(hydro_investment)

# Plotting the stacked bar chart
fig, ax = plt.subplots(figsize=(12, 8))
width = 0.6

# Plot bars
ax.bar(countries, solar_investment, label='Solar', color='#FFD700', width=width)
ax.bar(countries, wind_investment, bottom=solar_investment, label='Wind', color='#87CEEB', width=width)
ax.bar(countries, hydro_investment, bottom=np.array(solar_investment) + np.array(wind_investment), label='Hydroelectric', color='#228B22', width=width)

# Titles and labels
ax.set_title("Renewable Energy Investment by Country in 2023\nSolar, Wind, and Hydroelectric Sectors", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Countries", fontsize=12)
ax.set_ylabel("Investment in Millions of USD", fontsize=12)
ax.set_ylim(0, max(total_investment) + 100)
ax.legend(title="Energy Sector", loc='upper right')

# Grid for readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Add text annotations on bars
for idx, (country, total) in enumerate(zip(countries, total_investment)):
    ax.text(idx, total + 10, f"{total}M", ha='center', va='bottom', fontsize=10, fontweight='bold')

# Rotate x-tick labels
plt.xticks(rotation=45, ha='right')

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()