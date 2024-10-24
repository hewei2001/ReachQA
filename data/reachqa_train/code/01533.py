import matplotlib.pyplot as plt
import numpy as np

# Define the days of the week
days = np.array(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
num_days = len(days)

# Define the regions
regions = ['Sunnyville', 'Desertscape', 'Cloudland']
num_regions = len(regions)

# Power generation data in megawatts (MW)
power_data = np.array([
    [150, 180, 170, 200, 220, 230, 210],  # Sunnyville
    [260, 250, 240, 245, 265, 280, 275],  # Desertscape
    [60,  55,  65,  70,  68,  75,  72]    # Cloudland
])

# Create the meshgrid
x = np.arange(num_days)
y = np.arange(num_regions)
_xx, _yy = np.meshgrid(x, y)

# Prepare data for bar3d
x, y = _xx.ravel(), _yy.ravel()
z = np.zeros_like(x)
dz = power_data.ravel()

# Plotting
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# Color map for regions
colors = ['skyblue', 'sandybrown', 'lightgreen']

# Plot each region's data
for i, color in enumerate(colors):
    ax.bar3d(x[i*num_days:(i+1)*num_days], y[i*num_days:(i+1)*num_days], z[i*num_days:(i+1)*num_days],
             dx=0.6, dy=0.5, dz=dz[i*num_days:(i+1)*num_days], color=color, alpha=0.8, label=regions[i])

# Set axis labels
ax.set_xlabel('Days of the Week', labelpad=12)
ax.set_ylabel('Regions', labelpad=12)
ax.set_zlabel('Power Generation (MW)', labelpad=12)

# Set the ticks for x and y axes
ax.set_xticks(np.arange(num_days) + 0.3)
ax.set_xticklabels(days, rotation=45, ha='right')
ax.set_yticks(np.arange(num_regions) + 0.25)
ax.set_yticklabels(regions)

# Set a view angle
ax.view_init(elev=20, azim=40)

# Set the title
ax.set_title('Weekly Solar Power Generation\nAcross Different Regions', fontsize=16, fontweight='bold', pad=20)

# Add a legend
ax.legend(title="Regions", loc='upper left')

# Adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()