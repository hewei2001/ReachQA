import matplotlib.pyplot as plt

# Data representing average wait times (in minutes) at peak hours for each transport mode over four quarters
# Quarters: Q1, Q2, Q3, Q4
bus_wait_times = [8, 10, 12, 9, 15, 7, 9, 8, 10, 14, 10, 9, 8, 11, 10, 9, 12, 13, 14, 12]
subway_wait_times = [3, 4, 5, 3, 6, 5, 4, 3, 5, 3, 6, 5, 4, 3, 5, 4, 3, 4, 5, 3]
tram_wait_times = [5, 7, 6, 7, 8, 6, 6, 5, 7, 5, 8, 7, 6, 5, 8, 6, 5, 7, 6, 7]
ferry_wait_times = [10, 12, 11, 13, 14, 11, 12, 10, 11, 12, 14, 13, 11, 10, 13, 12, 11, 14, 13, 12]

# Combine the data into a list of lists for the box plot
wait_times_data = [bus_wait_times, subway_wait_times, tram_wait_times, ferry_wait_times]

# Labels for each transport mode
labels = ['Bus', 'Subway', 'Tram', 'Ferry']

# Plotting the Box Plot
fig, ax = plt.subplots(figsize=(10, 6))

ax.boxplot(wait_times_data, labels=labels, patch_artist=True, notch=True,
           boxprops=dict(facecolor='skyblue', color='darkblue'),
           whiskerprops=dict(color='darkblue'),
           capprops=dict(color='darkblue'),
           medianprops=dict(color='red', linewidth=2),
           flierprops=dict(marker='o', color='orange', markersize=5, alpha=0.6))

# Title and Labels
ax.set_title("Quarterly Passenger Wait Times in\nUrban Public Transport Modes", fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel("Transport Mode", fontsize=12)
ax.set_ylabel("Wait Time (Minutes)", fontsize=12)

# Adding grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Customize y-axis limit to better frame the data
ax.set_ylim(0, 20)

# Automatically adjust layout
plt.tight_layout()

# Displaying the plot
plt.show()