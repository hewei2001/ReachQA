import matplotlib.pyplot as plt
import numpy as np

# Initiatives and their corresponding funding in millions of dollars
initiatives = [
    "Coral Reef Restoration",
    "Marine Protected Areas",
    "Pollution Clean-up",
    "Sustainable Fisheries",
    "Public Education & Awareness",
    "Marine Research & Innovation"
]
funding = [25, 30, 15, 20, 10, 18]  # Funding in millions

# Hypothetical impact scores for each initiative
impact_scores = [8, 9, 6, 7, 4, 5]  # Impact scores out of 10

# Define a color palette using a colormap
cmap = plt.get_cmap('cool')
colors = cmap(np.linspace(0.15, 0.85, len(initiatives)))

# Create a figure and axis
fig, ax1 = plt.subplots(figsize=(12, 7))

# Create the horizontal bar chart
bars = ax1.barh(initiatives, funding, color=colors, edgecolor='black', height=0.6)

# Annotate the funding values on the bars
for bar in bars:
    ax1.text(
        bar.get_width() + 0.5,
        bar.get_y() + bar.get_height() / 2,
        f'{bar.get_width()}M',
        va='center',
        ha='left',
        fontsize=10,
        color='black'
    )

# Set the title and labels for the bar chart
ax1.set_title(
    'Funding Distribution and Impact Scores\nfor Ocean Conservation Initiatives',
    fontsize=14,
    fontweight='bold',
    pad=20
)
ax1.set_xlabel('Funding in Millions ($M)', fontsize=12)
ax1.set_ylabel('Initiatives', fontsize=12)

# Style adjustments for the bar chart
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_color('grey')
ax1.spines['bottom'].set_color('grey')

# Add vertical gridlines
ax1.xaxis.grid(True, linestyle='--', color='grey', alpha=0.6)

# Customize y-tick labels
ax1.set_yticks(np.arange(len(initiatives)))
ax1.set_yticklabels(initiatives, fontsize=11)

# Create a twin axis for the overlay plot
ax2 = ax1.twiny()

# Plot the impact scores as a line plot
ax2.plot(impact_scores, np.arange(len(initiatives)), 'o-', color='darkred', label='Impact Score')
ax2.set_xlabel('Impact Score (1-10)', fontsize=12, color='darkred')

# Customize the twin axis
ax2.spines['top'].set_visible(False)
ax2.tick_params(axis='x', colors='darkred')

# Add a legend for the line plot
ax2.legend(loc='lower right', fontsize=10)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()