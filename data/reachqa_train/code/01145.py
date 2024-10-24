import matplotlib.pyplot as plt

# Define data
civilizations = ['Egyptians', 'Mesopotamians', 'Greeks', 'Romans', 'Mayans']
wonders_count = [15, 8, 12, 20, 5]

# Define colors
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Explode the slice for better emphasis (e.g., Romans)
explode = (0, 0.1, 0, 0.1, 0)

# Create the pie chart with a white circle in the center
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    wonders_count,
    labels=civilizations,
    colors=colors,
    explode=explode,
    autopct='%1.1f%%',
    startangle=140,
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    shadow=True
)

# Draw a circle in the middle of the pie chart to create the 'donut' effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Title with backstory
plt.title(
    'Architectural Legacy of Ancient Civilizations:\nThe Wonders of the Ages',
    fontsize=14,
    fontweight='bold',
    color='navy',
    pad=20
)

# Enhance visual appearance
plt.setp(autotexts, size=10, weight='bold', color='black')
plt.setp(texts, size=10, weight='bold')

# Add a legend outside the plot for clarity
ax.legend(
    wedges, civilizations,
    title="Civilizations",
    loc='center left',
    bbox_to_anchor=(1, 0, 0.5, 1),
    fontsize=10,
    frameon=False
)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()