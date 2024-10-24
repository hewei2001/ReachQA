import matplotlib.pyplot as plt
import numpy as np

# Define the decades for the x-axis
decades = np.arange(1920, 2030, 10)

# Artificial data representing speed improvements in different sectors
computing_speed = [0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]
internet_speed = [0.05, 0.1, 0.3, 0.6, 1.5, 10, 30, 100, 300, 1000, 10000]
transport_speed = [60, 70, 85, 100, 150, 180, 200, 250, 300, 400, 500]

# Standard deviations (errors) for each sector
computing_error = [0.0005, 0.005, 0.02, 0.05, 1, 5, 50, 300, 1500, 8000, 50000]
internet_error = [0.02, 0.05, 0.1, 0.2, 0.5, 3, 8, 15, 30, 50, 300]
transport_error = [5, 5, 10, 10, 15, 10, 5, 20, 20, 30, 25]

# Create the line chart with error bars
fig, ax = plt.subplots(figsize=(12, 8))

# Plot lines with error bars for each technology
ax.errorbar(decades, computing_speed, yerr=computing_error, label='Computing Speed (FLOPS)', 
            fmt='-o', capsize=5, color='blue', linewidth=2, alpha=0.8)

ax.errorbar(decades, internet_speed, yerr=internet_error, label='Internet Speed (Mbps)', 
            fmt='-s', capsize=5, color='green', linewidth=2, alpha=0.8)

ax.errorbar(decades, transport_speed, yerr=transport_error, label='Transport Speed (km/h)', 
            fmt='-^', capsize=5, color='red', linewidth=2, alpha=0.8)

# Add titles and labels
ax.set_title("A Century of Innovations:\nUnraveling the Speed of Technological Evolution", fontsize=16, fontweight='bold')
ax.set_xlabel("Decade", fontsize=12)
ax.set_ylabel("Speed (in log scale for different units)", fontsize=12)

# Use log scale for y-axis to accommodate wide range
ax.set_yscale('log')

# Add a legend to the plot
ax.legend(loc='upper left', fontsize=10)

# Customize gridlines
ax.grid(True, which="both", linestyle='--', linewidth=0.5, alpha=0.7)

# Annotate a notable leap year in each field
ax.annotate('Internet Boom', xy=(2000, 300), xytext=(1980, 800),
            arrowprops=dict(facecolor='gray', shrink=0.05),
            fontsize=10, fontweight='bold', color='green')

ax.annotate('Computing Breakthrough', xy=(2010, 1000000), xytext=(1990, 2000000),
            arrowprops=dict(facecolor='gray', shrink=0.05),
            fontsize=10, fontweight='bold', color='blue')

ax.annotate('Transport Revolution', xy=(2020, 500), xytext=(2000, 1500),
            arrowprops=dict(facecolor='gray', shrink=0.05),
            fontsize=10, fontweight='bold', color='red')

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()