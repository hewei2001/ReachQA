import matplotlib.pyplot as plt

# Define device types and their energy consumption percentages
device_types = ['Heating System', 'Refrigerator', 'Lighting', 'Entertainment System', 'Kitchen Appliances']
energy_consumption_percentages = [40, 20, 15, 15, 10]

# Define time of day energy consumption data
time_of_day = ['Morning', 'Afternoon', 'Evening', 'Night']
time_consumption_percentages = [30, 25, 35, 10]

# Create a figure with two subplots
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))

# Horizontal bar chart for device type energy consumption
ax1 = axs[0]
bars = ax1.barh(device_types, energy_consumption_percentages, color=['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FFC300'])

# Add data labels to the bars
for bar, percentage in zip(bars, energy_consumption_percentages):
    ax1.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, f'{percentage}%', 
             va='center', ha='left', fontsize=10, color='black')

# Set titles and labels for the first subplot
ax1.set_title('Energy Consumption by Device Type\nin an EcoSmart Home (2050)', fontsize=14, pad=10)
ax1.set_xlabel('Percentage of Total Energy Consumption (%)', fontsize=10)
ax1.set_xlim(0, 50)
ax1.xaxis.grid(True, linestyle='--', alpha=0.7)

# Pie chart for time-of-day energy consumption
ax2 = axs[1]
wedges, texts, autotexts = ax2.pie(time_consumption_percentages, labels=time_of_day, autopct='%1.1f%%',
                                   startangle=90, colors=['#8C564B', '#E377C2', '#7F7F7F', '#BCBD22'],
                                   wedgeprops=dict(width=0.3), pctdistance=0.85)

# Set a title for the pie chart subplot
ax2.set_title('Energy Consumption by Time of Day', fontsize=14, pad=10)

# Adjust legend and text properties for clarity
plt.setp(autotexts, size=10, weight='bold', color='white')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()