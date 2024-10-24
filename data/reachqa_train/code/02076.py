import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

# Define data for centuries and average precision of brushstrokes
centuries = np.array([1600, 1700, 1800, 1900])
average_precision = np.array([45, 60, 75, 85])
variability_error = np.array([5, 7, 10, 8])
popularity = np.array([30, 50, 70, 80])  # New data for dual axis

# Create the figure and axis objects
fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot the line chart with error bars
color_precision = 'darkviolet'
ax1.errorbar(
    centuries, average_precision, yerr=variability_error, fmt='-o', color=color_precision, ecolor='lightgray',
    linestyle='-', capsize=5, capthick=2, markerfacecolor=color_precision, alpha=0.9, label='Precision of Brushstrokes'
)

# Set titles and labels
ax1.set_title("The Evolution of Brushstroke Techniques Over Centuries:\nUnveiling Artistic Experimentation", 
              fontsize=16, fontweight='bold', color='indigo', loc='left')
ax1.set_xlabel('Century', fontsize=12, fontweight='bold', color='darkslateblue')
ax1.set_ylabel('Average Precision (Unit)', fontsize=12, fontweight='bold', color=color_precision)

# Set century markers and y-axis ticks
ax1.set_xticks(centuries)
ax1.set_xticklabels(['1600s', '1700s', '1800s', '1900s'])
ax1.set_yticks(np.arange(40, 100, 10))
ax1.yaxis.set_minor_locator(MultipleLocator(5))

# Add a second y-axis
ax2 = ax1.twinx()
color_popularity = 'darkgreen'
ax2.plot(centuries, popularity, '-s', color=color_popularity, label='Popularity of Techniques')
ax2.set_ylabel('Popularity Index', fontsize=12, fontweight='bold', color=color_popularity)
ax2.set_yticks(np.arange(20, 100, 20))

# Grid and legend
ax1.grid(True, linestyle='--', alpha=0.6, color='gray')
ax1.legend(loc='upper left', fontsize=10)
ax2.legend(loc='upper right', fontsize=10)

# Add an annotation with historical context
ax1.text(1650, 75, 'Increased experimentation\nleads to variability', fontsize=10, style='italic', 
         bbox={'facecolor': 'lavender', 'alpha': 0.5, 'pad': 5})

# Shaded areas for historical significance
ax1.axvspan(1600, 1700, alpha=0.1, color='gray')
ax1.text(1625, 50, 'Baroque Era', fontsize=9, color='darkslateblue', alpha=0.7)

ax1.axvspan(1700, 1800, alpha=0.1, color='peachpuff')
ax1.text(1725, 65, 'Rococo Period', fontsize=9, color='saddlebrown', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()