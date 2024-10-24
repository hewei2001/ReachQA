import matplotlib.pyplot as plt
import numpy as np

# Data for tech startup funding
sectors = ['Artificial Intelligence', 'FinTech', 'HealthTech', 'EdTech', 'GreenTech']
funding_amounts = [350, 275, 220, 180, 150]
colors = ['#FF8A65', '#4DB6AC', '#7986CB', '#FFD54F', '#BA68C8']

# Create the bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Calculate positions for each bar based on the number of sectors
bar_positions = np.arange(len(sectors))

# Draw the bars
bars = ax.bar(bar_positions, funding_amounts, color=colors, edgecolor='black', alpha=0.85, width=0.6)

# Set the x-ticks to be at the center of each bar and label them with sector names
ax.set_xticks(bar_positions)
ax.set_xticklabels(sectors, rotation=15, ha='right', fontsize=12)

# Title and labels
ax.set_title('Venture Capital Funding Distribution\nin Silicon Valley Tech Sectors (2023)', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Tech Sectors', fontsize=14)
ax.set_ylabel('Funding Amount (Million USD)', fontsize=14)

# Add value labels above each bar
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height - 10, f'{height}M', 
            ha='center', va='bottom', fontsize=12, color='white', fontweight='bold')

# Add horizontal grid lines
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()