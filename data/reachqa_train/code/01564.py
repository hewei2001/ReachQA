import matplotlib.pyplot as plt
import numpy as np

# Define the focus areas and their corresponding concern levels
focus_areas = [
    'Air Quality', 
    'Water Conservation', 
    'Green Space & Biodiversity', 
    'Waste Management & Recycling', 
    'Renewable Energy Adoption'
]
concern_levels = [35, 20, 15, 20, 10]  # Adjusted for better representation

# Define a color palette for each focus area
colors = ['#1b9e77', '#d95f02', '#7570b3', '#e7298a', '#66a61e']
patterns = ['...', '///', '\\\\', '||', '++']

# Create the donut pie chart
fig, ax = plt.subplots(figsize=(9, 7))
wedges, texts, autotexts = ax.pie(
    concern_levels, 
    labels=focus_areas, 
    autopct='%1.1f%%',
    startangle=90, 
    colors=colors, 
    pctdistance=0.85,
    wedgeprops=dict(width=0.35, edgecolor='w', linestyle='-', hatch=patterns, linewidth=1),
    shadow=True,
    explode=(0.05, 0.05, 0.05, 0.05, 0.05)  # Slightly explode each segment
)

# Customizing autotexts for improved readability
plt.setp(autotexts, size=10, weight='bold', color='white')
plt.setp(texts, size=11, style='italic')

# Add a central circle for a donut effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white', edgecolor='gray', lw=1.5)
fig.gca().add_artist(centre_circle)

# Set a comprehensive title with line breaks
plt.title("Environmental Awareness in Urban Areas:\nFocus on Key Concerns", fontsize=14, fontweight='bold', family='serif')

# Ensure equal aspect ratio to draw the pie as a circle
ax.axis('equal')

# Add a legend
ax.legend(
    wedges, [f'{area} Focus' for area in focus_areas], 
    title="Focus Areas", 
    loc="center left", 
    bbox_to_anchor=(1, 0, 0.5, 1), 
    fontsize=10
)

# Annotate each wedge with a brief descriptive text
annotations = [
    "Major concern in cities due to pollution",
    "Vital for sustaining urban water resources",
    "Enhances urban ecological health",
    "Reduces waste impact on environment",
    "Integral for sustainable future energy"
]
for i, wedge in enumerate(wedges):
    angle = (wedge.theta2 - wedge.theta1) / 2. + wedge.theta1
    x = 1.25 * np.cos(np.radians(angle))
    y = 1.25 * np.sin(np.radians(angle))
    ax.annotate(
        annotations[i], xy=(x, y), xytext=(x*1.1, y*1.1),
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"), fontsize=9, family='sans-serif'
    )

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the final plot
plt.show()