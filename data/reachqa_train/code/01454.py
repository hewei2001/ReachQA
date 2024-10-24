import matplotlib.pyplot as plt

# Define data representing traffic congestion levels (percentages) for six cities
congestion_data = {
    'New York': [70, 72, 68, 65, 75, 80, 85, 77, 74, 73, 69, 66, 72, 78, 82, 79, 77, 75, 76, 73],
    'Los Angeles': [80, 83, 85, 82, 78, 81, 79, 84, 87, 88, 85, 84, 83, 82, 81, 80, 79, 84, 85, 86],
    'Chicago': [60, 62, 65, 64, 67, 69, 68, 70, 72, 74, 73, 71, 70, 68, 66, 65, 64, 63, 61, 62],
    'Houston': [55, 57, 59, 58, 60, 61, 62, 65, 66, 64, 63, 62, 60, 61, 60, 58, 57, 59, 62, 63],
    'Miami': [50, 52, 53, 55, 56, 57, 55, 54, 53, 52, 51, 50, 55, 54, 53, 52, 51, 50, 52, 54],
    'Seattle': [68, 70, 72, 71, 69, 67, 68, 70, 73, 75, 74, 73, 72, 71, 70, 68, 69, 71, 72, 73]
}

# Prepare data and labels for plotting
city_names = list(congestion_data.keys())
congestion_values = list(congestion_data.values())

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot a vertical box plot
boxplot = ax.boxplot(congestion_values, vert=True, patch_artist=True, notch=True, labels=city_names)

# Customize the appearance of the box plots
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.5)

# Style other elements of the box plot
plt.setp(boxplot['whiskers'], color='gray', linestyle='--')
plt.setp(boxplot['caps'], color='gray')
plt.setp(boxplot['medians'], color='black')

# Set title and labels
ax.set_title("Urban Traffic Congestion Analysis:\nPeak Morning Hours (8 AM - 10 AM)", fontsize=16, fontweight='bold')
ax.set_ylabel("Congestion Level (%)", fontsize=12)
ax.set_xlabel("Cities", fontsize=12)

# Enable grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()