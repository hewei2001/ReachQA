import matplotlib.pyplot as plt
import numpy as np

# Define genres and their proportion of stalls
genres = ['Classic Literature', 'Science Fiction', 'Fantasy', 'Mystery & Thriller', 'Non-Fiction', 'Young Adult']
stalls_percentage = [20, 15, 25, 10, 15, 15]

# Define absolute number of stalls for the bar chart
stalls_count = [200, 150, 250, 100, 150, 150]

# Define colors for each genre
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Create figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# --- Donut Chart (Left Subplot) ---
explode = (0, 0, 0.1, 0, 0, 0)  # Highlight "Fantasy"
ax1.pie(
    stalls_percentage,
    explode=explode,
    labels=genres,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    pctdistance=0.85,
    textprops={'fontsize': 10, 'weight': 'bold'}
)
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax1.add_artist(centre_circle)
ax1.set_title(
    "LitCity's Annual Book Fest\nGenre Distribution of Book Stalls",
    fontsize=14,
    fontweight='bold',
    wrap=True
)
ax1.axis('equal')

# --- Bar Chart (Right Subplot) ---
x = np.arange(len(genres))
ax2.bar(x, stalls_count, color=colors, alpha=0.7)
ax2.set_xticks(x)
ax2.set_xticklabels(genres, rotation=45, ha='right', fontsize=10)
ax2.set_ylabel('Number of Stalls', fontsize=12)
ax2.set_title('Number of Stalls by Genre', fontsize=14, fontweight='bold')
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Add bar labels
for i, v in enumerate(stalls_count):
    ax2.text(i, v + 5, str(v), ha='center', fontweight='bold')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()