import matplotlib.pyplot as plt
import numpy as np

# Define regions
regions = [
    "Carnival City", 
    "Festival Valley", 
    "Heritage Plains", 
    "Tradition Town", 
    "Celebration Heights"
]

# Define attendance data (in thousands) for each region
attendance_data = [
    [45, 47, 50, 55, 60, 65, 50, 45, 55, 50],  # Carnival City
    [20, 22, 23, 25, 30, 35, 28, 26, 29, 33],  # Festival Valley
    [55, 60, 65, 70, 68, 72, 75, 63, 64, 67],  # Heritage Plains
    [30, 32, 31, 40, 35, 38, 36, 33, 30, 37],  # Tradition Town
    [10, 15, 10, 12, 11, 15, 17, 18, 14, 13]   # Celebration Heights
]

# Create synthetic time data for scatter plot
months = np.arange(1, 11)

# Set up the plot with two subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 7))

# Boxplot on the left
ax1 = axes[0]
bp = ax1.boxplot(attendance_data, vert=False, patch_artist=True, showmeans=True, notch=True,
                 boxprops=dict(facecolor="#add8e6", color="#000080", linewidth=1.2), 
                 medianprops=dict(color="#ff4500", linewidth=1.5),
                 meanprops=dict(marker='D', markeredgecolor='black', markerfacecolor='#32cd32'),
                 whiskerprops=dict(color="#000080"), capprops=dict(color="#000080"))

ax1.set_yticklabels(regions, fontsize=11)
ax1.set_title("Annual Traditional Festival Attendance\nAcross Regions in 2022", fontsize=14, fontweight='bold', pad=15)
ax1.set_xlabel("Number of Attendees (in thousands)", fontsize=12)
ax1.set_ylabel("Regions", fontsize=12)
ax1.xaxis.grid(True, linestyle='--', alpha=0.7)

# Scatter plot on the right
ax2 = axes[1]
for idx, region_data in enumerate(attendance_data):
    ax2.scatter(months, region_data, label=regions[idx], s=100, alpha=0.7, edgecolors='w')

ax2.set_title("Monthly Festival Attendance Trends in 2022", fontsize=14, fontweight='bold', pad=15)
ax2.set_xlabel("Months", fontsize=12)
ax2.set_ylabel("Number of Attendees (in thousands)", fontsize=12)
ax2.legend(title='Regions', fontsize=9, title_fontsize=10)
ax2.yaxis.grid(True, linestyle='--', alpha=0.7)
ax2.set_xticks(months)
ax2.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"])

# Adjust layout for better fit
plt.tight_layout()

# Display the plots
plt.show()