import matplotlib.pyplot as plt
import numpy as np

# Synthetic graduation rate data (%) for each department over the past five years
comp_sci_graduation_rates = np.array([85, 88, 90, 87, 89])
arts_hum_graduation_rates = np.array([70, 75, 72, 74, 73])
business_graduation_rates = np.array([82, 80, 85, 83, 81])
biology_graduation_rates = np.array([78, 76, 80, 79, 77])
mech_eng_graduation_rates = np.array([88, 85, 87, 86, 89])

# Collecting data into a list for vertical box plot
data = [comp_sci_graduation_rates, arts_hum_graduation_rates, business_graduation_rates, biology_graduation_rates, mech_eng_graduation_rates]

# Create the vertical box plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting the boxplot vertically
bp = ax.boxplot(data, patch_artist=True, vert=True, widths=0.6, notch=True,
                boxprops=dict(facecolor='lightgrey', color='black'),
                whiskerprops=dict(color='black'), capprops=dict(color='black'),
                medianprops=dict(color='blue', linewidth=2),
                flierprops=dict(marker='o', color='red', alpha=0.6))

# Adding grid for clarity
ax.yaxis.grid(True, linestyle='--', color='grey', alpha=0.7)

# Customizing plot labels and title
ax.set_xticklabels(['Comp Sci', 'Arts & Hum', 'Business', 'Biology', 'Mech Eng'], fontsize=10, rotation=15)
ax.set_ylabel('Graduation Rate (%)', fontsize=12)
ax.set_title('Variability in Graduation Rates\nAcross University Departments',
             fontsize=14, fontweight='bold', pad=15)

# Highlighting medians with annotations
for i, median in enumerate(bp['medians']):
    x_median = median.get_xdata()[1]
    y_median = median.get_ydata()[1]
    ax.annotate(f'{y_median:.0f}%', xy=(x_median, y_median), xytext=(0, 5), 
                textcoords='offset points', color='blue', fontsize=10, ha='center')

# Enhancing visual distinctiveness by coloring the boxes differently
colors = ['lightblue', 'lightgreen', 'lightpink', 'lightyellow', 'lightcoral']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Ensure no overlap and improve layout
plt.tight_layout()

# Display the chart
plt.show()