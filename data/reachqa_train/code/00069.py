import matplotlib.pyplot as plt
import numpy as np

# Define disciplines and funding sources
disciplines = ['Sciences', 'Engineering', 'Humanities', 'Social Sciences']
funding_sources = ['Government Grants', 'Private Sector', 'University Funds', 'Non-Profit Organizations']

# Data: Amount of funding in million USD
funding_data = np.array([
    [60, 30, 20, 10],  # Sciences
    [70, 20, 30, 15],  # Engineering
    [20, 10, 40, 30],  # Humanities
    [40, 15, 25, 20],  # Social Sciences
])

# Set up colors for different funding sources
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Create the stacked bar chart
fig, ax = plt.subplots(figsize=(10, 7))
bottom = np.zeros(len(disciplines))

for i, source in enumerate(funding_sources):
    ax.bar(disciplines, funding_data[:, i], label=source, bottom=bottom, color=colors[i], alpha=0.85)
    bottom += funding_data[:, i]

# Adding details to the plot
ax.set_title("Research Funding Sources by Discipline\nat Imaginary University", fontsize=14, fontweight='bold')
ax.set_xlabel('Academic Disciplines', fontsize=12)
ax.set_ylabel('Funding Amount (Million USD)', fontsize=12)
ax.legend(title='Funding Sources', loc='upper left', bbox_to_anchor=(1.05, 1), fontsize='small')

# Customize the y-axis
ax.set_yticks(np.arange(0, 141, 20))
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Rotate x-axis labels if needed
plt.xticks(rotation=15)

# Automatically adjust layout for better fit
plt.tight_layout()

# Show the plot
plt.show()