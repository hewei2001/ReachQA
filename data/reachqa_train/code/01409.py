import matplotlib.pyplot as plt
import numpy as np

# Days of the week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Energy consumption data for each device category in kWh over the week
lighting = [3.2, 3.0, 3.1, 3.3, 3.0, 2.9, 3.1]
heating = [5.5, 5.2, 5.3, 5.8, 6.0, 6.2, 5.9]
entertainment = [2.0, 2.1, 2.0, 2.2, 2.1, 2.3, 2.2]
kitchen_appliances = [4.5, 4.8, 4.6, 5.0, 4.9, 5.1, 4.7]

# Setup data for stacked bar plot
data = np.array([lighting, heating, entertainment, kitchen_appliances])
categories = ['Lighting', 'Heating', 'Entertainment', 'Kitchen Appliances']
colors = ['#FFDD44', '#FF4D4D', '#4DA6FF', '#85E085']

# Plot configuration
fig, ax = plt.subplots(figsize=(12, 7))

# Plot each category's bar
bottom = np.zeros(len(days))
for i, category_data in enumerate(data):
    ax.bar(days, category_data, label=categories[i], color=colors[i], bottom=bottom, alpha=0.85)
    bottom += category_data

# Titles and labels
ax.set_title("Smart Home Energy Consumption:\nA Weekly Overview", fontsize=16, fontweight='bold')
ax.set_xlabel("Days of the Week", fontsize=12)
ax.set_ylabel("Energy Consumption (kWh)", fontsize=12)

# Add a legend and improve layout
ax.legend(title='Device Categories', loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2, frameon=False)
plt.xticks(rotation=30, ha='right')  # Rotate x-axis labels for better visibility

# Adding grid for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout automatically
plt.tight_layout()

# Show the plot
plt.show()