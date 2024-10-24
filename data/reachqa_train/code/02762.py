import matplotlib.pyplot as plt

# Define themes and their popularity percentages
themes = ['Space Exploration', 'Time Travel', 'Artificial Intelligence', 'Dystopia', 'Cyberpunk', 'Alien Encounters']
popularity_percentages = [25, 20, 18, 15, 12, 10]

# Define colors for each theme
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']

# Explode the 'Space Exploration' theme for emphasis
explode = (0.1, 0, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    popularity_percentages, labels=themes, colors=colors, explode=explode, shadow=True,
    autopct='%1.1f%%', startangle=140, pctdistance=0.85
)

# Customize the text properties
for text in texts:
    text.set_fontsize(11)
    text.set_fontweight('bold')

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

# Add a circle at the center to create a donut chart effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)

# Equal aspect ratio ensures the pie chart is circular
ax.axis('equal')

# Set the title of the chart
plt.title('Global Science Fiction Literature:\nThemes and Popularity', fontsize=16, fontweight='bold')

# Add a legend
ax.legend(wedges, themes, title="Themes", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Adjust layout for optimal display
plt.tight_layout()

# Display the chart
plt.show()