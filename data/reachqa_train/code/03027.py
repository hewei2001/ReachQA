import matplotlib.pyplot as plt

# Data: Hours spent exercising per week by participants
exercise_hours = [
    5, 6, 7, 6, 5, 7, 8, 9, 6, 5, 10, 8, 7, 6, 8, 9, 10, 11, 9, 7,
    5, 12, 13, 7, 5, 8, 10, 11, 15, 16, 6, 8, 7, 5, 10, 9, 12, 14, 7, 6,
    9, 11, 9, 8, 10, 6, 12, 13, 5, 14, 17, 8, 9, 7, 10, 8, 6, 10, 11, 12
]

# Plot setup
plt.figure(figsize=(12, 7))
bins = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
plt.hist(exercise_hours, bins=bins, color='skyblue', edgecolor='black', alpha=0.7, histtype='bar')

# Titles and labels
plt.title('Distribution of Weekly Exercise Hours\nat the Wellness and Fitness Retreat', fontsize=16, fontweight='bold')
plt.xlabel('Hours Spent Exercising per Week', fontsize=14)
plt.ylabel('Number of Participants', fontsize=14)

# Grid and layout adjustments
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Annotating a significant detail
plt.annotate('Most Common\nExercise Range', xy=(8, 14), xytext=(10, 17),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
             fontsize=12, color='black', ha='center')

# Ensuring layout adjusts to avoid overlap
plt.xticks(bins, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()

# Display the plot
plt.show()