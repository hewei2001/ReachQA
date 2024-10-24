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

# Calculate total investments per year
total_investment = ai_investment + quantum_investment + iot_investment + cybersecurity_investment + blockchain_investment

# Calculate year-over-year growth rates for total investments
growth_rate = np.zeros_like(total_investment)
growth_rate[1:] = ((total_investment[1:] - total_investment[:-1]) / total_investment[:-1]) * 100

# Stack the data for area chart
investment_data = np.vstack([ai_investment, quantum_investment, iot_investment, cybersecurity_investment, blockchain_investment])

# Colors for each area
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Plotting the area chart
ax1.stackplot(years, investment_data, labels=['AI', 'Quantum Computing', 'IoT', 'Cybersecurity', 'Blockchain'], colors=colors, alpha=0.8)
ax1.set_title("TechInnovate Corp's Strategic Investments\nin Emerging Technologies (2019-2023)", fontsize=14, weight='bold')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Investment (in million $)", fontsize=12)
ax1.legend(loc='upper left', fontsize=10)
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax1.set_xticks(years)
ax1.set_xticklabels(years, fontsize=10)

# Plotting the growth rate chart
ax2.plot(years, growth_rate, marker='o', color='tab:red', linestyle='-')
ax2.set_title("Year-over-Year Growth Rate\nof Total Investments", fontsize=14, weight='bold')
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Growth Rate (%)", fontsize=12)
ax2.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax2.set_xticks(years)
ax2.set_xticklabels(years, fontsize=10)
ax2.set_yticks(np.arange(-10, 110, 10))
ax2.axhline(0, color='black', linewidth=0.8, linestyle='-')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()