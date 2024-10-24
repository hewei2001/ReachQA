import matplotlib.pyplot as plt
import numpy as np

# Data: Years, computational power, model complexity, and hypothetical paper counts
years = np.arange(1980, 2021, 5)
computational_power = [0.001, 0.01, 0.1, 1, 10, 100, 1000, 5000, 10000]
model_complexity = [0.001, 0.01, 0.05, 0.2, 1, 10, 50, 200, 400]
paper_count = [10, 15, 20, 30, 50, 80, 150, 300, 450]  # Hypothetical paper counts

# Milestones annotations
milestones = {
    1985: "First\nNeural Networks",
    1995: "Rise of\nSVMs",
    2005: "Deep\nLearning Boom",
    2012: "AlexNet\nBreakthrough",
    2020: "Large-scale\nLanguage Models"
}

# Create the figure and main axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot lines for computational power and model complexity
ax1.plot(years, computational_power, label='Computational Power (TeraFLOPS)', color='navy', marker='o', linestyle='-', linewidth=2)
ax1.plot(years, model_complexity, label='Model Complexity (Billions of Params)', color='orangered', marker='o', linestyle='-', linewidth=2)

# Fill between lines to highlight the gap
ax1.fill_between(years, computational_power, model_complexity, color='lightgray', alpha=0.3)

# Secondary y-axis for the number of papers
ax2 = ax1.twinx()
ax2.bar(years, paper_count, color='lightgreen', alpha=0.6, width=2, label='ML Papers Published')

# Annotations for significant milestones
for year, event in milestones.items():
    comp_power = computational_power[(year - 1980) // 5]
    ax1.annotate(event,
                 xy=(year, comp_power),
                 xytext=(year, comp_power * 3),
                 arrowprops=dict(facecolor='black', arrowstyle='->', lw=0.8),
                 fontsize=9,
                 ha='center',
                 bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightblue'))

# Customizing plot appearance
ax1.set_title("Evolution of Computational Power and Machine Learning Model Complexity\nwith Research Output from 1980 to 2020",
              fontsize=16, fontweight='bold', ha='center')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Scale (Logarithmic)", fontsize=12)
ax1.set_yscale('log')
ax2.set_ylabel("Number of ML Papers", fontsize=12)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)
ax1.grid(True, linestyle='--', alpha=0.7)

# Adding legends
fig.legend(loc='upper left', fontsize=10, frameon=False, bbox_to_anchor=(0.1, 0.9))

# Tight layout for better spacing
fig.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display the plot
plt.show()