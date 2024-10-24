import matplotlib.pyplot as plt

# Data: Annual budget allocations for space missions by country (in million USD)
countries = ['USA', 'China', 'India', 'Russia', 'Japan']
budgets = [
    [1200, 1300, 1250, 1320, 1340, 1280, 1350, 1400, 1290, 1310],  # USA
    [980, 1020, 990, 1000, 1050, 1030, 1060, 1100, 1070, 1090],    # China
    [450, 470, 460, 480, 490, 500, 510, 495, 505, 485],            # India
    [820, 830, 845, 860, 855, 870, 890, 900, 895, 880],            # Russia
    [500, 520, 540, 530, 560, 550, 570, 580, 590, 575]             # Japan
]

# Plot configuration
fig, ax = plt.subplots(figsize=(12, 8))

# Create the horizontal box plot
boxplot = ax.boxplot(budgets, vert=False, patch_artist=True, notch=True, labels=countries)

# Customize colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)

# Customize whiskers, caps, medians
for whisker, cap in zip(boxplot['whiskers'], boxplot['caps']):
    whisker.set(color='#2C3E50', linewidth=1.5)
    cap.set(color='#2C3E50', linewidth=1.5)

for median in boxplot['medians']:
    median.set(color='#E74C3C', linewidth=2)

# Chart details
ax.set_title('Annual Budget Allocation in Space Programs\nby Country (2023)', fontsize=14, pad=20)
ax.set_xlabel('Budget (Million USD)', fontsize=12)
ax.set_ylabel('Country', fontsize=12)
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Legend for colors
legend_elements = [plt.Line2D([0], [0], color=color, lw=4, label=country) for color, country in zip(colors, countries)]
ax.legend(handles=legend_elements, title='Countries', loc='upper right', fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()