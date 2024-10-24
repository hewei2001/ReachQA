import matplotlib.pyplot as plt
import numpy as np

# Define the decades and the corresponding data for art movements
decades = ['1980s', '1990s', '2000s', '2010s', '2020s']
impressionism = [120, 150, 180, 200, 220]
abstract_art = [60, 90, 110, 140, 160]
modernism = [100, 130, 140, 160, 170]
surrealism = [70, 85, 90, 120, 130]

# Create a bar chart
fig, ax = plt.subplots(figsize=(10, 7))

# Define width of the bars
width = 0.35  # the width of the bars
ind = np.arange(len(decades))  # the x locations for the groups

# Plotting each art movement with bars
p1 = ax.bar(ind, impressionism, width, label='Impressionism', color='#FF6347')
p2 = ax.bar(ind, abstract_art, width, bottom=impressionism, label='Abstract Art', color='#FFD700')
p3 = ax.bar(ind, modernism, width, bottom=np.array(impressionism) + np.array(abstract_art), 
            label='Modernism', color='#4B0082')
p4 = ax.bar(ind, surrealism, width, bottom=np.array(impressionism) + np.array(abstract_art) + np.array(modernism), 
            label='Surrealism', color='#98FB98')

# Adding labels and title
ax.set_ylabel('Number of Exhibitions')
ax.set_title('Popularity of Art Movements (1980-2020)\nby Number of Global Exhibitions', fontsize=14)
ax.set_xticks(ind)
ax.set_xticklabels(decades, rotation=45)
ax.legend(loc='upper left', fontsize=10)

# Adding data annotations for each bar
for bars in [p1, p2, p3, p4]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{int(height)}',  # Ensure integer display
                    xy=(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2),
                    xytext=(0, 0),  # Offset for text
                    textcoords="offset points",
                    ha='center', va='center',
                    fontsize=9, color='black', fontweight='bold')

# Gridlines for y-axis
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to prevent text clipping and overlapping
plt.tight_layout()

# Show the plot
plt.show()