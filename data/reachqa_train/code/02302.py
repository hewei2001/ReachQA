import matplotlib.pyplot as plt
import numpy as np

# Years of observation
years = np.array([2019, 2020, 2021, 2022, 2023])

# Energy consumption for each vehicle type (in GWh)
cars = np.array([20, 25, 30, 35, 40])
buses = np.array([15, 18, 22, 25, 30])
bikes = np.array([5, 7, 10, 13, 15])

# Create a stacked area chart
fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(years, cars, buses, bikes, labels=['Cars', 'Buses', 'Bikes'], colors=['#FF9999', '#66B2FF', '#99FF99'], alpha=0.8)

# Add a grid
ax.grid(alpha=0.3)

# Set the title and labels, using multi-line for clarity
ax.set_title('The Rise of Electric Vehicles:\nEnergy Consumption Trends in Urban Transport', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Consumption (GWh)', fontsize=14)

# Set the x and y ticks for readability
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 101, 10))

# Add a legend, positioned to minimize data obstruction
ax.legend(loc='upper left', title='Vehicle Types', fontsize=12, title_fontsize=13)

# Annotate the final values for each segment on the plot for emphasis
for y, consumption in zip(years, cars + buses + bikes):
    ax.annotate(f'{consumption} GWh', xy=(y, consumption), xytext=(0, 10), textcoords='offset points', ha='center', fontsize=10, color='black')

# Adjust the layout to avoid overlapping text and elements
plt.tight_layout()

# Display the plot
plt.show()