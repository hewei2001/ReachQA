import matplotlib.pyplot as plt
import numpy as np

# Define the time periods
years = ['2019', '2020', '2021', '2022', '2023']

# Define the changes in savings (in thousands of dollars)
changes = [0, 25, 25, -10, 30]  # Starting with 0 as the base year

# Cumulative savings starting from zero
cumulative_savings = np.cumsum(changes)

# Determine colors based on positive or negative changes
colors = ['grey' if change == 0 else ('green' if change > 0 else 'red') for change in changes]

# Initialize plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot bars with cumulative sum
ax.bar(years, cumulative_savings, color=colors, edgecolor='black')

# Add value annotations on each bar
for i in range(len(years)):
    change_label = f"+${changes[i]:.0f}k" if changes[i] > 0 else f"${changes[i]:.0f}k"
    ax.text(i, cumulative_savings[i] - 5 if changes[i] < 0 else cumulative_savings[i] + 2,
            f"{change_label}\n${cumulative_savings[i]:.0f}k", ha='center', va='bottom',
            fontweight='bold', fontsize=10, color='black')

# Add connecting lines between bars to depict flow
for i in range(1, len(years)):
    ax.plot([i - 1, i], [cumulative_savings[i - 1], cumulative_savings[i]], color='black', linewidth=1, linestyle='--')

# Set title and labels
ax.set_title('Solar Power Installation Impact on\nCommunity Energy Savings (2020 - 2023)',
             fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Cumulative Energy Savings ($k)', fontsize=12)

# Add gridlines for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Rotate x-axis labels for clarity
plt.xticks(rotation=45)

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Show plot
plt.show()