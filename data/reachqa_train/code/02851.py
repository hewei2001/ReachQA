import matplotlib.pyplot as plt
import numpy as np

# Define fantasy sub-genres and their popularity in percentages
genres = ['Epic Fantasy', 'Urban Fantasy', 'Dark Fantasy', 'Magical Realism', 'Mythic Fantasy', 'Sword & Sorcery']
popularity_percentages = [25, 20, 15, 18, 12, 10]

# Define colors for each genre
colors = ['#FF5733', '#C70039', '#900C3F', '#581845', '#2E86C1', '#28B463']

# Explode the first slice to highlight "Epic Fantasy"
explode = (0.1, 0, 0, 0, 0, 0)  # Only "Epic Fantasy" is exploded

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
ax.pie(popularity_percentages, explode=explode, labels=genres, colors=colors, autopct='%1.1f%%',
       shadow=True, startangle=140, wedgeprops=dict(edgecolor='black'))

# Set the title and style it
ax.set_title('2025 Fantasy Books Genre Popularity:\nA Slice of Imagination', fontsize=16, fontweight='bold', pad=20)

# Position the legend
ax.legend(title='Genres', loc='upper left', bbox_to_anchor=(1, 0.8), shadow=True, fontsize=10)

# Adjust layout to ensure no overlap
plt.tight_layout()

# Show the plot
plt.show()