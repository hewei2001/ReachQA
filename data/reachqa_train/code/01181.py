import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
countries = ['Country A', 'Country B', 'Country C', 'Country D', 'Country E']
tea_consumption = [2.5, 4.2, 1.8, 3.6, 2.9]

# Creating bar chart
fig, ax = plt.subplots(figsize=(10, 6))
x_pos = np.arange(len(countries))
colors = ['#B5651D', '#8B4513', '#A0522D', '#CD853F', '#D2691E']
bars = ax.bar(x_pos, tea_consumption, color=colors, alpha=0.8, width=0.5)

# Add data annotations
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2.0, height + 0.1,
            f'{height:.1f}', ha='center', va='bottom', fontsize=10)

# Set the title and labels
ax.set_title('Average Annual Tea Consumption\nPer Person by Country', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Country', fontsize=12)
ax.set_ylabel('Tea Consumption (kg/person/year)', fontsize=12)

# Set x-axis tick positions and labels
ax.set_xticks(x_pos)
ax.set_xticklabels(countries, rotation=30, ha='right', fontsize=10)

# Adding grid only on y-axis for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.6, alpha=0.7)

# Adjust layout
plt.tight_layout()

# Show the chart
plt.show()