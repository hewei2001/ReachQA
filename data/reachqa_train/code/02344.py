import matplotlib.pyplot as plt

# Define the e-book consumption data for each generation
baby_boomers = [3, 5, 4, 4, 6, 5, 3, 7, 4, 5]
generation_x = [8, 10, 9, 8, 11, 7, 10, 9, 8, 12]
millennials = [15, 17, 16, 19, 14, 18, 20, 19, 16, 17]
generation_z = [22, 25, 24, 21, 23, 22, 24, 26, 25, 23]

# Combine all generation data into a list for the box plot
ebook_data = [
    baby_boomers,
    generation_x,
    millennials,
    generation_z
]

# Generation labels for the box plot
generation_labels = ["Baby Boomers", "Generation X", "Millennials", "Generation Z"]

# Create the figure and axis for the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the box plots horizontally
box = ax.boxplot(ebook_data, labels=generation_labels, patch_artist=True, vert=False, notch=True)

# Customize the box plots with different colors for differentiation
colors = ['#8DD3C7', '#FFFFB3', '#BEBADA', '#FB8072']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Customize other plot elements
ax.set_title("E-Book Consumption Patterns Across Generations:\nA Box Plot Analysis", fontsize=16, fontweight='bold')
ax.set_xlabel("Number of E-Books Read Per Month", fontsize=13)
ax.set_ylabel("Generation", fontsize=13)
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Further customize the box plot components
plt.setp(box['whiskers'], color='grey', linewidth=1.5)
plt.setp(box['caps'], color='grey', linewidth=1.5)
plt.setp(box['medians'], color='black', linewidth=2)
plt.setp(box['fliers'], marker='o', color='red', markersize=5, alpha=0.6)

# Automatically adjust layout to prevent text overlap and enhance clarity
plt.tight_layout()

# Display the plot
plt.show()