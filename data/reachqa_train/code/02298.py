import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

# Define extended districts of GreenVille
districts = [
    "Central", "North", "East", "South", "West", "Uptown", 
    "Downtown", "Lakeside", "Old Town", "Newbury", "Riverside", "Hilltop"
]

# Define the extended years from 2010 to 2025
years = np.arange(2010, 2026)

# AQI data with more complexity and new metrics
aqi_data = np.array([
    [85, 82, 80, 78, 75, 72, 70, 68, 65, 63, 60, 58, 55, 52, 50, 48],  # Central
    [90, 87, 85, 84, 83, 80, 79, 76, 74, 71, 69, 67, 64, 62, 60, 58],  # North
    [88, 86, 84, 83, 80, 77, 75, 73, 70, 68, 65, 63, 61, 59, 57, 55],  # East
    [92, 89, 88, 86, 84, 82, 79, 78, 76, 74, 72, 70, 68, 66, 64, 62],  # South
    [87, 85, 83, 82, 80, 78, 75, 73, 71, 68, 66, 64, 62, 60, 58, 56],  # West
    [91, 88, 86, 84, 83, 81, 78, 76, 73, 70, 68, 66, 64, 62, 60, 58],  # Uptown
    [93, 90, 88, 87, 85, 82, 80, 78, 76, 73, 70, 68, 66, 64, 62, 60],  # Downtown
    [86, 84, 82, 81, 79, 77, 74, 72, 70, 68, 65, 63, 61, 59, 57, 55],  # Lakeside
    [89, 87, 85, 83, 82, 79, 77, 75, 72, 70, 68, 66, 64, 62, 60, 58],  # Old Town
    [85, 83, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54],  # Newbury
    [88, 86, 84, 82, 80, 77, 75, 73, 71, 69, 67, 65, 63, 61, 59, 57],  # Riverside
    [87, 85, 83, 81, 79, 77, 75, 73, 71, 69, 67, 65, 63, 61, 59, 57]   # Hilltop
])

# Transpose data for correct orientation in heatmap
aqi_data_transposed = aqi_data.T

# Create a grid for multiple plots
fig = plt.figure(figsize=(16, 10))
gs = gridspec.GridSpec(2, 1, height_ratios=[4, 1])

# Main heatmap plot
ax0 = plt.subplot(gs[0])
heatmap = ax0.imshow(aqi_data_transposed, cmap='YlGn', aspect='auto', interpolation='nearest')

ax0.set_title("Air Quality Improvement in GreenVille Districts\nA Decade and Half of Green Initiatives", fontsize=16, fontweight='bold', pad=20)
ax0.set_xlabel('Districts of GreenVille', fontsize=12)
ax0.set_ylabel('Year', fontsize=12)
ax0.set_xticks(np.arange(len(districts)))
ax0.set_xticklabels(districts, rotation=45, ha='right')
ax0.set_yticks(np.arange(len(years)))
ax0.set_yticklabels(years)

# Add a color bar to the heatmap
cbar = plt.colorbar(heatmap, ax=ax0, orientation='vertical')
cbar.set_label('Air Quality Index (AQI)', fontsize=12)
cbar.ax.invert_yaxis()

# Annotate each cell with AQI value
for i in range(len(years)):
    for j in range(len(districts)):
        ax0.text(j, i, aqi_data_transposed[i, j], ha='center', va='center', color='black', fontsize=8)

# Additional bar chart for total improvement
ax1 = plt.subplot(gs[1])
total_improvement = aqi_data[:, 0] - aqi_data[:, -1]
ax1.bar(districts, total_improvement, color='darkgreen')
ax1.set_title("Total AQI Reduction Over Time per District", fontsize=12, pad=10)
ax1.set_ylabel('Total AQI Reduction', fontsize=10)
ax1.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()