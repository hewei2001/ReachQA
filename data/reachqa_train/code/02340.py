import matplotlib.pyplot as plt
import numpy as np

# Define extended years
years = np.arange(2025, 2046)

# Data for each sector in arbitrary units representing integration and adoption
exoskeletons = np.array([3, 5, 7, 10, 15, 20, 30, 40, 55, 70, 85, 100, 120, 135, 150, 160, 170, 180, 190, 195, 200])
robotic_prosthetics = np.array([10, 15, 20, 25, 30, 35, 45, 55, 65, 75, 85, 90, 95, 98, 100, 102, 104, 106, 108, 109, 110])
ai_companions = np.array([5, 8, 12, 18, 25, 30, 40, 55, 60, 65, 70, 75, 80, 82, 84, 86, 88, 90, 92, 95, 98])
domestic_robotics = np.array([7, 10, 15, 25, 45, 55, 60, 70, 75, 80, 82, 85, 88, 90, 92, 94, 96, 97, 98, 99, 100])
humanoid_assistants = np.array([0, 2, 5, 10, 15, 25, 35, 50, 65, 75, 80, 90, 95, 97, 98, 99, 100, 102, 104, 106, 108])

# Create a line plot
fig, ax1 = plt.subplots(figsize=(14, 10))

# Plot each category as a line with distinct styles
ax1.plot(years, exoskeletons, label='Exoskeletons', color='teal', linewidth=2, marker='o', linestyle='-')
ax1.plot(years, robotic_prosthetics, label='Robotic Prosthetics', color='magenta', linewidth=2, marker='s', linestyle='--')
ax1.plot(years, ai_companions, label='AI Companions', color='orange', linewidth=2, marker='^', linestyle='-.')
ax1.plot(years, domestic_robotics, label='Domestic Robotics', color='steelblue', linewidth=2, marker='D', linestyle=':')
ax1.plot(years, humanoid_assistants, label='Humanoid Assistants', color='green', linewidth=2, marker='x', linestyle='-')

# Add titles and labels with breaks for readability
ax1.set_title('Evolution of Robotics & Human Integration\n(2025-2045)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Integration & Adoption (Arbitrary Units)', fontsize=12)

# Add grid for readability
ax1.grid(True, linestyle='--', alpha=0.6)

# Add legend and ensure it doesn't obstruct data
ax1.legend(title='Robotics Sectors', fontsize=10, loc='upper left', bbox_to_anchor=(1, 1))

# Annotate significant developments to draw attention
ax1.annotate('Exoskeleton Boom', xy=(2035, 30), xytext=(2030, 55),
             arrowprops=dict(facecolor='teal', arrowstyle='->', lw=1.5),
             fontsize=10, color='teal')

ax1.annotate('AI Companion Peak', xy=(2040, 95), xytext=(2035, 110),
             arrowprops=dict(facecolor='orange', arrowstyle='->', lw=1.5),
             fontsize=10, color='orange')

# Enhance readability of x-axis labels by rotating
plt.xticks(years, rotation=45)

# Add a second Y-axis for an aggregate sum plot
ax2 = ax1.twinx()
aggregate = exoskeletons + robotic_prosthetics + ai_companions + domestic_robotics + humanoid_assistants
ax2.plot(years, aggregate, label='Total Integration', color='black', linewidth=3, linestyle='--')
ax2.set_ylabel('Total Integration (Aggregated Units)', fontsize=12)
ax2.legend(loc='upper right', bbox_to_anchor=(1, 0.9), title='Aggregate')

# Automatically adjust layout to prevent overlap and clipping
plt.tight_layout()

# Display the plot
plt.show()