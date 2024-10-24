import matplotlib.pyplot as plt
import numpy as np

# Define the years with annual data points
years = np.arange(1980, 2021)

# Define expanded data with additional complexity
hand_drawing = np.linspace(80, 5, len(years))
cad_software = np.piecewise(years,
                            [years < 1990, (years >= 1990) & (years < 2000), (years >= 2000)],
                            [lambda x: 10 + 0.2*(x-1980), lambda x: 30 + 0.15*(x-1990), lambda x: 45 + 0.05*(x-2000)])
graphic_design = np.piecewise(years,
                              [years < 1995, (years >= 1995) & (years < 2010), (years >= 2010)],
                              [lambda x: 5 + 0.3*(x-1980), lambda x: 40 + 0.2*(x-1995), lambda x: 60 - 0.05*(x-2010)])
modeling_3d = np.piecewise(years,
                           [years < 2000, (years >= 2000) & (years < 2010), (years >= 2010)],
                           [lambda x: 2 + 0.15*(x-1980), lambda x: 30 + 0.2*(x-2000), lambda x: 40 + 0.3*(x-2010)])
cloud_design = np.piecewise(years,
                            [years < 2010, years >= 2010],
                            [lambda x: 3*(x-1980), lambda x: 70 + 0.5*(x-2010)])
ai_design = np.piecewise(years,
                         [years < 2015, years >= 2015],
                         [lambda x: 0, lambda x: 5 + 0.3*(x-2015)])

# Recalculate the final distribution to ensure the sum equals 100
total_percent = hand_drawing + cad_software + graphic_design + modeling_3d + cloud_design + ai_design
hand_drawing = hand_drawing / total_percent * 100
cad_software = cad_software / total_percent * 100
graphic_design = graphic_design / total_percent * 100
modeling_3d = modeling_3d / total_percent * 100
cloud_design = cloud_design / total_percent * 100
ai_design = ai_design / total_percent * 100

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(16, 10))

# Define the color palette for different design tools
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb366']

# Plot data with stackplot
ax.stackplot(years, hand_drawing, cad_software, graphic_design, modeling_3d, cloud_design, ai_design,
             labels=["Hand-drawing & Sketching", "CAD Software", "Graphic Design Software", 
                     "3D Modeling Software", "Cloud-based Design Platforms", "AI-powered Design Tools"],
             colors=colors, alpha=0.85)

# Add titles and labels with improved styling
ax.set_title("Evolution of Innovative Design Tools Over the Years (1980-2020)", fontsize=18, fontweight='bold')
ax.set_xlabel("Year", fontsize=14, fontweight='semibold')
ax.set_ylabel("Usage (%)", fontsize=14, fontweight='semibold')

# Add grid lines for better readability
ax.grid(linestyle='--', alpha=0.5)

# Customize the legend and position it above the plot for better readability
ax.legend(loc='upper left', bbox_to_anchor=(0.1, 1.05), title='Design Tool Categories', title_fontsize='13', fontsize=11, ncol=2)

# Set x-axis ticks to improve readability
plt.xticks(years[::5], rotation=45)

# Add annotations for significant shifts and trends
annotated_shifts = {1985: "DTP Era Begins", 2000: "3D Modeling Spike", 2015: "AI Emergence"}
for year, label in annotated_shifts.items():
    ax.annotate(label, xy=(year, 80), xytext=(year + 1, 90),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Automatically adjust the layout for optimal viewing
plt.tight_layout()

# Display the plot
plt.show()