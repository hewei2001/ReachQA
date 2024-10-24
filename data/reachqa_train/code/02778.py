import matplotlib.pyplot as plt
import numpy as np

# Regions known for vibrant festivals
regions = [
    "Carnival City", 
    "Festival Valley", 
    "Heritage Plains", 
    "Tradition Town", 
    "Celebration Heights"
]

# Artificial attendance data (in thousands) for each region
attendance_data = [
    [45, 47, 50, 55, 60, 65, 50, 45, 55, 50],  # Carnival City
    [20, 22, 23, 25, 30, 35, 28, 26, 29, 33],  # Festival Valley
    [55, 60, 65, 70, 68, 72, 75, 63, 64, 67],  # Heritage Plains
    [30, 32, 31, 40, 35, 38, 36, 33, 30, 37],  # Tradition Town
    [10, 15, 10, 12, 11, 15, 17, 18, 14, 13]   # Celebration Heights
]

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Create horizontal boxplot
bp = ax.boxplot(attendance_data, vert=False, patch_artist=True, showmeans=True, notch=True,
                boxprops=dict(facecolor="#add8e6", color="#000080", linewidth=1.2), 
                medianprops=dict(color="#ff4500", linewidth=1.5),
                meanprops=dict(marker='D', markeredgecolor='black', markerfacecolor='#32cd32'),
                whiskerprops=dict(color="#000080"), capprops=dict(color="#000080"))

# Customize the y-axis with region names
ax.set_yticklabels(regions, fontsize=11)

# Set titles and labels
ax.set_title("Annual Traditional Festival Attendance\nAcross Regions in 2022", fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel("Number of Attendees (in thousands)", fontsize=12)
ax.set_ylabel("Regions", fontsize=12)

# Add grid for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout for better fit
plt.tight_layout()

# Display the plot
plt.show()