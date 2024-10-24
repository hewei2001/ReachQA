import matplotlib.pyplot as plt
import numpy as np

# Years and disciplines
years = np.arange(2010, 2020)
disciplines = ['Biology', 'Computer Science', 'Physics', 'Mathematics', 'Chemistry']

# Artificial data for paper submissions
paper_submissions = np.array([
    [50, 52, 60, 65, 70, 80, 95, 100, 110, 115],  # Biology
    [30, 35, 40, 50, 55, 65, 70, 85, 90, 100],   # Computer Science
    [40, 45, 50, 55, 60, 70, 80, 90, 100, 110],  # Physics
    [35, 40, 45, 50, 55, 60, 65, 70, 75, 80],    # Mathematics
    [25, 30, 35, 40, 50, 55, 60, 70, 80, 90],    # Chemistry
])

# Creating the heat map
plt.figure(figsize=(12, 7))
heat_map = plt.imshow(paper_submissions, cmap='YlGnBu', aspect='auto', interpolation='nearest')

# Adding a color bar with label
color_bar = plt.colorbar(heat_map)
color_bar.set_label('Number of Submissions', fontsize=12, labelpad=15)

# Titles and axis labels
plt.title('Trends in Scientific Paper Submissions\n(2010-2019)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Discipline', fontsize=12)

# Setting the ticks and labels for axes
plt.xticks(ticks=np.arange(len(years)), labels=years, rotation=45, ha='right')
plt.yticks(ticks=np.arange(len(disciplines)), labels=disciplines)

# Adding annotations for notable trends
plt.text(9, 0, 'Biology Surge', fontsize=10, color='black', ha='center', va='center', 
         bbox=dict(facecolor='white', edgecolor='none', alpha=0.8))
plt.text(9, 1, 'CS Innovation', fontsize=10, color='black', ha='center', va='center', 
         bbox=dict(facecolor='white', edgecolor='none', alpha=0.8))

# Adjusting layout for better fit and visibility
plt.tight_layout()

# Displaying the plot
plt.show()