import matplotlib.pyplot as plt
import numpy as np

# Data: Investments in quantum computing by region in 2023 (in billion USD)
regions = ["North America", "Europe", "East Asia", "South Asia", 
           "Middle East", "Latin America", "Sub-Saharan Africa", "Oceania"]
investment_amounts = [25.4, 18.2, 30.7, 8.5, 10.3, 6.7, 3.1, 5.9]

# Calculate global total investment
total_investment = np.sum(investment_amounts)

# Calculate percentage share for each region
investment_shares = [(amount / total_investment) * 100 for amount in investment_amounts]

# Prepare subplots
fig, axes = plt.subplots(1, 2, figsize=(15, 7))

# Main bar chart on the left
ax1 = axes[0]
x_positions = np.arange(len(regions))
bars = ax1.bar(x_positions, investment_amounts, color=['#4e79a7', '#f28e2b', '#e15759', '#76b7b2', '#59a14f', 
                                                        '#edc949', '#b07aa1', '#ff9da7'], width=0.6)

for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, f'${yval:.1f}B', ha='center', va='bottom', fontsize=10)

# Add a horizontal line for the global average
global_average = np.mean(investment_amounts)
ax1.axhline(global_average, color='gray', linestyle='--', linewidth=1.5, label=f'Global Avg: ${global_average:.1f}B')

ax1.set_title("Quantum Leap: Global Investment in Quantum Computing\nby Region (2023)", fontsize=14, weight='bold', pad=10)
ax1.set_xlabel("Region", fontsize=12)
ax1.set_ylabel("Investment (Billion USD)", fontsize=12)
ax1.set_xticks(x_positions)
ax1.set_xticklabels(regions, rotation=45, ha='right', fontsize=11)
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)
ax1.legend()

# Pie chart on the right
ax2 = axes[1]
ax2.pie(investment_shares, labels=regions, autopct='%1.1f%%', startangle=140,
        colors=['#4e79a7', '#f28e2b', '#e15759', '#76b7b2', '#59a14f', 
                '#edc949', '#b07aa1', '#ff9da7'], wedgeprops={'edgecolor': 'w'})

ax2.set_title("Investment Share by Region\n(Percentage of Total)", fontsize=14, weight='bold', pad=10)

# Ensure the layout is tight
plt.tight_layout()

# Display the plot
plt.show()