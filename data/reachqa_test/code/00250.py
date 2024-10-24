import matplotlib.pyplot as plt
import numpy as np

# Enhanced Dataset: Programming languages
languages = ['Python', 'JavaScript', 'Java', 'C#', 'C++', 'Ruby', 'Swift', 'Go', 'Rust', 'PHP', 
             'Kotlin', 'TypeScript', 'Scala', 'Perl', 'Objective-C', 'Dart', 'Elixir', 'Haskell', 'Lua', 'MATLAB']

# Popularity (%) - estimated fictitious values
popularity = np.array([40, 30, 20, 15, 10, 5, 7, 6, 4, 8, 
                       11, 25, 9, 3, 2, 4, 1, 1.5, 2.5, 1])

# Average Salaries (in thousands USD) - estimated fictitious values
salaries = np.array([115, 110, 105, 100, 95, 90, 98, 105, 110, 85, 
                     100, 108, 103, 89, 92, 88, 80, 97, 94, 83])

# Community Engagement Score (0-10 scale) - fictional values
engagement = np.array([9, 8.5, 8, 7.5, 6.5, 4, 6, 7, 7.5, 5, 
                       6.5, 8, 7, 4.5, 5, 5.5, 3.5, 4, 6, 3])

# Define the size of each point based on the popularity
sizes = popularity * 10

# Create figure and axes for 2D plot
fig, ax = plt.subplots(figsize=(14, 10))

# Scatter plot with color based on salary and size based on popularity
scatter = ax.scatter(popularity, salaries, s=sizes, c=engagement, cmap='viridis', alpha=0.7, edgecolor='w', linewidth=0.5)

# Title and labels with line breaks
ax.set_title('Programming Language Popularity vs.\nDeveloper Salaries and Community Engagement', fontsize=18, fontweight='bold', loc='left', ha='left')
ax.set_xlabel('Popularity (%)', fontsize=14)
ax.set_ylabel('Average Salary (USD thousands)', fontsize=14)

# Custom ticks for clarity with logarithmic scale
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xticks([1, 5, 10, 20, 40])
ax.set_xticklabels(['1', '5', '10', '20', '40'])
ax.set_yticks([80, 90, 100, 110, 120])
ax.set_yticklabels(['80', '90', '100', '110', '120'])

# Gridlines
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Labels for each language, adjusted for clarity
for i, language in enumerate(languages):
    ax.text(popularity[i], salaries[i], language, fontsize=8, ha='right', va='bottom', 
            bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))

# Color bar for community engagement
colorbar = fig.colorbar(scatter, ax=ax)
colorbar.set_label('Community Engagement Score', fontsize=12)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()