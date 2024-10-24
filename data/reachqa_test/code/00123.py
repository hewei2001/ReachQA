import matplotlib.pyplot as plt
import numpy as np

# Define the years and genres
years = np.arange(2010, 2021)
genres = ['Action', 'Comedy', 'Drama']

# Data: Global box office revenue (in billions USD) for each genre over the years
action_revenue = np.array([20, 22, 25, 28, 31, 33, 36, 37, 40, 42, 45])
comedy_revenue = np.array([15, 16, 18, 19, 21, 22, 23, 24, 26, 26.5, 27])
drama_revenue = np.array([10, 11, 12, 12.5, 13, 13.8, 14.5, 15, 15.5, 16, 16.5])

# Calculate total revenue across all genres for each year
total_revenue = action_revenue + comedy_revenue + drama_revenue

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot each genre's data with markers and line styles
ax1.plot(years, action_revenue, label='Action', marker='o', linestyle='-', linewidth=2, color='darkred')
ax1.plot(years, comedy_revenue, label='Comedy', marker='s', linestyle='--', linewidth=2, color='gold')
ax1.plot(years, drama_revenue, label='Drama', marker='^', linestyle='-.', linewidth=2, color='navy')

# Add an area plot for the total revenue
ax2 = ax1.twinx()  # Create a second y-axis
ax2.fill_between(years, total_revenue, color='lightgrey', alpha=0.5, label='Total Revenue (All Genres)')

# Add titles and labels
ax1.set_title("Global Cinema Revenue Trends: \nA Decade of Blockbusters and Flops (2010-2020)", fontsize=16, pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Revenue per Genre (Billion USD)', fontsize=12)
ax2.set_ylabel('Total Revenue (Billion USD)', fontsize=12)

# Add grid, legend, and customize tick marks
ax1.grid(True, linestyle='--', color='grey', alpha=0.5)
fig.legend(loc='upper center', fontsize=10, ncol=4, bbox_to_anchor=(0.5, 0.9))
plt.xticks(years, rotation=45)

# Annotate specific years with events that influenced these genres
annotations = [
    (2012, action_revenue[2], "Avengers Franchise\nDebut"),
    (2014, comedy_revenue[4], "Rise of\nStreaming Services"),
    (2018, drama_revenue[8], "Oscar-winning\nDramas Surge")
]

for year, value, note in annotations:
    ax1.annotate(note, (year, value), textcoords="offset points", xytext=(-70,10), ha='center',
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='black'))

# Annotate each data point with its value for genre lines
for i, year in enumerate(years):
    ax1.text(year, action_revenue[i] + 0.5, f'{action_revenue[i]}', fontsize=9, color='darkred', ha='center')
    ax1.text(year, comedy_revenue[i] + 0.5, f'{comedy_revenue[i]}', fontsize=9, color='gold', ha='center')
    ax1.text(year, drama_revenue[i] + 0.5, f'{drama_revenue[i]}', fontsize=9, color='navy', ha='center')

# Ensure the layout is tight so nothing is cut off
plt.tight_layout()

# Display the chart
plt.show()