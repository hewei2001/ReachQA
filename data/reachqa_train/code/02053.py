import matplotlib.pyplot as plt

# Define device types and their energy consumption as a percentage of total energy used in the EcoSmart home
device_types = ['Heating System', 'Refrigerator', 'Lighting', 'Entertainment System', 'Kitchen Appliances']
energy_consumption_percentages = [40, 20, 15, 15, 10]

# Create a figure and axis for a horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 7))

# Plot the horizontal bar chart
bars = ax.barh(device_types, energy_consumption_percentages, color=['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FFC300'])

# Add data labels directly on the bars
for bar, percentage in zip(bars, energy_consumption_percentages):
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, f'{percentage}%', 
            va='center', ha='left', fontsize=12, color='black')

# Set the title and labels with line breaks if necessary for clarity
ax.set_title('Energy Consumption by Device Type\nin an EcoSmart Home (2050)', fontsize=16, pad=20)
ax.set_xlabel('Percentage of Total Energy Consumption (%)', fontsize=12)
ax.set_xlim(0, 50)  # Set the x-axis limit to visualize percentages clearly

# Customize grid and layout for a clean look
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust the plot to ensure everything fits well
plt.tight_layout()

# Display the plot
plt.show()