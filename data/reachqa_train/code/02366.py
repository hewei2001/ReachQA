import matplotlib.pyplot as plt
import numpy as np

# Define the years and mission success rates
years = np.arange(2000, 2021)
success_rates = [
    85, 80, 82, 88, 90, 92, 93, 95, 94, 96, 98, 97, 99, 92, 91, 93, 95, 97, 98, 99, 100
]

# Annotations for significant events
annotations = {
    2003: "First Mars Rover\nSuccessful Landing",
    2006: "First Exoplanet\nDiscovered",
    2010: "Major Satellite\nDeployment",
    2015: "Interstellar\nProbe Launched",
    2020: "100th Mission\nAchieved"
}

# Plot the line chart
plt.figure(figsize=(14, 8))
plt.plot(years, success_rates, color='teal', marker='o', linestyle='-', linewidth=2, markersize=6, label='Success Rate')

# Add annotations for significant years
for year, event in annotations.items():
    plt.annotate(event,
                 xy=(year, success_rates[year - 2000]),
                 xytext=(year, success_rates[year - 2000] - 10),
                 arrowprops=dict(facecolor='black', arrowstyle='->', lw=0.8),
                 fontsize=9,
                 ha='center',
                 bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightyellow'))

# Customizing the plot
plt.title("Success Rates of Space Missions: A Journey\nThrough the Cosmos", fontsize=16, fontweight='bold', ha='center')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Success Rate (%)", fontsize=12)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(80, 101, 2))
plt.grid(True, linestyle='--', alpha=0.7)

# Highlighting the 100% success rate point
plt.scatter([2020], [100], color='darkred', marker='D', s=80, label='Milestone: 100th Success')

# Adding a legend
plt.legend(loc='lower right', fontsize=10, frameon=False)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()