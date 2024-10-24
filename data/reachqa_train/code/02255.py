import matplotlib.pyplot as plt
import numpy as np

# Define the technology sectors
sectors = ['Artificial Intelligence', 'Cybersecurity', 'Fintech', 'EdTech', 'HealthTech']

# Artificial annual revenue growth data in percentage for five years
ai_growth = [22, 27, 19, 25, 30]  # AI
cyber_growth = [12, 18, 15, 22, 17]  # Cybersecurity
fintech_growth = [35, 28, 40, 33, 45]  # Fintech
edtech_growth = [8, 15, 10, 14, 9]  # EdTech
healthtech_growth = [25, 23, 20, 26, 27]  # HealthTech

# Compile data for box plots
growth_data = [ai_growth, cyber_growth, fintech_growth, edtech_growth, healthtech_growth]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Create vertical box plots
bp = ax.boxplot(growth_data, vert=True, notch=True, patch_artist=True,
                labels=sectors, 
                boxprops=dict(facecolor='lightgreen', color='darkgreen'),
                whiskerprops=dict(color='darkgreen'),
                capprops=dict(color='darkgreen'),
                medianprops=dict(color='red', linewidth=2),
                flierprops=dict(marker='o', color='darkgreen', markersize=8, alpha=0.5))

# Set the title and labels
ax.set_title('Growth Analysis of Tech Startups by Sector\nAnnual Revenue Growth (5-Year Data)', fontsize=14, fontweight='bold')
ax.set_ylabel('Annual Revenue Growth (%)', fontsize=12)
ax.set_xlabel('Technology Sectors', fontsize=12)

# Enhance readability with grid lines
ax.yaxis.grid(True, linestyle='--', which='major', color='lightgrey', alpha=0.7)

# Rotate the x-axis labels for better readability
plt.xticks(rotation=15)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()