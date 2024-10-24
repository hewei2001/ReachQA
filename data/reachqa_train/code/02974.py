import matplotlib.pyplot as plt

# Define coffee consumption data (in cups per month) for each age group
teens = [15, 20, 14, 18, 19, 13, 22, 21, 17, 16, 18, 20]
young_adults = [25, 30, 32, 29, 28, 27, 35, 33, 31, 30, 26, 29]
adults = [40, 42, 44, 38, 39, 41, 43, 45, 46, 37, 40, 39]
middle_aged = [35, 38, 36, 34, 33, 32, 39, 37, 40, 31, 35, 34]
seniors = [25, 23, 22, 28, 27, 29, 30, 24, 26, 21, 25, 23]

# Create the box plot
plt.figure(figsize=(12, 7))

# Box plot for the data
plt.boxplot(
    [teens, young_adults, adults, middle_aged, seniors],
    labels=['Teens\n(13-19)', 'Young Adults\n(20-29)', 'Adults\n(30-49)', 'Middle-Aged\n(50-64)', 'Seniors\n(65+)'],
    patch_artist=True,
    notch=True,
    boxprops=dict(facecolor='#FFDDC1', color='navy'),
    whiskerprops=dict(color='darkorange', linewidth=1.5),
    capprops=dict(color='darkorange', linewidth=1.5),
    medianprops=dict(color='red', linewidth=2),
    flierprops=dict(marker='o', color='darkorange', markersize=6, alpha=0.5)
)

# Add title and labels
plt.title("Global Coffee Consumption Survey 2023\nMonthly Coffee Consumption by Age Group", fontsize=14, fontweight='bold')
plt.xlabel('Age Groups', fontsize=12)
plt.ylabel('Cups of Coffee per Month', fontsize=12)

# Add grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()