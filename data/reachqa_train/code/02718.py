import matplotlib.pyplot as plt
import numpy as np

# Decades from the 1980s to the 2020s
decades = ['1980s', '1990s', '2000s', '2010s', '2020s']

# Data for renewable energy adoption in gigawatts (GW)
solar_power = [2, 4, 18, 200, 600]   # Rapid growth especially in recent decades
wind_power = [10, 25, 100, 400, 700]  # Consistent increase over time
hydroelectric_power = [500, 600, 750, 850, 900]  # Gradual and steady growth

# Initialize the plot
plt.figure(figsize=(12, 7))

# Plot each energy source
plt.plot(decades, solar_power, marker='o', linestyle='-', color='gold', linewidth=2.5, label='Solar Power')
plt.plot(decades, wind_power, marker='s', linestyle='-', color='skyblue', linewidth=2.5, label='Wind Power')
plt.plot(decades, hydroelectric_power, marker='^', linestyle='-', color='seagreen', linewidth=2.5, label='Hydroelectric Power')

# Title and labels with adjusted line breaks for clarity
plt.title("Renewable Energy Adoption Over the Decades\nFrom the 1980s to the 2020s", fontsize=16, fontweight='bold')
plt.xlabel("Decade", fontsize=12)
plt.ylabel("Energy Production (Gigawatts)", fontsize=12)

# Adding grid for better readability
plt.grid(True, linestyle='--', alpha=0.7)

# Adding legend for clarity
plt.legend(title='Energy Source', loc='upper left', fontsize=11)

# Annotate data points to highlight the growth
for i, (solar, wind, hydro) in enumerate(zip(solar_power, wind_power, hydroelectric_power)):
    plt.text(i, solar + 30, f"{solar} GW", ha='center', fontsize=10)
    plt.text(i, wind + 30, f"{wind} GW", ha='center', fontsize=10)
    plt.text(i, hydro + 30, f"{hydro} GW", ha='center', fontsize=10)

# Adjust layout to ensure no overlap
plt.tight_layout()

# Display the plot
plt.show()