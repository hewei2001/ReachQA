import matplotlib.pyplot as plt

# Data for cosmic influence elements
labels = ['Solar Flares', 'Planetary Alignments', 'Lunar Phases', 'Galactic Winds', 'Comet Showers']
influence_percentages = [30, 25, 20, 15, 10]

# Define colors for each section of the pie chart
colors = ['gold', 'coral', 'skyblue', 'violet', 'cyan']

# Create the pie chart
fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(aspect="equal"))

# Create the wedges, include shadow, and add percentages inside the slices
wedges, texts, autotexts = ax.pie(
    influence_percentages, labels=labels, autopct='%1.1f%%', startangle=140,
    colors=colors, shadow=True, wedgeprops=dict(edgecolor='w'), explode=(0.1, 0, 0, 0, 0)
)

# Customize the text inside the pie chart slices
plt.setp(autotexts, size=10, weight="bold", color="navy",
         bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='whitesmoke'))

# Annotate the center with a theme-related title
ax.annotate('Cosmic Influence\non Civilization', xy=(0, 0), fontsize=13, ha='center', fontweight='bold')

# Set the title of the chart with line breaks for better fit
ax.set_title('Elements of Cosmic Influence\non Planetary Development', fontsize=16, fontweight='bold', pad=30)

# Place the legend on the side for better clarity
ax.legend(wedges, labels, title="Cosmic Elements", loc="center left", bbox_to_anchor=(1.1, 0.5))

# Automatically adjust the layout
plt.tight_layout()

# Display the chart
plt.show()