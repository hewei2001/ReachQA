import matplotlib.pyplot as plt
import numpy as np

# Simulated data: hours spent on leisure activities per week
sports_hours = [3, 6, 9, 12, 1, 5, 11, 14, 10, 9, 2, 8, 12, 6, 7, 5, 3, 12, 11, 7, 4, 6, 8, 9, 10, 12, 14, 15, 3, 4, 8, 5, 7, 2, 10, 11, 13, 15, 5, 6, 9]
reading_hours = [2, 4, 3, 6, 3, 5, 7, 6, 8, 2, 1, 4, 3, 6, 4, 5, 3, 0, 2, 6, 5, 4, 3, 1, 8, 7, 9, 6, 5, 3, 2, 4, 5, 3, 6]
socializing_hours = [12, 14, 16, 18, 15, 17, 13, 20, 19, 11, 14, 16, 13, 15, 17, 19, 20, 18, 15, 13, 14, 16, 18, 19, 17, 15, 14, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
watching_tv_hours = [25, 28, 26, 30, 29, 27, 24, 23, 21, 22, 30, 28, 25, 24, 23, 29, 27, 26, 25, 24, 23, 22, 21, 20, 29, 30, 28, 26, 25, 24, 23, 22, 21, 20]
others_hours = [1, 2, 1, 3, 4, 2, 5, 1, 3, 2, 4, 1, 2, 3, 1, 4, 5, 2, 1, 2, 3, 1, 4, 5, 2, 3, 4, 0]

# Plotting the histogram
plt.figure(figsize=(14, 8))

# Defining custom bins for better visual grouping
bins = np.arange(0, 35, 5)

# Creating the histogram
plt.hist([sports_hours, reading_hours, socializing_hours, watching_tv_hours, others_hours], 
         bins=bins, 
         label=['Sports', 'Reading', 'Socializing', 'Watching TV', 'Others'], 
         alpha=0.7, 
         color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], 
         edgecolor='black')

# Title and axis labels
plt.title('Leisure Time Allocation in Leisureville:\nWeekly Hours Spent on Activities', fontsize=16, fontweight='bold')
plt.xlabel('Hours Spent', fontsize=12)
plt.ylabel('Number of Participants', fontsize=12)

# Adding legend
plt.legend(loc='upper right', title='Activities', title_fontsize='13')

# Applying grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()