import matplotlib.pyplot as plt

# Paint color preferences by continent (in percentages)
labels = ['Blue', 'Green', 'Red', 'Yellow', 'Purple', 'Orange']
north_america = [25, 15, 20, 10, 20, 10]
south_america = [20, 25, 15, 15, 10, 15]
europe = [30, 10, 25, 10, 15, 10]
africa = [10, 30, 10, 25, 15, 10]
asia = [20, 10, 15, 20, 25, 10]

data = [north_america, south_america, europe, africa, asia]
continent_labels = ['North America', 'South America', 'Europe', 'Africa', 'Asia']

# Colors for the donut segments
colors = ['deepskyblue', 'mediumseagreen', 'crimson', 'gold', 'mediumpurple', 'darkorange']

# Function to plot donut charts
def plot_donut(ax, data, title):
    wedges, texts, autotexts = ax.pie(data, labels=labels, autopct='%1.1f%%', startangle=90,
                                      colors=colors, pctdistance=0.85, wedgeprops=dict(width=0.3), shadow=True)
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    ax.add_artist(centre_circle)
    ax.axis('equal')
    ax.set_title(title, fontsize=12, fontweight='bold')

# Create the subplot grid
fig, axs = plt.subplots(2, 3, figsize=(14, 8))
axs = axs.flatten()

# Plot each continent's data
for i, ax in enumerate(axs[:5]):
    plot_donut(ax, data[i], continent_labels[i])

# Add a central title
plt.suptitle("The Global Palette:\nWorld Paint Color Preferences by Continent", fontsize=16, fontweight='bold')

# Remove the last subplot which is unused
fig.delaxes(axs[5])

# Add a shared legend outside the plot area
fig.legend(labels, loc='center right', fontsize=10, title="Colors", title_fontsize='13', bbox_to_anchor=(1.15, 0.5))

# Adjust layout to ensure everything fits well
plt.tight_layout(rect=[0, 0, 0.9, 1])

# Display the plot
plt.show()