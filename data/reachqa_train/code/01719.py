import matplotlib.pyplot as plt

# Define the data for each major, representing sleep hours in a day
computer_science_sleep = [5, 6, 6, 5.5, 7, 6.5, 6, 7, 6, 8]
literature_sleep = [6, 7, 7.5, 6.5, 8, 7.5, 7, 8, 6, 7.5]
engineering_sleep = [5, 5.5, 6, 5, 6.5, 5.5, 6, 6, 5.5, 7]
psychology_sleep = [6, 7, 6.5, 7, 7.5, 7, 7, 8, 7.5, 8.5]
fine_arts_sleep = [7, 8, 8.5, 7.5, 8, 7.5, 7, 9, 8, 8.5]

# Combine the datasets
sleep_data = [computer_science_sleep, literature_sleep, engineering_sleep, psychology_sleep, fine_arts_sleep]

# Define labels for the majors
majors = ['Computer Science', 'Literature', 'Engineering', 'Psychology', 'Fine Arts']

# Create the horizontal box plot
fig, ax = plt.subplots(figsize=(12, 8))
boxplot = ax.boxplot(sleep_data, vert=False, patch_artist=True, notch=True,
                     boxprops=dict(facecolor='lightblue', color='blue'),
                     whiskerprops=dict(color='blue'), capprops=dict(color='blue'),
                     flierprops=dict(marker='o', color='red', alpha=0.5),
                     medianprops=dict(color='red', linewidth=2))

# Set the labels and title
ax.set_yticklabels(majors, fontsize=12)
ax.set_xlabel('Hours of Sleep per Day', fontsize=12)
ax.set_title('Student Sleep Patterns Across Various University Majors\nA Comparative Study', fontsize=14, fontweight='bold')

# Customize the plot further
colors = ['lightcoral', 'lightgreen', 'lightskyblue', 'plum', 'wheat']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)

# Adding grid for readability
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Adjust layout to avoid overlapping
plt.tight_layout()

# Display the plot
plt.show()