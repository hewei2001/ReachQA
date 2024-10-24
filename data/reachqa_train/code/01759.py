import matplotlib.pyplot as plt
import numpy as np

# Months for x-axis
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Viewership share data for each platform (%)
streamflix_share = [30, 32, 31, 33, 35, 34, 33, 34, 36, 38, 37, 40]
bingenet_share = [25, 24, 26, 25, 24, 26, 27, 26, 25, 24, 26, 25]
directstream_share = [20, 19, 18, 19, 18, 18, 18, 17, 16, 17, 16, 15]
quickwatch_share = [25, 25, 25, 23, 23, 22, 22, 23, 23, 21, 21, 20]

# Convert to numpy arrays for stacking
streamflix = np.array(streamflix_share)
bingenet = np.array(bingenet_share)
directstream = np.array(directstream_share)
quickwatch = np.array(quickwatch_share)

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot stacked area chart
ax.stackplot(months, streamflix, bingenet, directstream, quickwatch,
             labels=['StreamFlix', 'BingeNet', 'DirectStream', 'QuickWatch'],
             colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'],
             alpha=0.85)

# Set title and labels with appropriate breaks for clarity
ax.set_title('2023 Viewership Share Dynamics:\nCompeting Streaming Platforms', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Months', fontsize=12)
ax.set_ylabel('Viewership Share (%)', fontsize=12)

# Customize grid
ax.grid(True, linestyle='--', alpha=0.5)

# Add legend outside the plot area to prevent occlusion of data
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Adjust layout to accommodate legend
plt.tight_layout()

# Display the plot
plt.show()