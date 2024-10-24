import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2022
years = np.arange(2010, 2023)

# Successful missions data for each agency
nasa_missions = [5, 6, 7, 8, 10, 12, 15, 18, 20, 21, 22, 25, 26]
esa_missions = [3, 4, 4, 5, 6, 7, 7, 8, 9, 10, 11, 12, 13]
roscosmos_missions = [10, 11, 11, 12, 12, 14, 14, 15, 16, 16, 17, 18, 19]
cnsa_missions = [2, 3, 3, 4, 5, 7, 9, 12, 13, 14, 15, 17, 18]
isro_missions = [1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 10, 11, 13]

# Cumulative successful missions data for each agency
cumulative_data = {
    'NASA': sum(nasa_missions),
    'ESA': sum(esa_missions),
    'Roscosmos': sum(roscosmos_missions),
    'CNSA': sum(cnsa_missions),
    'ISRO': sum(isro_missions)
}

# Create a figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(18, 8))

# Plot line chart on the first subplot
axes[0].plot(years, nasa_missions, marker='o', color='blue', linewidth=2, linestyle='-', label='NASA')
axes[0].plot(years, esa_missions, marker='s', color='green', linewidth=2, linestyle='--', label='ESA')
axes[0].plot(years, roscosmos_missions, marker='^', color='red', linewidth=2, linestyle='-.', label='Roscosmos')
axes[0].plot(years, cnsa_missions, marker='d', color='orange', linewidth=2, linestyle=':', label='CNSA')
axes[0].plot(years, isro_missions, marker='x', color='purple', linewidth=2, linestyle='-', label='ISRO')
axes[0].annotate('NASA Peak', xy=(2022, 26), xytext=(2020, 28), 
                 arrowprops=dict(facecolor='blue', arrowstyle='->'), fontsize=10, color='blue')
axes[0].annotate('ISRO Rapid Growth', xy=(2022, 13), xytext=(2018, 15),
                 arrowprops=dict(facecolor='purple', arrowstyle='->'), fontsize=10, color='purple')
axes[0].set_title('Milestone Missions in Space Exploration\n(2010-2022)', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Year', fontsize=12)
axes[0].set_ylabel('Number of Successful Missions', fontsize=12)
axes[0].grid(True, linestyle='--', alpha=0.6)
axes[0].legend(loc='upper left', fontsize=11)
axes[0].set_xticks(years)
axes[0].tick_params(axis='x', rotation=45)

# Plot bar chart on the second subplot
agency_names = list(cumulative_data.keys())
mission_counts = list(cumulative_data.values())
axes[1].bar(agency_names, mission_counts, color=['blue', 'green', 'red', 'orange', 'purple'])
axes[1].set_title('Cumulative Missions (2010-2022)', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Space Agencies', fontsize=12)
axes[1].set_ylabel('Total Successful Missions', fontsize=12)
axes[1].grid(axis='y', linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()