import matplotlib.pyplot as plt

# Data representing the number of books read annually by age groups
data = {
    "Teens": [0, 1, 2, 3, 4, 5, 6, 1, 2, 3, 7, 8],
    "Young Adults": [3, 4, 5, 10, 12, 8, 15, 7, 6, 10, 9, 8, 6],
    "Adults": [5, 10, 12, 15, 10, 8, 20, 18, 12, 14, 9, 13, 15],
    "Seniors": [8, 10, 12, 25, 20, 15, 10, 14, 12, 17, 16, 18],
}

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plotting the box plot
box = ax.boxplot(data.values(), 
                 patch_artist=True, 
                 notch=True, 
                 boxprops=dict(facecolor='#AED6F1', color='navy', linewidth=1.5),
                 medianprops=dict(color='red', linewidth=1.5),
                 whiskerprops=dict(color='gray', linewidth=1.2),
                 capprops=dict(color='gray', linewidth=1.2),
                 flierprops=dict(marker='o', color='orange', alpha=0.5))

# Customizing the plot
ax.set_title('Annual Book Reading Habits Across Age Groups', fontsize=14, color='darkblue', loc='center', pad=20)
ax.set_xlabel('Age Groups', fontsize=12)
ax.set_ylabel('Number of Books Read', fontsize=12)
ax.set_xticklabels(data.keys(), fontsize=11)
ax.grid(True, linestyle='--', alpha=0.5, axis='y')

# Highlighting each box
for patch, color in zip(box['boxes'], ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()