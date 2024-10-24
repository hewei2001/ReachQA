import matplotlib.pyplot as plt
import numpy as np

# Define the decades and power generation data for each renewable source
decades = np.arange(1980, 2030, 10)
solar_power = [5, 10, 40, 100, 250]  # Exponential growth in solar power generation
wind_power = [10, 20, 50, 150, 400]  # Significant increase in wind power
hydro_power = [100, 110, 120, 130, 140]  # Steady growth for hydroelectric power
geothermal_power = [15, 18, 25, 35, 50]  # Gradual increase in geothermal power

# Stack the data to create a stacked area chart
renewable_data = np.vstack([solar_power, wind_power, hydro_power, geothermal_power])

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the stacked area chart with transparency
ax.stackplot(decades, renewable_data, labels=['Solar', 'Wind', 'Hydro', 'Geothermal'],
             colors=['#ffd700', '#1e90ff', '#32cd32', '#ff6347'], alpha=0.8)

# Add title and labels
ax.set_title('The Rise of Renewable Energy:\nA Decadal Surge in Power Generation', fontsize=16, fontweight='bold')
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Power Generation (TWh)', fontsize=12)

# Customize x-axis labels
plt.xticks(decades, fontsize=10)
plt.yticks(fontsize=10)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Annotate key points to provide additional insights
for i, (decade, solar, wind, hydro, geo) in enumerate(zip(decades, solar_power, wind_power, hydro_power, geothermal_power)):
    ax.annotate(f'{solar} TWh', xy=(decade, solar), textcoords='offset points', xytext=(-10, 10), ha='center', fontsize=9, color='#ffd700')
    ax.annotate(f'{wind} TWh', xy=(decade, wind), textcoords='offset points', xytext=(-10, 20), ha='center', fontsize=9, color='#1e90ff')
    ax.annotate(f'{hydro} TWh', xy=(decade, hydro), textcoords='offset points', xytext=(-10, 30), ha='center', fontsize=9, color='#32cd32')
    ax.annotate(f'{geo} TWh', xy=(decade, geo), textcoords='offset points', xytext=(-10, 40), ha='center', fontsize=9, color='#ff6347')

# Add legend
ax.legend(loc='upper left', title='Renewable Sources', fontsize=10, title_fontsize='13')

# Adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()