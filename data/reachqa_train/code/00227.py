import matplotlib.pyplot as plt
import numpy as np

# Define the transport categories and their corresponding percentages
modes_of_transport = ['Bicycles', 'Public Transit', 'Ride-sharing', 'Walking', 'Personal Cars']
percentages = [25, 40, 15, 10, 10]

# Additional data for a new subplot: hypothetical changes in mode usage over three years
years = ['2021', '2022', '2023']
usage_by_year = {
    'Bicycles': [20, 22, 25],
    'Public Transit': [35, 38, 40],
    'Ride-sharing': [12, 14, 15],
    'Walking': [8, 9, 10],
    'Personal Cars': [25, 17, 10]
}

colors = ['#f4a582', '#92c5de', '#d5a6bd', '#a1dab4', '#d6604d']

fig, axes = plt.subplots(1, 2, figsize=(15, 6))
fig.suptitle('Urban Transportation Preferences in 2023 and Trends Over Time', fontsize=18, weight='bold', y=1.05)

# First subplot: Horizontal bar chart
ax1 = axes[0]
bars = ax1.barh(modes_of_transport, percentages, color=colors, edgecolor='black', height=0.6)
for bar, percentage in zip(bars, percentages):
    ax1.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, f'{percentage}%', va='center', fontsize=10)

ax1.set_title('2023 Commuter Choices', fontsize=14)
ax1.set_xlabel('Percentage of Daily Commute')
ax1.set_ylabel('Modes of Transport')
ax1.xaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
ax1.set_xlim(0, 50)
ax1.invert_yaxis()
ax1.set_xticks(np.arange(0, 51, 10))

# Second subplot: Line plot showing trends over years
ax2 = axes[1]
for mode in modes_of_transport:
    ax2.plot(years, usage_by_year[mode], marker='o', label=mode, color=colors[modes_of_transport.index(mode)])

ax2.set_title('Trends in Transportation (2021-2023)', fontsize=14)
ax2.set_xlabel('Year')
ax2.set_ylabel('Usage Percentage')
ax2.set_ylim(0, 50)
ax2.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
ax2.legend(title='Modes of Transport', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
ax2.set_xticks(years)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()