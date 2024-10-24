import matplotlib.pyplot as plt
import numpy as np

# Define the space agencies and their budget allocations for 2025
agencies = ['NASA', 'ESA', 'Roscosmos', 'CNSA', 'ISRO', 'Other Initiatives']
budgets_2025 = [35, 20, 15, 15, 10, 5]

# Define hypothetical budget allocations for 2024 for comparison
budgets_2024 = [33, 19, 14, 16, 11, 4]

# Colors for each sector, consistent across charts
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2C2F0', '#F6BD60']

# Calculate changes in budget
budget_changes = np.array(budgets_2025) - np.array(budgets_2024)

# Create a subplot grid
fig, axes = plt.subplots(1, 2, figsize=(16, 7))

# Pie chart for 2025 budgets
wedges, texts, autotexts = axes[0].pie(
    budgets_2025,
    labels=agencies,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=(0.1, 0, 0, 0, 0, 0),
    shadow=True
)

# Customize text appearance in pie chart
for text in texts:
    text.set_fontsize(12)
    text.set_fontweight('bold')

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

# Add a title to the pie chart
axes[0].set_title('2025 Global Space Exploration Budget\nAllocation', fontsize=14, fontweight='bold', pad=10)

# Bar chart for budget changes from 2024 to 2025
x = np.arange(len(agencies))
axes[1].bar(x, budget_changes, color=colors, edgecolor='black')

# Customize bar chart appearance
axes[1].set_title('Budget Change from 2024 to 2025\n(Space Agencies)', fontsize=14, fontweight='bold', pad=10)
axes[1].set_xticks(x)
axes[1].set_xticklabels(agencies, rotation=45, ha='right', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Change in Budget (Billion $)', fontsize=12)
axes[1].grid(True, axis='y', linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()