import matplotlib.pyplot as plt
import numpy as np

# Initial budget and changes (in million dollars)
initial_budget = 100
changes = {
    'Public Health': 20,
    'Hospitals': 15,
    'R&D': 10,
    'Tech Upgrade': 8,
    'Emergency Services': -5,
    'Pandemic Preparedness': 12
}

# Calculate cumulative values for the waterfall
cumulative_values = [initial_budget]
labels = ['Initial Budget']
for key, change in changes.items():
    cumulative_values.append(cumulative_values[-1] + change)
    labels.append(key)

# Determine colors for positive (green) and negative (red) changes
colors = ['#76c7c0' if change >= 0 else '#f77f7f' for change in changes.values()]

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the bars
for i in range(1, len(cumulative_values)):
    start_value = cumulative_values[i-1]
    end_value = cumulative_values[i]
    ax.bar(labels[i], end_value - start_value, bottom=start_value, color=colors[i-1], edgecolor='black')

    # Connect bars with a line
    ax.plot([i-1, i], [start_value, end_value], color='gray', linewidth=1.5)

# Add labels and title
plt.xlabel('Budget Categories', fontsize=12)
plt.ylabel('Budget (Million $)', fontsize=12)
plt.title('Healthcare Budget Allocation\nfor 2023', fontsize=14, fontweight='bold', pad=20)

# Annotate changes on bars
for i in range(1, len(cumulative_values)):
    change_value = changes[labels[i]]
    ax.text(i, cumulative_values[i] + (2 if change_value > 0 else -3), 
            f"{change_value:+}M", ha='center', va='bottom' if change_value > 0 else 'top', 
            color='black', fontsize=10, fontweight='bold')

# Annotate cumulative values
for i in range(len(cumulative_values)):
    ax.text(i, cumulative_values[i] + 2, f"{cumulative_values[i]}M", ha='center', 
            va='bottom', color='black', fontsize=10)

# Add grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust x-axis labels to avoid overlap
plt.xticks(rotation=30, ha='right', fontsize=10)

# Adjust layout to prevent overlap and ensure clarity
plt.tight_layout()

# Show plot
plt.show()