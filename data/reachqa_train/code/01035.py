import matplotlib.pyplot as plt
import numpy as np

# Cuisines and their popularity percentages
cuisines = ['Italian', 'Chinese', 'Japanese', 'Indian', 'Mexican', 'French', 'Thai', 'Greek', 'Spanish']
preferences = [22, 18, 15, 13, 12, 9, 5, 4, 2]  # These percentages sum to 100

# Colors for the cuisines, using a coherent and appealing palette
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700', '#FFB6C1', '#FF69B4', '#B0E0E6', '#ADD8E6']

# Explode a bit for highlighting Italian cuisine
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0)

# Create a donut pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    preferences,
    explode=explode,
    labels=cuisines,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w'),  # Create donut by adjusting the width
    shadow=True  # Add a shadow effect for depth
)

# Customize text properties for clarity and style
plt.setp(texts, size=10, fontweight="bold")
plt.setp(autotexts, size=10, color="black", fontweight="bold")

# Adding a legend outside the pie chart
ax.legend(
    wedges, cuisines,
    title="Cuisines",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1)
)

# Title with multi-line for better fit and readability
ax.set_title(
    'Global Culinary Preferences:\nWorld\'s Favorite Cuisines Survey',
    fontsize=16,
    fontweight='bold',
    color='darkblue'
)

# Automatically adjust layout for better fit
plt.tight_layout()

# Show the plot
plt.show()