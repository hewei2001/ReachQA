import matplotlib.pyplot as plt
import numpy as np

# Define decades and cumulative number of space missions
decades = np.array(['1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s'])
nasa_missions = np.array([5, 30, 80, 130, 190, 250, 300])
esa_missions = np.array([0, 10, 25, 50, 95, 140, 180])
roscosmos_missions = np.array([10, 50, 100, 150, 210, 260, 290])

# Create the plot
plt.figure(figsize=(12, 8))

# Plot data for each space agency
plt.plot(decades, nasa_missions, marker='o', linestyle='-', linewidth=2, color='blue', label='NASA')
plt.plot(decades, esa_missions, marker='s', linestyle='--', linewidth=2, color='green', label='ESA')
plt.plot(decades, roscosmos_missions, marker='^', linestyle='-.', linewidth=2, color='red', label='Roscosmos')

# Annotate notable points
notable_events = {
    '1970s': (nasa_missions[1], "Viking Mars Missions"),
    '2000s': (esa_missions[4], "Rosetta Comet Mission"),
    '1960s': (roscosmos_missions[0], "Luna 9 Moon Landing")
}
for decade, (y_value, event) in notable_events.items():
    plt.annotate(event, xy=(decade, y_value), xytext=(0, 10), textcoords="offset points",
                 ha='center', fontsize=9, color='darkgrey', arrowprops=dict(arrowstyle='->', color='black'))

# Customize plot
plt.title("Exploration of the Cosmos: A Decade-by-Decade Journey of\nSpace Missions", fontsize=16, weight='bold')
plt.xlabel("Decades", fontsize=14)
plt.ylabel("Cumulative Number of Missions", fontsize=14)
plt.xticks(decades, fontsize=12)
plt.yticks(fontsize=12)
plt.legend(loc='upper left', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()