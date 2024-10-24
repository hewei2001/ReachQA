import matplotlib.pyplot as plt
import numpy as np

# Sample word counts for classic novels
word_counts = np.array([
    48000, 73000, 98000, 123000, 180000, 56000, 75000,
    88000, 95000, 46000, 120000, 137000, 90000, 52000,
    65000, 99000, 105000, 123000, 67000, 87000, 45000,
    78000, 94000, 55000, 110000, 140000, 82000
])

# Filter word counts less than 150000
adjusted_max = word_counts[word_counts < 150000]

# Define bins for word count ranges (10,000-word intervals)
bins = np.arange(40000, 150000, 10000)

# Create the histogram
fig, ax1 = plt.subplots(figsize=(12, 7))
ax1.hist(adjusted_max, bins=bins, color='mediumseagreen', edgecolor='black', alpha=0.75, label='Word Count Distribution')

# Add cumulative line plot
ax2 = ax1.twinx()  # Create a secondary y-axis
sorted_counts = np.sort(adjusted_max)
cumulative = np.cumsum(sorted_counts) / np.sum(sorted_counts) * 100
ax2.plot(sorted_counts, cumulative, color='royalblue', linestyle='--', marker='o', label='Cumulative Distribution')

# Plot details
ax1.set_title('Distribution and Cumulative Word Count\nin Classic Novels', fontsize=16, fontweight='bold')
ax1.set_xlabel('Word Count Range', fontsize=12)
ax1.set_ylabel('Number of Novels', fontsize=12, color='mediumseagreen')
ax2.set_ylabel('Cumulative Percentage (%)', fontsize=12, color='royalblue')

ax1.tick_params(axis='x', rotation=45, labelsize=10)
ax1.tick_params(axis='y', labelsize=10, colors='mediumseagreen')
ax2.tick_params(axis='y', labelsize=10, colors='royalblue')

ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Annotate with an insight
ax1.text(100000, 6, 'Classic Literature is Diverse\nin Length and Style', fontsize=10, ha='center', color='darkgreen')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()