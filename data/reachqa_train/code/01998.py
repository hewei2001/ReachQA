import matplotlib.pyplot as plt

# Define the number of books read per year by individuals in each age group
teenagers = [5, 12, 8, 10, 15, 18, 20, 7, 13, 10, 9, 11, 16, 14, 8]
young_adults = [10, 15, 22, 18, 25, 30, 14, 20, 16, 19, 21, 24, 23, 17, 29]
adults = [20, 25, 28, 22, 30, 35, 27, 32, 26, 31, 33, 34, 29, 23, 38]
middle_aged = [15, 18, 20, 25, 22, 24, 28, 21, 17, 30, 29, 26, 19, 23, 27]
seniors = [8, 12, 10, 11, 9, 13, 15, 17, 14, 16, 19, 20, 22, 21, 18]

# Compile the data into a list of lists for each age group
reading_data = [teenagers, young_adults, adults, middle_aged, seniors]

# Create labels for the age groups
age_labels = ['10-19', '20-29', '30-39', '40-49', '50+']

# Set up the figure for the box plot
fig, ax = plt.subplots(figsize=(10, 7))
box = ax.boxplot(reading_data, vert=True, patch_artist=True, labels=age_labels, notch=True, whis=1.5)

# Customizing the plot with colors and styles
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#CC99FF']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

# Customize whiskers, caps, and medians
for whisker in box['whiskers']:
    whisker.set(color='#8B8B8B', linewidth=1.5, linestyle='--')

for cap in box['caps']:
    cap.set(color='#8B8B8B', linewidth=1.5)

for median in box['medians']:
    median.set(color='black', linewidth=2)

# Title and labels
ax.set_title("Annual Reading Habits by Age Group:\nExploring Book Engagement Across Generations", fontsize=14, fontweight='bold')
ax.set_xlabel('Age Groups', fontsize=12)
ax.set_ylabel('Number of Books Read', fontsize=12)

# Adding annotations for outliers
for i, line in enumerate(box['fliers']):
    y = line.get_ydata()
    x = line.get_xdata()
    for (xi, yi) in zip(x, y):
        ax.text(xi, yi, f'{yi}', va='bottom', ha='right', fontsize=8, color=colors[i % len(colors)], alpha=0.8)

# Enhance the visual appeal
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Display the chart
plt.show()