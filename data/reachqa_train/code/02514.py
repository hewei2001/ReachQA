import matplotlib.pyplot as plt
import numpy as np

# Define time periods and experience points
eras = ['Ancient World', 'Middle Ages', 'Renaissance', 'Industrial Age', 'Modern Era']
years = np.arange(600, 2100, 100)  # Corrected: From 600 to 2000, 15 values

# Experience points accumulated over each century in respective eras
experience_points = np.array([
    [100, 300, 450, 600, 800, 1000, 1200, 1300, 1500, 1700, 1900, 2100, 2300, 2500, 2700],  # Ancient World
    [300, 500, 700, 900, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200],  # Middle Ages
    [200, 400, 600, 850, 1050, 1250, 1450, 1650, 1850, 2050, 2250, 2450, 2650, 2850, 3050],  # Renaissance
    [250, 450, 650, 850, 1100, 1300, 1500, 1700, 1900, 2100, 2300, 2500, 2700, 2900, 3100],  # Industrial Age
    [350, 550, 750, 950, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200],  # Modern Era
])

# Stack the experience points to create cumulative experience
cumulative_points = np.cumsum(experience_points, axis=0)

# Plot the area chart
plt.figure(figsize=(14, 9))
plt.stackplot(years, cumulative_points, labels=eras, colors=['#FFD700', '#C0C0C0', '#CD7F32', '#7B68EE', '#FF6347'])

# Add title and labels
plt.title("Journey Through Time: A Time Traveler's\nExperience Accumulation", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Cumulative Experience Points", fontsize=12)

# Add legend and grid
plt.legend(loc='upper left', title="Historical Eras", fontsize=10)
plt.grid(linestyle='--', alpha=0.7)

# Annotate significant points
significant_points = [(600, 100), (1600, 1800), (2000, 3000)]
for year, value in significant_points:
    plt.annotate(f'({year}, {value})', xy=(year, value), xytext=(year+50, value+200),
                 arrowprops=dict(facecolor='black', shrink=0.05), fontsize=9, color='black')

# Adjust x-ticks for better readability
plt.xticks(years, rotation=45, fontsize=10)

# Improve layout
plt.tight_layout()

# Show plot
plt.show()