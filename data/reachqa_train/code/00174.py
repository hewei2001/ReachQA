import matplotlib.pyplot as plt

# Define companies and their employee satisfaction scores
companies = ['Company A', 'Company B', 'Company C', 'Company D', 'Company E']
satisfaction_scores = [
    [7, 8, 9, 6, 8, 9, 7, 8, 10, 7],  # Company A
    [5, 6, 5, 7, 6, 8, 5, 7, 6, 7],  # Company B
    [9, 8, 10, 7, 9, 8, 10, 9, 8, 9], # Company C
    [6, 7, 6, 5, 7, 6, 8, 7, 5, 6],  # Company D
    [8, 9, 8, 9, 7, 9, 8, 10, 8, 9]  # Company E
]

# Create a horizontal box chart
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data with notches to show confidence intervals
boxplot = ax.boxplot(satisfaction_scores, vert=False, patch_artist=True, notch=True, whis=1.5)

# Customize the appearance
colors = ['skyblue', 'lightgreen', 'salmon', 'lightcoral', 'plum']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)

# Whisker lines customization
for whisker in boxplot['whiskers']:
    whisker.set(color='black', linewidth=1.5)

# Median line customization
for median in boxplot['medians']:
    median.set(color='blue', linewidth=2)

# Set axis labels and title with multiline for clarity
ax.set_yticklabels(companies)
ax.set_xlabel('Satisfaction Score', fontsize=12)
ax.set_title('Employee Satisfaction Scores\nAcross Leading Tech Companies', fontsize=14, fontweight='bold', pad=15)

# Enable grid lines for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout
plt.tight_layout()

# Display the chart
plt.show()