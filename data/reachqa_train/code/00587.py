import matplotlib.pyplot as plt
import numpy as np

# Define categories and regions
categories = ['Meditation', 'Prayer', 'Rituals', 'Festivals', 'Pilgrimages']
regions = ['North America', 'South America', 'Europe', 'Asia', 'Africa']

# Affinity scores for each region
affinity_scores = {
    'North America': [60, 70, 40, 50, 30],
    'South America': [50, 80, 70, 60, 40],
    'Europe': [70, 60, 50, 70, 45],
    'Asia': [80, 75, 90, 85, 95],
    'Africa': [65, 85, 75, 80, 55],
}

# Number of variables we're plotting
num_vars = len(categories)

# Create a list of angles for the radar chart
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Initialize figure and subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14, 7), subplot_kw=dict(polar=True))

# Radar Chart (ax1)
def plot_radar(region, data, color, ax):
    ax.plot(angles, data, label=region, color=color, linewidth=2, linestyle='solid')
    ax.fill(angles, data, color=color, alpha=0.25)

colors = ['#FF6347', '#FF69B4', '#8A2BE2', '#00CED1', '#ADFF2F']
for region, data in affinity_scores.items():
    data = data + data[:1]  # Close the loop
    color = colors.pop(0)
    plot_radar(region, data, color, ax1)

ax1.set_xticks(angles[:-1])
ax1.set_xticklabels(categories, color='grey', size=10)
ax1.set_yticks([20, 40, 60, 80, 100])
ax1.set_yticklabels(["20", "40", "60", "80", "100"], color="grey", size=7)
ax1.set_ylim(0, 100)
ax1.set_title("Cultural Affinity Radar:\nUnderstanding Global Spiritual Practices", size=14, color='navy')
ax1.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

# Calculate average affinity scores for each category
average_affinity = np.mean(np.array(list(affinity_scores.values())), axis=0)

# Bar Chart (ax2)
ax2 = fig.add_subplot(122)  # Ensuring this is a normal subplot
ax2.barh(categories, average_affinity, color='#4682B4', edgecolor='black')
ax2.set_xlim(0, 100)
ax2.set_title("Average Affinity Score per Category", size=14, color='navy')
ax2.set_xlabel('Average Score', size=10)
ax2.set_ylabel('Category', size=10)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()