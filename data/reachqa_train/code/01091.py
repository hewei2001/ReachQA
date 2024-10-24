import matplotlib.pyplot as plt
import numpy as np

# Years of analysis
years = np.array([2000, 2005, 2010, 2015, 2020, 2025, 2030])

# Popularity data for each futuristic concept
ai_popularity = np.array([10, 20, 40, 70, 85, 95, 100])
vr_popularity = np.array([5, 15, 35, 50, 60, 75, 90])
qc_popularity = np.array([2, 10, 25, 45, 70, 80, 85])
nano_popularity = np.array([15, 25, 40, 55, 65, 70, 80])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting each concept with distinct style
ax.plot(years, ai_popularity, label='AI', marker='o', linestyle='-', color='b', linewidth=2)
ax.plot(years, vr_popularity, label='VR', marker='s', linestyle='--', color='r', linewidth=2)
ax.plot(years, qc_popularity, label='QC', marker='^', linestyle='-.', color='g', linewidth=2)
ax.plot(years, nano_popularity, label='Nano', marker='d', linestyle=':', color='purple', linewidth=2)

# Title and axis labels
ax.set_title("Techno-Cultural Evolution:\nPopularity of Futuristic Concepts (2000-2030)", fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Popularity Score', fontsize=12)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Legends to distinguish different lines
ax.legend(loc='upper left', fontsize=10, title='Concepts')

# Annotating key events or shifts
ax.annotate('AI Breakthrough', xy=(2020, 85), xytext=(2012, 90),
            arrowprops=dict(facecolor='blue', arrowstyle='->', lw=1.5), fontsize=11, color='blue')

ax.annotate('VR Mainstream', xy=(2025, 75), xytext=(2015, 80),
            arrowprops=dict(facecolor='red', arrowstyle='->', lw=1.5), fontsize=11, color='red')

ax.annotate('QC Milestone', xy=(2030, 85), xytext=(2020, 88),
            arrowprops=dict(facecolor='green', arrowstyle='->', lw=1.5), fontsize=11, color='green')

ax.annotate('Nano in Health', xy=(2030, 80), xytext=(2020, 75),
            arrowprops=dict(facecolor='purple', arrowstyle='->', lw=1.5), fontsize=11, color='purple')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()