import matplotlib.pyplot as plt
import numpy as np

# Expanded Tech Company Data
companies = ["Innovatech", "Cyberdyne", "NextGen", "TechHub", "QuantumLeap", "FutureGenius", "UltraTech", "NanoCorp", "CodeBuster", "AIResearch"]
rd_investments = [5.2, 3.6, 4.1, 2.8, 3.0, 4.5, 2.2, 3.8, 5.0, 2.5]
total_revenue = [25.0, 30.0, 22.0, 18.0, 20.0, 28.0, 15.0, 23.0, 27.0, 16.0]
marketing_spend = [2.5, 1.8, 2.1, 1.2, 1.5, 2.7, 1.0, 2.0, 2.3, 1.4]

# Calculate the percentage of revenue spent on R&D and Marketing
rd_percentage = [(rd / total) * 100 for rd, total in zip(rd_investments, total_revenue)]
marketing_percentage = [(marketing / total) * 100 for marketing, total in zip(marketing_spend, total_revenue)]

# Setup the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Define colors for each stack
colors_rd = '#1f77b4'
colors_marketing = '#ff7f0e'

# Create the stacked bar chart
bar_positions = np.arange(len(companies))
bars_rd = ax.bar(bar_positions, rd_investments, color=colors_rd, width=0.4, label='R&D Investment')
bars_marketing = ax.bar(bar_positions, marketing_spend, bottom=rd_investments, color=colors_marketing, width=0.4, label='Marketing Spend')

# Add data labels
for i, (bar, mkt) in enumerate(zip(bars_rd, marketing_spend)):
    yval = bar.get_height()
    mkt_val = yval + mkt
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, f'{rd_percentage[i]:.1f}%', ha='center', va='bottom', fontsize=9, color='black')
    ax.text(bar.get_x() + bar.get_width() / 2, mkt_val + 0.1, f'{marketing_percentage[i]:.1f}%', ha='center', va='bottom', fontsize=9, color='black')

# Customize chart elements
ax.set_title("Tech Company Investment Distribution in Fiscal Year 2025", fontsize=18, pad=30)
ax.set_xlabel("Company", fontsize=12)
ax.set_ylabel("Investment (Billion USD)", fontsize=12)
ax.set_xticks(bar_positions)
ax.set_xticklabels(companies, fontsize=10, rotation=45, ha='right')
ax.set_ylim(0, 10)

# Add grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Add a legend
ax.legend(loc='upper right', fontsize=11)

# Annotate for highest total investment
max_investment_idx = rd_investments.index(max(rd_investments))
ax.annotate('Highest R&D investment', xy=(max_investment_idx, rd_investments[max_investment_idx]), xytext=(max_investment_idx + 0.5, 8),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=11, color='darkred')

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the chart
plt.show()