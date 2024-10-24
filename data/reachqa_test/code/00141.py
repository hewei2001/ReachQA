import matplotlib.pyplot as plt
import numpy as np

# Original data for the bar chart
animals = ['Squirrels', 'Raccoons', 'Pigeons', 'Foxes', 'Hawks', 'Bats']
sightings = [150, 45, 90, 20, 30, 60]

# New data for the line chart
weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4']
squirrel_sightings = [40, 35, 50, 25]  # Weekly squirrel sightings

# Create a figure and two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plot the bar chart on the first subplot
bars = ax1.bar(animals, sightings, color=['#7A9E9F', '#FFB85F', '#C8C8A9', '#FF7A5A', '#FF6F61', '#3E606F'])
ax1.set_title('Urban Wildlife Sightings in Metrotown\nSurveyed Over a Month', fontsize=14, pad=20)
ax1.set_xlabel('Type of Animal', fontsize=12)
ax1.set_ylabel('Number of Sightings', fontsize=12)
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Add value labels on top of each bar
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, height + 2, f'{height}', ha='center', va='bottom', fontsize=10, color='black')

# Plot the line chart on the second subplot
ax2.plot(weeks, squirrel_sightings, marker='o', linestyle='-', color='#FF6F61', markersize=8, linewidth=2)
ax2.set_title('Weekly Squirrel Sightings', fontsize=14, pad=20)
ax2.set_xlabel('Week', fontsize=12)
ax2.set_ylabel('Number of Sightings', fontsize=12)
ax2.grid(linestyle='--', alpha=0.7)

# Annotate specific data points on the line chart
for i, (week, sighting) in enumerate(zip(weeks, squirrel_sightings)):
    ax2.annotate(f'{sighting}', (week, sighting), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10)

# Adjust layout to prevent overlap and ensure readability
plt.tight_layout()

# Display the combined plot
plt.show()