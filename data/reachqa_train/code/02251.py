import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Biodiversity index (out of 100)
biodiversity = [65, 68, 70, 72, 73, 74, 76, 75, 73, 71, 69]

# Water clarity index (out of 100)
water_clarity = [80, 82, 81, 79, 78, 76, 75, 74, 73, 71, 70]

# Coral health index (out of 100)
coral_health = [60, 62, 63, 64, 65, 64, 63, 62, 61, 59, 57]

# Plot the data
plt.figure(figsize=(14, 8))

# Plot each line with different styles
plt.plot(years, biodiversity, marker='o', linestyle='-', linewidth=2, color='seagreen', label='Biodiversity Index')
plt.plot(years, water_clarity, marker='s', linestyle='--', linewidth=2, color='dodgerblue', label='Water Clarity Index')
plt.plot(years, coral_health, marker='^', linestyle='-.', linewidth=2, color='coral', label='Coral Health Index')

# Titles, labels, and legend
plt.title("Decadal Exploration of Underwater Ecosystems in the\nGreat Barrier Reef (2010-2020)", fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Index Score (0-100)', fontsize=12)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(50, 101, 5))
plt.legend(loc='lower left', fontsize=10)

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()