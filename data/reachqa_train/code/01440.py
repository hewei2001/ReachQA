import matplotlib.pyplot as plt

# Define the data for the architectural styles
styles = [
    'Modern', 'Classical', 'Art Deco', 'Gothic', 'Futuristic',
    'Baroque', 'Renaissance', 'Neoclassical', 'Minimalist', 'Brutalism', 'Romanesque'
]
percentages = [20.5, 15.5, 10.2, 8.8, 7.0, 6.5, 5.5, 5.5, 6.0, 7.0, 7.0]

# The sum of percentages must exactly equal 100, accounting for minor floating-point errors
# However, here it's slightly off, so let's fix it by making a small adjustment.
total = sum(percentages)
correction = 100 - total
percentages[-1] += correction  # Adjust the last percentage to make the sum exactly 100

# Recheck if the sum of percentages equals 100 (allowing a small floating-point margin)
assert abs(sum(percentages) - 100) < 1e-9, "Percentages must sum up to 100."

# Define colors using a color map for better diversity and visibility
colors = plt.cm.viridis([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.15, 0.25])

# Set explode to highlight significant categories
explode = tuple(0.1 if p >= 10 else 0 for p in percentages)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 10))
wedges, texts, autotexts = ax.pie(
    percentages,
    labels=styles,
    autopct=lambda pct: f'{pct:.1f}%\n({pct / 100 * 1000:.0f}/1000)',
    startangle=140,
    colors=colors,
    explode=explode
)

# Styling the text
plt.setp(autotexts, size=10, weight='bold', color='white')
plt.setp(texts, size=10)

# Add a title, breaking it into multiple lines if necessary
ax.set_title(
    'Architectural Styles Distribution in Architectura City\n'
    'Breakdown of New Developments in the 2020s\n'
    'Data as Percentage and Fractional Representation',
    fontsize=14,
    fontweight='bold'
)

# Add a legend with title
ax.legend(
    wedges,
    styles,
    title='Styles',
    loc='upper left',
    bbox_to_anchor=(1, 1)
)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()