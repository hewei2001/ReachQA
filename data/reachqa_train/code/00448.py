import matplotlib.pyplot as plt
import numpy as np

# Define the decades and manually constructed data
decades = ['1960s', '1970s', '1980s', '1990s', '2000s', '2010s']
data = [
    [250, 280, 220, 340, 300, 310],
    [350, 370, 320, 400, 360, 390],
    [480, 510, 470, 520, 490, 530],
    [420, 460, 430, 440, 410, 470],
    [650, 670, 720, 680, 710, 690],
    [580, 600, 620, 610, 630, 590],
]

# Calculate median values for overlay line plot
medians = [np.median(d) for d in data]

# Create the figure and axes
fig, ax = plt.subplots(2, 1, figsize=(12, 12), gridspec_kw={'height_ratios': [3, 1]})

# Plotting the vertical box chart with enhanced visual styling
boxprops = dict(color='darkblue')
whiskerprops = dict(color='darkblue', linestyle='--')
capprops = dict(color='darkblue')
flierprops = dict(markerfacecolor='red', marker='o', markersize=8)
medianprops = dict(color='darkgreen', linewidth=2)

boxes = ax[0].boxplot(data, vert=True, patch_artist=True, notch=True,
                      boxprops=boxprops, whiskerprops=whiskerprops,
                      capprops=capprops, flierprops=flierprops,
                      medianprops=medianprops)

# Add colors with gradients for boxes
colors = ['#FFCCCC', '#FFCC99', '#FFFFCC', '#CCFFCC', '#CCCCFF', '#E0CCFF']
for patch, color in zip(boxes['boxes'], colors):
    patch.set_facecolor(color)

# Overlay a line plot for medians
ax[0].plot(range(1, len(medians) + 1), medians, color='orange', marker='o', markersize=8, label='Median Trend')
ax[0].set_xticklabels(decades, fontsize=11)
ax[0].yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
ax[0].set_title("Fantasy Novel Lengths by Decade\n(Page Count Analysis)", fontsize=16, fontweight='bold')
ax[0].set_xlabel("Decade", fontsize=12)
ax[0].set_ylabel("Number of Pages", fontsize=12)
ax[0].legend(loc='upper left', fontsize=10, title='Key')

# Annotate the maximum and minimum median points
max_median_decade = decades[np.argmax(medians)]
min_median_decade = decades[np.argmin(medians)]
ax[0].annotate(f'Max Median\n{max_median_decade}', xy=(np.argmax(medians)+1, max(medians)), 
               xytext=(np.argmax(medians)+1.5, max(medians)+30),
               arrowprops=dict(facecolor='black', shrink=0.05),
               fontsize=10, color='darkred')
ax[0].annotate(f'Min Median\n{min_median_decade}', xy=(np.argmin(medians)+1, min(medians)), 
               xytext=(np.argmin(medians)+1.5, min(medians)-50),
               arrowprops=dict(facecolor='black', shrink=0.05),
               fontsize=10, color='darkgreen')

# Additional subplot for average page counts
average_page_counts = [np.mean(d) for d in data]
ax[1].bar(decades, average_page_counts, color='lightblue', edgecolor='darkblue')
ax[1].set_title("Average Page Counts by Decade", fontsize=14, fontweight='bold')
ax[1].set_xlabel("Decade", fontsize=12)
ax[1].set_ylabel("Average Pages", fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()