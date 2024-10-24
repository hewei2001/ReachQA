import matplotlib.pyplot as plt

# Data setup for endangered species in Crystal Lake National Park
species = ['Amethyst Frogs', 'Emerald Owls', 'Golden Eagles', 'Ruby Bears']
population_counts = [45, 30, 20, 5]

# Define distinct colors for each species
colors = ['#8e44ad', '#27ae60', '#f39c12', '#e74c3c']

# Option to highlight one species by separating its slice
explode = (0.1, 0, 0, 0)  # Explode the first slice for Amethyst Frogs

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    population_counts,
    labels=species,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode,
    shadow=True,
    pctdistance=0.85
)

# Customize text properties for clarity and style
for text in texts + autotexts:
    text.set_fontsize(10)
    text.set_weight('bold')
for autotext in autotexts:
    autotext.set_color('white')

# Draw a circle at the center to transform pie into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Title with multiple lines for better readability
plt.title('Distribution of Endangered Species\nin Crystal Lake National Park',
          fontsize=14, fontweight='bold', pad=20)

# Position the legend outside the pie chart
ax.legend(wedges, species, title='Species', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

# Ensure layout is optimized to prevent overlap
plt.tight_layout()

# Display the pie chart
plt.show()