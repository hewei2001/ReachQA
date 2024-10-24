import matplotlib.pyplot as plt
import numpy as np

# Original art style preferences data
art_styles = ['Contemporary', 'Abstract', 'Surrealism', 'Impressionism', 'Minimalism', 'Traditional']
preferences = [28, 20, 18, 15, 12, 7]

# New hypothetical data for bar chart: percentage of preferences across different age groups
age_groups = ['18-24', '25-34', '35-44', '45-54', '55+']
preferences_by_age = {
    'Contemporary': [30, 35, 25, 20, 15],
    'Abstract': [25, 20, 22, 18, 15],
    'Surrealism': [20, 15, 18, 20, 12],
    'Impressionism': [15, 10, 15, 22, 18],
    'Minimalism': [5, 8, 10, 15, 20],
    'Traditional': [5, 12, 10, 5, 20]
}

# Define colors for the charts
colors = ['#6A5ACD', '#FF6347', '#FFD700', '#32CD32', '#FF69B4', '#8A2BE2']

# Create a 1x2 grid of subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Pie chart for art style preferences
explode = (0.1, 0, 0, 0, 0, 0)  # Emphasize the Contemporary slice
ax1.pie(preferences, labels=art_styles, autopct='%1.1f%%', startangle=90, colors=colors,
        explode=explode, shadow=True, wedgeprops=dict(edgecolor='w', linewidth=1.5))
ax1.set_title("Art Enthusiasts' Favorite Styles in 2023:\nA Snapshot of Global Artistic Preferences",
              fontsize=14, weight='bold')

# Bar chart for preferences by age group
bar_width = 0.15
x = np.arange(len(age_groups))

# Plot each style as a separate bar, offset by bar_width
for idx, style in enumerate(art_styles):
    ax2.bar(x + idx * bar_width, preferences_by_age[style], bar_width, label=style, color=colors[idx])

ax2.set_xlabel('Age Groups', fontsize=12, weight='bold')
ax2.set_ylabel('Preference (%)', fontsize=12, weight='bold')
ax2.set_title('Preferences by Age Group', fontsize=14, weight='bold')
ax2.set_xticks(x + bar_width * 2.5)  # Center tick labels with an offset
ax2.set_xticklabels(age_groups)
ax2.legend(title='Art Styles', bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the figure
plt.show()