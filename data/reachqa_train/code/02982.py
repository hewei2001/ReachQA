import matplotlib.pyplot as plt
import numpy as np

# Define step count ranges and their corresponding frequency of employees
step_ranges = [
    '0-2000', '2000-5000', '5000-7500', 
    '7500-10000', '10000-15000', '15000-20000'
]
frequency = np.array([12, 58, 32, 18, 7, 3])  # Modified hypothetical data for illustration

# Define the bins for the histogram
bins = [0, 2000, 5000, 7500, 10000, 15000, 20000]

# Plotting the histogram
plt.figure(figsize=(12, 7))
plt.hist(bins[:-1], bins=bins, weights=frequency, color='lightseagreen', edgecolor='black', alpha=0.7)

# Add annotations (step ranges) as text on the histogram
for i, count in enumerate(frequency):
    plt.text(bins[i] + (bins[i+1] - bins[i]) / 2, count + 1, f'{step_ranges[i]}: {count}', 
             fontsize=10, ha='center', va='bottom')

# Customizing plot details
plt.title('Daily Steps Distribution\nin a Tech Company', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Step Count Range', fontsize=14)
plt.ylabel('Number of Employees', fontsize=14)
plt.xticks(bins)
plt.ylim(0, max(frequency) + 5)
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the plot
plt.show()