import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

# Data for the ring chart
sectors = [
    'Quantum Hardware Development', 
    'Quantum Algorithms', 
    'Quantum Cryptography', 
    'Cloud Quantum Services', 
    'Quantum Software Development'
]
investments = [150, 100, 80, 120, 50]

# Data for the bar chart - Projected growth rates (as percentages)
growth_rates = [10, 15, 12, 9, 20]

# Define colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
bar_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create the overall figure and grid
fig = plt.figure(figsize=(14, 7))
gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1], wspace=0.3)

# Plotting the ring chart
ax1 = fig.add_subplot(gs[0, 0])
wedges, texts, autotexts = ax1.pie(
    investments, labels=sectors, autopct='%1.1f%%', startangle=90, colors=colors,
    explode=(0.1, 0, 0, 0, 0), pctdistance=0.85, wedgeprops=dict(width=0.3, edgecolor='w')
)
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax1.add_artist(centre_circle)
ax1.axis('equal')
plt.setp(autotexts, size=10, weight="bold", color="white")
plt.setp(texts, size=10)
ax1.text(0, 0, "Quantum Computing\nInvestments\n2035", 
         ha='center', va='center', fontsize=12, fontweight='bold')
ax1.set_title("Investment Allocation in Quantum\nComputing Ventures - 2035", 
              fontsize=14, fontweight='bold')

# Plotting the bar chart
ax2 = fig.add_subplot(gs[0, 1])
bars = ax2.bar(sectors, growth_rates, color=bar_colors, edgecolor='black')
ax2.set_title('Projected Growth Rates\nfor Quantum Sectors', fontsize=14, fontweight='bold')
ax2.set_xlabel('Sectors', fontsize=12)
ax2.set_ylabel('Growth Rate (%)', fontsize=12)
ax2.set_xticklabels(sectors, rotation=45, ha='right', fontsize=10)
ax2.set_yticks(np.arange(0, 25, 5))
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Annotate bars with growth rates
for bar in bars:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, f'{yval}%', 
             ha='center', va='bottom', fontsize=10)

# Ensure layout is tidy
plt.tight_layout()

# Show the combined plot
plt.show()