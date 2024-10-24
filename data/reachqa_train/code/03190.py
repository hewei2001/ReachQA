import matplotlib.pyplot as plt
import numpy as np

# Energy consumption data for various appliances (in kWh per use)
refrigerator_consumption = [1.5, 1.6, 1.4, 1.7, 1.5, 1.8, 1.6, 1.7, 1.5, 1.6, 1.5, 1.7, 1.8, 1.6, 1.5, 1.6, 1.7]
washing_machine_consumption = [2.5, 2.7, 2.6, 2.4, 2.8, 2.6, 2.5, 2.7, 2.8, 2.6, 2.5, 2.6, 2.7, 2.4, 2.5, 2.6, 2.8, 2.7]
microwave_consumption = [0.8, 0.9, 0.7, 0.8, 0.9, 1.0, 0.8, 0.9, 0.7, 0.8, 0.9, 0.9, 0.8, 0.7, 0.8, 0.9, 1.0]
dishwasher_consumption = [1.9, 2.0, 2.1, 2.0, 2.2, 2.0, 2.1, 2.0, 2.1, 1.9, 2.0, 2.2, 2.1, 2.0, 2.1, 2.2]

# Calculate average consumption
avg_refrigerator = np.mean(refrigerator_consumption)
avg_washing_machine = np.mean(washing_machine_consumption)
avg_microwave = np.mean(microwave_consumption)
avg_dishwasher = np.mean(dishwasher_consumption)

# Set up data for histograms and line plot
consumption_data = [
    (refrigerator_consumption, 'Refrigerator', '#1f77b4', avg_refrigerator),
    (washing_machine_consumption, 'Washing Machine', '#ff7f0e', avg_washing_machine),
    (microwave_consumption, 'Microwave', '#2ca02c', avg_microwave),
    (dishwasher_consumption, 'Dishwasher', '#d62728', avg_dishwasher),
]

plt.figure(figsize=(12, 8))

# Plot histograms and overlay with line plots for average consumption
for data, label, color, avg in consumption_data:
    # Histogram
    plt.hist(data, bins=5, alpha=0.6, label=label, color=color, edgecolor='black', linewidth=1.2)
    # Line plot for average consumption
    plt.axvline(avg, color=color, linestyle='--', linewidth=2, label=f'{label} Avg: {avg:.2f} kWh')

# Set chart attributes
plt.title('Energy Consumption Distribution and Averages\nof Household Appliances', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Energy Consumption per Use (kWh)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.legend(title='Appliance Type & Average Consumption', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()