import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# Define initiatives and their budget allocations in percentages
initiatives = [
    "Renewable Energy",
    "Urban Greening",
    "Waste Reduction",
    "Sustainable Transport",
    "Water Conservation"
]

# Budget allocation percentages
budget_allocation = np.array([35, 25, 15, 15, 10])

# Total budget in million dollars (hypothetical)
total_budget = 100

# Create a gradient color map
cmap = LinearSegmentedColormap.from_list(
    'custom_cmap', ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854'])

# Create the donut pie chart
fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))

# Generate wedges with gradient color
wedges, texts, autotexts = ax.pie(
    budget_allocation,
    labels=initiatives,
    autopct=lambda p: '{:.1f}%\n(${:.1f}M)'.format(p, p * total_budget / 100),
    startangle=140,
    colors=[cmap(i / len(budget_allocation)) for i in range(len(budget_allocation))],
    pctdistance=0.8,
    wedgeprops=dict(width=0.4, edgecolor='w', linewidth=1),
    explode=[0.1 if i == 0 else 0.05 for i in range(len(initiatives))],  # More explode on first segment
)

# Add a circle in the center to create a donut shape
centre_circle = plt.Circle((0, 0), 0.6, fc='white')
ax.add_artist(centre_circle)

# Equal aspect ratio ensures the pie chart is a circle
ax.axis('equal')

# Adjust text properties
plt.setp(autotexts, size=9, weight='bold', color='black')
plt.setp(texts, size=10)

# Add a subtle radial gradient background
fig.patch.set_facecolor('#f0f0f0')
ax.set_facecolor('#e0e0e0')

# Title and legend
plt.title("Greenberg's Climate Change Budget Allocation\nfor 2025", fontsize=14, weight='bold', pad=20)
ax.legend(wedges, initiatives, title="Initiatives", loc="upper left", bbox_to_anchor=(1, 1))

# Automatic layout adjustment to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()