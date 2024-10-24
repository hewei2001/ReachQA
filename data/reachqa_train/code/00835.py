import matplotlib.pyplot as plt
import numpy as np

# Months of the year
months = np.arange(1, 13)
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Fictional solar energy output data in MWh
solar_output = np.array([350, 380, 420, 500, 550, 600, 
                         580, 560, 480, 400, 370, 330])

# Simulated error margins due to weather variability
error_margins = np.array([20, 25, 30, 35, 25, 20, 
                          15, 18, 28, 30, 25, 22])

# Additional data: Average daily solar radiation in kWh/m²
solar_radiation = np.array([3.0, 3.5, 4.2, 5.5, 6.5, 7.2,
                            6.8, 6.0, 5.0, 4.2, 3.5, 3.1])

# Figure and subplots setup
fig, axs = plt.subplots(1, 2, figsize=(16, 7))

# Subplot 1: Line chart with error bars for solar output
axs[0].errorbar(months, solar_output, yerr=error_margins, fmt='-o', color='royalblue',
                ecolor='coral', elinewidth=2, capsize=5, capthick=2, label='Solar Output (MWh)', alpha=0.8)
axs[0].set_title("Sunshine Valley Solar Farm\nMonthly Energy Output & Weather Variability", 
                 fontsize=14, fontweight='bold', pad=10)
axs[0].set_xlabel("Month", fontsize=11)
axs[0].set_ylabel("Energy Output (MWh)", fontsize=11)
axs[0].set_xticks(months)
axs[0].set_xticklabels(month_names, fontsize=10)
axs[0].grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.6)
axs[0].set_ylim(300, 650)
axs[0].legend(loc='upper right', fontsize=10, frameon=True)

# Annotating the peak month for emphasis
peak_month = 5  # May
axs[0].annotate('Peak Production', xy=(peak_month, solar_output[peak_month - 1]),
                xytext=(peak_month + 0.5, solar_output[peak_month - 1] + 80),
                arrowprops=dict(facecolor='darkgreen', arrowstyle='->', lw=1.5), 
                fontsize=11, color='darkgreen', 
                bbox=dict(facecolor='white', alpha=0.8))

# Subplot 2: Bar chart for solar radiation
axs[1].bar(months, solar_radiation, color='skyblue', edgecolor='darkblue', alpha=0.7,
           yerr=0.2, capsize=5, ecolor='darkblue', label='Solar Radiation (kWh/m²)')

axs[1].set_title("Monthly Average Daily Solar Radiation", fontsize=14, fontweight='bold', pad=10)
axs[1].set_xlabel("Month", fontsize=11)
axs[1].set_ylabel("Solar Radiation (kWh/m²)", fontsize=11)
axs[1].set_xticks(months)
axs[1].set_xticklabels(month_names, fontsize=10)
axs[1].grid(True, which='major', linestyle=':', linewidth=0.7, alpha=0.6)
axs[1].legend(loc='upper right', fontsize=10, frameon=True)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()