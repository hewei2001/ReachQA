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

# Create a horizontal box plot
fig, ax = plt.subplots(figsize=(10, 6))
box = ax.boxplot(data, vert=False, patch_artist=True, notch=True, whis=1.5, 
                 positions=np.arange(1, len(screen_time_categories) + 1))

# Set custom colors for each box
colors = ['#FF6347', '#FFD700', '#4682B4', '#ADFF2F']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Set the y-ticks and labels
ax.set_yticks(np.arange(1, len(screen_time_categories) + 1))
ax.set_yticklabels(screen_time_categories)

# Title and labels
ax.set_title('Screen Time vs. GPA:\nAnalyzing Student Habits', fontsize=16, fontweight='bold', color='navy')
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

# Avoid overlapping and ensure the layout is tight
plt.tight_layout()

# Display the plot
plt.show()