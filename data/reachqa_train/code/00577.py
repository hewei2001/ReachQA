import matplotlib.pyplot as plt
import numpy as np

# Define the months and corresponding solar energy production data
months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
energy_production = np.array([240, 260, 320, 400, 450, 470, 480, 470, 420, 350, 300, 250])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the energy production line with markers and customized styles
ax.plot(months, energy_production, marker='o', linestyle='-', color='#2ecc71', linewidth=2, label='Solar Energy Production')

# Add title and labels
ax.set_title("Monthly Solar Energy Production\nin GreenVille (2023)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Month", fontsize=12)
ax.set_ylabel("Energy Production (MWh)", fontsize=12)

# Add a legend
ax.legend(loc='upper right', fontsize=12)

# Enable grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Annotate significant production points: peak and lowest
ax.annotate('Peak Production', xy=('Jul', 480), xytext=('Aug', 500),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, ha='center', color='red')
ax.annotate('Lowest Production', xy=('Jan', 240), xytext=('Feb', 150),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, ha='center', color='red')

# Adjust the layout to prevent overlap and make all elements visible
plt.tight_layout()

# Display the chart
plt.show()