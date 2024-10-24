import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Data for the pie chart
destinations = ['Lunar Surface', 'Mars Base', 'Asteroid Resorts', 'Jupiter Orbit Hotel', 'Saturn Rings Cruise', 'Titan Outpost']
visit_percentages = [40, 30, 15, 5, 5, 5]

# Colors and patterns for each segment of the pie chart
colors = ['lightgray', 'red', 'darkorange', 'dodgerblue', 'lightyellow', 'violet']
patterns = ['/', '//', '\\', '\\\\', 'x', 'o']  # Add patterns to slices

# Highlight the Mars Base segment
explode = (0, 0.1, 0, 0, 0, 0)  # Only "explode" the Mars Base slice

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    visit_percentages,
    labels=destinations,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    explode=explode,
    wedgeprops={'edgecolor': 'black', 'linewidth': 1.5},
    shadow=True
)

# Adding patterns to each pie slice
for wedge, pattern in zip(wedges, patterns):
    wedge.set_hatch(pattern)

# Setting properties for text in the chart
plt.setp(autotexts, size=10, weight="bold", color="black")
plt.setp(texts, size=11, weight="bold")

# Set title and subtitle with line break
ax.set_title('Favorite Destinations for Space Tourism\nin 2040: A Futuristic Voyage', fontsize=14, fontweight='bold', pad=30)

# Adding detailed annotations for Mars Base segment
ax.annotate('Mars Base: Out of this world experience!',
            xy=(0, 0.5), xytext=(-80, 60),
            textcoords='offset points', arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, weight='bold')

# Adding a legend with custom icons representing destinations
custom_legends = [mpatches.Patch(color=col, label=dest) for col, dest in zip(colors, destinations)]
ax.legend(
    handles=custom_legends,
    title='Destinations',
    loc='center left',
    bbox_to_anchor=(1, 0.5),
    fontsize=10
)

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the plot
plt.show()