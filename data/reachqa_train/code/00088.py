import matplotlib.pyplot as plt
import numpy as np

# Data: Projected Energy Mix in 2050
energy_sources = ['Solar', 'Wind', 'Hydropower', 'Nuclear', 'Coal', 'Natural Gas', 'Other Renewables']
percentages_2050 = [25, 20, 15, 10, 10, 15, 5]

# Historical Data: Energy Mix in 2020 (for comparison)
percentages_2020 = [3, 6, 15, 10, 27, 34, 5]

# Create a figure with two subplots: one for the bar chart and one for the pie chart
fig, axs = plt.subplots(1, 2, figsize=(16, 8), gridspec_kw={'width_ratios': [1.5, 1]})

# Plotting the percentage bar chart for 2050
bars = axs[0].barh(energy_sources, percentages_2050, color=['#FFD700', '#1E90FF', '#32CD32', '#FFA07A', '#A9A9A9', '#FF4500', '#9370DB'])
axs[0].xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)
axs[0].bar_label(bars, fmt='%.1f%%')
axs[0].set_title('Projected Global Energy Source Composition\nfor Sustainability in 2050', fontsize=16, pad=20)
axs[0].set_xlabel('Percentage of Total Energy Consumption', fontsize=12)
axs[0].set_xlim(0, 30)
axs[0].set_yticklabels(energy_sources, fontsize=11)

# Plotting the pie chart for 2020
axs[1].pie(percentages_2020, labels=energy_sources, autopct='%1.1f%%',
           startangle=90, colors=['#FFD700', '#1E90FF', '#32CD32', '#FFA07A', '#A9A9A9', '#FF4500', '#9370DB'])
axs[1].set_title('Energy Source Composition in 2020', fontsize=14, pad=20)

# Ensure the layout is adjusted
plt.tight_layout()

# Show the plot
plt.show()