import matplotlib.pyplot as plt
import numpy as np

# Define decades and cumulative number of space missions
decades = np.array(['1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s'])
nasa_missions = np.array([5, 30, 80, 130, 190, 250, 300])
esa_missions = np.array([0, 10, 25, 50, 95, 140, 180])
roscosmos_missions = np.array([10, 50, 100, 150, 210, 260, 290])

# Define related data for the overlay bar chart
nasa_probes = np.array([1, 5, 15, 20, 45, 55, 70])
esa_probes = np.array([0, 2, 5, 10, 20, 30, 35])
roscosmos_probes = np.array([2, 10, 20, 35, 50, 65, 75])

# Create the main plot with overlays
fig, ax1 = plt.subplots(figsize=(14, 8))

# Line plot for cumulative missions
ax1.plot(decades, nasa_missions, marker='o', linestyle='-', linewidth=2, color='blue', label='NASA Missions')
ax1.plot(decades, esa_missions, marker='s', linestyle='--', linewidth=2, color='green', label='ESA Missions')
ax1.plot(decades, roscosmos_missions, marker='^', linestyle='-.', linewidth=2, color='red', label='Roscosmos Missions')

# Overlay bar chart for space probes
ax2 = ax1.twinx()
width = 0.2  # Width of bars
ax2.bar(decades, nasa_probes, width, alpha=0.4, color='blue', label='NASA Probes', align='center')
ax2.bar(decades, esa_probes, width, alpha=0.4, color='green', label='ESA Probes', align='center')
ax2.bar(decades, roscosmos_probes, width, alpha=0.4, color='red', label='Roscosmos Probes', align='center')

# Annotate notable points
notable_events = {
    '1970s': (nasa_missions[1], "Viking Mars Missions"),
    '2000s': (esa_missions[4], "Rosetta Comet Mission"),
    '1960s': (roscosmos_missions[0], "Luna 9 Moon Landing")
}
for decade, (y_value, event) in notable_events.items():
    ax1.annotate(event, xy=(decade, y_value), xytext=(0, 10), textcoords="offset points",
                 ha='center', fontsize=9, color='darkgrey', arrowprops=dict(arrowstyle='->', color='black'))

# Customize the main plot
ax1.set_title("Exploration of the Cosmos: A Decade-by-Decade Journey of\nSpace Missions and Probes", fontsize=16, weight='bold')
ax1.set_xlabel("Decades", fontsize=14)
ax1.set_ylabel("Cumulative Number of Missions", fontsize=14, color='black')
ax1.tick_params(axis='y', labelcolor='black')
ax1.set_xticks(decades)
ax1.set_xticklabels(decades, fontsize=12)
ax1.legend(loc='upper left', fontsize=10)

# Customize the secondary plot
ax2.set_ylabel('Number of Space Probes', fontsize=14, color='gray')
ax2.tick_params(axis='y', labelcolor='gray')
ax2.legend(loc='upper right', fontsize=10)

# Grid and layout adjustment
ax1.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# Display the plot
plt.show()