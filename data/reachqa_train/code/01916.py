import matplotlib.pyplot as plt
import numpy as np

# Original data: Robotics utilization in different sectors from 2000 to 2020
years = np.arange(2000, 2021)
manufacturing = np.array([10, 15, 20, 28, 35, 45, 55, 65, 75, 85, 100, 115, 130, 145, 160, 175, 190, 210, 230, 250, 270])
healthcare = np.array([5, 7, 10, 13, 18, 23, 30, 38, 45, 55, 65, 75, 88, 100, 115, 130, 145, 160, 175, 190, 205])
retail = np.array([3, 5, 7, 10, 13, 17, 22, 28, 35, 42, 50, 58, 67, 77, 88, 100, 113, 126, 140, 155, 170])
agriculture = np.array([2, 3, 4, 6, 8, 10, 13, 17, 21, 26, 32, 39, 47, 56, 66, 77, 89, 102, 116, 131, 147])

# Calculate average annual growth rate for each sector
growth_rates = (manufacturing[-1] - manufacturing[0]) / len(years), \
               (healthcare[-1] - healthcare[0]) / len(years), \
               (retail[-1] - retail[0]) / len(years), \
               (agriculture[-1] - agriculture[0]) / len(years)

sectors = ['Manufacturing', 'Healthcare', 'Retail', 'Agriculture']

# Set up a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8), gridspec_kw={'width_ratios': [2, 1]})

# Plot the stackplot in the first subplot
ax1.stackplot(years, manufacturing, healthcare, retail, agriculture,
              labels=sectors,
              colors=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99'], alpha=0.7)
ax1.set_title("The Evolution of Robotics in Industry\nfrom 2000 to 2020", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Robotics Utilization (Arbitrary Units)", fontsize=12)
ax1.legend(loc='upper left', fontsize=10, title="Industry Sectors")
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax1.tick_params(axis='x', rotation=45)

# Plot the bar chart in the second subplot
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']
ax2.bar(sectors, growth_rates, color=colors, alpha=0.8)
ax2.set_title("Average Annual Growth Rate\nof Robotics Utilization", fontsize=14, pad=20)
ax2.set_ylabel("Growth Rate (Units per Year)", fontsize=12)
ax2.set_xticklabels(sectors, rotation=30, ha='right')

# Add data labels to the bar chart
for i, rate in enumerate(growth_rates):
    ax2.text(i, rate + 2, f'{rate:.2f}', ha='center', va='bottom', fontweight='bold')

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the chart
plt.show()