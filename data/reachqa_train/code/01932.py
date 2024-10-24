import matplotlib.pyplot as plt
import numpy as np

# Expanded fictional worlds and their corresponding number of languages
worlds = ['Middle-earth', 'Westeros', 'Star Wars Galaxy', 'Star Trek Universe', 
          'Harry Potter World', 'Narnia', 'Discworld', 'Asimov Universe', 
          'Marvel Multiverse', 'DC Universe']
languages = [12, 8, 21, 12, 6, 7, 10, 15, 25, 20]

# Average complexity score for languages in each world
complexity = [4.5, 3.2, 5.8, 4.0, 3.0, 3.5, 4.0, 4.5, 6.0, 5.0]

# Colors for each bar
colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', 
          '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe']

# Plotting
fig, ax1 = plt.subplots(figsize=(14, 9))

# Create horizontal bars for the number of languages
bars = ax1.barh(worlds, languages, color=colors, edgecolor='black')

# Add data labels at the end of each bar for languages
for i, (value, world) in enumerate(zip(languages, worlds)):
    ax1.text(value + 0.5, i, f'{value}', va='center', fontsize=9, fontweight='bold', color='black')

# Twin axis for complexity scores
ax2 = ax1.twiny()
ax2.plot(complexity, np.arange(len(worlds)), 'o-', color='purple', marker='D', label='Average Complexity')

# Customize plots
ax1.set_xlabel('Number of Languages', fontsize=12, weight='bold')
ax1.set_ylabel('Fictional Worlds', fontsize=12, weight='bold')
ax2.set_xlabel('Average Complexity of Languages', fontsize=12, weight='bold', color='purple')
ax1.set_xlim(0, max(languages) + 5)
ax2.set_xlim(min(complexity) - 1, max(complexity) + 1)
ax1.grid(axis='x', linestyle='--', alpha=0.7)

# Enhance y-axis labels
ax1.set_yticklabels(worlds, fontsize=11, weight='bold', color='navy')

# Adding legends
ax1.legend(['Number of Languages'], loc='lower right', fontsize=10, frameon=False)
ax2.legend(loc='upper right', fontsize=10, frameon=False)

# Multiline title
plt.title('Linguistic Diversity and Complexity\n in Popular Fictional Worlds', fontsize=16, fontweight='bold', ha='center')

# Add average line
average_languages = np.mean(languages)
ax1.axvline(average_languages, color='grey', linewidth=1.5, linestyle='--')
ax1.text(average_languages + 1, len(worlds) - 1, f'Avg: {average_languages:.1f}', color='grey', fontsize=10, fontweight='bold')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the chart
plt.show()