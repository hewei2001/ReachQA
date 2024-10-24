import matplotlib.pyplot as plt
import numpy as np

# Capitals and corresponding solar installations (artificial data)
capitals = ['Berlin', 'Paris', 'Madrid', 'Rome', 'Amsterdam']
installations = [15000, 12000, 18000, 13000, 16000]
growth_rate = [5.2, 3.8, 4.5, 6.0, 4.1]  # Hypothetical annual growth rates in percentage

# Data preparation for plotting
x = np.arange(len(capitals))
colors = ['#4CAF50', '#FF9800', '#2196F3', '#FFC107', '#9C27B0']

# Plotting
fig, ax1 = plt.subplots(figsize=(12, 7))

# Create bar plot
bars = ax1.bar(x, installations, color=colors, edgecolor='black', width=0.6, label='Installations Count')
ax1.set_xlabel('Capital Cities', fontsize=13)
ax1.set_ylabel('Installations Count', fontsize=13, color='black')
ax1.set_xticks(x)
ax1.set_xticklabels(capitals, fontsize=11)
ax1.yaxis.grid(True, linestyle='--', alpha=0.5)
plt.xticks(rotation=15)

# Annotate bars with values
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 200, f"{yval:,}", ha='center', va='bottom', fontsize=11, fontweight='bold', color='black')

# Create a secondary y-axis for the growth rate line plot
ax2 = ax1.twinx()
ax2.plot(x, growth_rate, color='brown', marker='o', linestyle='--', linewidth=2, label='Growth Rate (%)')
ax2.set_ylabel('Growth Rate (%)', fontsize=13, color='brown')

# Annotate key points on the line plot
for i, (xi, rate) in enumerate(zip(x, growth_rate)):
    ax2.text(xi, rate + 0.2, f"{rate}%", ha='center', va='bottom', fontsize=11, fontweight='bold', color='brown')

# Title and adjust layout
ax1.set_title('Solar Energy Adoption and Growth Rate in European Capitals\n(2023)', fontsize=18, fontweight='bold')
fig.tight_layout()

# Add legends for both plots
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Show the plot
plt.show()