import matplotlib.pyplot as plt
import numpy as np

# Define months and digital sales growth data for 2023
months = np.arange(1, 13)
ebook_growth = [5, 7, 10, 12, 15, 20, 18, 25, 28, 30, 35, 40]  # in percentage
audiobook_growth = [10, 15, 18, 20, 22, 25, 27, 30, 33, 37, 40, 45]  # in percentage
digital_magazines_growth = [3, 4, 6, 8, 10, 12, 14, 17, 20, 22, 25, 28]  # in percentage

fig, ax = plt.subplots(figsize=(14, 9))
fig.patch.set_facecolor('#f0f0f5')

# Plotting each category with enhanced line styles and colors
ax.plot(months, ebook_growth, marker='o', linestyle='-', linewidth=2.5, color='#D35400', label='E-Books')
ax.plot(months, audiobook_growth, marker='s', linestyle='--', linewidth=2.5, color='#1F618D', label='Audiobooks')
ax.plot(months, digital_magazines_growth, marker='^', linestyle='-.', linewidth=2.5, color='#229954', label='Digital Magazines')

# Adding titles and labels
plt.title('The Rise of E-Publishing:\nMonthly Digital Sales Growth in 2023', fontsize=18, fontweight='bold', pad=30)
plt.xlabel('Month', fontsize=14, fontweight='semibold')
plt.ylabel('Growth in Sales (%)', fontsize=14, fontweight='semibold')

# Customize ticks and grid
plt.xticks(months, labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)
plt.yticks(np.arange(0, 51, 5))
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7, color='grey')

# Add a legend with enhanced detail
plt.legend(loc='upper left', fontsize=12, frameon=False, title='Sales Channels')

# Shading the area between different growth trends to highlight differences
ax.fill_between(months, ebook_growth, audiobook_growth, color='orange', alpha=0.1)
ax.fill_between(months, audiobook_growth, digital_magazines_growth, color='blue', alpha=0.1)

# Annotations for notable growth points
ax.annotate('Audiobook Peak', xy=(12, 45), xytext=(9.5, 47),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=11, color='blue', fontweight='bold')

ax.annotate('E-book Surge', xy=(6, 20), xytext=(2, 35),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=11, color='red', fontweight='bold')

ax.annotate('Digital Magazines Rising', xy=(9, 20), xytext=(6.5, 25),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=11, color='green', fontweight='bold')

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()