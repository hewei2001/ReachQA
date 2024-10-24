import matplotlib.pyplot as plt
import numpy as np

# Define the data for bar chart
continents = ['Asia', 'Africa', 'Europe', 'North America', 'South America', 'Oceania']
popularity_increase = [42.1, 35.9, 28.3, 18.5, 15.2, 12.4]

# Define the data for line plot (the number of new listeners in millions)
new_listeners = [120, 75, 60, 45, 30, 20]

# Set up the figure and axis
plt.figure(figsize=(12, 8))
ax = plt.gca()  # Get current axis

# Plotting the bar chart
bar_positions = np.arange(len(continents))
bars = ax.bar(bar_positions, popularity_increase, color=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#CCCCFF', '#99FFCC'], edgecolor='black')

# Add data annotation on bars
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, round(yval, 1), ha='center', va='bottom', fontsize=10)

# Set the labels and title for bar chart
ax.set_ylabel('Increase in Listenership (%)', fontsize=12)
ax.set_xticks(bar_positions)
ax.set_xticklabels(continents, rotation=45, ha='right', fontsize=10)
ax.set_title('Renaissance of Classical Music:\nWorldwide Popularity in 2023', fontsize=14)

# Grid lines along the y-axis for better readability
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)

# Create a secondary axis for the line plot
ax2 = ax.twinx()

# Plot the line chart
line = ax2.plot(bar_positions, new_listeners, marker='o', color='black', label='New Listeners (in millions)')

# Set labels for the secondary y-axis
ax2.set_ylabel('New Listeners (in millions)', fontsize=12)
ax2.tick_params(axis='y', labelcolor='black')

# Ensure all elements fit well, adjust layout
plt.tight_layout()

# Add legend to show the data source of the line chart
ax2.legend(loc='upper right')

# Display the chart
plt.show()