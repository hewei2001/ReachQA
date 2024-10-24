import matplotlib.pyplot as plt
import numpy as np

# Original travel categories and corresponding data for each decade
categories = ["Adventure", "Relaxation", "Cultural", "Nature"]
# Adventure, Relaxation, Cultural, Nature for each decade (1980s, 1990s, 2000s, 2010s)
travel_data = [
    [60, 65, 80, 70],  # Adventure
    [70, 75, 80, 85],  # Relaxation
    [50, 55, 60, 75],  # Cultural
    [55, 60, 65, 70],  # Nature
]

# Transpose data to fit the format required for box plots
transposed_data = np.array(travel_data).T

# Create additional data for the line plot
years = ["1980s", "1990s", "2000s", "2010s"]
# Introduce slight variance for visual interest
line_data = np.array([
    [58, 63, 78, 73],  # Adventure with slight variance
    [72, 78, 77, 86],  # Relaxation with slight variance
    [52, 57, 62, 72],  # Cultural with slight variance
    [53, 62, 67, 68],  # Nature with slight variance
])

# Create the figure and axes for subplots
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

# Create the box plot on the first subplot
boxprops = dict(linestyle='-', linewidth=2, color='darkblue')
medianprops = dict(linestyle='-', linewidth=2, color='darkgreen')
bp = axs[0].boxplot(transposed_data, vert=True, patch_artist=True, labels=categories,
                boxprops=boxprops, medianprops=medianprops, notch=True,
                whiskerprops=dict(linewidth=1.5, color='black'),
                capprops=dict(linewidth=1.5),
                flierprops=dict(marker='o', color='red', markersize=5, alpha=0.5))

colors = ['lightcoral', 'lightblue', 'lightgreen', 'lightyellow']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

axs[0].set_title("Evolution of Travel Preferences\n(1980s-2010s)", fontsize=14)
axs[0].set_xlabel("Travel Categories", fontsize=12)
axs[0].set_ylabel("Preference Score (out of 100)", fontsize=12)
axs[0].yaxis.grid(True, linestyle='--', alpha=0.7)

# Add a legend for the box plot
legend_labels = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
axs[0].legend(legend_labels, years, title="Decades", loc='upper left')

# Create the line plot on the second subplot
for idx, category in enumerate(categories):
    axs[1].plot(years, line_data[idx], marker='o', label=category)

axs[1].set_title("Trends in Travel Preferences\nby Category", fontsize=14)
axs[1].set_xlabel("Decades", fontsize=12)
axs[1].set_ylabel("Preference Score (out of 100)", fontsize=12)
axs[1].yaxis.grid(True, linestyle='--', alpha=0.7)

# Add a legend for the line plot
axs[1].legend(title="Categories", loc='upper left')

# Automatically adjust layout for readability
plt.tight_layout()

# Show the plot
plt.show()