import matplotlib.pyplot as plt

# Data for the pie chart
labels = ['Solar Energy', 'Wind Energy', 'Hydropower', 'Biomass', 'Geothermal']
sizes = [25, 20, 30, 15, 10]
colors = ['#FFD700', '#1E90FF', '#228B22', '#8B4513', '#FF4500']
explode = (0.1, 0, 0, 0, 0)  # Explode the largest section to highlight Hydropower

# Create the pie chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, pctdistance=0.85, textprops=dict(color="w"))

# Style the text to ensure readability
for text in texts:
    text.set_fontsize(10)
    text.set_color('black')
for autotext in autotexts:
    autotext.set_fontsize(8)
    autotext.set_weight('bold')

# Draw circle for 'doughnut' effect
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')  

# Set title with a line break for better readability
plt.title("Distribution of Renewable Energy Sources\nin EcoLand - 2023", fontsize=14, weight='bold', y=1.05)

# Legend outside the pie chart
plt.legend(wedges, labels, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Adjust layout
plt.tight_layout()

# Show the pie chart
plt.show()