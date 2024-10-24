import matplotlib.pyplot as plt
import numpy as np

# Define the research focus areas and corresponding data
focus_areas = ['AI', 'Cybersecurity', 'Quantum Computing', 
               'Software Engineering', 'Data Science', 'Blockchain']
data = [
    [150, 160, 180, 210, 230, 250, 280, 310, 340, 380, 420],  # AI
    [100, 105, 110, 120, 130, 140, 155, 170, 190, 210, 230],  # Cybersecurity
    [30, 35, 40, 50, 60, 70, 90, 110, 130, 155, 180],          # Quantum Computing
    [200, 195, 190, 185, 180, 175, 170, 165, 160, 155, 150],  # Software Engineering
    [50, 60, 70, 90, 110, 140, 180, 220, 270, 330, 400],      # Data Science
    [10, 20, 35, 50, 70, 95, 120, 150, 185, 220, 260]         # Blockchain
]
years = np.arange(2015, 2026)

# Create a figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# First subplot: Box Plot
ax1 = axes[0]
bp = ax1.boxplot(data, vert=True, patch_artist=True, labels=focus_areas, notch=True)
colors = ['#FF5733', '#33FF57', '#3357FF', '#F333FF', '#FF8333', '#33FFF2']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

plt.setp(bp['whiskers'], color='grey', linestyle='--')
plt.setp(bp['caps'], color='grey')
plt.setp(bp['medians'], color='black', linewidth=2)

ax1.set_title("Evolution of Computer Science Research Focus Areas\n2015-2025", fontsize=14, fontweight='bold', pad=15)
ax1.set_ylabel("Number of Research Papers", fontsize=12)
ax1.set_xlabel("Research Focus Areas", fontsize=12)
ax1.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)
plt.xticks(rotation=15)

# Second subplot: Cumulative Line Plot
ax2 = axes[1]
for i, area in enumerate(focus_areas):
    cumulative_data = np.cumsum(data[i])
    ax2.plot(years, cumulative_data, marker='o', label=area, color=colors[i], linewidth=2, alpha=0.7)

ax2.set_title("Cumulative Research Paper Growth\n2015-2025", fontsize=14, fontweight='bold', pad=15)
ax2.set_ylabel("Cumulative Number of Research Papers", fontsize=12)
ax2.set_xlabel("Year", fontsize=12)
ax2.legend(title="Focus Areas", fontsize=10, loc='upper left')
ax2.grid(True, linestyle='--', color='grey', alpha=0.7)

# Adjust layout for better fit
plt.tight_layout()

# Display the plots
plt.show()