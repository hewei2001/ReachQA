import matplotlib.pyplot as plt
import numpy as np

# Data for tech startup funding
sectors = ['Artificial Intelligence', 'FinTech', 'HealthTech', 'EdTech', 'GreenTech']
funding_amounts = [350, 275, 220, 180, 150]
colors = ['#FF8A65', '#4DB6AC', '#7986CB', '#FFD54F', '#BA68C8']

# Additional data for the pie chart - market share by sector
market_share = [25, 20, 18, 15, 22]

# Create the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Bar Chart
bar_positions = np.arange(len(sectors))
bars = ax1.bar(bar_positions, funding_amounts, color=colors, edgecolor='black', alpha=0.85, width=0.6)

ax1.set_xticks(bar_positions)
ax1.set_xticklabels(sectors, rotation=15, ha='right', fontsize=12)
ax1.set_title('Venture Capital Funding Distribution\nin Silicon Valley Tech Sectors (2023)', 
              fontsize=14, fontweight='bold', pad=15)
ax1.set_xlabel('Tech Sectors', fontsize=12)
ax1.set_ylabel('Funding Amount (Million USD)', fontsize=12)

# Adding value labels to bars
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, height - 10, f'{height}M', 
             ha='center', va='bottom', fontsize=10, color='white', fontweight='bold')

ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Pie Chart
ax2.pie(market_share, labels=sectors, autopct='%1.1f%%', startangle=140, colors=colors, wedgeprops=dict(edgecolor='black'))

ax2.set_title('Market Share by Tech Sector\nin Silicon Valley (2023)', fontsize=14, fontweight='bold', pad=15)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()