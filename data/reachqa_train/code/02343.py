import matplotlib.pyplot as plt
import numpy as np

# Define decades for annotations
decades = np.array(['1920s', '1930s', '1940s', '1950s', '1960s', 
                    '1970s', '1980s', '1990s', '2000s', '2010s'])

# Number of attendees per genre (in hundreds)
fiction_attendees = np.array([5, 6, 8, 10, 12, 14, 15, 16, 20, 25])
non_fiction_attendees = np.array([4, 5, 7, 9, 11, 13, 13, 14, 15, 18])
poetry_attendees = np.array([3, 4, 4, 5, 6, 7, 8, 9, 11, 12])

# Average number of seminars offered per genre each decade
fiction_seminars = np.array([2, 3, 4, 5, 6, 7, 8, 9, 11, 13])
non_fiction_seminars = np.array([3, 3, 4, 5, 6, 7, 8, 8, 10, 11])
poetry_seminars = np.array([1, 2, 2, 3, 3, 4, 5, 6, 7, 8])

# Create the scatter plot
plt.figure(figsize=(12, 8))

# Plot each genre with different colors and markers
plt.scatter(fiction_attendees, fiction_seminars, c='navy', label='Fiction', marker='o', s=100, alpha=0.7)
plt.scatter(non_fiction_attendees, non_fiction_seminars, c='crimson', label='Non-fiction', marker='^', s=100, alpha=0.7)
plt.scatter(poetry_attendees, poetry_seminars, c='teal', label='Poetry', marker='s', s=100, alpha=0.7)

# Annotate points with respective decades
for i, decade in enumerate(decades):
    plt.annotate(decade, (fiction_attendees[i], fiction_seminars[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    plt.annotate(decade, (non_fiction_attendees[i], non_fiction_seminars[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    plt.annotate(decade, (poetry_attendees[i], poetry_seminars[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)

# Set titles and labels
plt.title('Ink and Insights: A Century of Famous Author Conventions', fontsize=16, fontweight='bold')
plt.xlabel('Number of Attendees (in hundreds)', fontsize=14)
plt.ylabel('Average Number of Seminars Offered', fontsize=14)

# Add a grid and legend
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(title='Literary Genres', title_fontsize='12', loc='upper left', fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()