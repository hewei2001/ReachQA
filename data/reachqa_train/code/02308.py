import matplotlib.pyplot as plt
import numpy as np

# Data preparation for the first subplot
decades = np.array([1960, 1970, 1980, 1990, 2000, 2010, 2020])
awards = np.array([3, 7, 12, 15, 20, 25, 30])

# Related but distinct data for the second subplot
# Hypothetical data representing the number of award events per decade
events_per_decade = np.array([1, 1, 2, 3, 4, 5, 6])
average_awards_per_event = awards / events_per_decade

# Annotations for key milestones in genre recognition
annotations = [
    "1965: Hugo Award established",
    "1970: Nebula Awards gain popularity",
    "1985: World Fantasy Award launched",
    "1995: SFWA Grand Master Award created",
    "2005: Increased award diversity",
    "2015: More genre-specific awards",
    "2025: Major international acceptance"
]

# Create the figure and subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 6), constrained_layout=True)

# First subplot: Line chart of number of awards
axs[0].plot(decades, awards, marker='o', color='teal', linestyle='-', linewidth=2, markersize=8, label='Number of Awards')
for i, txt in enumerate(annotations):
    axs[0].annotate(txt, (decades[i], awards[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8, color='darkgreen', 
                    bbox=dict(facecolor='lightyellow', edgecolor='gray', boxstyle='round,pad=0.3'))

axs[0].set_title('Evolution of Literary Awards for Sci-Fi & Fantasy\n(1960s to 2020s)', fontsize=12, fontweight='bold', ha='center')
axs[0].set_xlabel('Decade', fontsize=11)
axs[0].set_ylabel('Number of Awards', fontsize=11)
axs[0].grid(True, linestyle='--', alpha=0.6)
axs[0].legend(loc='upper left', frameon=False)

# Second subplot: Bar chart of average number of awards per event
axs[1].bar(decades, average_awards_per_event, color='orange', alpha=0.7)
axs[1].set_title('Average Awards per Event (1960s to 2020s)', fontsize=12, fontweight='bold')
axs[1].set_xlabel('Decade', fontsize=11)
axs[1].set_ylabel('Average Awards per Event', fontsize=11)
axs[1].set_xticks(decades)
axs[1].grid(True, linestyle='--', alpha=0.6)

# Show the plot
plt.show()