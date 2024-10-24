import matplotlib.pyplot as plt
import numpy as np

# Original data
data = {
    "Teens": [0, 1, 2, 3, 4, 5, 6, 1, 2, 3, 7, 8],
    "Young Adults": [3, 4, 5, 10, 12, 8, 15, 7, 6, 10, 9, 8, 6],
    "Adults": [5, 10, 12, 15, 10, 8, 20, 18, 12, 14, 9, 13, 15],
    "Seniors": [8, 10, 12, 25, 20, 15, 10, 14, 12, 17, 16, 18],
}

# Compute additional data for the subplot
average_books = {age_group: np.mean(books) for age_group, books in data.items()}
age_groups = list(average_books.keys())
averages = list(average_books.values())

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Plotting the box plot on the first subplot
box = ax1.boxplot(data.values(),
                  patch_artist=True,
                  notch=True,
                  boxprops=dict(facecolor='#AED6F1', color='navy', linewidth=1.5),
                  medianprops=dict(color='red', linewidth=1.5),
                  whiskerprops=dict(color='gray', linewidth=1.2),
                  capprops=dict(color='gray', linewidth=1.2),
                  flierprops=dict(marker='o', color='orange', alpha=0.5))

ax1.set_title('Annual Book Reading Habits\nAcross Age Groups', fontsize=14, color='darkblue', loc='center', pad=20)
ax1.set_xlabel('Age Groups', fontsize=12)
ax1.set_ylabel('Number of Books Read', fontsize=12)
ax1.set_xticklabels(data.keys(), fontsize=11)
ax1.grid(True, linestyle='--', alpha=0.5, axis='y')

# Highlighting each box
for patch, color in zip(box['boxes'], ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

# Plotting the bar chart on the second subplot
ax2.bar(age_groups, averages, color=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99'], alpha=0.7)
ax2.set_title('Average Books Read Per Year\nby Age Group', fontsize=14, color='darkgreen', loc='center', pad=20)
ax2.set_xlabel('Age Groups', fontsize=12)
ax2.set_ylabel('Average Number of Books', fontsize=12)
ax2.set_ylim(0, max(averages) + 5)
ax2.grid(True, linestyle='--', alpha=0.5, axis='y')

# Annotating the bar chart with values
for i, avg in enumerate(averages):
    ax2.text(i, avg + 0.5, f'{avg:.1f}', ha='center', va='bottom', fontsize=10, color='black')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()