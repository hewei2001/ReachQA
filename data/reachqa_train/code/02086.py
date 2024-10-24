import matplotlib.pyplot as plt
import numpy as np

# Define cities and their corresponding attendance numbers
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'San Francisco']
attendance = np.array([150000, 120000, 110000, 90000, 85000])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the bar chart
bar_positions = np.arange(len(cities))
bars = ax.bar(bar_positions, attendance, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], width=0.6)

# Annotate each bar with the attendance numbers
for bar, city in zip(bars, cities):
    height = bar.get_height()
    ax.annotate(f'{height:,}', 
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), 
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10, color='black')

# Set title and labels
ax.set_title('2023 Annual Arts Festival Attendance\nAcross Major Cities', fontsize=16, fontweight='bold')
ax.set_xlabel('City', fontsize=12)
ax.set_ylabel('Number of Attendees', fontsize=12)

# Set x-ticks and x-tick labels
ax.set_xticks(bar_positions)
ax.set_xticklabels(cities, rotation=45, ha='right', fontsize=10)

# Format y-axis to use commas in large numbers
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{int(x):,}"))

# Add gridlines to y-axis for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.6)

# Use tight layout to adjust the layout
plt.tight_layout()

# Display the plot
plt.show()