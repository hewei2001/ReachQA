import matplotlib.pyplot as plt
import numpy as np

# Data representing average wait times (in minutes) at peak hours for each transport mode over four quarters
# Quarters: Q1, Q2, Q3, Q4
bus_wait_times = [8, 10, 12, 9, 15, 7, 9, 8, 10, 14, 10, 9, 8, 11, 10, 9, 12, 13, 14, 12]
subway_wait_times = [3, 4, 5, 3, 6, 5, 4, 3, 5, 3, 6, 5, 4, 3, 5, 4, 3, 4, 5, 3]
tram_wait_times = [5, 7, 6, 7, 8, 6, 6, 5, 7, 5, 8, 7, 6, 5, 8, 6, 5, 7, 6, 7]
ferry_wait_times = [10, 12, 11, 13, 14, 11, 12, 10, 11, 12, 14, 13, 11, 10, 13, 12, 11, 14, 13, 12]

# Quarters division
quarters = ['Q1', 'Q2', 'Q3', 'Q4']

# Calculate average wait times per quarter for each transport mode
bus_avg = np.mean(np.reshape(bus_wait_times, (4, 5)), axis=1)
subway_avg = np.mean(np.reshape(subway_wait_times, (4, 5)), axis=1)
tram_avg = np.mean(np.reshape(tram_wait_times, (4, 5)), axis=1)
ferry_avg = np.mean(np.reshape(ferry_wait_times, (4, 5)), axis=1)

# Plotting
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Box Plot
axs[0].boxplot([bus_wait_times, subway_wait_times, tram_wait_times, ferry_wait_times],
               labels=['Bus', 'Subway', 'Tram', 'Ferry'], patch_artist=True, notch=True,
               boxprops=dict(facecolor='skyblue', color='darkblue'),
               whiskerprops=dict(color='darkblue'),
               capprops=dict(color='darkblue'),
               medianprops=dict(color='red', linewidth=2),
               flierprops=dict(marker='o', color='orange', markersize=5, alpha=0.6))
axs[0].set_title("Quarterly Passenger Wait Times in\nUrban Public Transport Modes", fontsize=14, fontweight='bold', pad=20)
axs[0].set_xlabel("Transport Mode", fontsize=12)
axs[0].set_ylabel("Wait Time (Minutes)", fontsize=12)
axs[0].yaxis.grid(True, linestyle='--', alpha=0.7)
axs[0].set_ylim(0, 20)

# Line Plot
axs[1].plot(quarters, bus_avg, marker='o', linestyle='-', color='blue', label='Bus')
axs[1].plot(quarters, subway_avg, marker='s', linestyle='--', color='green', label='Subway')
axs[1].plot(quarters, tram_avg, marker='^', linestyle='-.', color='purple', label='Tram')
axs[1].plot(quarters, ferry_avg, marker='d', linestyle=':', color='orange', label='Ferry')
axs[1].set_title("Average Wait Times per Quarter", fontsize=14, fontweight='bold')
axs[1].set_xlabel("Quarters", fontsize=12)
axs[1].set_ylabel("Average Wait Time (Minutes)", fontsize=12)
axs[1].legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)
axs[1].yaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout
plt.tight_layout(rect=[0, 0, 0.95, 1])  # Adjust to leave space for legend

# Display the plots
plt.show()