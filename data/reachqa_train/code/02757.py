import matplotlib.pyplot as plt

# Define project names
projects = ['Mars Colonization', 'Asteroid Mining', 'Space Telescope Development', 
            'Lunar Research', 'Exoplanet Discovery']

# Data: Percentage budget allocations for each project
budget_allocations = [30, 25, 20, 15, 10]  # Sum = 100%

# Colors for each project segment
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create the pie chart
plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(budget_allocations, 
                                   labels=projects, 
                                   colors=colors, 
                                   autopct='%1.1f%%',
                                   startangle=90, 
                                   pctdistance=0.85,
                                   wedgeprops=dict(width=0.3),
                                   explode=(0.05, 0, 0, 0, 0),
                                   shadow=True)

# Enhance percentage text inside the pie slices
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)

# Add a circle at the center to create a donut chart effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Ensure aspect ratio is equal to maintain the circular shape
plt.axis('equal')  

# Title of the chart
plt.title('IRA 2023 Budget Allocations\nStrategic Projects in Space Exploration', 
          fontsize=16, fontweight='bold', pad=20)

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Show the plot
plt.show()