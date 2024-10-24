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

# Average price per book in dollars
average_prices = np.array([
    [12, 14, 10, 15],  # 2018
    [13, 15, 11, 16],  # 2019
    [14, 16, 12, 17],  # 2020
    [15, 17, 13, 18],  # 2021
    [16, 18, 14, 19]   # 2022
])

# Calculate total revenue per year in millions of dollars
revenue = np.sum(sales_data * average_prices, axis=1)

# Colors for each genre
colors = {
    'Fiction': '#1f77b4',
    'Non-Fiction': '#ff7f0e',
    'Science Fiction': '#2ca02c',
    'Fantasy': '#d62728'
}

# Create figure and axis
fig, ax1 = plt.subplots(figsize=(12, 7))

# Initialize the bottom offset for stacking bars
bottoms = np.zeros(len(years))

# Plot each genre's sales on top of each other
for idx, genre in enumerate(genres):
    ax1.bar(years, sales_data[:, idx], label=genre, bottom=bottoms, color=colors[genre], alpha=0.8)
    bottoms += sales_data[:, idx]

# Set title and labels for the bar chart
ax1.set_title("Global Book Sales & Revenue Trends:\nGenre Insights from 2018 to 2022", fontsize=14, weight='bold')
ax1.set_ylabel("Sales (Millions of Copies)", fontsize=12)
ax1.set_xlabel("Year", fontsize=12)
ax1.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
plt.xticks(rotation=45)

# Create a second y-axis for the line plot
ax2 = ax1.twinx()
ax2.plot(years, revenue, label='Total Revenue', color='purple', marker='o', linestyle='-', linewidth=2, markersize=6)
ax2.set_ylabel("Revenue (Millions of Dollars)", fontsize=12, color='purple')
ax2.tick_params(axis='y', labelcolor='purple')

# Show legends for both plots
ax1.legend(title='Genre', loc='upper left', bbox_to_anchor=(1, 1))
ax2.legend(loc='upper left', bbox_to_anchor=(1, 0.9))

# Adjust layout to prevent clipping of ylabel/legend
fig.tight_layout()

# Display the plot
plt.show()