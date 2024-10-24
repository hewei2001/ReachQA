import matplotlib.pyplot as plt
import numpy as np

# Settlement data and their resource contributions
settlements = ['Luna', 'Mars', 'Europa', 'Titan', 'Earth']
resource_percentages = [25, 20, 15, 10, 30]

# Annotations for the settlements
annotations = ["Helium-3", "Agriculture", "Water", "Methane", "R&D"]

# Color scheme for the settlements
colors = ['#c0c0c0', '#ff6347', '#1e90ff', '#ffa500', '#32cd32']

# Plot the ring chart
fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    resource_percentages,
    labels=settlements,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w', alpha=0.9)
)

# Add a circle at the center to transform it into a ring chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)

# Setting the font size and weight for texts
plt.setp(texts, size=10, weight='bold', color='black')
plt.setp(autotexts, size=9, weight='bold', color='white')

# Title with multiple lines for clarity
ax.set_title(
    "Resource Allocation in Galactic Settlements:\nA Glimpse into the Future",
    fontsize=14,
    weight='bold',
    position=(0.5, 1.05)
)

# Central label inside the ring
ax.text(0, 0, 'Galactic\nResources', ha='center', va='center', fontsize=12, weight='bold', color='gray')

# Adding a legend with optimized placement
ax.legend(
    wedges,
    [f"{settlements[i]}: {annotations[i]}" for i in range(len(settlements))],
    title="Settlement Functions",
    loc='center left',
    bbox_to_anchor=(1, 0.5),
    fontsize=10
)

# Adjust layout to prevent clipping
plt.tight_layout()

# Display the plot
plt.show()