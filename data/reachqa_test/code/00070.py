import matplotlib.pyplot as plt
import numpy as np

# Data setup
years = np.arange(2010, 2021)

# Internet usage percentages for different age groups
usage_10_19 = [50, 55, 60, 65, 72, 80, 85, 88, 90, 93, 95]
usage_20_29 = [70, 75, 78, 80, 83, 85, 88, 90, 92, 94, 95]
usage_30_49 = [60, 63, 66, 68, 72, 75, 78, 80, 82, 85, 87]
usage_50_plus = [30, 35, 40, 45, 50, 55, 58, 62, 66, 70, 74]

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 9))

# Plot with enhanced styles
ax.plot(years, usage_10_19, marker='o', linestyle='-', linewidth=2, color='skyblue', label='10-19 years')
ax.plot(years, usage_20_29, marker='s', linestyle='--', linewidth=2, color='salmon', label='20-29 years')
ax.plot(years, usage_30_49, marker='^', linestyle='-.', linewidth=2, color='lightgreen', label='30-49 years')
ax.plot(years, usage_50_plus, marker='d', linestyle=':', linewidth=2, color='gold', label='50+ years')

# Annotations
for i, year in enumerate(years):
    ax.annotate(f'{usage_10_19[i]}%', (year, usage_10_19[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, color='darkblue')
    ax.annotate(f'{usage_20_29[i]}%', (year, usage_20_29[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, color='darkred')
    ax.annotate(f'{usage_30_49[i]}%', (year, usage_30_49[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, color='darkgreen')
    ax.annotate(f'{usage_50_plus[i]}%', (year, usage_50_plus[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, color='darkorange')

# Background gradient
ax.set_facecolor('whitesmoke')

# Grid customization
ax.grid(axis='y', linestyle='--', alpha=0.6)
ax.set_axisbelow(True)

# Titles and labels
ax.set_title("Evolution of Internet Usage by Age Group\n2010-2020", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Percentage of Internet Users", fontsize=14)

# Legends
ax.legend(title="Age Groups", loc='upper left', fontsize=11)

# Secondary y-axis for potential additional data
ax2 = ax.twinx()
ax2.set_yticks([])
ax2.set_ylabel('')

# Layout adjustment
plt.tight_layout()

# Display the plot
plt.show()