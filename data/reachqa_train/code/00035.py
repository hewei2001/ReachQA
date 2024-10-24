import matplotlib.pyplot as plt

# Define the categories and their corresponding percentage values
activities = ['Heating & Cooling', 'Water Heating', 'Lighting', 'Appliances', 'Electronics', 'Other']
percentages = [40, 20, 10, 15, 10, 5]

# Define a color palette
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create a horizontal stacked bar chart
ax.barh(activities, percentages, color=colors)

# Add percentage labels inside the bars
for i, (activity, percentage) in enumerate(zip(activities, percentages)):
    ax.text(percentage / 2, i, f'{percentage}%', va='center', ha='center', color='black', fontsize=10)

# Set title and labels
ax.set_title('Household Energy Consumption by Activity', fontsize=16, pad=20)
ax.set_xlabel('Percentage of Total Energy (%)', fontsize=12)

# Set x-axis range to ensure it covers 0-100%
ax.set_xlim(0, 100)

# Improve layout spacing to avoid overlapping
plt.tight_layout()

# Display the plot
plt.show()