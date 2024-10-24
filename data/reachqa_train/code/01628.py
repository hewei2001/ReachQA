import matplotlib.pyplot as plt

# Define legal systems and their distribution worldwide
legal_systems = ['Civil Law', 'Common Law', 'Customary Law', 'Mixed Systems', 'Other']
distribution = [40, 30, 15, 10, 5]

# Define distinct colors for each sector
colors = ['#4CAF50', '#FFC107', '#FF5722', '#00BCD4', '#9C27B0']

# Create a pie chart with customization
plt.figure(figsize=(8, 8))
wedges, texts, autotexts = plt.pie(
    distribution, labels=legal_systems, colors=colors,
    autopct='%1.1f%%', startangle=140, pctdistance=0.85,
    explode=(0.05, 0, 0.1, 0, 0.2)  # Highlight Mixed Systems and Other
)

# Customize text appearance
for text in texts:
    text.set_fontsize(12)
    text.set_fontweight('bold')

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

# Draw a circle at the center of the pie chart for a donut style
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Ensure the pie chart is a circle
plt.axis('equal')

# Add title
plt.title('Distribution of Global Legal Systems\nby Type', fontsize=16, fontweight='bold')

# Place legend outside the pie chart
plt.legend(wedges, legal_systems, title="Legal Systems", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust layout
plt.tight_layout()

# Display the chart
plt.show()