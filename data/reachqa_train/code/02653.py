import matplotlib.pyplot as plt
import numpy as np

# Define the expanded dataset
months = ['March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'January', 'February']
# Manually crafted data reflecting fictional resident activity percentages over months
hiking = [35, 40, 50, 30, 20, 15, 25, 20, 30, 20, 15, 25]
swimming = [15, 25, 30, 45, 50, 55, 30, 20, 10, 5, 0, 10]
cycling = [20, 25, 35, 30, 25, 20, 25, 20, 30, 25, 20, 30]
gardening = [30, 35, 40, 35, 25, 20, 30, 40, 50, 35, 30, 35]
running = [25, 30, 20, 25, 20, 15, 20, 25, 30, 25, 30, 40]
yoga = [10, 15, 20, 20, 25, 30, 25, 20, 15, 10, 5, 10]

# Stack data for plot
activities = np.vstack([hiking, swimming, cycling, gardening, running, yoga])

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting the stacked area chart
ax.stackplot(months, activities, labels=['Hiking', 'Swimming', 'Cycling', 'Gardening', 'Running', 'Yoga'],
             colors=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700', '#FF7F50'], alpha=0.85)

# Title and labels
ax.set_title("Diverse Recreational Activity Engagement\nin Sunnytown Across the Year", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Percentage of Population', fontsize=14)

# Enhance the legend
ax.legend(loc='upper left', fontsize=12, title='Activities', title_fontsize='13')

# Grid customization
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Annotate specific data points for educational insight
for month, hike, swim in zip(months, hiking, swimming):
    if hike == max(hiking):
        ax.annotate('Peak Hiking', xy=(month, sum(activities[:, months.index(month)])),
                    xytext=(month, sum(activities[:, months.index(month)]) + 10),
                    arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)

    if swim == max(swimming):
        ax.annotate('Peak Swimming', xy=(month, sum(activities[:, months.index(month)])),
                    xytext=(month, sum(activities[:, months.index(month)]) + 10),
                    arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()