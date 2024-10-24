import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Define demographics and technologies
demographics = ['North America', 'Europe', 'Asia-Pacific', 'Latin America', 'Africa']
technologies = ['Quantum Computing', 'AI-driven Automation', 'Blockchain', 'Extended Reality (XR)']

# Define percentage usage of each technology by demographic
usage_percentages = np.array([
    [25, 40, 20, 15],  # North America
    [22, 45, 18, 15],  # Europe
    [30, 35, 25, 10],  # Asia-Pacific
    [18, 30, 25, 27],  # Latin America
    [20, 25, 20, 35]   # Africa
])

# Construct trend data for additional plot
trend_percentages = np.array([25, 28, 30, 22, 25])  # Example trend data for total usage

# Define colors
base_colors = ['#FF8C00', '#6A5ACD', '#228B22', '#DC143C']

# Plot settings
fig, ax = plt.subplots(figsize=(14, 8))

# Plot stacked bar chart
bottoms = np.zeros(len(demographics))
for i, technology in enumerate(technologies):
    bar = ax.bar(demographics, usage_percentages[:, i], label=technology, color=base_colors[i], bottom=bottoms, edgecolor='gray')
    bottoms += usage_percentages[:, i]

    # Annotate percentage usage
    for j in range(len(demographics)):
        ax.text(j, bottoms[j] - usage_percentages[j, i] / 2, f"{usage_percentages[j, i]}%", 
                ha='center', va='center', fontsize=10, color='white', fontweight='bold')

# Overlay line plot to show trend
ax2 = ax.twinx()
ax2.plot(demographics, trend_percentages, 'o-', color='black', markersize=8, linewidth=2, label='Overall Technology Usage')
ax2.set_ylabel('Overall Usage (%)', fontsize=12)
ax2.set_ylim(0, 100)
ax2.yaxis.set_visible(False)  # Hide secondary y-axis line for cleaner look

# Set axis labels and title
ax.set_ylabel('Percentage Usage by Technology (%)', fontsize=12)
ax.set_title('Navigating the Digital Frontier:\nTechnology Usage Across Continents in 2040', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_ylim(0, 100)
ax.set_yticks(np.arange(0, 101, 10))

# Enhance plot appearance
ax.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Custom legend
handles = [Patch(color=base_colors[i], label=tech) for i, tech in enumerate(technologies)]
handles.append(Patch(facecolor='none', edgecolor='black', label='Overall Usage'))
ax.legend(handles=handles, title='Technology', loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()