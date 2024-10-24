import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2030, 2041)

# Data for each sector in arbitrary units representing integration and adoption
exoskeletons = [5, 10, 15, 20, 30, 40, 55, 70, 85, 100, 120]
robotic_prosthetics = [20, 25, 30, 35, 45, 55, 65, 75, 85, 90, 95]
ai_companions = [10, 15, 20, 30, 40, 55, 60, 65, 70, 75, 80]
domestic_robotics = [15, 25, 45, 55, 60, 70, 75, 80, 82, 85, 88]

# Create the line plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each category as a line with distinct styles
ax.plot(years, exoskeletons, label='Exoskeletons', color='teal', linewidth=2, marker='o', linestyle='-')
ax.plot(years, robotic_prosthetics, label='Robotic Prosthetics', color='magenta', linewidth=2, marker='s', linestyle='--')
ax.plot(years, ai_companions, label='AI Companions', color='orange', linewidth=2, marker='^', linestyle='-.')
ax.plot(years, domestic_robotics, label='Domestic Robotics', color='steelblue', linewidth=2, marker='D', linestyle=':')

# Add titles and labels with appropriate breaks for readability
ax.set_title('The Evolution of Robotics:\nEnhancing Human Abilities (2030-2040)', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Integration & Adoption (Arbitrary Units)', fontsize=12)

# Add grid for readability
ax.grid(True, linestyle='--', alpha=0.6)

# Add legend and ensure it doesn't obstruct data
ax.legend(title='Robotics Sectors', fontsize=10, loc='upper left', bbox_to_anchor=(1, 1))

# Annotate significant developments to draw attention
ax.annotate('Exoskeleton Boom', xy=(2035, 30), xytext=(2032, 50),
            arrowprops=dict(facecolor='teal', arrowstyle='->', lw=1.5),
            fontsize=10, color='teal')

ax.annotate('Rise of AI Companions', xy=(2038, 65), xytext=(2035, 80),
            arrowprops=dict(facecolor='orange', arrowstyle='->', lw=1.5),
            fontsize=10, color='orange')

# Enhance readability of x-axis labels by rotating
plt.xticks(years, rotation=45)

# Automatically adjust layout to prevent overlap and clipping
plt.tight_layout()

# Display the plot
plt.show()