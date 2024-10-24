import matplotlib.pyplot as plt
import numpy as np

# Data for specializations in Computer Science and Information Technology
specializations = [
    'Data Science', 
    'Cybersecurity', 
    'AI & ML', 
    'Software Engineering', 
    'Networking', 
    'Web Development'
]
percentages = [25, 20, 15, 18, 12, 10]

# Define a color palette
colors = plt.cm.Set3(np.linspace(0, 1, len(specializations)))

# Explode the 'Data Science' segment to highlight it
explode = (0.1, 0, 0, 0, 0, 0)  

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    percentages, 
    labels=specializations, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors, 
    pctdistance=0.85,
    explode=explode
)

# Enhance appearance of the pie chart
plt.setp(autotexts, size=10, weight="bold", color="black")
plt.setp(texts, size=12)

# Draw a circle at the center to transform the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Set the title of the pie chart, split into multiple lines for clarity
plt.title(
    'Distribution of Specializations Among \n'
    'Computer Science and Information Technology Graduates (2023)',
    fontsize=14, fontweight='bold'
)

# Equal aspect ratio ensures the pie chart is circular
ax.axis('equal')  

# Add a legend to the side
ax.legend(wedges, specializations, title="Specializations", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust layout to prevent clipping
plt.tight_layout()

# Show the plot
plt.show()