import matplotlib.pyplot as plt
import numpy as np

# Generate Soil Quality Index data for four regions
region_1_sqi = np.array([68, 72, 75, 70, 71, 69, 73, 68, 75, 74, 76])
region_2_sqi = np.array([55, 58, 60, 59, 57, 62, 61, 63, 58, 56, 59])
region_3_sqi = np.array([85, 88, 90, 87, 86, 89, 91, 90, 92, 88, 86])
region_4_sqi = np.array([45, 48, 47, 49, 44, 46, 45, 47, 48, 49, 50])

# Generate related Soil Nutrient Index (SNI) data
region_1_sni = np.array([70, 73, 76, 71, 72, 71, 74, 69, 76, 75, 77])
region_2_sni = np.array([57, 59, 61, 60, 58, 63, 62, 64, 59, 57, 60])
region_3_sni = np.array([87, 89, 92, 89, 88, 90, 92, 91, 93, 89, 87])
region_4_sni = np.array([46, 49, 48, 50, 45, 47, 46, 48, 49, 50, 51])

# Combine data into a list for box plotting
data = [region_1_sqi, region_2_sqi, region_3_sqi, region_4_sqi]

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize=(12, 7))

# Create the box plot with customized appearance
box = ax.boxplot(data, patch_artist=True, notch=True,
                 boxprops=dict(facecolor='lightblue', color='blue'),
                 whiskerprops=dict(color='blue'),
                 capprops=dict(color='blue'),
                 medianprops=dict(color='red'))

# Customize individual box colors for better distinction
colors = ['lightgreen', 'lightcoral', 'lightblue', 'lightgoldenrodyellow']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Overlay line plot for Soil Nutrient Index
x_positions = np.arange(1, 5)
mean_sni = [np.mean(region_1_sni), np.mean(region_2_sni), np.mean(region_3_sni), np.mean(region_4_sni)]
ax.plot(x_positions, mean_sni, label='Mean SNI', color='purple', marker='o', markersize=8, linestyle='--')

# Add x-ticks and labels
ax.set_xticks([1, 2, 3, 4])
ax.set_xticklabels(['Region A', 'Region B', 'Region C', 'Region D'], fontsize=10)

# Add axis labels and title
ax.set_xlabel('Regions', fontsize=12)
ax.set_ylabel('Soil Quality Index (SQI)', fontsize=12)
ax.set_title('Soil Quality and Nutrient Assessment\nAcross Different Regions',
             fontsize=14, fontweight='bold', pad=20)

# Enable grid on y-axis for easier interpretation
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Add legend for the overlay plot
ax.legend(loc='upper right', fontsize=10, frameon=False)

# Adjust layout to prevent text from overlapping
plt.tight_layout()

# Display the plot
plt.show()