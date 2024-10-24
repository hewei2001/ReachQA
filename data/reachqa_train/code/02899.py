import matplotlib.pyplot as plt
import numpy as np

# Define the categories for flavor profiles
categories = ['Citrus', 'Floral', 'Earthy', 'Spicy', 'Sweet']
n_categories = len(categories)

# Data for each tea blend (flavor profile scores from 0 to 10)
chamomile_dream = [2, 8, 6, 3, 7]
minty_fresh = [1, 5, 8, 5, 6]
spice_harmony = [3, 4, 5, 9, 5]
citrus_bliss = [9, 3, 4, 2, 6]

# Aggregate the data and tea names
tea_data = [chamomile_dream, minty_fresh, spice_harmony, citrus_bliss]
tea_names = ['Chamomile Dream', 'Minty Fresh', 'Spice Harmony', 'Citrus Bliss']

# Create angles for radar chart
angles = np.linspace(0, 2 * np.pi, n_categories, endpoint=False).tolist()
angles += angles[:1]  # complete the circle

# Initialize the radar chart plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each tea's flavor profile on the radar chart
for i, data in enumerate(tea_data):
    data += data[:1]  # Repeat the first value to close the chart
    ax.fill(angles, data, alpha=0.25, label=tea_names[i], edgecolor='darkorange')
    ax.plot(angles, data, linewidth=2, linestyle='solid')

# Set labels for each spoke
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12)

# Configure the radial ticks and grid
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels([], color='gray')
ax.grid(True, linestyle='--', linewidth=0.5, color='gray', alpha=0.7)

# Add the title
ax.set_title('Flavor Profiles of Herbal Tea Blends', size=16, weight='bold', pad=20)

# Add the legend and adjust its position
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=12)

# Automatically adjust the layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()