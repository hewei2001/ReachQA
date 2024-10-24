import matplotlib.pyplot as plt

# Data: Projected global book publishing shares by genre in 2025 (in percentage)
genres = ['Fiction', 'Non-fiction', 'Science Fiction', 'Biography', 'Fantasy', 'Mystery', 'Romance']
percentages = [25, 20, 15, 10, 15, 10, 5]

# Colors for the slices
colors = ['#fa8072', '#8fbc8f', '#dda0dd', '#ffd700', '#6495ed', '#ee82ee', '#ffa500']

# Create the ring chart (donut chart)
plt.figure(figsize=(10, 7))
wedges, texts, autotexts = plt.pie(
    percentages,
    labels=genres,
    colors=colors,
    startangle=90,
    autopct='%1.1f%%',
    pctdistance=0.85,
    wedgeprops=dict(width=0.4, edgecolor='w'),
    textprops=dict(color='navy', fontsize=10)
)

# Enhance the aesthetics of the autotexts (percentage labels)
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontweight('bold')

# Draw a white circle in the center to create the ring effect
centre_circle = plt.Circle((0, 0), 0.75, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Title and layout adjustments
plt.title("Projected Global Book Publishing by Genre (2025)\nA Look Into Literary Trends", fontsize=14, weight='bold')

# Adjust layout to prevent text overlapping
plt.tight_layout()

# Add a legend that is outside the pie chart to avoid overlap
plt.legend(wedges, genres, title="Genres", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Show the plot
plt.show()