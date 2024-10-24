import matplotlib.pyplot as plt

# Define the activities and their corresponding time allocations
activities = ['Research & Conceptualization', 'Sketching & Ideation',
              'Client Meetings', 'Software Modeling', 'Administrative']
time_distribution = [25, 20, 15, 30, 10]

# Define colors for each slice
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

# Create a sector pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(time_distribution, labels=activities, colors=colors,
                                  autopct='%1.1f%%', startangle=140, pctdistance=0.85,
                                  explode=(0.1, 0, 0, 0, 0))

# Enhance the text appearance
for text in texts:
    text.set_fontsize(10)
    text.set_weight('bold')
for autotext in autotexts:
    autotext.set_fontsize(9)
    autotext.set_color('black')

# Add a circle at the center to transform the pie chart into a donut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

# Add a title and subtitle to give more context
plt.title("Architect's Time Allocation\nDuring Conceptual Design Phase",
          fontsize=16, fontweight='bold', pad=20)

# Add a legend with a subtle shadow
plt.legend(wedges, activities, title="Activities", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), shadow=True)

# Automatically adjust layout for clarity and avoid occlusion
plt.tight_layout()

# Show the plot
plt.show()