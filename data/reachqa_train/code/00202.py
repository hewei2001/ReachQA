import matplotlib.pyplot as plt

# Define the art style categories and their corresponding preferences
art_styles = [
    'Contemporary', 
    'Abstract', 
    'Surrealism', 
    'Impressionism', 
    'Minimalism', 
    'Traditional'
]
preferences = [28, 20, 18, 15, 12, 7]

# Define colors for the pie chart slices
colors = ['#6A5ACD', '#FF6347', '#FFD700', '#32CD32', '#FF69B4', '#8A2BE2']

# Explode the slice for Contemporary art to emphasize its popularity
explode = (0.1, 0, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(8, 8))

wedges, texts, autotexts = ax.pie(
    preferences, 
    labels=art_styles, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors,
    explode=explode,
    shadow=True,
    wedgeprops=dict(edgecolor='w', linewidth=1.5)
)

# Style the labels and percentage texts
for text in texts + autotexts:
    text.set_fontsize(10)
    text.set_weight('bold')

# Set title for the pie chart
ax.set_title(
    "Art Enthusiasts' Favorite Styles in 2023:\n"
    "A Snapshot of Global Artistic Preferences",
    fontsize=14, weight='bold', pad=20
)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the pie chart
plt.show()