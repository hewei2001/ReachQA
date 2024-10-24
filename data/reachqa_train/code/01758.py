import matplotlib.pyplot as plt
import numpy as np

# Data for the energy source distribution on Mars in 2050
energy_sources = ['Solar', 'Nuclear', 'Wind', 'Geothermal', 'Biofuel']
percentages = [40, 25, 10, 15, 10]
absolute_units = [800, 500, 200, 300, 200]  # Hypothetical energy units in arbitrary units

# Colors for each section of the donut
colors = ['#FFD700', '#8B0000', '#1E90FF', '#32CD32', '#FFA500']

# Explode the first and second slices slightly for emphasis
explode = (0.1, 0.1, 0, 0, 0)

# Create figure and main axis for the donut chart
fig, ax = plt.subplots(figsize=(12, 8), subplot_kw=dict(aspect="equal"))

# Plot donut chart with gradient shading and enhanced shadow
wedges, texts, autotexts = ax.pie(
    percentages, 
    colors=colors, 
    startangle=140, 
    autopct=lambda pct: f'{pct:.1f}%\n({pct*sum(absolute_units)/100:.0f} units)', 
    pctdistance=0.85,
    explode=explode,
    wedgeprops=dict(width=0.3, edgecolor='w', linewidth=2, alpha=0.9),
    shadow=True
)

# Add a circle at the center to create a donut effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white', edgecolor='white', linewidth=1.5)
ax.add_artist(centre_circle)

# Title
ax.set_title("Energy Source Distribution for\nFuture Martian Colonies - 2050", fontsize=16, weight='bold', pad=20)

# Legend with thematic icons
ax.legend(wedges, energy_sources, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Customize text
plt.setp(autotexts, size=9, weight="bold", color='black')
plt.setp(texts, size=12, color='black')

# Inset plot for energy source trend over years
ax_inset = fig.add_axes([0.72, 0.6, 0.2, 0.3])  # Positioning inset
years = [2020, 2030, 2040, 2050]
solar_trend = [20, 30, 35, 40]
nuclear_trend = [15, 20, 23, 25]
ax_inset.plot(years, solar_trend, label='Solar', color='#FFD700', marker='o')
ax_inset.plot(years, nuclear_trend, label='Nuclear', color='#8B0000', marker='o')
ax_inset.set_title("Energy Trends Over Time", fontsize=10)
ax_inset.set_xticks(years)
ax_inset.set_yticks([10, 20, 30, 40])
ax_inset.set_xlabel("Year", fontsize=8)
ax_inset.set_ylabel("Percentage", fontsize=8)
ax_inset.legend(fontsize=8, loc='upper left')
ax_inset.grid(True, linestyle='--', alpha=0.6)

# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Display the chart
plt.show()