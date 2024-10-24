import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2000 to 2020
years = np.arange(2000, 2021)

# Innovation adoption in educational sector over the years
e_learning = np.array([1, 2, 3, 5, 8, 12, 16, 20, 25, 31, 38, 46, 55, 65, 76, 88, 100, 113, 127, 142, 160])
collaboration_tools = np.array([0, 0, 1, 3, 5, 8, 12, 17, 23, 30, 38, 47, 57, 68, 80, 93, 107, 122, 138, 155, 173])
ai_learning = np.array([0, 0, 0, 1, 2, 3, 5, 8, 12, 17, 23, 30, 38, 47, 57, 68, 80, 93, 107, 122, 138])
virtual_classrooms = np.array([0, 0, 0, 0, 1, 3, 5, 8, 12, 16, 21, 27, 34, 42, 51, 61, 72, 84, 97, 111, 126])
digital_content = np.array([0, 0, 1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56, 67, 79, 92, 106, 121, 137, 154, 172])

# Create stacked area plot
fig, ax = plt.subplots(figsize=(14, 8))

# Stacking the areas to show cumulative values over time
ax.stackplot(years, e_learning, collaboration_tools, ai_learning, 
             virtual_classrooms, digital_content,
             labels=['E-Learning Platforms', 'Collaboration Tools', 'AI Learning Systems', 
                     'Virtual Classrooms', 'Digital Content'],
             colors=['#FF7F0E', '#1F77B4', '#2CA02C', '#D62728', '#9467BD'], alpha=0.85)

# Add labels, title, and legend with split title for better readability
ax.set_title("Technological Innovation in Education: \n2000-2020 Growth and Impact", 
             fontsize=18, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Impact Score on Education (Arbitrary Units)', fontsize=14)
ax.legend(loc='upper left', fontsize=12, bbox_to_anchor=(1.02, 1))
ax.grid(True, linestyle='--', alpha=0.5)

# Enhancing x-axis with year labels
ax.set_xticks(np.arange(2000, 2021, 5))
ax.tick_params(axis='x', rotation=45)

# Emphasize significant milestones with annotations
ax.annotate('Rise of E-Learning', xy=(2005, 5), xytext=(2006, 50),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='black')
ax.annotate('AI Integration Begins', xy=(2009, 1), xytext=(2010, 25),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='black')

# Automatically adjust layout for clarity
plt.tight_layout()

# Display the plot
plt.show()