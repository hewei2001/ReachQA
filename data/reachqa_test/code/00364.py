import matplotlib.pyplot as plt
import numpy as np

# Data
genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Romance', 'Sci-Fi', 'Thriller']
grossing_amounts = [15000, 12000, 9000, 7500, 6000, 4500, 3000]

# Colors
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ccccff', '#ff66cc', '#33cc33']

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Plot horizontal bars
ax.barh(genres, grossing_amounts, height=0.5, color=colors, edgecolor='black')

# Add value labels on the end of each bar
for i, amount in enumerate(grossing_amounts):
    ax.text(amount + 500, i, f'${amount}M', va='center', ha='left', weight='bold')

# Set title and labels
ax.set_title("Box Office Hits:\nTop-Grossing Movie Genres of the Last Decade",
             fontsize=14, fontweight='bold')
ax.set_xlabel('Grossing Amount (Millions of Dollars)', fontsize=12)
ax.set_ylabel('Movie Genre', fontsize=12)

# Adjust tick parameters
ax.tick_params(axis='y', length=0, labelsize=12)
ax.set_yticks(np.arange(len(genres)))
ax.set_yticklabels(genres, ha='center', fontsize=12)

# Add grid lines
ax.grid(axis='x', linestyle='--', alpha=0.5, linewidth=0.5)

# Add a legend
ax.legend(['Grossing Amount'], loc='upper right', fontsize=12, frameon=True)

# Automatically adjust the image layout
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Show the plot
plt.show()