import matplotlib.pyplot as plt
import numpy as np

# Define fantasy sub-genres and their popularity in percentages
genres = ['Epic Fantasy', 'Urban Fantasy', 'Dark Fantasy', 'Magical Realism', 'Mythic Fantasy', 'Sword & Sorcery']
popularity_percentages = [25, 20, 15, 18, 12, 10]

# Define colors for each genre
colors = ['#FF5733', '#C70039', '#900C3F', '#581845', '#2E86C1', '#28B463']

# Explode the first slice to highlight "Epic Fantasy"
explode = (0.1, 0, 0, 0, 0, 0)

# Create related data for the second subplot
growth_percentages = [5, 3, 4, 6, 2, 3]  # Annual growth rates for each genre

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

# Pie chart on the left
ax1.pie(popularity_percentages, explode=explode, labels=genres, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=140, wedgeprops=dict(edgecolor='black'))
ax1.set_title('2025 Fantasy Books Genre Popularity:\nA Slice of Imagination', fontsize=14, fontweight='bold', pad=20)
ax1.legend(title='Genres', loc='upper right', bbox_to_anchor=(1.2, 0.8), shadow=True, fontsize=10)

# Horizontal bar chart on the right
y_pos = np.arange(len(genres))
ax2.barh(y_pos, growth_percentages, color=colors, edgecolor='black')
ax2.set_yticks(y_pos)
ax2.set_yticklabels(genres)
ax2.invert_yaxis()  # To keep the highest growth rate on top
ax2.set_xlabel('Growth Rate (%)', fontsize=12)
ax2.set_title('Annual Growth Rates of Fantasy Genres', fontsize=14, fontweight='bold', pad=20)

# Annotate growth rates on the bars
for i, v in enumerate(growth_percentages):
    ax2.text(v + 0.1, i, f"{v}%", color='black', va='center', fontweight='bold')

# Adjust layout to ensure no overlap
plt.tight_layout()

# Show the plots
plt.show()