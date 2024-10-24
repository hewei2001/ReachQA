import matplotlib.pyplot as plt
import squarify

# Data: Estimated number of surviving manuscripts by civilization and genre
data = {
    'Ancient Egypt': {'Epic': 25, 'Poetry': 35, 'Philosophy': 10, 'Science': 15, 'Religious Texts': 50},
    'Ancient Greece': {'Epic': 50, 'Poetry': 40, 'Philosophy': 60, 'Science': 30, 'Religious Texts': 20},
    'Ancient China': {'Epic': 30, 'Poetry': 50, 'Philosophy': 40, 'Science': 35, 'Religious Texts': 45},
    'Ancient India': {'Epic': 45, 'Poetry': 55, 'Philosophy': 20, 'Science': 25, 'Religious Texts': 50},
    'Mesoamerica': {'Epic': 20, 'Poetry': 15, 'Philosophy': 5, 'Science': 10, 'Religious Texts': 25},
}

# Flatten data for squarify
labels = []
sizes = []
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']
color_mapping = {}

# Assign colors to each civilization
for i, civilization in enumerate(data.keys()):
    for genre, count in data[civilization].items():
        labels.append(f"{civilization}\n{genre}\n({count})")
        sizes.append(count)
        color_mapping[f"{civilization} {genre}"] = colors[i % len(colors)]

# Plotting the tree map
plt.figure(figsize=(14, 8))
squarify.plot(sizes=sizes, label=labels,
              color=[color_mapping["{} {}".format(l.split('\n')[0], l.split('\n')[1])] for l in labels],
              alpha=0.75, edgecolor="white", linewidth=2, text_kwargs={'fontsize': 10})

# Enhance plot aesthetics
plt.title("Surviving Manuscripts of Ancient Civilizations\nCategorized by Genre",
          fontsize=18, fontweight='bold', pad=15)
plt.axis('off')
plt.tight_layout()

# Display the plot
plt.show()