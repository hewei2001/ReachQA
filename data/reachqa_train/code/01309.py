import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
languages = ['English', 'Mandarin', 'Spanish', 'French', 'Arabic', 'Hindi']
communication_time = [5, 3.5, 4, 2.5, 1.5, 2]  # Average daily time in hours

# Colors for the bars
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Create a horizontal bar chart
bars = ax.barh(languages, communication_time, color=colors, edgecolor='black', height=0.7)

# Title and labels
ax.set_title('Average Daily Communication Time in Multiple Languages:\nA Study on Polyglots in 2040', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Time Spent Communicating (Hours)', fontsize=14)

# Add data labels to the bars
for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.2, bar.get_y() + bar.get_height() / 2,
            f'{width} hrs', va='center', ha='left', fontsize=12, color='darkblue')

# Improve layout
ax.tick_params(axis='y', labelsize=12)
ax.xaxis.grid(True, linestyle='--', alpha=0.6)

# Add a legend
ax.legend(bars, ['Mostly professional use', 'Cultural exchanges', 
                 'Commonly spoken at home', 'Used in academia', 
                 'Occasional usage', 'Community language'],
          title='Communication Context', loc='lower right', fontsize=10, title_fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()