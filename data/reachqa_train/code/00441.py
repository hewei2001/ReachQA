import matplotlib.pyplot as plt
import numpy as np

# Define the research categories and mission counts
categories = [
    'Planetary Exploration', 'Human Health',
    'Astrophysics', 'Satellite Tech', 'Earth Sciences',
    'Exoplanet Studies', 'Space Physics'
]
missions_count = np.array([50, 30, 45, 25, 40, 15, 35])

# Additional data for the line chart (Hypothetical trend data)
years = np.arange(1990, 2021, 5)
missions_trend = {
    'Planetary Exploration': [10, 20, 25, 35, 40, 50, 55],
    'Astrophysics': [5, 15, 20, 30, 40, 45, 48]
}

# Calculate the angles for the rose chart in polar coordinates
num_categories = len(categories)
angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()
angles += angles[:1]
missions_count = np.append(missions_count, missions_count[0])

# Create the figure and two subplots (polar and line chart)
fig, axs = plt.subplots(1, 2, figsize=(14, 7), subplot_kw=dict(polar=False))
fig.suptitle("Space Missions Analysis (1990-2020)\nInsights Across Various Research Domains", 
             fontsize=16, fontweight='bold', ha='center', y=1.05)

# Plot the rose chart
ax1 = plt.subplot(121, polar=True)
colors = ['#FF6347', '#FFD700', '#ADFF2F', '#20B2AA', '#9370DB', '#FF69B4', '#FF4500']
bars = ax1.bar(angles[:-1], missions_count[:-1], width=2*np.pi/num_categories, 
               color=colors, alpha=0.7, edgecolor='black', linewidth=1.5)
ax1.set_xticks(angles[:-1])
ax1.set_xticklabels(categories, fontsize=9, fontweight='bold')
ax1.set_ylim(0, max(missions_count) + 10)
ax1.yaxis.grid(True, linestyle='--', alpha=0.5)
ax1.legend(bars, categories, title="Research Focus", loc="upper right", bbox_to_anchor=(1.1, 1.1), fontsize=8)
ax1.set_title("Diversity in Research Objectives", fontsize=12, fontweight='bold', loc='center', pad=20)

# Plot the line chart
ax2 = plt.subplot(122)
for category, trend in missions_trend.items():
    ax2.plot(years, trend, marker='o', label=category)

ax2.set_title("Mission Trends Over Time", fontsize=12, fontweight='bold')
ax2.set_xlabel('Year')
ax2.set_ylabel('Number of Missions')
ax2.set_xticks(years)
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend(title="Research Category", loc="upper left", fontsize=9)

# Adjust layout to avoid overlap
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Display the combined plots
plt.show()