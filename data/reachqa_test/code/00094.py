import matplotlib.pyplot as plt
import numpy as np

# Define the years for the analysis
years = np.arange(2025, 2036)

# Data for eco-friendly transportation modes (in thousands of users)
bicycles = np.array([20, 25, 35, 50, 70, 90, 110, 135, 160, 185, 200])
e_scooters = np.array([10, 15, 20, 30, 50, 70, 90, 110, 130, 150, 170])
e_cars = np.array([5, 10, 15, 25, 40, 60, 85, 110, 135, 160, 190])
walking = np.array([30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])

# Calculate the average annual growth rates
modes = ['Bicycles', 'E-Scooters', 'E-Cars', 'Walking']
mode_data = [bicycles, e_scooters, e_cars, walking]
growth_rates = [(data[-1] - data[0]) / data[0] * 100 / (len(years) - 1) for data in mode_data]

# Prepare the figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(15, 7))

# Stacked area chart
axs[0].stackplot(years, mode_data, labels=modes, colors=['#FF6347', '#8A2BE2', '#3CB371', '#FFD700'], alpha=0.8)
axs[0].set_title("EcoMetropolis Green Transit Revolution\n(2025-2035)", fontsize=16, weight='bold')
axs[0].set_xlabel("Year", fontsize=12)
axs[0].set_ylabel("Number of Users (in thousands)", fontsize=12)
axs[0].tick_params(axis='x', rotation=45, labelsize=10)
axs[0].tick_params(axis='y', labelsize=10)
axs[0].grid(True, linestyle='--', alpha=0.6)
axs[0].legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Transport Modes', fontsize=10, title_fontsize='13')

# Annotating significant events
axs[0].annotate('E-Cars boom', xy=(2030, 250), xytext=(2028, 320),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9)
axs[0].annotate('E-Scooters surge', xy=(2027, 135), xytext=(2025, 200),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9)

# Bar chart for average annual growth rate
axs[1].bar(modes, growth_rates, color=['#FF6347', '#8A2BE2', '#3CB371', '#FFD700'])
axs[1].set_title("Average Annual Growth Rate\n(2025-2035)", fontsize=16, weight='bold')
axs[1].set_ylabel("Growth Rate (%)", fontsize=12)
axs[1].tick_params(axis='x', labelsize=12)
axs[1].tick_params(axis='y', labelsize=10)
axs[1].grid(True, linestyle='--', alpha=0.6)

# Adjust layout to prevent clipping
plt.tight_layout()

# Show the plots
plt.show()