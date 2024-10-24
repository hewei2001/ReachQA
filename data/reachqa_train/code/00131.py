import matplotlib.pyplot as plt

# Data for the donut pie chart
energy_sources = [40, 30, 15, 10, 5]
labels = ['Solar Energy', 'Wind Energy', 'Hydroelectric', 'Geothermal', 'Biomass']

# Colors for each segment
colors = ['#FDB813', '#2171B5', '#238B45', '#E6550D', '#756BB1']

# Explode the largest segment (Solar Energy) for emphasis
explode = (0.1, 0, 0, 0, 0)

# Create the pie chart with a donut shape
fig, ax = plt.subplots(figsize=(8, 8), dpi=100)
wedges, texts, autotexts = ax.pie(
    energy_sources,
    labels=labels,
    colors=colors,
    explode=explode,
    autopct='%1.1f%%',
    startangle=140,
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='white')
)

# Ensure the pie is drawn as a circle
ax.axis('equal')

# Set the title with a bold font style
ax.set_title('EcoCity 2030:\nRenewable Energy Sources Composition', fontsize=16, fontweight='bold', pad=20)

# Customize text and autotext for better visualization
for text, autotext in zip(texts, autotexts):
    text.set_fontsize(12)
    text.set_weight('semibold')
    autotext.set_color('white')
    autotext.set_fontsize(11)
    autotext.set_weight('bold')

# Add a legend explaining the colors
ax.legend(wedges, labels, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=11)

# Add annotation for the largest segment
ax.annotate('Leading Source: Solar',
            xy=(wedges[0].theta2 / 2, 1.1),
            xytext=(-1.5, 1.3),
            arrowprops=dict(facecolor='gray', shrink=0.05, width=1, headwidth=8),
            fontsize=11, fontweight='bold', color='black')

# Adjust layout
plt.tight_layout()

# Display the chart
plt.show()