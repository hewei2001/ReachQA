import matplotlib.pyplot as plt
import numpy as np

# Define the types of smart devices and the years
devices = ["Smart Lights", "Smart Thermostats", "Smart Security", "Smart Appliances"]
years = np.arange(2010, 2021)

# Define the artificial data for each smart device adoption rate
adoption_lights = [2, 4, 7, 10, 14, 20, 28, 38, 50, 65, 80]
adoption_thermostats = [1, 3, 5, 8, 12, 18, 25, 33, 44, 58, 73]
adoption_security = [1, 2, 4, 6, 9, 14, 21, 29, 38, 50, 65]
adoption_appliances = [0, 1, 2, 4, 7, 12, 18, 26, 35, 47, 60]

# Calculate total adoption rate for a line chart
total_adoption = np.array(adoption_lights) + np.array(adoption_thermostats) + \
                 np.array(adoption_security) + np.array(adoption_appliances)

# Calculate year-over-year growth rate for a scatter plot
growth_rates = {
    "Smart Lights": np.diff(adoption_lights) / np.array(adoption_lights[:-1]) * 100,
    "Smart Thermostats": np.diff(adoption_thermostats) / np.array(adoption_thermostats[:-1]) * 100,
    "Smart Security": np.diff(adoption_security) / np.array(adoption_security[:-1]) * 100,
    "Smart Appliances": np.diff(adoption_appliances) / np.array(adoption_appliances[:-1]) * 100
}
growth_years = years[1:]

# Create a figure and axis layout with 2 subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# Plot the stacked area chart
ax1.stackplot(years, adoption_lights, adoption_thermostats, adoption_security, adoption_appliances,
              labels=devices,
              colors=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99'], alpha=0.8)
ax1.set_title("Evolution of Household\nSmart Technology Adoption (2010-2020)", fontsize=16, fontweight='bold')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Adoption Rate (%)", fontsize=12)
ax1.set_xlim(years[0], years[-1])
ax1.set_xticks(years)
ax1.tick_params(axis='x', rotation=45)
ax1.legend(loc='upper left', fontsize=10, title='Smart Devices')
ax1.grid(visible=True, linestyle='--', alpha=0.5)

# Plot a line chart of total adoption rate
ax2.plot(years, total_adoption, marker='o', linestyle='-', color='#3333FF', label="Total Adoption")
ax2.set_title("Overall Smart Device Adoption Trend", fontsize=14, fontweight='bold')
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Total Adoption Rate (%)", fontsize=12)
ax2.set_xlim(years[0], years[-1])
ax2.set_xticks(years)
ax2.tick_params(axis='x', rotation=45)
ax2.grid(visible=True, linestyle='--', alpha=0.5)

# Plot year-over-year growth rates as scatter plot
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']
for idx, (device, growth) in enumerate(growth_rates.items()):
    ax2.scatter(growth_years, growth, color=colors[idx], label=f"{device} Growth", alpha=0.6, edgecolor='k')

ax2.legend(loc='upper left', fontsize=10)
plt.tight_layout()
plt.show()