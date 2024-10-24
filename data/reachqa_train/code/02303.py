import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# Years of observation
years = np.array([2019, 2020, 2021, 2022, 2023])

# Energy consumption for each vehicle type (in GWh)
cars = np.array([20, 25, 30, 35, 40])
buses = np.array([15, 18, 22, 25, 30])
bikes = np.array([5, 7, 10, 13, 15])

# Calculate total energy consumption
total_consumption = cars + buses + bikes

# Percentage contribution
percent_cars = cars / total_consumption * 100
percent_buses = buses / total_consumption * 100
percent_bikes = bikes / total_consumption * 100

# Create a stacked area chart with additional plot
fig, ax1 = plt.subplots(figsize=(14, 10))

# Plot stacked area chart
ax1.stackplot(years, cars, buses, bikes, labels=['Cars', 'Buses', 'Bikes'],
              colors=['#FF9999', '#66B2FF', '#99FF99'], alpha=0.8)

# Add trend lines with markers
ax1.plot(years, cars, color='#CC0000', linewidth=2, linestyle='--', marker='o', label='Cars Trend')
ax1.plot(years, buses, color='#0033CC', linewidth=2, linestyle='--', marker='o', label='Buses Trend')
ax1.plot(years, bikes, color='#009933', linewidth=2, linestyle='--', marker='o', label='Bikes Trend')

# Set title and labels
ax1.set_title('The Rise of Electric Vehicles:\nEnergy Consumption Trends in Urban Transport', fontsize=18, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Energy Consumption (GWh)', fontsize=14)

# Add grid lines
ax1.grid(alpha=0.3, linestyle='--')

# Set ticks and format y-ticks to show as GWh
ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, 101, 10))
ax1.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x:.0f} GWh'))

# Add a secondary y-axis for percentage contribution
ax2 = ax1.twinx()
ax2.plot(years, percent_cars, color='#FF6666', linestyle=':', marker='x', linewidth=1.5, label='Cars %')
ax2.plot(years, percent_buses, color='#3399FF', linestyle=':', marker='x', linewidth=1.5, label='Buses %')
ax2.plot(years, percent_bikes, color='#66FF66', linestyle=':', marker='x', linewidth=1.5, label='Bikes %')
ax2.set_ylabel('Percentage of Total Consumption (%)', fontsize=14)
ax2.set_yticks(np.arange(0, 101, 10))

# Combine and place the legend to minimize overlap
fig.legend(loc='upper center', ncol=3, fontsize=12, bbox_to_anchor=(0.5, -0.05), title='Legend', title_fontsize=13)

# Annotate the final values for each segment on the plot
for y, consumption in zip(years, total_consumption):
    ax1.annotate(f'{consumption} GWh', xy=(y, consumption), xytext=(0, 10),
                 textcoords='offset points', ha='center', fontsize=10, color='black')

# Adjust the layout
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Display the plot
plt.show()