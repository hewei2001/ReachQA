import matplotlib.pyplot as plt
import numpy as np

# Film genres
genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi']

# Revenue percentage data for each genre
revenue_percentages = [30, 25, 20, 15, 10]

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(10, 7))

# Define colors for each genre
colors = ['#FF4C4C', '#FFD700', '#82CAFF', '#FF7F50', '#9FE2BF']

# Create the bar chart
bars = ax.barh(genres, revenue_percentages, color=colors)

# Adding title and labels
ax.set_title("Global Box Office Revenue by Genre in 2023\n(Percentage Breakdown)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Revenue Percentage (%)", fontsize=14)
ax.set_ylabel("Film Genres", fontsize=14)

# Set x-axis limit for consistent percentage representation
ax.set_xlim(0, 100)

# Add percentage labels inside each bar
for bar, percentage in zip(bars, revenue_percentages):
    width = bar.get_width()
    ax.text(width - 5, bar.get_y() + bar.get_height()/2, f'{percentage}%', 
            ha='center', va='center', color='white', fontsize=12, fontweight='bold')

# Add grid for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust the layout to ensure everything fits well
plt.tight_layout()

# Show plot
plt.show()