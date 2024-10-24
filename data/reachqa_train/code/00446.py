import matplotlib.pyplot as plt
import numpy as np

# Define the months
months = np.array([
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
])

# Attendance data for each continent
africa_attendance = [120, 140, 150, 160, 170, 190, 200, 210, 205, 220, 230, 240]
asia_attendance = [220, 210, 230, 240, 250, 270, 300, 320, 310, 330, 350, 370]
europe_attendance = [180, 190, 200, 210, 220, 225, 230, 240, 245, 250, 255, 260]
north_america_attendance = [200, 210, 205, 210, 220, 230, 240, 250, 245, 260, 270, 280]
south_america_attendance = [150, 160, 170, 180, 190, 200, 210, 220, 215, 225, 235, 245]

# Initialize the plot
plt.figure(figsize=(14, 8))

# Plot each continent's data with distinct line styles and markers
plt.plot(months, africa_attendance, marker='o', linestyle='-', color='green', linewidth=2, label='Africa')
plt.plot(months, asia_attendance, marker='^', linestyle='--', color='red', linewidth=2, label='Asia')
plt.plot(months, europe_attendance, marker='s', linestyle='-.', color='blue', linewidth=2, label='Europe')
plt.plot(months, north_america_attendance, marker='D', linestyle=':', color='purple', linewidth=2, label='North America')
plt.plot(months, south_america_attendance, marker='*', linestyle='-', color='orange', linewidth=2, label='South America')

# Set title and labels
plt.title("Monthly Climate Change Awareness Event Attendance\nAcross Continents in 2023", fontsize=16, fontweight='bold')
plt.xlabel("Month", fontsize=12)
plt.ylabel("Number of Attendees", fontsize=12)

# Enhance x-axis ticks visibility
plt.xticks(rotation=45)

# Add gridlines for easier reading of values
plt.grid(True, linestyle='--', alpha=0.6)

# Add legend with optimal position
plt.legend(title="Continent", loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10)

# Automatically adjust layout for better visibility
plt.tight_layout()

# Display the plot
plt.show()