import matplotlib.pyplot as plt
import numpy as np

# Define ocean regions and health indicators
ocean_regions = ['Caribbean', 'Indian Ocean', 'Pacific Ocean', 'Atlantic Ocean']
indicators = ['Coral Cover', 'Biodiversity', 'Water Clarity']

# Define health index data (values between 0 and 100)
health_index = np.array([
    [65, 70, 55],  # Caribbean
    [75, 80, 60],  # Indian Ocean
    [85, 90, 80],  # Pacific Ocean
    [60, 65, 50]   # Atlantic Ocean
])

# Calculate average health index for each ocean region
average_health_index = np.mean(health_index, axis=1)

# Create subplots for the heatmap and bar chart
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Heatmap of health indices
cax = ax1.imshow(health_index, cmap='YlGnBu', aspect='auto')
ax1.set_xticks(np.arange(len(indicators)))
ax1.set_xticklabels(indicators, rotation=45, ha='right', fontsize=10)
ax1.set_yticks(np.arange(len(ocean_regions)))
ax1.set_yticklabels(ocean_regions, fontsize=10)
ax1.set_title('Coral Reef Health Across Tropical Oceans\nAn Underwater Ecosystem Survey', fontsize=12, weight='bold', pad=20)

# Annotate heatmap cells with scores
for i in range(len(ocean_regions)):
    for j in range(len(indicators)):
        ax1.text(j, i, str(health_index[i, j]), ha='center', va='center', color='black', fontsize=8)

# Color bar for the heatmap
cbar = fig.colorbar(cax, ax=ax1, orientation='vertical', pad=0.02)
cbar.set_label('Health Index Score', rotation=270, labelpad=15)

# Bar chart for average health indices
ax2.bar(ocean_regions, average_health_index, color=['lightcoral', 'lightseagreen', 'lightskyblue', 'lightgoldenrodyellow'])
ax2.set_ylim(0, 100)
ax2.set_title('Average Health Index per Ocean Region', fontsize=12, weight='bold', pad=20)
ax2.set_ylabel('Average Health Index', fontsize=10)
ax2.set_xlabel('Ocean Region', fontsize=10)

# Annotate bar chart with average scores
for i, v in enumerate(average_health_index):
    ax2.text(i, v + 2, f"{v:.1f}", ha='center', va='bottom', fontsize=9)

# Adjust layout to fit all elements neatly
plt.tight_layout()

# Display the plots
plt.show()