import matplotlib.pyplot as plt
import numpy as np

# Data preparation
years = np.arange(2010, 2021)
solar_power = np.array([30, 45, 70, 100, 150, 225, 320, 430, 560, 700, 850])
wind_power = np.array([140, 170, 220, 290, 360, 450, 560, 690, 850, 950, 1100])

# Create the plot
plt.figure(figsize=(14, 8))

# Plot solar power generation
plt.plot(years, solar_power, marker='o', linestyle='-', color='#FDB927', linewidth=2, label='Solar Power')

# Plot wind power generation
plt.plot(years, wind_power, marker='^', linestyle='-', color='#0074D9', linewidth=2, label='Wind Power')

# Titles and labels
plt.title('The Rise of Renewable Energy:\nSolar and Wind Power Trends (2010-2020)', fontsize=16, pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Energy Generation (TWh)', fontsize=12)

# Customize the x and y ticks
plt.xticks(years)
plt.yticks(np.arange(0, 1201, 100))

# Add a legend
plt.legend(title='Energy Source', loc='upper left')

# Add annotations for key milestones
plt.annotate('Solar Boom\nBegins', xy=(2014, 150), xytext=(2012, 320),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, color='black')

plt.annotate('Wind Milestone:\n1,000 TWh', xy=(2020, 1100), xytext=(2018, 1000),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, color='black')

# Annotate each data point with its value
for i, (y_solar, y_wind) in enumerate(zip(solar_power, wind_power)):
    plt.text(years[i], y_solar + 20, f'{y_solar}', ha='center', fontsize=9, color='#FDB927')
    plt.text(years[i], y_wind + 20, f'{y_wind}', ha='center', fontsize=9, color='#0074D9')

# Add gridlines for better readability
plt.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()