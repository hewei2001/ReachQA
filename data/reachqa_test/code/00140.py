import matplotlib.pyplot as plt
import numpy as np

# Original data: Hours spent weekly on different artistic disciplines by various artists
painting_hours = [12, 15, 14, 16, 20, 11, 13, 17, 18, 19, 15, 14, 16, 18, 17]
sculpting_hours = [10, 8, 9, 12, 11, 7, 8, 10, 9, 13, 11, 14, 9, 10, 12]
writing_hours = [20, 22, 21, 25, 23, 18, 19, 24, 23, 22, 21, 20, 22, 23, 25]
music_hours = [15, 18, 16, 17, 20, 14, 15, 19, 18, 21, 16, 17, 19, 16, 18]
digital_art_hours = [8, 12, 10, 14, 13, 7, 9, 15, 13, 14, 12, 13, 14, 11, 12]

# Related data: Average hours spent by different levels of artists
beginner_hours = [8, 9, 7, 10, 6]
intermediate_hours = [14, 13, 15, 12, 16]
expert_hours = [20, 18, 21, 19, 22]
artist_levels = ['Beginner', 'Intermediate', 'Expert']

# Data for plots
data = [painting_hours, sculpting_hours, writing_hours, music_hours, digital_art_hours]
average_hours = [beginner_hours, intermediate_hours, expert_hours]
disciplines = ['Painting', 'Sculpting', 'Writing', 'Music', 'Digital Art']

# Create figure and axis
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(14, 7), gridspec_kw={'width_ratios': [2, 1]})

# Box Plot
axs[0].boxplot(data, vert=False, patch_artist=True, labels=disciplines, notch=True, showmeans=True, meanline=True)
colors = ['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99']
for patch, color in zip(axs[0].artists, colors):
    patch.set_facecolor(color)
axs[0].set_title("The Secret Lives of Fictional Artists:\nAnalyzing Creative Time Allocation in 2023", fontsize=14, fontweight='bold')
axs[0].set_xlabel('Hours per Week', fontsize=12)
axs[0].set_ylabel('Artistic Disciplines', fontsize=12)
axs[0].xaxis.grid(True, linestyle='--', alpha=0.7)
means = [np.mean(hours) for hours in data]
for mean, discipline in zip(means, disciplines):
    axs[0].annotate(f'{mean:.1f}', xy=(mean, disciplines.index(discipline) + 1), xytext=(5, -5),
                    textcoords='offset points', fontsize=9, color='black', weight='bold')

# Violin Plot for Average Hours
parts = axs[1].violinplot(average_hours, vert=True, showmeans=True)
for i, pc in enumerate(parts['bodies']):
    pc.set_facecolor(colors[i])
axs[1].set_title("Average Hours by Artist Level", fontsize=12, fontweight='bold')
axs[1].set_xlabel('Artist Levels', fontsize=12)
axs[1].set_ylabel('Hours per Week', fontsize=12)
axs[1].set_xticks([1, 2, 3])
axs[1].set_xticklabels(artist_levels)
axs[1].grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()