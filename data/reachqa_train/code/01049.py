import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define expanded art movements and corresponding data
art_movements = ['Renaissance', 'Baroque', 'Rococo', 'Neoclassicism', 'Romanticism',
                 'Realism', 'Impressionism', 'Modernism', 'Postmodernism', 'Futurism']
buildings = np.array([500, 300, 600, 450, 400, 350, 650, 800, 350, 150])
years_since_emergence = np.array([600, 400, 300, 250, 200, 150, 120, 100, 50, 30])
regions = ['Europe', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe', 'Global', 'Global', 'Global']

# Sort years_since_emergence and corresponding buildings
sorted_indices = np.argsort(years_since_emergence)
years_since_emergence_sorted = years_since_emergence[sorted_indices]
buildings_sorted = buildings[sorted_indices]
art_movements_sorted = [art_movements[i] for i in sorted_indices]

# Generate a smooth line fit using B-spline interpolation
x_smooth = np.linspace(years_since_emergence_sorted.min(), years_since_emergence_sorted.max(), 300)
spline = make_interp_spline(years_since_emergence_sorted, buildings_sorted, k=3)
y_smooth = spline(x_smooth)

# Create the main figure and subplots
fig, ax = plt.subplots(figsize=(14, 10))

# Scatter plot with smooth trend line
scatter = ax.scatter(years_since_emergence_sorted, buildings_sorted, c=buildings_sorted, cmap='viridis', s=100,
                     label='Art Movements Influence', edgecolors='black', zorder=3)
ax.plot(x_smooth, y_smooth, color='navy', linewidth=2, linestyle='--', label='Trend Line (B-spline Fit)', zorder=2)

# Annotations
for i, movement in enumerate(art_movements_sorted):
    ax.annotate(movement, (years_since_emergence_sorted[i], buildings_sorted[i]), textcoords="offset points", xytext=(-15,10), ha='center', fontsize=8)

# Adding a colorbar
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Influence Intensity (Number of Buildings)', rotation=270, labelpad=15)

# Set labels and title
ax.set_xlabel('Years Since Emergence', fontsize=12)
ax.set_ylabel('Number of Influenced Buildings', fontsize=12)
ax.set_title('Cultural Flourish: Influence of Artistic Movements on Urban Architecture\nAcross Europe and Global Trends', fontsize=14, weight='bold')

# Add a legend
ax.legend(loc='upper right', fontsize=10)

# Grid and layout adjustments
ax.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Display the plot
plt.show()