import matplotlib.pyplot as plt
import numpy as np

# Define the time periods (in centuries)
centuries = np.array([-25, -20, -15, -10, -5])  # Representing 2500 BCE to 500 BCE

# Estimated populations in thousands (artificial data)
egyptian_population = [500, 800, 1500, 1800, 1300]
mesopotamian_population = [600, 1100, 1200, 900, 800]
indus_valley_population = [400, 900, 1100, 1000, 300]

# Estimated trade activity (artificial data)
egyptian_trade = [300, 600, 1400, 1700, 1100]
mesopotamian_trade = [400, 800, 1000, 850, 700]
indus_valley_trade = [200, 700, 900, 850, 400]

# Plotting the data
fig, ax1 = plt.subplots(figsize=(14, 9))

# Population line plots
ax1.plot(centuries, egyptian_population, marker='o', linestyle='-', linewidth=2, color='gold', label='Egyptian Population')
ax1.plot(centuries, mesopotamian_population, marker='s', linestyle='-', linewidth=2, color='teal', label='Mesopotamian Population')
ax1.plot(centuries, indus_valley_population, marker='^', linestyle='-', linewidth=2, color='indigo', label='Indus Valley Population')

# Annotations for population
for i, (ce, me, iv) in enumerate(zip(egyptian_population, mesopotamian_population, indus_valley_population)):
    ax1.text(centuries[i], ce + 50, f'{ce}k', ha='center', fontsize=9, color='goldenrod', fontweight='bold')
    ax1.text(centuries[i], me - 120, f'{me}k', ha='center', fontsize=9, color='darkcyan', fontweight='bold')
    ax1.text(centuries[i], iv + 50, f'{iv}k', ha='center', fontsize=9, color='purple', fontweight='bold')

# Creating a twin axis for the overlay plot
ax2 = ax1.twinx()

# Trade activity bar plots
width = 0.7  # Width of the bars
ax2.bar(centuries - width, egyptian_trade, width=width/3, color='navajowhite', alpha=0.6, label='Egyptian Trade')
ax2.bar(centuries, mesopotamian_trade, width=width/3, color='paleturquoise', alpha=0.6, label='Mesopotamian Trade')
ax2.bar(centuries + width, indus_valley_trade, width=width/3, color='plum', alpha=0.6, label='Indus Valley Trade')

# Title and labels
plt.title("Population Growth and Trade Activity of Ancient Civilizations\n2500 BCE - 500 BCE", fontsize=16, fontweight='bold')
ax1.set_xlabel("Time (Centuries BCE)", fontsize=14)
ax1.set_ylabel("Population (in thousands)", fontsize=14)
ax2.set_ylabel("Trade Activity (arbitrary units)", fontsize=14)

# Legends
ax1.legend(title='Population', fontsize=10, loc='upper left')
ax2.legend(title='Trade Activity', fontsize=10, loc='upper right')

# Grid lines for readability
ax1.grid(True, linestyle='--', alpha=0.6)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Reverse the x-axis to represent time from BCE to present
ax1.invert_xaxis()
ax2.invert_xaxis()

plt.show()