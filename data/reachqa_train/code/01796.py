import matplotlib.pyplot as plt

# Define programming languages and their popularity percentages
languages = ['Python', 'JavaScript', 'Java', 'C#', 'C++', 'Ruby', 'Go', 'Swift']
popularity = [25, 22, 17, 12, 10, 6, 5, 3]  # Hypothetical usage percentages

# Define colors for each language
colors = ['#377eb8', '#ff7f00', '#4daf4a', '#f781bf', '#a65628', '#984ea3', '#999999', '#e41a1c']

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))

# Plot the pie chart
wedges, texts, autotexts = ax.pie(
    popularity,
    labels=languages,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    pctdistance=0.85,
    wedgeprops=dict(edgecolor='white', linewidth=1.5),
    explode=(0.1, 0, 0, 0, 0, 0, 0, 0),  # Slightly explode Python for emphasis
    shadow=True  # Add a shadow effect
)

# Customize the autotexts (percentages) on pie wedges
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

# Adjust labels to ensure they don't overlap
for text in texts:
    text.set_fontsize(10)
    text.set_fontweight('normal')

# Add a title
ax.set_title(
    "Programming Languages Popularity in 2023:\nA Global Developer Survey",
    fontsize=14, fontweight='bold', pad=20
)

# Add a legend
ax.legend(
    wedges, languages,
    title="Languages", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1),
    fontsize=10, title_fontsize='11'
)

# Enhance the plot with a small circle in the middle for a donut effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()