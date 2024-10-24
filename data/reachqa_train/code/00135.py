import matplotlib.pyplot as plt
import numpy as np

# Define decades for x-axis
decades = np.arange(1920, 2030, 10)

# Speed improvements (original data)
computing_speed = [0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]
internet_speed = [0.05, 0.1, 0.3, 0.6, 1.5, 10, 30, 100, 300, 1000, 10000]
transport_speed = [60, 70, 85, 100, 150, 180, 200, 250, 300, 400, 500]

# Standard deviations (errors) for each sector
computing_error = [0.0005, 0.005, 0.02, 0.05, 1, 5, 50, 300, 1500, 8000, 50000]
internet_error = [0.02, 0.05, 0.1, 0.2, 0.5, 3, 8, 15, 30, 50, 300]
transport_error = [5, 5, 10, 10, 15, 10, 5, 20, 20, 30, 25]

# Additional data for bar plot (energy consumption per sector)
energy_consumption = {
    "Computing": [1, 5, 20, 60, 120, 200, 300, 450, 600, 700, 850],
    "Internet": [0.5, 1, 3, 7, 15, 30, 50, 80, 120, 160, 200],
    "Transport": [100, 110, 130, 150, 180, 210, 250, 300, 350, 400, 450]
}

# Setup the subplot layout
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Plotting the original line chart with error bars
ax1.errorbar(decades, computing_speed, yerr=computing_error, label='Computing Speed (FLOPS)', 
             fmt='-o', capsize=5, color='blue', linewidth=2, alpha=0.8)
ax1.errorbar(decades, internet_speed, yerr=internet_error, label='Internet Speed (Mbps)', 
             fmt='-s', capsize=5, color='green', linewidth=2, alpha=0.8)
ax1.errorbar(decades, transport_speed, yerr=transport_error, label='Transport Speed (km/h)', 
             fmt='-^', capsize=5, color='red', linewidth=2, alpha=0.8)

ax1.set_title("A Century of Innovations:\nUnraveling the Speed of Technological Evolution", fontsize=16, fontweight='bold')
ax1.set_xlabel("Decade", fontsize=12)
ax1.set_ylabel("Speed (log scale)", fontsize=12)
ax1.set_yscale('log')
ax1.legend(loc='upper left', fontsize=10)
ax1.grid(True, which="both", linestyle='--', linewidth=0.5, alpha=0.7)

# Annotations
ax1.annotate('Internet Boom', xy=(2000, 300), xytext=(1980, 800),
             arrowprops=dict(facecolor='gray', shrink=0.05),
             fontsize=10, fontweight='bold', color='green')
ax1.annotate('Computing Breakthrough', xy=(2010, 1000000), xytext=(1990, 2000000),
             arrowprops=dict(facecolor='gray', shrink=0.05),
             fontsize=10, fontweight='bold', color='blue')
ax1.annotate('Transport Revolution', xy=(2020, 500), xytext=(2000, 1500),
             arrowprops=dict(facecolor='gray', shrink=0.05),
             fontsize=10, fontweight='bold', color='red')

# Plotting the bar chart for energy consumption
categories = list(energy_consumption.keys())
bar_width = 2

for i, category in enumerate(categories):
    ax2.bar(decades + i*bar_width, energy_consumption[category], width=bar_width, label=f'{category} Energy (Units)', alpha=0.7)

ax2.set_title("Energy Consumption Trends\nAcross Different Technologies", fontsize=16, fontweight='bold')
ax2.set_xlabel("Decade", fontsize=12)
ax2.set_ylabel("Energy Consumption (Arbitrary Units)", fontsize=12)
ax2.legend(loc='upper left', fontsize=10)
ax2.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Improve layout
plt.tight_layout()

# Display the plots
plt.show()