import matplotlib.pyplot as plt
import numpy as np

# Data for box plot
digital_dreams_times = [25, 30, 45, 60, 40, 55, 70, 50, 65, 35]
soundscapes_times = [15, 20, 18, 22, 17, 19, 25, 20, 21, 16]
light_labyrinths_times = [30, 45, 35, 50, 40, 60, 55, 45, 50, 40]
kinetic_kinetics_times = [10, 15, 20, 25, 15, 18, 22, 20, 19, 17]
virtual_voyages_times = [60, 75, 90, 70, 80, 85, 95, 88, 72, 78]

# Combining data
box_data = [
    digital_dreams_times,
    soundscapes_times,
    light_labyrinths_times,
    kinetic_kinetics_times,
    virtual_voyages_times
]

# Labels for thematic zones
zones = [
    "Digital Dreams",
    "Soundscapes",
    "Light Labyrinths",
    "Kinetic Kinetics",
    "Virtual Voyages"
]

# New data for the line plot (average time spent over 10 days)
days = np.arange(1, 11)
avg_times = {
    "Digital Dreams": [45, 47, 50, 48, 46, 51, 52, 49, 53, 50],
    "Soundscapes": [19, 21, 20, 18, 22, 23, 21, 20, 19, 21],
    "Light Labyrinths": [40, 42, 45, 43, 41, 46, 47, 44, 48, 45],
    "Kinetic Kinetics": [17, 18, 20, 19, 17, 21, 20, 18, 19, 18],
    "Virtual Voyages": [80, 82, 85, 84, 81, 86, 88, 85, 87, 84]
}

# Create a 2x1 subplot layout
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

# Create horizontal box plot
bp = ax1.boxplot(box_data, vert=False, patch_artist=True, notch=True, whis=1.5)
colors = ['skyblue', 'lightgreen', 'lightcoral', 'lightgoldenrodyellow', 'lightpink']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

ax1.set_title("Visitor Engagement in Thematic Zones at 'Echoes of Tomorrow'\nFuturistic Art Exhibition", fontsize=13, pad=15)
ax1.set_xlabel("Time Spent (minutes)", fontsize=12)
ax1.set_yticks(np.arange(1, len(zones) + 1))
ax1.set_yticklabels(zones, fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.set_xlim(0, 100)

# Annotations for box plot
ax1.annotate('High Engagement', xy=(85, 5), xytext=(90, 5.5),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkred')
ax1.annotate('Balanced Interest', xy=(45, 3), xytext=(70, 3.5),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkgreen')

# Create a line plot for average times
for zone, times in avg_times.items():
    ax2.plot(days, times, label=zone, marker='o')

ax2.set_title("Average Time Spent Across 10 Days\nin Each Thematic Zone", fontsize=13, pad=15)
ax2.set_xlabel("Days", fontsize=12)
ax2.set_ylabel("Average Time Spent (minutes)", fontsize=12)
ax2.set_xticks(days)
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.legend(title="Zones", fontsize=10, loc='upper left')

# Automatically adjust layout
plt.tight_layout()

# Show the plots
plt.show()