import matplotlib.pyplot as plt

# Fictional data: Plant heights (in centimeters) in different environments
open_field = [45, 50, 47, 52, 48, 53, 46, 49, 54, 47]
greenhouse = [60, 63, 58, 65, 62, 67, 66, 64, 61, 59]
urban_roof = [30, 35, 33, 28, 32, 34, 31, 36, 29, 37]
dense_forest = [55, 50, 52, 57, 53, 54, 56, 51, 58, 55]
indoor_garden = [25, 27, 23, 26, 24, 22, 28, 29, 21, 30]

# Environments
environments = ['Open Field', 'Greenhouse', 'Urban Roof', 'Dense Forest', 'Indoor Garden']

# Data collection
data = [open_field, greenhouse, urban_roof, dense_forest, indoor_garden]

# Create a horizontal box chart
fig, ax = plt.subplots(figsize=(12, 7))
boxplots = ax.boxplot(data, vert=False, patch_artist=True, notch=True, whis=1.5)

# Customize box plots with colors and styles
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']
for patch, color in zip(boxplots['boxes'], colors):
    patch.set_facecolor(color)

# Axis labels and title
ax.set_yticklabels(environments, fontsize=11)
ax.set_title('Plant Growth Analysis: Distribution of Heights\nAcross Various Environments', fontsize=15, fontweight='bold', pad=20)
ax.set_xlabel('Height (cm)', fontsize=12)

# Grid and layout settings
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
plt.tight_layout()

# Display the plot
plt.show()