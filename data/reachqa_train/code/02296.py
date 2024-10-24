import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Delivery time data in hours for each city
delivery_times = {
    'New York': [1, 2, 2.5, 3, 4, 4.5, 5, 6, 6.5, 7, 8],
    'Los Angeles': [1.5, 2, 3, 3.5, 4, 4.5, 5.5, 6, 7, 8.5],
    'Chicago': [1, 2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8],
    'Houston': [2, 2.5, 3, 3.5, 4, 5, 5.5, 6, 6.5, 7, 9],
    'Miami': [1, 1.5, 2, 2.5, 3.5, 4, 5, 5.5, 6, 7, 8]
}

# Prepare data for the boxplot
data_to_plot = [delivery_times[city] for city in delivery_times]

# Set a style for the plot
sns.set(style="whitegrid")

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Create the horizontal box plot with additional features
box = ax.boxplot(data_to_plot, vert=False, patch_artist=True, 
                 labels=delivery_times.keys(), notch=True, whis=1.5, 
                 flierprops=dict(marker='o', color='r', alpha=0.5))

# Customize colors for each box and add mean indicators
colors = sns.color_palette("pastel")
means = []

for i, (patch, data) in enumerate(zip(box['boxes'], data_to_plot)):
    patch.set_facecolor(colors[i % len(colors)])
    # Calculate the mean for each city and plot it
    mean = np.mean(data)
    means.append(mean)
    ax.scatter(mean, i + 1, color='blue', marker='D', s=40, label='Mean' if i == 0 else "")

# Titles and labels
ax.set_title('E-commerce Delivery Time Distribution\nAcross Major US Cities', 
             fontsize=16, fontweight='bold', pad=20, loc='center')
ax.set_xlabel('Delivery Time (Hours)', fontsize=12)
ax.set_ylabel('Cities', fontsize=12)

# Add grid with minor ticks
ax.xaxis.grid(True, linestyle='--', alpha=0.7)
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.5))
ax.xaxis.grid(True, linestyle=':', which='minor', alpha=0.4)

# Add jittered scatter plot for raw data visibility
for i, data in enumerate(data_to_plot):
    y = np.random.normal(i + 1, 0.05, size=len(data))
    ax.scatter(data, y, alpha=0.4, color=colors[i % len(colors)], s=15)

# Annotate median and quartiles
for line, data in zip(box['medians'], data_to_plot):
    median = np.median(data)
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    x_median = line.get_xdata()[1]
    ax.text(x_median, line.get_ydata()[1] + 0.05, f'{median:.1f}', horizontalalignment='center')
    ax.annotate(f'Q1: {q1:.1f}', xy=(q1, line.get_ydata()[0]), 
                xytext=(q1, line.get_ydata()[0] - 0.3), textcoords='offset points', 
                arrowprops=dict(facecolor='black', arrowstyle='->', lw=0.5), fontsize=9)
    ax.annotate(f'Q3: {q3:.1f}', xy=(q3, line.get_ydata()[0]), 
                xytext=(q3, line.get_ydata()[0] + 0.3), textcoords='offset points', 
                arrowprops=dict(facecolor='black', arrowstyle='->', lw=0.5), fontsize=9)

# Legend
ax.legend(loc='upper right', fontsize=10)

# Use a tight layout to ensure nothing overlaps
plt.tight_layout()

# Display the plot
plt.show()