import matplotlib.pyplot as plt
import numpy as np

# Data: Time spent in each section by visitors, in minutes
digital_dreams_times = [25, 30, 45, 60, 40, 55, 70, 50, 65, 35]
soundscapes_times = [15, 20, 18, 22, 17, 19, 25, 20, 21, 16]
light_labyrinths_times = [30, 45, 35, 50, 40, 60, 55, 45, 50, 40]
kinetic_kinetics_times = [10, 15, 20, 25, 15, 18, 22, 20, 19, 17]
virtual_voyages_times = [60, 75, 90, 70, 80, 85, 95, 88, 72, 78]

# Combine all data for box plot
data = [
    digital_dreams_times,
    soundscapes_times,
    light_labyrinths_times,
    kinetic_kinetics_times,
    virtual_voyages_times
]

# Labels for each thematic zone
zones = [
    "Digital Dreams",
    "Soundscapes",
    "Light Labyrinths",
    "Kinetic Kinetics",
    "Virtual Voyages"
]

# Create a horizontal box plot
fig, ax = plt.subplots(figsize=(12, 6))
bp = ax.boxplot(data, vert=False, patch_artist=True, notch=True, whis=1.5)

# Set colors for each box
colors = ['skyblue', 'lightgreen', 'lightcoral', 'lightgoldenrodyellow', 'lightpink']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Title and labels
ax.set_title("Visitor Engagement in Thematic Zones at 'Echoes of Tomorrow'\nFuturistic Art Exhibition", fontsize=14, pad=20)
ax.set_xlabel("Time Spent (minutes)", fontsize=12)
ax.set_yticks(np.arange(1, len(zones) + 1))
ax.set_yticklabels(zones, fontsize=10)

# Customizing plot appearance
ax.grid(True, linestyle='--', alpha=0.7)
ax.set_xlim(0, 100)

# Annotate the plot with insights
ax.annotate('High Engagement', xy=(85, 5), xytext=(90, 5.5),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkred')
ax.annotate('Balanced Interest', xy=(45, 3), xytext=(70, 3.5),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkgreen')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()