import matplotlib.pyplot as plt

# Streaming services screen time data (in hours)
# Weekly average for each region
north_america = [18, 25, 15, 10, 20, 22, 21, 14, 19]
europe = [20, 17, 22, 18, 25, 19, 23, 16, 21]
asia = [15, 30, 18, 20, 28, 26, 22, 18, 24]
australia = [22, 28, 14, 16, 27, 23, 19, 21, 26]

# Compile data into a list for plotting
data = [north_america, europe, asia, australia]

# Regions
regions = ['North America', 'Europe', 'Asia', 'Australia']

# Create the horizontal box plot
fig, ax = plt.subplots(figsize=(12, 8))
boxprops = dict(facecolor='lightblue', color='blue', alpha=0.7)
whiskerprops = dict(color='blue', linestyle='--')
capprops = dict(color='blue')
medianprops = dict(color='darkblue', linewidth=2)

# Plotting the box plot
bplot = ax.boxplot(data, vert=False, patch_artist=True, labels=regions,
                   boxprops=boxprops, whiskerprops=whiskerprops,
                   capprops=capprops, medianprops=medianprops,
                   flierprops=dict(marker='o', color='blue', markersize=5, alpha=0.5))

# Title and labels
ax.set_title('Screen Time Consumption of Popular Streaming Services in 2023\n(Weekly Average Hours)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Screen Time (Hours)', fontsize=12)

# Grid for better readability
ax.grid(True, axis='x', linestyle='--', alpha=0.6)

# Annotate insights without overlapping text
annotations = {
    0: (22, 'Peak usage in\nNorth America with\nBingeWatch'),
    1: (25, 'Europe shows\nbalanced use'),
    2: (30, 'BingeWatch dominates\nin Asia'),
    3: (28, 'Australian StreamFlix\npreference')
}

for idx, (pos, text) in annotations.items():
    ax.annotate(text, xy=(pos, idx + 1), xytext=(pos + 5, idx + 1 - 0.1),
                arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=10, color='darkgreen', ha='center')

# Optimize layout to prevent any overlap
plt.tight_layout()

# Show the plot
plt.show()