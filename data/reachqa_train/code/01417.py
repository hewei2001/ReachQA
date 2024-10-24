import matplotlib.pyplot as plt

# Define the data for the architectural styles
styles = ['Modern', 'Classical', 'Art Deco', 'Gothic', 'Futuristic']
percentages = [35, 25, 15, 10, 15]
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']
explode = (0.1, 0, 0, 0, 0)  # Emphasize the Modern style

# Create the pie chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    percentages,
    labels=styles,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode
)

# Styling the text
plt.setp(autotexts, size=12, weight='bold', color='white')
plt.setp(texts, size=12)

# Add a title, breaking it into multiple lines if necessary
ax.set_title(
    'Architectural Styles in Architectura City\n'
    'Distribution of New Developments in the 2020s',
    fontsize=16,
    fontweight='bold'
)

# Add a legend with title
ax.legend(
    wedges,
    styles,
    title='Styles',
    loc='upper right',
    bbox_to_anchor=(1.3, 1)
)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()