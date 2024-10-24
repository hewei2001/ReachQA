import matplotlib.pyplot as plt

# Daily coffee consumption data (cups per day) for each age group
teens_coffee = [0, 1, 0, 2, 1, 0, 0, 1, 1, 2]
young_adults_coffee = [2, 3, 2, 1, 4, 2, 3, 2, 3, 3]
adults_coffee = [3, 4, 3, 5, 4, 3, 4, 3, 5, 4]
middle_aged_coffee = [2, 3, 3, 2, 4, 3, 2, 4, 3, 3]
seniors_coffee = [1, 1, 2, 1, 2, 1, 1, 0, 2, 1]

# Organize the data for the horizontal box plot
coffee_data = [teens_coffee, young_adults_coffee, adults_coffee, middle_aged_coffee, seniors_coffee]

# Age group labels
age_groups = ['Teens (13-19)', 'Young Adults (20-29)', 'Adults (30-49)', 'Middle-Aged (50-64)', 'Seniors (65+)']

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Create the horizontal box plot
boxes = ax.boxplot(coffee_data, vert=False, patch_artist=True, notch=True,
                   boxprops=dict(facecolor='#DAA520', color='black'),
                   whiskerprops=dict(color='black'),
                   capprops=dict(color='black'),
                   medianprops=dict(color='darkred'))

# Customize the box colors for differentiation
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFD700', '#FF66B2']
for patch, color in zip(boxes['boxes'], colors):
    patch.set_facecolor(color)

# Set titles and labels
ax.set_title("Caffeine Trends:\nDaily Coffee Consumption Across Age Groups", fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Daily Coffee Consumption (cups)', fontsize=12)
ax.set_yticklabels(age_groups, fontsize=12)

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()