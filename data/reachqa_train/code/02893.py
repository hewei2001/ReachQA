import matplotlib.pyplot as plt
import numpy as np

# Zodiac signs (each sign covers about one month)
zodiac_signs = [
    'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
    'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
]

# Influence strength for each zodiac over 12 months
influence_data = [
    8, 6, 5, 7, 9, 4, 6, 10, 8, 7, 5, 7  # Exemplary influence values
]

# Convert the data into a numpy array for convenience
influence_data = np.array(influence_data)

# Number of categories
num_categories = len(zodiac_signs)

# Compute the angle for each sector
sector_angle = (2 * np.pi) / num_categories

# Create an array of angles for each sector
angles = np.arange(0, 2 * np.pi, sector_angle)

# Set up the polar plot
fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))

# Plot each zodiac sign as a sector in the chart
bars = ax.bar(
    angles, 
    influence_data, 
    width=sector_angle, 
    bottom=0,
    color=plt.cm.viridis(np.linspace(0, 1, num_categories)),  # Use a colormap for colors
    alpha=0.6,
    edgecolor='k',
    linewidth=2
)

# Set the label for each sector
ax.set_xticks(angles)
ax.set_xticklabels(zodiac_signs)

# Remove radial labels for a cleaner look
ax.set_yticklabels([])

# Add a title with line breaks for readability
ax.set_title(
    "Celestial Influence of Zodiac Signs:\n"
    "A Year in the Cosmos",
    fontsize=16, fontweight='bold', pad=20
)

# Add legend outside the plot area
ax.legend(
    bars, zodiac_signs, 
    title="Zodiac Signs", 
    loc="upper left", 
    bbox_to_anchor=(1.1, 1.05),
    fontsize=10
)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the chart
plt.show()