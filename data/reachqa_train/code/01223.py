import matplotlib.pyplot as plt
import numpy as np

# Mission types and their proportions
mission_types = ['Landing Missions', 'Orbital Studies', 'Rover Explorations', 'Flyby Missions', 'Sample Return']
missions_proportions = [20, 35, 25, 10, 10]

# Hypothetical total missions and estimated count per mission type
total_missions = 1000
estimated_counts = [proportion * total_missions / 100 for proportion in missions_proportions]
error_margin = [5, 10, 7, 3, 3]  # Example error margins

# Define colors for each mission type
colors = ['#FFA07A', '#8A2BE2', '#7FFF00', '#DC143C', '#FFD700']

# Initialize the figure and two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Plot the original ring chart
wedges, texts, autotexts = ax1.pie(
    missions_proportions, labels=mission_types, autopct='%1.1f%%', startangle=140,
    colors=colors, pctdistance=0.85, wedgeprops=dict(width=0.3, edgecolor='white'))

plt.setp(autotexts, size=12, weight="bold", color='white')
plt.setp(texts, size=10)

ax1.set_title('AstroVentures Missions (2000-2023)\nPlanetary Exploration Focus', fontsize=14, weight='bold', pad=20)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

ax1.axis('equal')

ax1.legend(wedges, mission_types, title="Mission Types", loc='center left', bbox_to_anchor=(-0.4, 0.5), fontsize=10)
ax1.annotate('Focus on\nOrbital Studies', xy=(-0.7, 0.3), xytext=(-1.5, 0.9),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, ha='center', backgroundcolor='lightgrey')

# Plot the new bar chart
x = np.arange(len(mission_types))
ax2.bar(x, estimated_counts, yerr=error_margin, color=colors, capsize=5)

ax2.set_xticks(x)
ax2.set_xticklabels(mission_types, rotation=45, ha='right')
ax2.set_ylabel('Estimated Mission Count')
ax2.set_title('Estimated Mission Counts with Error Margins', fontsize=14, weight='bold')
ax2.set_xlabel('Mission Types')
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Show both plots and ensure layout is optimized
plt.tight_layout()
plt.show()