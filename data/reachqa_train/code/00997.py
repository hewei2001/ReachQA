import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Define major international ports for the study
ports = ['Los Angeles', 'Rotterdam', 'Shanghai', 'Singapore', 'Hamburg', 'Dubai']

# Define shipping delay data in hours for each port
delay_data = [
    [10, 12, 8, 11, 15, 17, 16, 19, 20, 22, 25],  # Los Angeles
    [7, 9, 6, 8, 7, 10, 11, 8, 6, 7, 9],          # Rotterdam
    [14, 13, 15, 17, 18, 19, 22, 23, 21, 20, 25], # Shanghai
    [6, 5, 7, 8, 8, 10, 12, 11, 9, 7, 6],         # Singapore
    [8, 10, 11, 9, 10, 13, 12, 11, 10, 12, 14],   # Hamburg
    [9, 8, 10, 11, 12, 15, 14, 16, 13, 12, 11]    # Dubai
]

# Initialize the style using Seaborn
sns.set_theme(style="darkgrid")

# Create the horizontal box plot
fig, ax = plt.subplots(figsize=(14, 9))
bp = ax.boxplot(delay_data, vert=False, patch_artist=True, notch=True, labels=ports)

# Customizing the appearance
colors = sns.color_palette("pastel", 6)
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Style the whiskers, caps, and medians
plt.setp(bp['whiskers'], color='gray', linestyle='--', linewidth=1.5)
plt.setp(bp['caps'], color='gray', linewidth=2)
plt.setp(bp['medians'], color='black', linewidth=2)

# Overlay jittered points for data distribution
for i, port_data in enumerate(delay_data):
    y = np.random.normal(i+1, 0.04, size=len(port_data))
    ax.plot(port_data, y, 'o', alpha=0.5, color='black', markersize=5)

# Add titles and labels
plt.title("Global Shipping Delays Across Major Ports in 2023:\nA Comparative Study", fontsize=18, weight='bold', pad=20)
plt.xlabel("Delays (Hours)", fontsize=14)
plt.ylabel("Ports", fontsize=14)

# Annotate the maximum delay in Los Angeles
max_delay_la = max(delay_data[0])
ax.annotate(f'Max Delay: {max_delay_la} hrs', xy=(max_delay_la, 1), xytext=(max_delay_la + 5, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, color='darkred')

# Add grid for better readability
ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Automatically adjust the layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()