import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Define significant years of space exploration events
years = np.array([1969, 1973, 1981, 1990, 1997, 2004, 2012, 2020])

# Define the public interest level in arbitrary units for those years
interest_levels = np.array([80, 45, 60, 75, 55, 70, 90, 85])

# Generate a smooth curve using spline interpolation
years_smooth = np.linspace(years.min(), years.max(), 300)
spline = make_interp_spline(years, interest_levels, k=3)
interest_smooth = spline(years_smooth)

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Scatter plot with varying marker sizes
scatter = ax.scatter(years, interest_levels, 
                     c=interest_levels, cmap='autumn', s=interest_levels*1.5, zorder=3, 
                     label='Interest Level')

# Smooth spline plot with gradient effect
for i in range(1, len(years_smooth)):
    ax.plot(years_smooth[i-1:i+1], interest_smooth[i-1:i+1], color=plt.cm.Blues(i/len(years_smooth)), lw=2)

# Add background with subtle gradient
ax.set_facecolor('#f7f7f7')

# Titles and labels
ax.set_title('Influence of Space Exploration Announcements\non Public Interest Over the Decades', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Public Interest (arbitrary units)', fontsize=12)

# Annotating significant events with styled text
events = {
    1969: 'Moon Landing 🌕',
    1981: 'First Shuttle Launch 🚀',
    1990: 'Hubble Telescope Launch 🛰️',
    2012: 'Curiosity Mars Rover Landing 🚜'
}
for year, event in events.items():
    ax.annotate(event, xy=(year, interest_levels[years.tolist().index(year)]), 
                xytext=(year, interest_levels[years.tolist().index(year)] + 12),
                arrowprops=dict(facecolor='gray', arrowstyle='->'),
                fontsize=10, ha='center', bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='#f2f2f2'))

# Enhancing gridlines
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

# Colorbar for scatter plot to represent levels of interest
cbar = plt.colorbar(scatter)
cbar.set_label('Interest Level Intensity', rotation=270, labelpad=15)

# Adjusting layout
plt.tight_layout()

# Show plot
plt.show()