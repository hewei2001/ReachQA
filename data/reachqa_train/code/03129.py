import matplotlib.pyplot as plt
import numpy as np

# Define years and entertainment categories
years = np.arange(1990, 2025, 5)
categories = ['Television', 'Internet', 'Radio', 'Gaming', 'Streaming']

# Adjusted data for each entertainment category over time
tv_engagement = [70, 65, 60, 50, 40, 30, 25]
internet_engagement = [5, 15, 25, 40, 50, 60, 65]
radio_engagement = [20, 15, 10, 8, 5, 3, 2]
gaming_engagement = [5, 10, 15, 20, 25, 30, 35]
streaming_engagement = [0, 5, 10, 15, 20, 30, 40]

# Stack data for the area chart
data = np.vstack([tv_engagement, internet_engagement, radio_engagement, gaming_engagement, streaming_engagement])

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(years, data, labels=categories, colors=['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6'], alpha=0.8)

# Title and labels
ax.set_title('Evolution of Entertainment Mediums\n(1990-2020)', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Percentage of Population Engaged (%)', fontsize=12)

# Add legend outside the plot area
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Mediums', fontsize=11)

# Enhance readability
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 101, 10))

# Adjust layout for better visibility
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Display the plot
plt.show()