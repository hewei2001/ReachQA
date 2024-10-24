import matplotlib.pyplot as plt
import numpy as np

# Define programming languages
languages = ['Python', 'JavaScript', 'Java', 'C++', 'Rust']

# Artificial survey data representing popularity scores
python_scores = [8, 9, 8, 10, 9, 7, 9, 8, 9, 10]
javascript_scores = [7, 8, 6, 7, 8, 7, 6, 7, 8, 8]
java_scores = [6, 7, 6, 5, 6, 7, 6, 7, 7, 6]
cplusplus_scores = [5, 6, 5, 6, 5, 4, 5, 6, 6, 5]
rust_scores = [9, 8, 9, 9, 9, 9, 8, 9, 8, 9]

# New data for line plot: average score over years
years = np.arange(2014, 2024)
avg_scores = {
    'Python': [7, 8, 8.5, 9, 8.7, 9, 9.2, 9.1, 9.3, 9.5],
    'JavaScript': [6, 7, 6.5, 7.5, 7, 7.2, 7.5, 7.4, 7.8, 7.9],
    'Java': [5.5, 6, 6.5, 6, 6.5, 6.8, 6.7, 6.9, 6.8, 6.7],
    'C++': [4.5, 5, 5.2, 5.5, 5.7, 5.5, 5.8, 5.9, 5.7, 6],
    'Rust': [8.5, 8.8, 9, 9.2, 9.1, 9.5, 9.3, 9.6, 9.7, 9.8]
}

# Combine scores into a list for the box plot
language_scores = [python_scores, javascript_scores, java_scores, cplusplus_scores, rust_scores]

# Create a figure with two subplots side by side
fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# Create the box plot
box = axes[0].boxplot(language_scores, vert=True, patch_artist=True, labels=languages, notch=False, showfliers=True, whis=1.5)
colors = ['#377eb8', '#ff7f00', '#4daf4a', '#f781bf', '#a65628']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.6)
for whisker, cap, median in zip(box['whiskers'], box['caps'], box['medians']):
    whisker.set(color='#555555', linewidth=1.5)
    cap.set(color='#555555', linewidth=1.5)
    median.set(color='#e41a1c', linewidth=2)

axes[0].set_title('Programming Language Popularity\nSurvey 2023', fontsize=14, fontweight='bold')
axes[0].set_ylabel('Popularity Score')
axes[0].grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Create the line plot
for lang, color in zip(languages, colors):
    axes[1].plot(years, avg_scores[lang], marker='o', label=lang, color=color, linewidth=2, alpha=0.7)

axes[1].set_title('Popularity Trends Over Years', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Year')
axes[1].set_ylabel('Average Popularity Score')
axes[1].grid(axis='both', linestyle='--', linewidth=0.5, alpha=0.7)
axes[1].legend(title='Languages', title_fontsize='10', fontsize='9', loc='upper left')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()