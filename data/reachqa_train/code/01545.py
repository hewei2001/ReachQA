import matplotlib.pyplot as plt
import squarify

# Extended Data: Estimated number of surviving manuscripts by civilization and genre
data = {
    'Ancient Egypt': {'Epic': 25, 'Lyric Poetry': 20, 'Philosophy': 10, 'Science': 15, 'Religious Texts': 50},
    'Ancient Greece': {'Epic': 50, 'Lyric Poetry': 25, 'Philosophy': 60, 'Science': 30, 'Religious Texts': 20},
    'Ancient China': {'Epic': 30, 'Narrative Poetry': 25, 'Philosophy': 40, 'Science': 35, 'Religious Texts': 45},
    'Ancient India': {'Epic': 45, 'Dramatic Poetry': 35, 'Philosophy': 20, 'Science': 25, 'Religious Texts': 50},
    'Mesoamerica': {'Epic': 20, 'Poetry': 15, 'Philosophy': 5, 'Science': 10, 'Religious Texts': 25},
    'Ancient Mesopotamia': {'Epic': 40, 'Lyric Poetry': 30, 'Philosophy': 15, 'Science': 20, 'Religious Texts': 35},
    'Roman Empire': {'Epic': 55, 'Narrative Poetry': 45, 'Philosophy': 55, 'Science': 40, 'Religious Texts': 50}
}

# Flatten data for squarify
labels = []
sizes = []
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700', '#C0C0C0', '#FFA07A']
color_mapping = {}

# Assign colors to each civilization
for i, (civilization, genres) in enumerate(data.items()):
    for genre, count in genres.items():
        label = f"{civilization}\n{genre}\n({count})"
        labels.append(label)
        sizes.append(count)
        color_mapping[label] = colors[i % len(colors)]

# Plotting the tree map
fig, ax = plt.subplots(figsize=(16, 9))
squarify.plot(sizes=sizes, label=labels,
              color=[color_mapping[label] for label in labels],
              alpha=0.75, edgecolor="white", linewidth=2, text_kwargs={'fontsize': 8})

# Enhance plot aesthetics
ax.set_title("Surviving Manuscripts of Ancient Civilizations\nCategorized by Genre and Sub-Genre",
             fontsize=18, fontweight='bold', pad=15)
ax.axis('off')

# Adjust layout to prevent overlapping text
plt.tight_layout()

# Add a secondary visualization: Pie chart to show overall genre distribution
genres_total = {}
for genres in data.values():
    for genre, count in genres.items():
        genres_total[genre] = genres_total.get(genre, 0) + count

# Create a pie chart
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(genres_total.values(), labels=genres_total.keys(), autopct='%1.1f%%',
       startangle=140, colors=colors[:len(genres_total)])
ax.set_title("Overall Genre Distribution Across Civilizations", fontsize=16, fontweight='bold')

# Display the plots
plt.show()