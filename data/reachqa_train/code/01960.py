import matplotlib.pyplot as plt
import numpy as np

# Define the categories of screen time and create corresponding GPA data
screen_time_categories = ['<3 hours', '3-5 hours', '5-7 hours', '>7 hours']

# Hypothetical GPA data for each screen time category
gpas_low = [3.5, 3.6, 3.8, 3.9, 4.0, 3.7, 3.6, 3.8, 3.9, 3.7, 3.8, 3.9]
gpas_moderate = [3.2, 3.4, 3.3, 3.5, 3.6, 3.4, 3.3, 3.5, 3.6, 3.3, 3.4, 3.5]
gpas_high = [3.0, 2.9, 3.1, 3.2, 3.0, 3.1, 3.0, 3.2, 3.1, 3.0, 3.0, 3.2]
gpas_very_high = [2.5, 2.6, 2.7, 2.8, 2.6, 2.7, 2.5, 2.6, 2.7, 2.8, 2.6, 2.7]

# Combine the data into a list for plotting
data = [gpas_low, gpas_moderate, gpas_high, gpas_very_high]

fig, ax = plt.subplots(figsize=(12, 8))

# Create a horizontal box plot
box = ax.boxplot(data, vert=False, patch_artist=True, notch=True, whis=1.5, 
                 positions=np.arange(1, len(screen_time_categories) + 1))

# Set custom colors for each box with gradients
colors = ['#FF6347', '#FFD700', '#4682B4', '#ADFF2F']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.6)

# Overlay a violin plot for more insight into data distribution
for i, d in enumerate(data):
    parts = ax.violinplot(d, positions=[i + 1], vert=False, showmeans=False, showmedians=False, showextrema=False)
    for pc in parts['bodies']:
        pc.set_facecolor(colors[i])
        pc.set_edgecolor('grey')
        pc.set_alpha(0.3)

# Scatter jittered data points
for i, category_data in enumerate(data):
    y = np.random.normal(i + 1, 0.02, size=len(category_data))
    ax.scatter(category_data, y, alpha=0.5, color='black', s=10, label='_nolegend_')

# Set the y-ticks and labels
ax.set_yticks(np.arange(1, len(screen_time_categories) + 1))
ax.set_yticklabels(screen_time_categories)

# Title and labels
ax.set_title('Screen Time vs. GPA:\nA Multi-Aspect Analysis of Student Habits', fontsize=16, fontweight='bold', color='navy')
ax.set_xlabel('GPA', fontsize=12)
ax.set_ylabel('Daily Screen Time Usage', fontsize=12)

# Add grid for better readability
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Customize whiskers and caps
for whisker, cap in zip(box['whiskers'], box['caps']):
    whisker.set(color='black', linewidth=1.5)
    cap.set(color='black', linewidth=1.5)

# Customize medians
for median in box['medians']:
    median.set(color='red', linewidth=2)

# Annotate median values
for i, median in enumerate(box['medians']):
    median_val = np.median(data[i])
    ax.annotate(f'{median_val:.2f}', xy=(median_val, i + 1), xytext=(5, -15), 
                textcoords='offset points', fontsize=10, color='darkred', weight='bold')

# Add a legend
colors_legend = ['Low (<3 hrs)', 'Moderate (3-5 hrs)', 'High (5-7 hrs)', 'Very High (>7 hrs)']
for i, color in enumerate(colors):
    ax.plot([], [], color=color, label=colors_legend[i], linewidth=7, alpha=0.6)
ax.legend(title='Screen Time Categories', loc='upper right', frameon=True)

# Adjust layout for better fit
plt.tight_layout()

# Display the plot
plt.show()