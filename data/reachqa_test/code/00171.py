import matplotlib.pyplot as plt
import numpy as np

# Data setup
scientists = ["Albert Einstein", "Marie Curie", "Isaac Newton", "Charles Darwin", "Ada Lovelace"]
citations = [1540, 1100, 1320, 980, 1210]
publications = [80, 60, 70, 50, 65]

# Plot setup
fig, ax1 = plt.subplots(figsize=(14, 8))

# Bar chart for citations
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
bars = ax1.bar(scientists, citations, color=colors, width=0.6, label='Citations')

# Setting titles and labels
ax1.set_title('Influential Scientific Publications\nCitations vs. Publications', fontsize=16, pad=20)
ax1.set_ylabel('Number of Citations', fontsize=12)
ax1.set_xlabel('Scientist', fontsize=12)

# Adding annotations for each bar
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 20, f'{yval:,}', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Adding a grid for better visualization
ax1.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Secondary y-axis for the line plot
ax2 = ax1.twinx()
ax2.set_ylabel('Number of Publications', fontsize=12)
line_plot = ax2.plot(scientists, publications, color='purple', linestyle='--', marker='o', linewidth=2, label='Publications')

# Legends for both plots
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper left')

# Adjust x-ticks to avoid label overlapping
plt.xticks(rotation=30, ha='right', fontsize=11)

# Ensuring a tight layout
plt.tight_layout()

# Display the chart
plt.show()