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

# Create a figure
fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot the solar energy production
color = 'tab:orange'
ax1.set_title("Effect of Sunshine Duration on Solar Energy Production\nin Solis City - Year 2023", fontsize=16, fontweight='bold', color='darkblue')
ax1.set_xlabel("Months", fontsize=12)
ax1.set_ylabel("Solar Energy Production (MWh)", color=color, fontsize=12)
ax1.plot(months, solar_production, marker='o', color=color, linestyle='-', linewidth=2, label="Solar Production")
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(axis='x', linestyle='--', alpha=0.7)

# Annotate significant points
for i, txt in enumerate(solar_production):
    if i in [3, 6, 11]:  # Annotate select months for emphasis
        ax1.annotate(f'{txt} MWh', (months[i], solar_production[i]), textcoords="offset points", xytext=(-10,10), ha='center', color=color)

# Create a second y-axis for sunshine duration
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel("Sunshine Duration (Hours)", color=color, fontsize=12)
ax2.plot(months, sunshine_hours, marker='s', linestyle='--', color=color, linewidth=2, label="Sunshine Duration")
ax2.tick_params(axis='y', labelcolor=color)

# Annotate significant points
for i, txt in enumerate(sunshine_hours):
    if i in [3, 6, 11]:  # Annotate select months for emphasis
        ax2.annotate(f'{txt} hrs', (months[i], sunshine_hours[i]), textcoords="offset points", xytext=(0,-15), ha='center', color=color)

# Adding a legend
fig.legend(loc='upper right', bbox_to_anchor=(0.88, 0.88), title='Metrics', fontsize=10)

# Adjust layout to fit the title and labels
plt.tight_layout()

# Display the chart
plt.show()