import matplotlib.pyplot as plt
import numpy as np

# Months of the year
months = np.arange(1, 13)

# Migration distance in kilometers (hypothetical data)
migration_distances = np.array([500, 800, 1300, 2000, 2500, 1800, 900, 1500, 2300, 2800, 1700, 800])

# Annotations for key migration points
annotations = {
    4: "Breeding Grounds",
    7: "Feeding Area",
    10: "Resting Point"
}

# Create the line chart
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the migration data
ax.plot(months, migration_distances, marker='o', linestyle='-', color='teal', linewidth=2, label='Migration Distance')

# Add annotations for key points in migration
for month, label in annotations.items():
    ax.annotate(label,
                (month, migration_distances[month - 1]),
                textcoords="offset points",
                xytext=(-20, 15),  # Position of the text
                ha='center',
                fontsize=10,
                bbox=dict(boxstyle="round,pad=0.3", edgecolor='blue', facecolor='lightyellow', alpha=0.7),
                arrowprops=dict(arrowstyle='->', connectionstyle="arc3", color='blue'))

# Annotate each data point with its distance
for month, distance in zip(months, migration_distances):
    ax.text(month, distance, f"{distance} km", fontsize=9, va='bottom', ha='right', color='black', rotation=45)

# Adding title and labels
ax.set_title('Migration Patterns of\nPacific Blue Giants', fontsize=16, fontweight='bold')
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Migration Distance (km)', fontsize=12)

# Customize the x-axis with month labels
ax.set_xticks(months)
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)

# Add gridlines for clarity
ax.grid(True, linestyle='--', alpha=0.5)

# Place the legend
ax.legend(loc='upper left', fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()