import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.array([2019, 2020, 2021, 2022, 2023])

# Investment data in millions
ai_investment = np.array([10, 15, 20, 30, 45])
quantum_investment = np.array([5, 10, 15, 20, 30])
iot_investment = np.array([8, 12, 18, 25, 35])
cybersecurity_investment = np.array([12, 18, 25, 35, 50])
blockchain_investment = np.array([3, 5, 8, 12, 20])

# Stack the data for area chart
investment_data = np.vstack([ai_investment, quantum_investment, iot_investment, cybersecurity_investment, blockchain_investment])

# Colors for each area
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Plotting the area chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(years, investment_data, labels=['AI', 'Quantum Computing', 'IoT', 'Cybersecurity', 'Blockchain'], colors=colors, alpha=0.8)

# Add title and labels
ax.set_title("TechInnovate Corp's Strategic Investments\nin Emerging Technologies (2019-2023)", fontsize=16, weight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Investment (in million $)", fontsize=12)

# Adding legend
ax.legend(loc='upper left', fontsize=10)

# Customize grid
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Adjusting x-ticks for better readability
ax.set_xticks(years)
ax.set_xticklabels(years, fontsize=10)

# Ensuring layout is adjusted properly
plt.tight_layout()

# Display the plot
plt.show()