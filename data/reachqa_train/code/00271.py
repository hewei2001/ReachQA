import matplotlib.pyplot as plt
import numpy as np

# Define the years and genres
years = ['2018', '2019', '2020', '2021', '2022']
genres = ['Fiction', 'Non-Fiction', 'Science Fiction', 'Fantasy']

# Data: sales in millions of copies
sales_data = np.array([
    [45, 30, 15, 10],  # 2018
    [50, 28, 17, 12],  # 2019
    [55, 25, 20, 15],  # 2020
    [52, 22, 25, 18],  # 2021
    [60, 20, 30, 20]   # 2022
])

# Colors for each genre
colors = {
    'Fiction': '#1f77b4',      # Blue
    'Non-Fiction': '#ff7f0e',  # Orange
    'Science Fiction': '#2ca02c', # Green
    'Fantasy': '#d62728'       # Red
}

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

# Initialize the bottom offset for stacking bars
bottoms = np.zeros(len(years))

# Plot each genre's sales on top of each other
for idx, genre in enumerate(genres):
    ax.bar(years, sales_data[:, idx], label=genre, bottom=bottoms, color=colors[genre], alpha=0.8)
    bottoms += sales_data[:, idx]

# Title and labels
ax.set_title("Trends in Global Book Sales:\nGenre Insights from 2018 to 2022", fontsize=14, weight='bold')
ax.set_ylabel("Sales (Millions of Copies)", fontsize=12)
ax.set_xlabel("Year", fontsize=12)

# Show legend
ax.legend(title='Genre', loc='upper left', bbox_to_anchor=(1, 1))

# Enable grid for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Adjust layout to prevent clipping of ylabel/legend
plt.tight_layout()

# Display the plot
plt.show()