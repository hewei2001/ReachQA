import matplotlib.pyplot as plt
import numpy as np

# Define the transport categories and their corresponding percentages
modes_of_transport = ['Bicycles', 'Public Transit', 'Ride-sharing', 'Walking', 'Personal Cars']
percentages = [25, 40, 15, 10, 10]

# Define colors for the bar chart
colors = ['#f4a582', '#92c5de', '#d5a6bd', '#a1dab4', '#d6604d']

# Create the percentage bar chart
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the horizontal bar chart
bars = ax.barh(modes_of_transport, percentages, color=colors, edgecolor='black', height=0.6)

# Adding the data labels
for bar, percentage in zip(bars, percentages):
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, f'{percentage}%', 
            va='center', color='black', fontsize=10)

# Set the title and labels
ax.set_title('Urban Transportation Preferences in 2023:\nCommuter Choices in a Modern City', 
             fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Percentage of Daily Commute', fontsize=12)
ax.set_ylabel('Modes of Transport', fontsize=12)

# Customizing the grid and axis
ax.xaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
ax.set_xlim(0, 50)  # Ensure 0-50 range to better visualize percentage differences
plt.xticks(np.arange(0, 51, 10))

# Invert the y-axis to have the largest percentage on top
ax.invert_yaxis()

# Ensure a tight layout
plt.tight_layout()

# Display the chart
plt.show()