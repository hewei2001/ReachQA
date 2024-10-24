import matplotlib.pyplot as plt

# Data for tiger populations in each national park over ten years
populations_yellowstone = [35, 40, 45, 42, 38, 44, 47, 48, 43, 45]
populations_sundarban = [23, 25, 26, 24, 22, 23, 27, 29, 28, 30]
populations_kanha = [51, 49, 52, 54, 53, 55, 57, 56, 59, 60]
populations_bandipur = [12, 14, 15, 16, 18, 17, 19, 21, 20, 22]

# National Parks labels
parks = ['Yellowstone', 'Sundarban', 'Kanha', 'Bandipur']
populations_data = [populations_yellowstone, populations_sundarban, populations_kanha, populations_bandipur]

# Create a horizontal box plot
plt.figure(figsize=(14, 8))
boxplot = plt.boxplot(populations_data, vert=False, patch_artist=True, notch=True,
            boxprops=dict(facecolor='lightgreen', color='darkgreen', alpha=0.6),
            capprops=dict(color='darkgreen'),
            whiskerprops=dict(color='darkgreen'),
            flierprops=dict(marker='o', color='red', alpha=0.5),
            medianprops=dict(color='gold', linewidth=2))

# Custom colors for each box
colors = ['#a7c957', '#6a994e', '#388659', '#10451d']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)

# Set labels and title
plt.yticks([1, 2, 3, 4], parks, fontsize=12)
plt.xlabel('Tiger Population Size', fontsize=14)
plt.title('Tiger Population Dynamics Across National Parks:\nA Decade of Conservation',
          fontsize=16, weight='bold', pad=20)

# Annotate insights
plt.annotate('Stable Growth in Kanha', xy=(60, 2.85), xytext=(62, 3),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, color='black')

plt.annotate('Challenges in Bandipur', xy=(12, 4.1), xytext=(15, 4.2),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, color='black')

# Customize grid and layout
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# Show the plot
plt.show()