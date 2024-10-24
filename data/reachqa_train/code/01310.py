import matplotlib.pyplot as plt
import numpy as np

# Data for the horizontal bar chart
languages = ['English', 'Mandarin', 'Spanish', 'French', 'Arabic', 'Hindi']
communication_time = [5, 3.5, 4, 2.5, 1.5, 2]
time_variability = [0.5, 0.4, 0.3, 0.2, 0.1, 0.15]

# Colors for the bars and pie chart
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Data for the pie chart
context_distribution = [30, 20, 25, 15, 5, 5]  # Percentage representation
context_labels = ['Professional', 'Cultural', 'Home', 'Academia', 'Occasional', 'Community']

# Create a figure with subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(15, 8))

# Horizontal bar chart
bars = ax1.barh(languages, communication_time, color=colors, edgecolor='black', 
                height=0.7, xerr=time_variability, capsize=5)
ax1.set_title('Average Daily Communication Time in Multiple Languages:\nA Study on Polyglots in 2040', 
              fontsize=14, fontweight='bold', pad=20)
ax1.set_xlabel('Time Spent Communicating (Hours)', fontsize=12)
for bar in bars:
    width = bar.get_width()
    ax1.text(width + 0.2, bar.get_y() + bar.get_height() / 2, f'{width} hrs', 
             va='center', ha='left', fontsize=10, color='darkblue')

ax1.tick_params(axis='y', labelsize=12)
ax1.xaxis.grid(True, linestyle='--', alpha=0.6)

# Pie chart for communication context distribution
ax2.pie(context_distribution, labels=context_labels, autopct='%1.1f%%', startangle=140, 
        colors=colors, wedgeprops={'edgecolor': 'black'})
ax2.set_title('Distribution of Communication Contexts', fontsize=14, fontweight='bold')

# Adjust layout
plt.tight_layout()
plt.subplots_adjust(wspace=0.5)

# Show plot
plt.show()