import matplotlib.pyplot as plt
import numpy as np

# Flavor intensity data for each region
colombia = {
    "Acidity": [75, 80, 82, 85, 70, 90, 88],
    "Body": [60, 65, 68, 70, 65, 62, 75],
    "Sweetness": [80, 78, 75, 72, 85, 88, 82],
    "Bitterness": [40, 45, 42, 50, 48, 46, 44]
}

ethiopia = {
    "Acidity": [85, 88, 90, 92, 86, 89, 87],
    "Body": [50, 52, 55, 60, 58, 57, 53],
    "Sweetness": [78, 80, 82, 85, 83, 81, 79],
    "Bitterness": [30, 35, 32, 38, 36, 34, 33]
}

indonesia = {
    "Acidity": [65, 68, 70, 72, 64, 67, 66],
    "Body": [80, 82, 85, 88, 87, 83, 81],
    "Sweetness": [60, 62, 58, 65, 63, 61, 64],
    "Bitterness": [60, 65, 62, 68, 66, 64, 63]
}

brazil = {
    "Acidity": [70, 72, 68, 75, 73, 71, 69],
    "Body": [75, 78, 80, 82, 79, 76, 74],
    "Sweetness": [85, 88, 90, 87, 86, 89, 84],
    "Bitterness": [35, 38, 36, 40, 42, 37, 39]
}

# Consolidate data for each attribute across regions
data_acidity = [colombia['Acidity'], ethiopia['Acidity'], indonesia['Acidity'], brazil['Acidity']]
data_body = [colombia['Body'], ethiopia['Body'], indonesia['Body'], brazil['Body']]
data_sweetness = [colombia['Sweetness'], ethiopia['Sweetness'], indonesia['Sweetness'], brazil['Sweetness']]
data_bitterness = [colombia['Bitterness'], ethiopia['Bitterness'], indonesia['Bitterness'], brazil['Bitterness']]

# Setup the plot
plt.figure(figsize=(14, 8))
positions = np.array([1, 2, 3, 4])

# Plot box plots for each flavor attribute
plt.boxplot(data_acidity, positions=positions - 0.3, widths=0.15, patch_artist=True, notch=True,
            boxprops=dict(facecolor='lightcoral', color='darkred'), whiskerprops=dict(color='darkred'), capprops=dict(color='darkred'), medianprops=dict(color='red'))
plt.boxplot(data_body, positions=positions - 0.1, widths=0.15, patch_artist=True, notch=True,
            boxprops=dict(facecolor='tan', color='brown'), whiskerprops=dict(color='brown'), capprops=dict(color='brown'), medianprops=dict(color='saddlebrown'))
plt.boxplot(data_sweetness, positions=positions + 0.1, widths=0.15, patch_artist=True, notch=True,
            boxprops=dict(facecolor='lightgreen', color='darkgreen'), whiskerprops=dict(color='darkgreen'), capprops=dict(color='darkgreen'), medianprops=dict(color='green'))
plt.boxplot(data_bitterness, positions=positions + 0.3, widths=0.15, patch_artist=True, notch=True,
            boxprops=dict(facecolor='lightblue', color='navy'), whiskerprops=dict(color='navy'), capprops=dict(color='navy'), medianprops=dict(color='blue'))

# Customize plot
plt.title("Flavor Profiles of Global Coffee Varieties:\nA Comparative Analysis", fontsize=16, fontweight='bold')
plt.xticks(positions, ['Colombia', 'Ethiopia', 'Indonesia', 'Brazil'], fontsize=12)
plt.ylabel('Flavor Intensity Score (0-100)', fontsize=12)
plt.legend(['Acidity', 'Body', 'Sweetness', 'Bitterness'], loc='upper left', fontsize=10)

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust layout for better appearance
plt.tight_layout()

# Show the plot
plt.show()