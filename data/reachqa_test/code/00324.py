import matplotlib.pyplot as plt
import numpy as np

# Data for urban fox sightings in different time slots
time_slots = ['Midnight-4AM', '4AM-8AM', '8AM-12PM', '12PM-4PM', '4PM-8PM', '8PM-Midnight']
sightings = [40, 35, 10, 5, 15, 45]  # Higher activity at night and early morning

# Related data: Noise levels in the city (decibels)
noise_levels = [30, 45, 60, 65, 55, 35]  # Hypothetical data

# Colors corresponding to time slots (dark for night, light for day)
colors = ['#2E4053', '#283747', '#F4D03F', '#F8C471', '#2874A6', '#1C2833']

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot histogram manually using bar() to apply different colors
for i in range(len(sightings)):
    ax1.bar(i, sightings[i], color=colors[i], edgecolor='black', linewidth=1.2, alpha=0.9)

# Add titles and labels
ax1.set_title('Urban Fox Activity Patterns\nSightings and Noise Levels Across Different Times of Day', fontsize=16, fontweight='bold')
ax1.set_xlabel('Time of Day', fontsize=14)
ax1.set_ylabel('Number of Sightings', fontsize=14, color='black')

# Set x-ticks to match the time slots, with rotation for clarity
ax1.set_xticks(np.arange(len(time_slots)))
ax1.set_xticklabels(time_slots, rotation=45, ha='right')

# Annotate each bar with the number of sightings
for i, count in enumerate(sightings):
    ax1.text(i, count + 1, str(count), ha='center', va='bottom', fontsize=11, fontweight='bold')

# Add gridlines for better readability
ax1.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

# Secondary axis for noise levels
ax2 = ax1.twinx()
ax2.plot(np.arange(len(noise_levels)), noise_levels, color='orange', linestyle='--', marker='o', linewidth=2, label='Noise Levels (dB)')
ax2.set_ylabel('Noise Levels (dB)', fontsize=14, color='orange')

# Add legend for secondary plot
ax1.legend(['Fox Sightings'], loc='upper left')
ax2.legend(loc='upper right')

# Automatically adjust layout for better fitting
plt.tight_layout()

# Display the plot
plt.show()