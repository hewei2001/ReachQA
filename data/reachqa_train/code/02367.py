import matplotlib.pyplot as plt
import numpy as np

# Define the years and mission success rates
years = np.arange(2000, 2021)
success_rates = [
    85, 80, 82, 88, 90, 92, 93, 95, 94, 96, 98, 97, 99, 92, 91, 93, 95, 97, 98, 99, 100
]

# Constructing related data for the additional plot
# Total number of missions per year (hypothetical data)
total_missions = [12, 14, 15, 13, 16, 18, 20, 22, 21, 23, 25, 24, 28, 30, 32, 30, 33, 35, 36, 38, 40]
failure_rates = [100 - rate for rate in success_rates]  # Calculate failure rates

# Annotations for significant events
annotations = {
    2003: "First Mars Rover\nSuccessful Landing",
    2006: "First Exoplanet\nDiscovered",
    2010: "Major Satellite\nDeployment",
    2015: "Interstellar\nProbe Launched",
    2020: "100th Mission\nAchieved"
}

# Create figure and subplots
fig, axs = plt.subplots(2, 1, figsize=(14, 12), gridspec_kw={'hspace': 0.3})

# Line chart for success rates
axs[0].plot(years, success_rates, color='teal', marker='o', linestyle='-', linewidth=2, markersize=6, label='Success Rate')
axs[0].set_title("Success Rates of Space Missions:\nA Journey Through the Cosmos", fontsize=16, fontweight='bold')
axs[0].set_xlabel("Year", fontsize=12)
axs[0].set_ylabel("Success Rate (%)", fontsize=12)
axs[0].set_xticks(years)
axs[0].set_yticks(np.arange(80, 101, 2))
axs[0].grid(True, linestyle='--', alpha=0.7)

# Add annotations for significant years
for year, event in annotations.items():
    axs[0].annotate(event,
                    xy=(year, success_rates[year - 2000]),
                    xytext=(year, success_rates[year - 2000] - 10),
                    arrowprops=dict(facecolor='black', arrowstyle='->', lw=0.8),
                    fontsize=9,
                    ha='center',
                    bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightyellow'))

# Highlighting the 100% success rate point
axs[0].scatter([2020], [100], color='darkred', marker='D', s=80, label='Milestone: 100th Success')

# Adding a legend
axs[0].legend(loc='lower right', fontsize=10, frameon=False)

# Bar chart for failure rates and total missions
axs[1].bar(years - 0.2, total_missions, width=0.4, color='skyblue', label='Total Missions')
axs[1].bar(years + 0.2, failure_rates, width=0.4, color='salmon', label='Failure Rate')

axs[1].set_title("Mission Counts and Failure Rates", fontsize=14, fontweight='bold')
axs[1].set_xlabel("Year", fontsize=12)
axs[1].set_ylabel("Count / Failure Rate (%)", fontsize=12)
axs[1].set_xticks(years)
axs[1].grid(True, linestyle='--', alpha=0.7)
axs[1].legend(loc='upper left', fontsize=10, frameon=False)

# Adjust layout to ensure no overlapping text
plt.tight_layout()

# Display the plots
plt.show()