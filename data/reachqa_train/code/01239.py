import matplotlib.pyplot as plt

# Satisfaction scores (1 to 10 scale) for each department
satisfaction_scores = {
    'Computer Science': [8, 7, 9, 6, 8, 7, 9, 10, 9, 5, 7, 6, 8, 9, 7, 9],
    'Humanities': [6, 5, 7, 8, 6, 5, 6, 7, 5, 5, 6, 7, 5, 8, 4, 5],
    'Business': [7, 8, 6, 8, 7, 7, 9, 6, 6, 7, 7, 6, 7, 8, 9, 7],
    'Engineering': [9, 8, 7, 9, 10, 8, 7, 9, 8, 9, 8, 8, 9, 9, 8, 7],
    'Sciences': [7, 8, 7, 8, 7, 8, 6, 7, 7, 8, 8, 9, 7, 8, 6, 7]
}

# Prepare data and labels
data = list(satisfaction_scores.values())
departments = list(satisfaction_scores.keys())

# Create the box plot
plt.figure(figsize=(12, 8))
box = plt.boxplot(data, notch=True, vert=True, patch_artist=True, labels=departments)

# Define colors and styling for each department box plot
colors = ['#FFDDC1', '#FFD1DC', '#C1E1FF', '#C1FFD7', '#FFE4C1']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Customize other elements of the box plot
plt.title('Student Satisfaction with Online Learning Platforms\nin Higher Education', fontsize=16, fontweight='bold')
plt.xlabel('Departments', fontsize=12)
plt.ylabel('Satisfaction Scores (1 to 10)', fontsize=12)
plt.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Set properties for whiskers and caps
for whisker in box['whiskers']:
    whisker.set(color='grey', linewidth=1.5)

for cap in box['caps']:
    cap.set(color='grey', linewidth=1.5)

for median in box['medians']:
    median.set(color='black', linewidth=2)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()