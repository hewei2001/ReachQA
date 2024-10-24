import matplotlib.pyplot as plt
import numpy as np

# Define the festivals and artistic mediums
festivals = ["Venice Biennale", "Edinburgh Festival", "Berlin Art Week", "Avignon Festival"]
mediums = ["Visual Arts", "Performing Arts", "Literature", "Digital Arts"]

# Number of participations in each medium at each festival
visual_arts = [45, 30, 35, 25]
performing_arts = [20, 50, 25, 40]
literature = [10, 15, 20, 35]
digital_arts = [25, 10, 20, 15]

# Combine the data into a list of lists for stacking
data = np.array([visual_arts, performing_arts, literature, digital_arts])

# Define colors for each medium
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']

# Create the figure and subplots
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(16, 7))

# Bottom positions for stacking in the first plot
bottom_positions = np.zeros(len(festivals))

# Plot the stacked bar chart
for i, (medium, color) in enumerate(zip(mediums, colors)):
    axs[0].bar(festivals, data[i], bottom=bottom_positions, color=color, label=medium, alpha=0.9, edgecolor='black')
    bottom_positions += data[i]

# Add title and labels for the stacked bar chart
axs[0].set_title("Distribution of Creative Mediums Across\nArt Festivals in Europe (2023)", fontsize=14, fontweight='bold', pad=20)
axs[0].set_xlabel("Art Festivals", fontsize=11, labelpad=10)
axs[0].set_ylabel("Number of Participations", fontsize=11, labelpad=10)
axs[0].set_xticks(range(len(festivals)))
axs[0].set_xticklabels(festivals, rotation=45, ha='right', fontsize=10)
axs[0].grid(axis='y', linestyle='--', alpha=0.7)
axs[0].legend(title="Artistic Mediums", fontsize=9, loc='upper left', bbox_to_anchor=(1, 1), title_fontsize='11')

# Data for line plot (Yearly trend hypothetical data)
years = ['2021', '2022', '2023']
trend_data = {
    "Visual Arts": [30, 40, 45],
    "Performing Arts": [35, 40, 50],
    "Literature": [18, 19, 20],
    "Digital Arts": [22, 28, 25]
}

# Plot the line chart for yearly trends
for medium, color in zip(mediums, colors):
    axs[1].plot(years, trend_data[medium], marker='o', color=color, label=medium, linewidth=2)

# Add title and labels for the line chart
axs[1].set_title("Participation Trends Over the Years", fontsize=14, fontweight='bold', pad=20)
axs[1].set_xlabel("Year", fontsize=11, labelpad=10)
axs[1].set_ylabel("Number of Participations", fontsize=11, labelpad=10)
axs[1].grid(linestyle='--', alpha=0.7)
axs[1].legend(title="Artistic Mediums", fontsize=9, loc='upper left', bbox_to_anchor=(1, 1), title_fontsize='11')

# Adjust layout to ensure nothing overlaps
plt.tight_layout()

# Display the plots
plt.show()