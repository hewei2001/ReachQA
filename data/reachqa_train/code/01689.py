import matplotlib.pyplot as plt
import numpy as np

# Years for the timeline
years = np.arange(2000, 2026)

# Area data for each type of green space (in square kilometers)
parks_area = [15, 16, 17, 18, 19, 20, 22, 24, 26, 28, 30, 32, 35, 39, 42, 45, 48, 52, 55, 58, 61, 65, 70, 75, 80, 85]
community_gardens_area = [1, 1.2, 1.5, 1.8, 2.1, 2.5, 2.9, 3.4, 3.9, 4.5, 5.1, 5.8, 6.5, 7.3, 8.1, 9.0, 10.0, 11.1, 12.3, 13.6, 15, 16.5, 18, 19.5, 21, 22.5]
rooftop_gardens_area = [0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 1.0, 1.3, 1.7, 2.2, 2.7, 3.3, 4.0, 4.8, 5.7, 6.7, 7.8, 9.0, 10.3, 11.7, 13.2, 14.8, 16.5, 18.3, 20.2, 22.2]
green_corridors_area = [2, 2.1, 2.3, 2.6, 2.9, 3.3, 3.8, 4.4, 5.0, 5.7, 6.5, 7.4, 8.4, 9.5, 10.7, 12.0, 13.4, 14.9, 16.5, 18.2, 20, 22, 24.2, 26.5, 29, 31.6]

# Calculate the total area and annual changes
total_area = np.array(parks_area) + np.array(community_gardens_area) + np.array(rooftop_gardens_area) + np.array(green_corridors_area)
annual_change = np.diff(total_area, prepend=0)

# Plot setup with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Subplot 1: Line chart of green spaces evolution
ax1.plot(years, parks_area, label='Parks', color='forestgreen', linestyle='-', marker='o', linewidth=2)
ax1.plot(years, community_gardens_area, label='Community Gardens', color='orange', linestyle='-', marker='s', linewidth=2)
ax1.plot(years, rooftop_gardens_area, label='Rooftop Gardens', color='royalblue', linestyle='-', marker='^', linewidth=2)
ax1.plot(years, green_corridors_area, label='Green Corridors', color='darkred', linestyle='-', marker='x', linewidth=2)

ax1.set_title('Evolution of Urban Green Spaces\n(2000-2025)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Area (Square Kilometers)', fontsize=12)
ax1.set_xticks(years[::2])
ax1.set_xticklabels(years[::2], rotation=45)
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax1.legend(title='Types of Green Spaces', fontsize=10, loc='upper left')

# Annotate key milestones
milestones = {2010: ('Rooftop Gardens Start', 2), 2020: ('Community Gardens Peak', 18)}
for year, (text, y_pos) in milestones.items():
    ax1.annotate(text, xy=(year, y_pos), xytext=(year, y_pos + 5),
                 arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9, ha='center')

# Subplot 2: Bar chart of annual change in total area
ax2.bar(years, annual_change, color=['green' if x >= 0 else 'red' for x in annual_change])
ax2.set_title('Annual Change in Total Green Space Area\n(2000-2025)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Annual Change (Square Kilometers)', fontsize=12)
ax2.set_xticks(years[::2])
ax2.set_xticklabels(years[::2], rotation=45)
ax2.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()