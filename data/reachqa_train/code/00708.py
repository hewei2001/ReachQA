import matplotlib.pyplot as plt

# Data for the proportions of mythical creatures in folklore
mythical_creatures = ['Dragons', 'Unicorns', 'Fairies', 'Giants', 'Mermaids']
proportions = [35, 15, 20, 10, 20]

# Colors for each section of the donut chart
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create the donut pie chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(proportions, labels=mythical_creatures, colors=colors,
                                  autopct='%1.1f%%', startangle=140, pctdistance=0.85,
                                  wedgeprops=dict(width=0.3, edgecolor='w'), 
                                  explode=(0.05, 0, 0, 0, 0))

# Draw a circle at the center to ensure it appears as a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Ensure the pie is circular by setting equal aspect ratio
ax.axis('equal')  

# Add a title to the chart, using multiple lines for better readability
plt.title("Proportion of Mythical Creatures\nin Folklore Narratives", fontsize=16, pad=20)

# Modify the properties of the autotexts for better visibility
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(12)
    autotext.set_weight('bold')

# Add a legend with a slight outside offset to avoid overlapping the chart
plt.legend(wedges, mythical_creatures, title="Creatures", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust the layout to prevent overlapping text
plt.tight_layout()

# Display the plot
plt.show()