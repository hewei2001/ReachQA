import matplotlib.pyplot as plt
import numpy as np

# Define the decades
decades = np.array(['1970s', '1980s', '1990s', '2000s', '2010s', '2020s'])
decade_numeric = np.arange(len(decades))

# Fashion styles representation (in percentage)
disco = np.array([40, 20, 5, 0, 0, 0])
punk = np.array([15, 25, 20, 5, 0, 0])
grunge = np.array([0, 10, 35, 15, 5, 0])
hip_hop = np.array([5, 15, 25, 40, 30, 20])
sustainable = np.array([0, 0, 0, 10, 25, 40])

# Calculate cumulative data for stacking
cumulative_top = disco + punk + grunge + hip_hop + sustainable
cumulative_hiphop = disco + punk + grunge + hip_hop
cumulative_grunge = disco + punk + grunge
cumulative_punk = disco + punk

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Stack the area plot using fill_between
ax.fill_between(decade_numeric, 0, disco, color='#FFD700', alpha=0.8, label='Disco')
ax.fill_between(decade_numeric, disco, cumulative_punk, color='#FF6347', alpha=0.8, label='Punk')
ax.fill_between(decade_numeric, cumulative_punk, cumulative_grunge, color='#8B4513', alpha=0.8, label='Grunge')
ax.fill_between(decade_numeric, cumulative_grunge, cumulative_hiphop, color='#4682B4', alpha=0.8, label='Hip-Hop')
ax.fill_between(decade_numeric, cumulative_hiphop, cumulative_top, color='#2E8B57', alpha=0.8, label='Sustainable')

# Adding text and annotations
ax.set_title('Evolution of Fashion Styles\nOver the Decades', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Decades', fontsize=14)
ax.set_ylabel('Prominence (%)', fontsize=14)
ax.set_xlim(-0.5, len(decades) - 0.5)
ax.set_ylim(0, 100)
ax.set_xticks(decade_numeric)
ax.set_xticklabels(decades, rotation=45, ha='right')

# Highlight key fashion moments
ax.annotate('Punk Peaks', xy=(1, 25), xytext=(1, 50),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='#FF6347')
ax.annotate('Grunge Dominates', xy=(2, 50), xytext=(2, 70),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='#8B4513')
ax.annotate('Sustainability Emerges', xy=(4, 75), xytext=(4, 90),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='#2E8B57')

# Grid and legend
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(loc='upper left', fontsize=10, title='Fashion Styles')

# Adjust layout for better spacing and visibility
plt.tight_layout()

# Display the plot
plt.show()