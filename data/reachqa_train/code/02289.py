import matplotlib.pyplot as plt
import numpy as np

# Define the decades
years = np.arange(1980, 2021, 10)

# Create data representing the percentage use of each design tool category
hand_drawing = np.array([80, 60, 40, 20, 10])
cad_software = np.array([10, 30, 45, 50, 45])
graphic_design = np.array([5, 20, 40, 50, 40])
modeling_3d = np.array([2, 10, 30, 40, 50])
cloud_design = 100 - (hand_drawing + cad_software + graphic_design + modeling_3d)

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))

# Define the color palette for different design tools
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

# Plot data with stackplot
ax.stackplot(years, hand_drawing, cad_software, graphic_design, modeling_3d, cloud_design,
             labels=["Hand-drawing & Sketching", "CAD Software", "Graphic Design Software", 
                     "3D Modeling Software", "Cloud-based Design Platforms"], colors=colors, alpha=0.85)

# Add titles and labels with improved styling
ax.set_title("Innovative Design Tools Through the Decades\n(1980-2020)", fontsize=18, fontweight='bold')
ax.set_xlabel("Year", fontsize=14, fontweight='semibold')
ax.set_ylabel("Percentage of Use (%)", fontsize=14, fontweight='semibold')

# Add grid lines for better readability
ax.grid(linestyle='--', alpha=0.5)

# Customize the legend and position it below the title to avoid overlap
ax.legend(loc='upper left', bbox_to_anchor=(0.1, -0.2), title='Design Tool Categories', title_fontsize='13', fontsize=11, ncol=2)

# Set x-axis ticks to avoid label overlap and improve layout
plt.xticks(years, rotation=45)

# Annotations for significant shifts
annotated_shifts = {1990: "Desktop Publishing Boom", 2000: "3D Modeling Expansion", 2010: "Cloud Collaboration Rise"}
for year, label in annotated_shifts.items():
    ax.annotate(label, xy=(year, 55), xytext=(year + 1, 70),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Automatically adjust the layout for optimal viewing
plt.tight_layout()

# Display the plot
plt.show()