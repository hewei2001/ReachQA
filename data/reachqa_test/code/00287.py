import numpy as np
import matplotlib.pyplot as plt

# Define time intervals (hours of the day)
time_intervals = np.arange(0, 24, 2)

# Solar energy production data for each season
spring_production = [0, 0, 2, 5, 10, 15, 18, 15, 10, 5, 2, 0]
summer_production = [0, 0, 3, 8, 14, 20, 25, 20, 14, 8, 3, 0]
autumn_production = [0, 0, 1, 3, 7, 12, 15, 12, 7, 3, 1, 0]
winter_production = [0, 0, 0, 1, 3, 6, 8, 6, 3, 1, 0, 0]

# Calculate average production
average_production = np.mean([spring_production, summer_production, autumn_production, winter_production], axis=0)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Plot area for each season
ax.fill_between(time_intervals, spring_production, label='Spring', color='lightgreen', alpha=0.6)
ax.fill_between(time_intervals, summer_production, label='Summer', color='gold', alpha=0.6)
ax.fill_between(time_intervals, autumn_production, label='Autumn', color='orange', alpha=0.6)
ax.fill_between(time_intervals, winter_production, label='Winter', color='lightblue', alpha=0.6)

# Overlay line plot for average production
ax.plot(time_intervals, average_production, label='Average Production', color='darkred', linestyle='--', linewidth=2, marker='o')

# Set titles and labels
ax.set_title('Solar Energy Production Throughout the Day\nin Different Seasons with Average Overlay', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Time of Day (Hours)', fontsize=12)
ax.set_ylabel('Energy Production (kW)', fontsize=12)

# Customize x and y ticks
ax.set_xticks(time_intervals)
ax.set_xticklabels([f'{int(t)}:00' for t in time_intervals], rotation=45, fontsize=10)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Add a legend
ax.legend(loc='upper left', fontsize=10, title='Seasons & Average', title_fontsize='13')

# Enhancing the appearance with a background color
fig.patch.set_facecolor('#f7f7f7')

# Add annotations for peak average production
peak_index = np.argmax(average_production)
peak_time = time_intervals[peak_index]
peak_value = average_production[peak_index]
ax.annotate(f'Peak\n{peak_value:.1f} kW', xy=(peak_time, peak_value), xytext=(peak_time+1, peak_value+2),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkred')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()