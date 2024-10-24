import matplotlib.pyplot as plt
import numpy as np

# Decade labels and genre data (in thousands of albums)
decades = ['1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s']
rock = np.array([5, 15, 25, 35, 30, 28, 25, 18])
pop = np.array([3, 10, 20, 30, 40, 45, 40, 35])
jazz = np.array([20, 18, 15, 10, 8, 6, 5, 4])
classical = np.array([10, 8, 6, 5, 4, 3, 2, 2])
hiphop = np.array([0, 0, 0, 5, 10, 20, 25, 30])

# Total album releases data for line plot overlay
total_albums = rock + pop + jazz + classical + hiphop + np.array([5, 7, 10, 15, 18, 20, 19, 17])

# Stack the data to find cumulative positions for each genre
album_data = np.vstack([rock, pop, jazz, classical, hiphop])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Define colors for genres
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Plot each genre as a stacked bar
ax.bar(decades, rock, color=colors[0], label='Rock', edgecolor='grey')
ax.bar(decades, pop, bottom=rock, color=colors[1], label='Pop', edgecolor='grey')
ax.bar(decades, jazz, bottom=rock+pop, color=colors[2], label='Jazz', edgecolor='grey')
ax.bar(decades, classical, bottom=rock+pop+jazz, color=colors[3], label='Classical', edgecolor='grey')
ax.bar(decades, hiphop, bottom=rock+pop+jazz+classical, color=colors[4], label='Hip-hop', edgecolor='grey')

# Overlay line plot for total albums
ax.plot(decades, total_albums, marker='o', color='black', linewidth=2.5, linestyle='-', label='Total Albums')

# Title and labels with adjustments
ax.set_title("Decades of Harmony:\nThe Evolution of Music Genres & Total Albums (1950s to 2020s)", fontsize=14, weight='bold', pad=20)
ax.set_xlabel("Decade", fontsize=12)
ax.set_ylabel("Albums Released (thousands)", fontsize=12)

# Rotate x-axis labels to avoid overlap
plt.xticks(rotation=45)

# Add a legend
ax.legend(title="Genres", loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10)

# Annotate key points in the line plot
for i, txt in enumerate(total_albums):
    ax.annotate(txt, (decades[i], total_albums[i]), textcoords="offset points", xytext=(-10,5), ha='center', fontsize=9, color='black')

# Add grid lines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Ensure the layout is tight and clear
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Display the plot
plt.show()