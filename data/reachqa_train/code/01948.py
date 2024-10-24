import matplotlib.pyplot as plt
import numpy as np

# Define months and digital sales growth data for 2023
months = np.arange(1, 13)
ebook_growth = [5, 7, 10, 12, 15, 20, 18, 25, 28, 30, 35, 40]  # in percentage
audiobook_growth = [10, 15, 18, 20, 22, 25, 27, 30, 33, 37, 40, 45]  # in percentage
digital_magazines_growth = [3, 4, 6, 8, 10, 12, 14, 17, 20, 22, 25, 28]  # in percentage

# Create the line chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting each category with distinct styles
ax.plot(months, ebook_growth, marker='o', linestyle='-', linewidth=2, color='#FF5733', label='E-Books')
ax.plot(months, audiobook_growth, marker='s', linestyle='--', linewidth=2, color='#33C1FF', label='Audiobooks')
ax.plot(months, digital_magazines_growth, marker='^', linestyle='-.', linewidth=2, color='#28B463', label='Digital Magazines')

# Adding titles and labels
plt.title('The Rise of E-Publishing:\nMonthly Digital Sales Growth in 2023', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Growth in Sales (%)', fontsize=12)

# Customize ticks and grid
plt.xticks(months, labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)
plt.yticks(np.arange(0, 51, 5))
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Add a legend
plt.legend(loc='upper left', fontsize=10, frameon=False)

# Annotations for notable growth points
ax.annotate('Audiobook Peak', xy=(12, 45), xytext=(9, 50),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, color='blue')

ax.annotate('E-book Surge', xy=(6, 20), xytext=(2, 35),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, color='red')

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()