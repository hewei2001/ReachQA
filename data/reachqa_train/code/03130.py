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

# Construct data for a new subplot - average daily time spent (hours)
tv_hours = [4, 3.5, 3, 2.5, 2, 1.5, 1.2]
internet_hours = [0.5, 1, 1.5, 2.5, 3, 3.5, 4]
radio_hours = [1.5, 1.2, 1, 0.8, 0.6, 0.3, 0.2]
gaming_hours = [0.5, 1, 1.5, 2, 2.5, 3, 3.5]
streaming_hours = [0, 0.5, 1, 1.5, 2, 2.5, 3]

# Stack data for the area chart
data = np.vstack([tv_engagement, internet_engagement, radio_engagement, gaming_engagement, streaming_engagement])

# Create a subplot layout for both charts
fig, axes = plt.subplots(1, 2, figsize=(16, 7))
fig.suptitle('Evolution and Impact of Entertainment Mediums\n(1990-2020)', fontsize=16, fontweight='bold', y=1.05)

# Stacked area chart
ax1 = axes[0]
ax1.stackplot(years, data, labels=categories, colors=['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6'], alpha=0.8)
ax1.set_title('Population Engagement (%)', fontsize=14)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Percentage (%)', fontsize=12)
ax1.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10, title='Mediums')
ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, 101, 20))
ax1.tick_params(axis='x', rotation=45)

# Line chart for average daily hours spent
ax2 = axes[1]
ax2.plot(years, tv_hours, marker='o', label='Television', color='#fbb4ae', linewidth=2)
ax2.plot(years, internet_hours, marker='o', label='Internet', color='#b3cde3', linewidth=2)
ax2.plot(years, radio_hours, marker='o', label='Radio', color='#ccebc5', linewidth=2)
ax2.plot(years, gaming_hours, marker='o', label='Gaming', color='#decbe4', linewidth=2)
ax2.plot(years, streaming_hours, marker='o', label='Streaming', color='#fed9a6', linewidth=2)
ax2.set_title('Average Daily Time Spent (Hours)', fontsize=14)
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Hours per Day', fontsize=12)
ax2.legend(loc='upper left', fontsize=10)
ax2.set_xticks(years)
ax2.set_yticks(np.arange(0, 5, 0.5))
ax2.tick_params(axis='x', rotation=45)

# Adjust layout to prevent overlap and ensure clarity
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()