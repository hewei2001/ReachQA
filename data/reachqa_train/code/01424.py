import matplotlib.pyplot as plt
import numpy as np

# Define the data
labels = [
    'Smart Speakers', 'Smart Thermostats', 'Smart LED Bulbs', 
    'Smart RGB Strips', 'Smart Security Cameras', 'Smart Door Locks', 
    'Smart Smoke Detectors', 'Smart Refrigerators', 'Smart Ovens', 
    'Smart Washing Machines', 'Smart Irrigation Systems', 'Smart Vacuums'
]
sizes = [10, 8, 7, 5, 15, 6, 4, 9, 7, 8, 6, 15]
colors = plt.cm.viridis(np.linspace(0, 1, len(labels)))

# Create a figure and axis for plotting
fig, ax = plt.subplots(figsize=(11, 11), subplot_kw=dict(aspect="equal"))

# Create the donut pie chart
wedges, texts, autotexts = ax.pie(
    sizes, 
    labels=labels, 
    colors=colors, 
    autopct=lambda pct: '{:.1f}%\n({:d})'.format(pct, int(np.round(pct/100.*np.sum(sizes)))),
    startangle=140, 
    pctdistance=0.85,
    wedgeprops=dict(width=0.3), 
    explode=[0.05]*len(labels)
)

# Draw a white circle at the center to create the donut shape
center_circle = plt.Circle((0, 0), 0.55, fc='white')
fig.gca().add_artist(center_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')

# Adding title with line break for clarity
plt.title('Detailed Adoption Rates of Smart Home Technologies\n(A Comprehensive Survey)', fontsize=14, fontweight='bold', y=1.08)

# Customize the text of the percentage labels
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_size(10)
    autotext.set_weight('bold')

# Add a legend
ax.legend(wedges, labels, title="Technologies", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Automatically adjust the layout to ensure everything fits without overlapping
plt.tight_layout()

# Display the chart
plt.show()