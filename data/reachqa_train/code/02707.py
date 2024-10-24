import matplotlib.pyplot as plt

# Initial grant budget (in million dollars)
initial_grant_budget = 200

# Changes in grant allocation for 2025 (in million dollars)
grant_changes = {
    'Quantum Algorithms': 25,
    'Quantum Hardware': -10,
    'Software Development': 15,
    'Quantum Cryptography': -5,
    'International Collaboration': 30,
    'Education & Outreach': 5
}

# Calculate cumulative values for the waterfall
cumulative_grants = [initial_grant_budget]
grant_labels = ['Initial Budget']
for sector, change in grant_changes.items():
    cumulative_grants.append(cumulative_grants[-1] + change)
    grant_labels.append(sector)

# Determine colors for positive (green) and negative (red) changes
bar_colors = ['#8fd175' if change >= 0 else '#d17575' for change in grant_changes.values()]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the bars
for i in range(1, len(cumulative_grants)):
    start_value = cumulative_grants[i-1]
    end_value = cumulative_grants[i]
    ax.bar(grant_labels[i], end_value - start_value, bottom=start_value, color=bar_colors[i-1], edgecolor='black')

    # Connect bars with a line
    ax.plot([i-1, i], [start_value, end_value], color='gray', linewidth=1.5)

# Add labels and title
plt.xlabel('Research Sectors', fontsize=12)
plt.ylabel('Grants (Million $)', fontsize=12)
plt.title('The Evolution of Quantum Computing\nResearch Grants: 2025 Budget Adjustments', fontsize=14, fontweight='bold', pad=20)

# Annotate changes on bars
for i in range(1, len(cumulative_grants)):
    change_value = grant_changes[grant_labels[i]]
    ax.text(i, cumulative_grants[i] + (2 if change_value > 0 else -3), 
            f"{change_value:+}M", ha='center', va='bottom' if change_value > 0 else 'top', 
            color='black', fontsize=10, fontweight='bold')

# Annotate cumulative values
for i in range(len(cumulative_grants)):
    ax.text(i, cumulative_grants[i] + 2, f"{cumulative_grants[i]}M", ha='center', 
            va='bottom', color='black', fontsize=10)

# Add grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust x-axis labels to avoid overlap
plt.xticks(rotation=30, ha='right', fontsize=10)

# Adjust layout to prevent overlap and ensure clarity
plt.tight_layout()

# Show plot
plt.show()