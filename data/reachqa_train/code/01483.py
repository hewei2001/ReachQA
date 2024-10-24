import matplotlib.pyplot as plt

# Data for the Imaginaria festival interest distribution
art_forms = ['Painting', 'Sculpture', 'Music', 'Dance', 'Digital Art', 'Theater']
interests = [25, 15, 20, 10, 20, 10]

# Colors to represent each art form uniquely
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Explode the 'Painting' and 'Digital Art' slices for emphasis
explode = (0.1, 0, 0, 0, 0.1, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    interests, explode=explode, labels=art_forms, autopct='%1.1f%%',
    startangle=140, colors=colors, wedgeprops={'edgecolor': 'black'}, shadow=True
)

# Beautify text
for text in texts:
    text.set_fontsize(11)
    text.set_color('black')
    text.set_weight('bold')

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')
    autotext.set_fontsize(10)

# Add a title with context
plt.title(
    'Interest Distribution in Art Forms\nImaginaria: The Festival of Arts, 2023',
    fontsize=16, fontweight='bold', pad=20
)

# Enhanced legend
plt.legend(
    wedges, art_forms, title="Art Forms", loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10
)

# Additional annotation for context
plt.annotate(
    "Painting and Digital Art lead the festival's interest",
    xy=(-1.3, 1.1), xycoords='data', fontsize=10,
    bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='none')
)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()