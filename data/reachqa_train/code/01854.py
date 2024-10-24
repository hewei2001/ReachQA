import matplotlib.pyplot as plt
import numpy as np

# Data for response times across different sectors (in hours)
financial_services = [1.5, 2.0, 2.5, 1.8, 2.1, 2.6, 1.7, 2.4, 2.9, 2.3]
healthcare = [3.0, 2.8, 3.2, 3.1, 3.5, 3.4, 3.3, 2.9, 3.6, 3.7]
technology = [1.0, 1.2, 1.3, 1.1, 1.4, 1.0, 1.2, 1.5, 1.6, 1.3]
government = [4.5, 4.0, 4.2, 4.8, 5.0, 4.7, 4.3, 4.6, 4.4, 4.9]
education = [3.8, 4.2, 3.9, 4.0, 4.1, 3.6, 3.7, 3.8, 4.3, 4.4]

# Combine data into a list for plotting
data = [financial_services, healthcare, technology, government, education]

# Colors for each box
colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightsalmon', 'lightpink']

# Create a horizontal box plot
plt.figure(figsize=(14, 8))
bp = plt.boxplot(data, vert=False, patch_artist=True, notch=True,
                 boxprops=dict(color='black'),
                 medianprops=dict(color='red', linewidth=2),
                 whiskerprops=dict(color='grey', linewidth=1.5),
                 capprops=dict(color='grey', linewidth=1.5),
                 flierprops=dict(marker='o', color='orange', markersize=8, linestyle='none', markeredgecolor='orange'))

# Set colors for each box
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Set title and labels
plt.title('Sector-Wise Cybersecurity\nIncident Response Times Analysis', fontsize=16, fontweight='bold')
plt.xlabel('Incident Response Time (Hours)', fontsize=12)
plt.ylabel('Sectors', fontsize=12)

# Set y-tick labels
plt.yticks([1, 2, 3, 4, 5], ['Financial Services', 'Healthcare', 'Technology', 'Government', 'Education'])

# Add a legend
legend_labels = ['Financial Services', 'Healthcare', 'Technology', 'Government', 'Education']
plt.legend([bp["boxes"][i] for i in range(5)], legend_labels, loc='lower right')

# Display means and annotate them
means = [np.mean(data_set) for data_set in data]
for idx, mean in enumerate(means, start=1):
    plt.scatter(mean, idx, color='purple', zorder=3)
    plt.annotate(f'Mean: {mean:.2f}', xy=(mean, idx), xytext=(mean + 0.2, idx - 0.3),
                 fontsize=9, color='purple', arrowprops=dict(facecolor='purple', arrowstyle='->', lw=1.5))

# Add gridlines for readability
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Add a reference line for the average response time
average_response_time = np.mean([item for sublist in data for item in sublist])
plt.axvline(average_response_time, color='blue', linestyle='--', linewidth=1.5, label=f'Overall Average: {average_response_time:.2f} hrs')

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()