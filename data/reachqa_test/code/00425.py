import matplotlib.pyplot as plt
import numpy as np

# Original data construction: Sales figures (in thousands) for 50 records in each genre
genres = ['Pop', 'Rock', 'Jazz', 'Country', 'Hip-Hop']
pop_sales = [300 + np.random.randint(100, 300) for _ in range(50)]
rock_sales = [200 + np.random.randint(100, 400) for _ in range(50)]
jazz_sales = [50 + np.random.randint(0, 250) for _ in range(50)]
country_sales = [100 + np.random.randint(0, 300) for _ in range(50)]
hiphop_sales = [250 + np.random.randint(100, 400) for _ in range(50)]
sales_data = [pop_sales, rock_sales, jazz_sales, country_sales, hiphop_sales]

# New data: Percentage increase in sales over the last year
pop_increase = [10 + 5 * np.random.randn() for _ in range(50)]
rock_increase = [5 + 10 * np.random.randn() for _ in range(50)]
jazz_increase = [3 + 8 * np.random.randn() for _ in range(50)]
country_increase = [8 + 6 * np.random.randn() for _ in range(50)]
hiphop_increase = [15 + 10 * np.random.randn() for _ in range(50)]
increase_data = [pop_increase, rock_increase, jazz_increase, country_increase, hiphop_increase]

# Define the positions of the boxes
positions = [1, 2, 3, 4, 5]

# Create a figure and two axes for plotting with optimized size
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Custom parameters for the box plot
box1 = ax1.boxplot(
    sales_data,
    positions=positions,
    vert=True,
    patch_artist=True,
    notch=True,
    showmeans=True,
    meanprops={"marker":"s", "markerfacecolor":"white", "markeredgecolor":"black", "markersize":"10"},
    medianprops=dict(color='black', linewidth=2),
    boxprops=dict(linewidth=2),
    capprops=dict(linewidth=2),
    whiskerprops=dict(linewidth=2),
    flierprops=dict(marker='o', markerfacecolor='red', markersize=6, markeredgecolor='red', linestyle='none'),
)

# Set the face color of boxes
colors = ['skyblue', 'salmon', 'palegreen', 'lightcoral', 'lightslategrey']
for patch, color in zip(box1['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_edgecolor('black')

# Set axes labels for box plot
ax1.set_xticks(positions)
ax1.set_xticklabels(genres, fontsize=14)
ax1.set_xlabel('Music Genre', fontsize=18)
ax1.set_ylabel('Album Sales (in thousands)', fontsize=18)
ax1.set_title('Melodies and Numbers:\nA Deep Dive into\nMusic Genre Sales', fontsize=20)

# Add grid to box plot
ax1.yaxis.grid(True, linestyle='--', which='major', color='lightgrey', alpha=0.5)

# Create the violin plot
vp = ax2.violinplot(increase_data, showmeans=True, showmedians=True, showextrema=True)

# Customize the violin plot
for body in vp['bodies']:
    body.set_alpha(0.7)
    body.set_color('skyblue')
vp['cmeans'].set_color('black')
vp['cmedians'].set_color('red')
vp['cbars'].set_color('black')
vp['cmins'].set_color('black')
vp['cmaxes'].set_color('black')

# Set axes labels for violin plot
ax2.set_xticks(positions)
ax2.set_xticklabels(genres, fontsize=14)
ax2.set_xlabel('Music Genre', fontsize=18)
ax2.set_ylabel('Percentage Increase in Sales', fontsize=18)
ax2.set_title('Harmonious Growth:\nYearly Sales Increase by Genre', fontsize=20)

# Add grid to violin plot
ax2.yaxis.grid(True, linestyle='--', which='major', color='lightgrey', alpha=0.5)

# Improve readability by automatically adjusting image layout
plt.tight_layout()

# Display the plot
plt.show()