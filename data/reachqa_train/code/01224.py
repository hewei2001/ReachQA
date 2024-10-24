import matplotlib.pyplot as plt
import squarify

# Data for urban garden spaces in square meters
urban_gardens = {
    'New York': {'Community Gardens': 5000, 'Rooftop Gardens': 3000, 'Vertical Gardens': 2000, 'Allotments': 1500},
    'Los Angeles': {'Community Gardens': 4500, 'Rooftop Gardens': 3500, 'Vertical Gardens': 2500, 'Allotments': 1700},
    'Chicago': {'Community Gardens': 4000, 'Rooftop Gardens': 3200, 'Vertical Gardens': 2200, 'Allotments': 1300},
    'San Francisco': {'Community Gardens': 3000, 'Rooftop Gardens': 2800, 'Vertical Gardens': 1500, 'Allotments': 1000},
    'Seattle': {'Community Gardens': 3500, 'Rooftop Gardens': 3000, 'Vertical Gardens': 1800, 'Allotments': 1200},
}

# Flatten the dictionary for plotting
labels = []
sizes = []
colors = ['#77DD77', '#FFB347', '#AEC6CF', '#FF6961', '#CB99C9', '#FDFD96', '#C23B22', '#FFB347', '#DEA5A4', '#77DD77']
counter = 0

for city, gardens in urban_gardens.items():
    for garden_type, area in gardens.items():
        labels.append(f'{city}\n{garden_type}\n{area} sq.m')
        sizes.append(area)
        counter += 1

# Plot the tree map
plt.figure(figsize=(14, 10))
squarify.plot(sizes=sizes, label=labels, color=colors[:len(sizes)], alpha=0.8, text_kwargs={'fontsize': 10})

# Title
plt.title("Urban Gardening Space Allocation\nin Major US Cities", fontsize=16, fontweight='bold', pad=20)

# Remove axes
plt.axis('off')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()