import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Data representing the distribution of magical creatures
creature_labels = ['Unicorns', 'Dragons', 'Fairies', 'Elves', 'Gnomes']
creature_distribution = [25, 15, 30, 20, 10]

# Define gradient-like colors and patterns for each slice of the pie chart
creature_colors = ['#FFB6C1', '#DC143C', '#FFD700', '#32CD32', '#8B4513']

# Create the pie chart with 3D effect
fig, ax = plt.subplots(figsize=(12, 8), subplot_kw=dict(aspect="equal"))
wedges, texts, autotexts = ax.pie(
    creature_distribution,
    labels=creature_labels,
    autopct='%1.1f%%',
    startangle=140,
    colors=creature_colors,
    pctdistance=0.85,
    wedgeprops=dict(edgecolor='black', linewidth=1.5),
    explode=(0.1, 0, 0, 0, 0),  # Explode the Unicorns slice for emphasis
    shadow=True
)

# Customize text and autotext properties for readability
plt.setp(texts, size=12, weight="bold")
plt.setp(autotexts, size=12, color='white', weight="bold")

# Add a donut effect by drawing a circle at the center
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Add annotations to the chart
for i, wedge in enumerate(wedges):
    angle = (wedge.theta2 - wedge.theta1) / 2. + wedge.theta1
    x = 0.7 * np.cos(np.deg2rad(angle))
    y = 0.7 * np.sin(np.deg2rad(angle))
    ax.annotate(f"{creature_labels[i]}\n({creature_distribution[i]}%)",
                xy=(x, y),
                xytext=(1.1, 0.6 - i*0.2),
                arrowprops=dict(arrowstyle="->", color='black'),
                bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='lightgrey'))

# Add a title with a line break for better layout
plt.title("Distribution of Magical Creatures\nin Enchanted Forests", fontsize=16, fontweight='bold', pad=30)

# Create a subplot with another pie to show additional details
fig, ax2 = plt.subplots(figsize=(8, 6))
gender_distribution_labels = ['Male', 'Female', 'Other']
gender_distribution = [40, 45, 15]  # Hypothetical gender distribution data

ax2.pie(
    gender_distribution,
    labels=gender_distribution_labels,
    autopct='%1.1f%%',
    startangle=90,
    colors=['#87CEEB', '#FF69B4', '#9370DB'],
    pctdistance=0.75,
    wedgeprops=dict(edgecolor='black', linewidth=1.2),
    shadow=True
)

# Add a subtitle for the new subplot
plt.title("Gender Distribution of Magical Creatures", fontsize=14, fontweight='bold', pad=20)

# Create legends for both plots
main_legend = mpatches.Patch(color='none', label='Main Chart: Creature Types')
gender_legend = mpatches.Patch(color='none', label='Subplot: Gender Distribution')

ax.legend(wedges, creature_labels, title="Creatures", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=12)
ax2.legend(loc="upper left", fontsize=10)

# Adjust layout for both plots to fit
plt.tight_layout()

# Show both plots
plt.show()