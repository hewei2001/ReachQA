import matplotlib.pyplot as plt
import numpy as np

# Define the months and corresponding solar energy production data for 2023
months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
energy_production_2023 = np.array([240, 260, 320, 400, 450, 470, 480, 470, 420, 350, 300, 250])

# Define historical average energy production data for comparison
historical_average = np.array([230, 250, 310, 390, 440, 460, 470, 460, 410, 340, 290, 240])

# Create the plot with a specific figure size
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the 2023 energy production data as a line chart
ax1.plot(months, energy_production_2023, marker='o', linestyle='-', color='#2ecc71', linewidth=2, label='2023 Solar Energy Production')

# Overlay the historical average as a bar chart
ax1.bar(months, historical_average, color='#3498db', alpha=0.6, label='Historical Average (2018-2022)')

# Add title and labels with split title for better readability
ax1.set_title("Comparative Monthly Solar Energy Production\nGreenVille (2023 vs. 2018-2022 Average)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Month", fontsize=12)
ax1.set_ylabel("Energy Production (MWh)", fontsize=12)

# Add legends for both plots
ax1.legend(loc='upper left', fontsize=12)

# Enable grid for better readability
ax1.grid(True, linestyle='--', alpha=0.7)

# Annotate significant production points
ax1.annotate('Peak Production 2023', xy=('Jul', 480), xytext=('Aug', 520),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, ha='center', color='red')
ax1.annotate('Lowest Production 2023', xy=('Jan', 240), xytext=('Feb', 150),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, ha='center', color='red')

# Adjust the layout to prevent overlap and make all elements visible
plt.tight_layout()

# Display the chart
plt.show()