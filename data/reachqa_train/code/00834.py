import matplotlib.pyplot as plt
import numpy as np

# Months of the year
months = np.arange(1, 13)

# Fictional solar energy output data in MWh
solar_output = np.array([350, 380, 420, 500, 550, 600, 580, 560, 480, 400, 370, 330])

# Simulated error margins due to weather variability
error_margins = np.array([20, 25, 30, 35, 25, 20, 15, 18, 28, 30, 25, 22])

# Plotting the line chart with error bars
plt.figure(figsize=(12, 7))
plt.errorbar(months, solar_output, yerr=error_margins, fmt='-o', color='royalblue',
             ecolor='coral', elinewidth=2, capsize=5, capthick=2, label='Solar Output (MWh)', alpha=0.8)

# Titles and labels
plt.title("Sunshine Valley Solar Farm\nMonthly Energy Output & Weather Variability", 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Energy Output (MWh)", fontsize=12)

# Customizing x-axis ticks to show month names
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.xticks(months, month_names, fontsize=11)

# Adding grid for better readability
plt.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.6)

# Annotating the peak month for emphasis
peak_month = 5  # May
plt.annotate('Peak Production', xy=(peak_month, solar_output[peak_month - 1]),
             xytext=(peak_month + 0.5, solar_output[peak_month - 1] + 80),
             arrowprops=dict(facecolor='darkgreen', arrowstyle='->', lw=1.5), 
             fontsize=12, color='darkgreen', bbox=dict(facecolor='white', alpha=0.8))

# Adjusting y-axis to ensure visibility of all error margins
plt.ylim(300, 650)

# Legend
plt.legend(loc='upper right', fontsize=11, frameon=True)

# Adjusting layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()