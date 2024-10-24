import matplotlib.pyplot as plt

# Data: Number of unique spices and ingredients for 10 dishes in each cuisine
italian = [12, 14, 15, 11, 13, 16, 14, 15, 13, 12]
indian = [18, 20, 19, 17, 21, 22, 23, 19, 20, 21]
chinese = [10, 12, 13, 11, 10, 9, 12, 11, 10, 13]
mexican = [15, 14, 16, 17, 15, 13, 12, 14, 16, 17]
french = [11, 10, 12, 14, 13, 12, 11, 15, 14, 12]

# Combine the data into a list
data = [italian, indian, chinese, mexican, french]

# Labels for the cuisines
cuisines = ['Italian', 'Indian', 'Chinese', 'Mexican', 'French']

# Create a figure and an axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create the boxplot
bp = ax.boxplot(data, patch_artist=True, notch=True, vert=True, labels=cuisines)

# Customizing boxplot appearance
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Styling whiskers, caps, and medians
for whisker in bp['whiskers']:
    whisker.set(color='black', linewidth=1.5, linestyle="--")
for cap in bp['caps']:
    cap.set(color='black', linewidth=1.5)
for median in bp['medians']:
    median.set(color='orange', linewidth=2)

# Adding grid, title, and labels
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_title('Flavors of the World:\nA Culinary Journey Through International Cuisine', fontsize=14)
ax.set_xlabel('Cuisine Type', fontsize=12)
ax.set_ylabel('Number of Unique Spices & Ingredients', fontsize=12)

# Add a legend
plt.legend([bp["boxes"][i] for i in range(len(cuisines))], cuisines, loc='upper right', title='Cuisines', frameon=False)

# Adjust layout for readability
plt.tight_layout()

# Display the plot
plt.show()