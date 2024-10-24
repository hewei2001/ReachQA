import matplotlib.pyplot as plt
import matplotlib.patheffects as patheffects

# Data for the chart
tea_types = ['Green Tea', 'Black Tea', 'Herbal Tea', 'Oolong Tea', 'White Tea']
consumption_percentages = [30, 45, 10, 8, 7]

# Colors for each tea type
colors = ['#76c7c0', '#ff6347', '#98fb98', '#8a2be2', '#ffeb3b']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(aspect="equal"))

# Exploding the first segment (Green Tea) for emphasis
explode = [0.1, 0, 0, 0, 0]

# Plotting the donut pie chart
wedges, texts, autotexts = ax.pie(
    consumption_percentages,
    labels=tea_types,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    pctdistance=0.85,
    explode=explode,
    wedgeprops=dict(width=0.3, edgecolor='w')
)

# Add a shadow for depth
plt.setp(wedges, path_effects=[
    patheffects.withStroke(linewidth=3, foreground='white')
])

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')

# Add a title
plt.title('Global Tea Consumption Preferences', fontsize=14, fontweight='bold', pad=20)

# Customize the autotexts
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(12)
    autotext.set_fontweight('bold')

# Customize the legend
plt.legend(wedges, tea_types, title="Tea Types", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()