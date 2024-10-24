import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Define civilizations and their hypothetical contribution percentages
civilizations = ['Mesopotamia', 'Ancient Egypt', 'Indus Valley', 'Ancient China', 'Mesoamerican']
contributions = [25, 20, 18, 27, 10]  # Hypothetical data for illustration

# Colors for each civilization
colors = ['#e63946', '#f1faee', '#a8dadc', '#457b9d', '#2a9d8f']

# Create a figure for the ring chart
fig, ax = plt.subplots(figsize=(10, 7))

# Create the ring chart
wedges, texts, autotexts = ax.pie(
    contributions,
    labels=civilizations,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    wedgeprops=dict(width=0.4, edgecolor='w')
)

# Add an inner circle for the ring effect
inner_circle = Circle((0, 0), 0.55, color='white')
ax.add_artist(inner_circle)

# Central label
ax.text(0, 0, 'Tech Contributions', horizontalalignment='center', verticalalignment='center', fontsize=14, fontweight='bold', color='black')

# Equal aspect ratio ensures the pie chart is circular
ax.axis('equal')

# Title of the chart
ax.set_title("Ancient Civilizations' Technological Contributions", fontsize=16, fontweight='bold', pad=20)

# Ensure text size is consistent and readable
plt.setp(texts, size=10, fontweight='bold')
plt.setp(autotexts, size=9, color='black')

# Adjust layout to fit all elements nicely
plt.tight_layout()

# Display the chart
plt.show()