import matplotlib.pyplot as plt

# Data for the wizarding economy sectors
labels = [
    'Potion Ingredients', 
    'Magical Artifacts', 
    'Transport & Logistics', 
    'Defense & Protection', 
    'Recreation & Events'
]
sizes = [30, 25, 20, 15, 10]  # Percentage contributions
colors = ['#FFDDC1', '#C3E2DD', '#FFD1D1', '#FFE5B4', '#C9B6E4']  # Enchanted color palette
explode = (0.1, 0, 0, 0, 0)  # Slightly explode the 'Potion Ingredients' sector

# Create the sector pie chart
plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(
    sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140,
    pctdistance=0.85, explode=explode
)

# Enhance the pie chart with magic-inspired properties
for text in texts + autotexts:
    text.set_color('darkblue')
    text.set_fontweight('bold')

# Draw a circle in the center to turn the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Title of the chart
plt.title("Contribution of Magical Creatures\n to Wizarding Economy", fontsize=16, fontweight='bold', color='darkgreen')

# Aspect ratio to ensure it's a circle
plt.axis('equal')

# Add a legend to the side
plt.legend(wedges, labels, title="Sectors", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=12)

# Automatically adjust layout for better fit
plt.tight_layout()

# Show the plot
plt.show()