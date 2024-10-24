import matplotlib.pyplot as plt
import numpy as np

# Data representing communication latency times (in minutes) for different civilizations
# These values are fictional and created for illustrative purposes
alpha_centauri_latency = [12, 14, 15, 13, 18, 16, 17, 14, 12, 15]
betelgeuse_latency = [25, 28, 30, 27, 22, 20, 24, 29, 26, 23]
vega_latency = [5, 6, 7, 8, 7, 6, 5, 9, 10, 8]
proxima_latency = [9, 11, 10, 13, 12, 8, 10, 11, 10, 12]
sirius_latency = [17, 16, 19, 18, 20, 22, 21, 19, 17, 18]

# Combining the data into a single list
latency_data = [alpha_centauri_latency, betelgeuse_latency, vega_latency, proxima_latency, sirius_latency]

# Creating labels for each civilization
civilizations = ['Alpha Centauri', 'Betelgeuse', 'Vega', 'Proxima', 'Sirius']

# Plotting the horizontal box plot
plt.figure(figsize=(12, 6))
boxes = plt.boxplot(latency_data, vert=False, patch_artist=True, labels=civilizations,
                    boxprops=dict(facecolor='skyblue', color='navy', linewidth=1.5),
                    whiskerprops=dict(color='navy', linewidth=1.5),
                    capprops=dict(color='navy', linewidth=1.5),
                    medianprops=dict(color='firebrick', linewidth=2),
                    flierprops=dict(marker='o', color='orange', markersize=6),
                    notch=True)

# Customizing each box with different colors for distinction
colors = ['lightcoral', 'lightblue', 'lightgreen', 'lightyellow', 'lightpink']
for patch, color in zip(boxes['boxes'], colors):
    patch.set_facecolor(color)

# Adding titles and labels
plt.title('Galactic Messaging:\nCommunication Latency Among Extraterrestrial Civilizations', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Latency Time (minutes)', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Adding a grid for better readability
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Adjust layout to avoid overlap and ensure a clean appearance
plt.tight_layout()

# Display the plot
plt.show()