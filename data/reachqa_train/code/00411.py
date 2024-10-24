import matplotlib.pyplot as plt
import numpy as np

# Data representing the number of participants enrolled in different wellness programs at community centers
yoga_participants = [25, 50, 20, 40, 35]
nutrition_workshops_participants = [30, 40, 45, 20, 25]
fitness_boot_camps_participants = [50, 70, 55, 60, 65]
mental_wellness_sessions_participants = [15, 20, 25, 30, 20]

# Aggregate data for box plot
data = [yoga_participants, nutrition_workshops_participants, 
        fitness_boot_camps_participants, mental_wellness_sessions_participants]

# Program labels
program_labels = ['Yoga', 'Nutrition Workshops', 'Fitness Boot Camps', 'Mental Wellness Sessions']

# Create the horizontal box plot
plt.figure(figsize=(12, 6))
box = plt.boxplot(data, vert=False, patch_artist=True, labels=program_labels, notch=True,
                  boxprops=dict(facecolor='lightblue', color='blue'),
                  whiskerprops=dict(color='blue'),
                  capprops=dict(color='blue'),
                  medianprops=dict(color='darkblue', linewidth=1.5))

# Customize colors for each box
colors = ['lightgreen', 'lightcoral', 'lightblue', 'plum']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Title and labels
plt.title('Participant Distribution in Wellville Community Wellness Programs', fontsize=14, weight='bold', pad=15)
plt.xlabel('Number of Participants', fontsize=12)
plt.ylabel('Wellness Program Type', fontsize=12)

# Grid and layout adjustments
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7, axis='x')
plt.tight_layout()

# Show the plot
plt.show()