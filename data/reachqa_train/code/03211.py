import matplotlib.pyplot as plt
import numpy as np

# Tech company data
companies = ["Innovatech", "Cyberdyne", "NextGen", "TechHub", "QuantumLeap"]
rd_investments = [5.2, 3.6, 4.1, 2.8, 3.0]  # R&D investments in billion USD
total_revenue = [25.0, 30.0, 22.0, 18.0, 20.0]  # Total revenue in billion USD

# Calculate the percentage of revenue spent on R&D
rd_percentage = [(rd / total) * 100 for rd, total in zip(rd_investments, total_revenue)]

# Setup the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Define colors for each bar
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create the bar chart
bar_positions = np.arange(len(companies))
bars = ax.bar(bar_positions, rd_investments, color=colors, width=0.5)

# Add data labels
for i, bar in enumerate(bars):
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, f'{yval:.1f}B\n({rd_percentage[i]:.1f}%)',
            ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

# Customize chart elements
ax.set_title("Tech Company R&D Investments in\nFiscal Year 2025", fontsize=16, pad=20)
ax.set_xlabel("Company", fontsize=12)
ax.set_ylabel("R&D Investment (Billion USD)", fontsize=12)
ax.set_xticks(bar_positions)
ax.set_xticklabels(companies, fontsize=11, rotation=45, ha='right')
ax.set_ylim(0, 6)

# Add grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.6)

# Add annotation for the highest investment
ax.annotate('Highest investment by Innovatech', xy=(0, 5.2), xytext=(0.8, 5.5),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=11, color='darkred')

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the chart
plt.show()