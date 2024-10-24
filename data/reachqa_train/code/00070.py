import matplotlib.pyplot as plt
import numpy as np

# Define a larger set of disciplines and funding sources
disciplines = [
    'Sciences', 'Engineering', 'Humanities', 'Social Sciences',
    'Business', 'Mathematics', 'Medicine', 'Law', 'Art', 'Education'
]
funding_sources = [
    'Government Grants', 'Private Sector', 'University Funds',
    'Non-Profit Organizations', 'International Bodies'
]

# Construct complex funding data matrix: Amounts in million USD over 3 years
funding_data = np.array([
    [[60, 65, 70], [30, 28, 35], [20, 25, 27], [10, 15, 18], [5, 7, 9]],  # Sciences
    [[70, 72, 75], [20, 22, 21], [30, 35, 33], [15, 18, 22], [8, 9, 12]],  # Engineering
    [[20, 22, 25], [10, 12, 13], [40, 42, 45], [30, 32, 31], [12, 15, 14]], # Humanities
    [[40, 43, 48], [15, 18, 20], [25, 27, 26], [20, 25, 24], [10, 11, 13]], # Social Sciences
    [[35, 36, 40], [20, 18, 22], [22, 24, 25], [18, 20, 19], [11, 10, 9]],  # Business
    [[25, 27, 29], [10, 14, 16], [18, 20, 21], [15, 13, 14], [8, 7, 6]],    # Mathematics
    [[80, 85, 90], [25, 27, 30], [35, 38, 40], [30, 35, 38], [12, 15, 17]], # Medicine
    [[30, 33, 34], [12, 15, 16], [28, 30, 33], [20, 22, 21], [9, 10, 11]],  # Law
    [[15, 17, 19], [8, 7, 9], [12, 15, 17], [18, 16, 19], [6, 8, 5]],       # Art
    [[45, 48, 50], [20, 22, 23], [30, 33, 35], [25, 27, 29], [11, 12, 13]], # Education
])

# Set up colors for different funding sources
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create a plot for each year to show changes over time
fig, axs = plt.subplots(3, 1, figsize=(14, 18), sharex=True)

years = [2021, 2022, 2023]
for year_index, ax in enumerate(axs):
    bottom = np.zeros(len(disciplines))
    for i, source in enumerate(funding_sources):
        ax.bar(disciplines, funding_data[:, i, year_index], label=source if year_index == 0 else "", bottom=bottom, color=colors[i], alpha=0.85)
        bottom += funding_data[:, i, year_index]
    ax.set_title(f"Research Funding Sources by Discipline in {years[year_index]}")
    ax.set_ylabel('Funding Amount (Million USD)')
    ax.yaxis.grid(True, linestyle='--', alpha=0.7)
    ax.set_ylim(0, 250)  # Adjust y-axis for clarity
    ax.annotate(f'Total Funding: {int(bottom.sum())} M USD', xy=(0.5, 0.9), xycoords='axes fraction', fontsize=10, ha='center')

# Set a common x-axis label
axs[-1].set_xlabel('Academic Disciplines')
plt.xticks(rotation=45, ha='right')

# Add a global title
fig.suptitle("Research Funding Distribution by Discipline over Three Years\nat Imaginary University", fontsize=16, fontweight='bold')

# Add the legend to the first subplot
axs[0].legend(title='Funding Sources', loc='upper left', bbox_to_anchor=(1.05, 1), fontsize='small')

# Automatically adjust layout for better fit
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Show the plot
plt.show()