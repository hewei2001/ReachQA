import matplotlib.pyplot as plt

# Listening hours data for each composer across the century
beethoven_data = [55, 60, 58, 57, 61, 59, 65, 68, 60, 62, 65, 63, 70, 72, 66, 65, 68, 70, 75, 76]
mozart_data = [50, 52, 54, 55, 56, 58, 60, 65, 60, 63, 64, 68, 66, 70, 71, 69, 72, 74, 76, 78]
bach_data = [40, 43, 50, 45, 48, 46, 49, 55, 53, 56, 58, 62, 64, 67, 70, 72, 74, 73, 76, 78]
tchaikovsky_data = [45, 47, 46, 50, 54, 49, 53, 55, 58, 56, 60, 62, 65, 63, 67, 69, 70, 72, 71, 74]
brahms_data = [30, 35, 37, 38, 40, 45, 48, 50, 55, 60, 62, 65, 67, 70, 71, 73, 75, 77, 80, 82]

# Organizing data into a list of lists for boxplot
data = [beethoven_data, mozart_data, bach_data, tchaikovsky_data, brahms_data]

# Composer labels
composers = ["Beethoven", "Mozart", "Bach", "Tchaikovsky", "Brahms"]

# Colors for the boxes
colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightsalmon', 'lightpink']

# Create a horizontal box plot
plt.figure(figsize=(14, 8))
bplot = plt.boxplot(data, vert=False, patch_artist=True, notch=True, 
                    boxprops=dict(facecolor='w', color='black', linewidth=1.5),
                    whiskerprops=dict(color='black', linewidth=1.5),
                    capprops=dict(color='black', linewidth=1.5),
                    flierprops=dict(marker='o', color='red', alpha=0.5),
                    medianprops=dict(color='darkorange', linewidth=2))

# Set individual box colors
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

# Add chart title and labels
plt.title('Century of Classical Listening:\nVariability in Composer Popularity (1920-2020)', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Listening Hours per Year', fontsize=12)
plt.yticks(range(1, len(composers) + 1), composers, fontsize=12)

# Enhancing layout
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()

# Display the plot
plt.show()