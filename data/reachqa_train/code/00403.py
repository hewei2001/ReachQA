import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np

# Data: percentage share of renewable energy sources in 2023
energy_sources = ['Solar', 'Wind', 'Hydropower', 'Biomass', 'Geothermal']
percentages = [35, 25, 18, 12, 10]
growth_rates = [2.5, 1.8, 1.2, 0.5, 0.3]  # Annual growth rates in percentage

# Colors and patterns for each renewable energy source
colors = ['#FFBB33', '#66BB6A', '#42A5F5', '#AB47BC', '#FF7043']
patterns = ['/', '\\', '|', '-', '+']  # Patterns to fill slices

fig, ax = plt.subplots(figsize=(10, 7))

# Creating a pie chart with a donut hole and patterns
wedges, texts, autotexts = ax.pie(
    percentages,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=140,
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w', linewidth=2),
    explode=[0.1 if energy == 'Solar' else 0 for energy in energy_sources],
    shadow=True
)

# Applying patterns to each wedge
for i, wedge in enumerate(wedges):
    wedge.set_hatch(patterns[i])

# Setting text properties
plt.setp(autotexts, size=10, weight='bold', color='darkblue')
plt.setp(texts, size=12)

# Ensure the pie chart is a circle
ax.axis('equal')

# Adding annotations for growth rates
for i, (percent, wedge) in enumerate(zip(percentages, wedges)):
    angle = (wedge.theta2 - wedge.theta1) / 2 + wedge.theta1
    x = np.cos(np.radians(angle))
    y = np.sin(np.radians(angle))
    ax.annotate(f"Growth: {growth_rates[i]}%", xy=(x, y), xytext=(1.35 * x, 1.35 * y),
                arrowprops=dict(arrowstyle="->", color='grey'), fontsize=9, color='black')

# Title with line breaks for clarity
plt.title("Green Innovations:\nRenewable Energy Sources' Share & Growth (2023)",
          pad=20, fontsize=14, fontweight='bold', color='darkgreen', ha='center')

# Adding a legend with patterns
legend_elements = [Patch(facecolor=colors[i], hatch=patterns[i], label=energy_sources[i]) for i in range(len(energy_sources))]
ax.legend(handles=legend_elements, title="Energy Sources", loc='center left',
          bbox_to_anchor=(1, 0.5), fontsize='medium', frameon=False)

# Adding a subplot for historical growth rates
ax2 = fig.add_axes([0.8, 0.1, 0.15, 0.3])  # Positioning inset at the right
ax2.barh(energy_sources, growth_rates, color=colors, edgecolor='black', height=0.5)
ax2.set_title('Annual Growth %', fontsize=10, color='darkgreen')
ax2.set_xlim(0, max(growth_rates) + 0.5)
ax2.invert_yaxis()
ax2.set_xticks([])  # Hiding x-axis ticks for clarity

# Adjust layout to prevent overlapping elements
plt.tight_layout(rect=[0, 0, 0.75, 1])

# Show the chart
plt.show()