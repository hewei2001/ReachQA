import matplotlib.pyplot as plt
import numpy as np

# Months of the year
months = np.arange(1, 13)

# Migration distance in kilometers (hypothetical data)
migration_distances = np.array([500, 800, 1300, 2000, 2500, 1800, 900, 1500, 2300, 2800, 1700, 800])

# Hypothetical average temperature data (°C) for added context
average_temperatures = np.array([5, 7, 10, 15, 20, 25, 30, 28, 22, 17, 10, 6])

# Annotations for key migration points
annotations = {
    4: "Breeding Grounds",
    7: "Feeding Area",
    10: "Resting Point"
}

# Create the main plot
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot the migration data
migration_line = ax1.plot(months, migration_distances, marker='o', linestyle='-', color='teal', linewidth=2, label='Migration Distance')

# Fill between the curve and a reference value (e.g., 1000 km)
ax1.fill_between(months, migration_distances, 1000, color='lightblue', alpha=0.2)

# Add annotations for key points in migration
for month, label in annotations.items():
    ax1.annotate(label,
                 (month, migration_distances[month - 1]),
                 textcoords="offset points",
                 xytext=(-30, 15),
                 ha='center',
                 fontsize=9,
                 bbox=dict(boxstyle="round,pad=0.3", edgecolor='blue', facecolor='lightyellow', alpha=0.7),
                 arrowprops=dict(arrowstyle='->', connectionstyle="arc3", color='blue'))

# Annotate each data point with its distance
for month, distance in zip(months, migration_distances):
    ax1.text(month, distance, f"{distance} km", fontsize=9, va='bottom', ha='right', color='black', rotation=45)

# Secondary y-axis for average temperature
ax2 = ax1.twinx()
temp_line = ax2.plot(months, average_temperatures, color='red', linestyle='--', linewidth=2, label='Avg Temperature (°C)')

# Adding titles and labels
ax1.set_title('Migration Patterns of\nPacific Blue Giants & Associated Temperatures', fontsize=16, fontweight='bold')
ax1.set_xlabel('Month', fontsize=12)
ax1.set_ylabel('Migration Distance (km)', fontsize=12)
ax2.set_ylabel('Average Temperature (°C)', fontsize=12)

# Customize the x-axis with month labels
ax1.set_xticks(months)
ax1.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                     'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)

# Add gridlines for clarity
ax1.grid(True, linestyle='--', alpha=0.5)

# Combine legends from both axes
lines = migration_line + temp_line
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc='upper left', fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()