import matplotlib.pyplot as plt
import numpy as np

# Define the months for the dataset
months = np.array(['January', 'February', 'March', 'April', 'May', 'June'])

# Data for the original plot
average_execution_time = np.array([180, 165, 155, 145, 138, 130])
execution_std_dev = np.array([10, 12, 11, 9, 8, 7])

# Additional data for new subplot (e.g., number of operations executed)
operations_executed = np.array([1000, 1200, 1350, 1500, 1600, 1750])

# Create the plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1: Line chart with error bars for execution time
ax1.errorbar(
    months, 
    average_execution_time, 
    yerr=execution_std_dev, 
    fmt='-o', 
    color='navy', 
    ecolor='lightcoral', 
    elinewidth=2, 
    capsize=5, 
    capthick=1.5, 
    alpha=0.8,
    label='Avg Execution Time with Variability'
)
ax1.set_title('Algorithm Performance Analysis\nQuantumCompute Innovations', fontsize=14)
ax1.set_xlabel('Month', fontsize=12)
ax1.set_ylabel('Execution Time (ms)', fontsize=12, color='navy')
ax1.set_ylim(120, 200)
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax1.legend(loc='upper right', fontsize=10)
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha='right')

# Plot 2: Bar chart for operations executed
ax2.bar(months, operations_executed, color='teal', alpha=0.7)
ax2.set_title('Operational Throughput\nQuantumCompute Innovations', fontsize=14)
ax2.set_xlabel('Month', fontsize=12)
ax2.set_ylabel('Operations Executed', fontsize=12, color='teal')
ax2.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Automatically adjust the layout for better viewing
plt.tight_layout()

# Display the plot
plt.show()