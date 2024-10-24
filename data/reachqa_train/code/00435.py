import matplotlib.pyplot as plt
import numpy as np

# Emotional impact scores for different music genres
classical_scores = [85, 90, 78, 92, 88, 84, 79, 95, 93, 86]
jazz_scores = [70, 75, 60, 80, 65, 85, 74, 82, 77, 68]
rock_scores = [55, 60, 58, 72, 65, 68, 75, 70, 66, 62]
pop_scores = [78, 80, 85, 83, 75, 80, 77, 82, 76, 79]
electronic_scores = [65, 70, 72, 68, 74, 75, 73, 78, 71, 69]

# Combine data into a list
data = [classical_scores, jazz_scores, rock_scores, pop_scores, electronic_scores]

# Labels for the genres
genres = ['Classical', 'Jazz', 'Rock', 'Pop', 'Electronic']

# Calculate average scores for the bar chart
average_scores = [np.mean(scores) for scores in data]

# Initialize the subplot with one row and two columns
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# Box Plot
box = axs[0].boxplot(data, patch_artist=True, notch=True, vert=False, labels=genres)
colors = ['#FFDDC1', '#D4A5A5', '#A1C4FD', '#C2CAD0', '#D6E0F0']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
axs[0].set_title("Emotional Impact of Music Genres on Listeners\n(Distribution View)", fontsize=14, fontweight='bold')
axs[0].set_xlabel("Emotional Impact Score")
axs[0].set_ylabel("Music Genres")
axs[0].grid(axis='x', linestyle='--', alpha=0.7)

# Violin Plot
violin = axs[1].violinplot(data, vert=False, showmeans=True, showextrema=True, showmedians=True)
axs[1].set_yticks(np.arange(1, len(genres) + 1))
axs[1].set_yticklabels(genres)
axs[1].set_title("Emotional Impact of Music Genres on Listeners\n(Density View)", fontsize=14, fontweight='bold')
axs[1].set_xlabel("Emotional Impact Score")
axs[1].grid(axis='x', linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()