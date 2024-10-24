import matplotlib.pyplot as plt
import numpy as np

# Define the months
months = np.array([
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
])

# Monthly solar energy production in MWh
solar_production = np.array([280, 320, 410, 500, 620, 700, 720, 680, 610, 520, 400, 300])

# Monthly sunshine duration in hours
sunshine_hours = np.array([160, 180, 210, 230, 270, 300, 310, 290, 260, 220, 190, 170])

# Construct synthetic data for average monthly temperature (°C)
average_temperature = np.array([5, 7, 10, 15, 20, 25, 28, 27, 22, 16, 10, 6])

# Create a figure with two subplots
fig, (ax1, ax3) = plt.subplots(1, 2, figsize=(18, 7), gridspec_kw={'width_ratios': [2, 1]})

# Plot the solar energy production and sunshine duration
color1, color2 = 'tab:orange', 'tab:blue'
ax1.set_title("Effect of Sunshine Duration on Solar Energy Production\nin Solis City - Year 2023", fontsize=14, fontweight='bold', color='darkblue')
ax1.set_xlabel("Months", fontsize=12)
ax1.set_ylabel("Solar Energy Production (MWh)", color=color1, fontsize=12)
ax1.plot(months, solar_production, marker='o', color=color1, linestyle='-', linewidth=2, label="Solar Production")
ax1.tick_params(axis='y', labelcolor=color1)
ax1.grid(axis='x', linestyle='--', alpha=0.7)

# Annotate significant points for solar production
for i in [3, 6, 11]:
    ax1.annotate(f'{solar_production[i]} MWh', (months[i], solar_production[i]),
                 textcoords="offset points", xytext=(-10,10), ha='center', color=color1)

# Secondary y-axis for sunshine duration
ax2 = ax1.twinx()
ax2.set_ylabel("Sunshine Duration (Hours)", color=color2, fontsize=12)
ax2.plot(months, sunshine_hours, marker='s', linestyle='--', color=color2, linewidth=2, label="Sunshine Duration")
ax2.tick_params(axis='y', labelcolor=color2)

# Annotate significant points for sunshine hours
for i in [3, 6, 11]:
    ax2.annotate(f'{sunshine_hours[i]} hrs', (months[i], sunshine_hours[i]),
                 textcoords="offset points", xytext=(0,-15), ha='center', color=color2)

# Additional Subplot: Bar chart for average monthly temperature
ax3.set_title("Average Monthly Temperature\nin Solis City - Year 2023", fontsize=14, color='darkgreen')
ax3.set_xlabel("Months", fontsize=12)
ax3.set_ylabel("Average Temperature (°C)", fontsize=12)
bars = ax3.bar(months, average_temperature, color='tab:green', alpha=0.7)

# Annotate temperatures
for bar, temp in zip(bars, average_temperature):
    ax3.annotate(f'{temp}°C', xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                 xytext=(0, 3), textcoords='offset points', ha='center', color='black')

# Adding a legend for the line plots
fig.legend(loc='upper right', bbox_to_anchor=(0.85, 0.95), title='Metrics', fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the charts
plt.show()