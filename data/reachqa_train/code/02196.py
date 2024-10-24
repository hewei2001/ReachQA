import matplotlib.pyplot as plt
import numpy as np

# Define the years from 1990 to 2030
years = np.arange(1990, 2031)

# Create extended datasets with consistent lengths
e_learning = np.array([0]*10 + [1, 2, 3, 5, 8, 12, 16, 20, 25, 31, 38, 46, 55, 65, 76, 88, 100, 113, 127, 142, 160, 175, 192, 210, 230, 255, 280, 310, 340, 380, 420])
collaboration_tools = np.array([0]*10 + [0, 0, 1, 3, 5, 8, 12, 17, 23, 30, 38, 47, 57, 68, 80, 93, 107, 122, 138, 155, 173, 192, 212, 233, 255, 278, 302, 328, 355, 384, 415])
ai_learning = np.array([0]*10 + [0, 0, 0, 0, 1, 2, 3, 5, 8, 12, 17, 23, 30, 38, 47, 57, 68, 80, 93, 107, 122, 138, 155, 173, 192, 212, 233, 255, 278, 302, 328])
virtual_classrooms = np.array([0]*10 + [0, 0, 0, 0, 0, 1, 3, 5, 8, 12, 16, 21, 27, 34, 42, 51, 61, 72, 84, 97, 111, 126, 142, 159, 177, 196, 216, 237, 259, 282, 306])
digital_content = np.array([0]*10 + [0, 0, 1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56, 67, 79, 92, 106, 121, 137, 154, 172, 191, 211, 232, 254, 277, 301, 326, 352, 379, 407])
virtual_reality = np.array([0]*10 + [0, 0, 0, 0, 0, 1, 2, 4, 6, 9, 12, 16, 20, 25, 31, 38, 46, 55, 65, 76, 88, 101, 115, 130, 146, 163, 181, 200, 220, 241, 263])

# Create stacked area plot
fig, ax = plt.subplots(figsize=(14, 10))

# Stacking the areas to show cumulative values over time
ax.stackplot(years, e_learning, collaboration_tools, ai_learning, 
             virtual_classrooms, digital_content, virtual_reality,
             labels=['E-Learning Platforms', 'Collaboration Tools', 
                     'AI Learning Systems', 'Virtual Classrooms', 
                     'Digital Content', 'Virtual Reality'],
             colors=['#FF7F0E', '#1F77B4', '#2CA02C', '#D62728', '#9467BD', '#8C564B'], alpha=0.85)

# Enhance chart readability and aesthetics
ax.set_title("Technological Innovation in Education (1990-2030): \nGrowth and Impact Analysis", fontsize=18, fontweight='bold', ha='center')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Impact Score on Education (Arbitrary Units)', fontsize=14)
ax.legend(loc='upper left', fontsize=11, bbox_to_anchor=(1.01, 1))
ax.grid(True, linestyle='--', alpha=0.5)

# Enhance x-axis with year labels
ax.set_xticks(np.arange(1990, 2031, 5))
ax.tick_params(axis='x', rotation=45)

# Emphasize significant milestones with annotations
ax.annotate('E-Learning Surge', xy=(2005, 10), xytext=(1998, 100),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='black')
ax.annotate('AI Era Begins', xy=(2009, 1), xytext=(2003, 200),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='black')
ax.annotate('VR Adoption', xy=(2020, 10), xytext=(2025, 400),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='black')

# Automatically adjust layout for clarity
plt.tight_layout()

# Display the plot
plt.show()