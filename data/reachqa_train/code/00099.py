import matplotlib.pyplot as plt

# Data for the chart
transport_modes = ['Hyperloop', 'Electric Cars', 'Autonomous Drones', 'Maglev Trains', 'Bicycles', 'Electric Scooters', 'Walking']
usage_percentage = [25, 20, 15, 15, 10, 8, 7]
colors = ['#ff5733', '#33c4ff', '#ff33e1', '#33ff57', '#337fff', '#ff9f33', '#a633ff']
explode = (0.1, 0, 0.1, 0, 0, 0, 0)  # emphasize Hyperloop and Autonomous Drones

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

# Pie Chart
wedges, texts, autotexts = ax.pie(
    usage_percentage, 
    colors=colors, 
    labels=transport_modes, 
    autopct='%1.1f%%', 
    startangle=140, 
    explode=explode,
    wedgeprops=dict(edgecolor='white', linewidth=2),
    shadow=True
)

# Style the text
plt.setp(autotexts, size=10, weight="bold", color='black')
plt.setp(texts, size=11, weight='bold')

# Add a legend
ax.legend(wedges, transport_modes, title="Transport Modes", loc="center left", bbox_to_anchor=(0.9, 0, 0.5, 1))

# Set the title
ax.set_title("2025 Vision:\nThe Future of Transport Modes", fontsize=16, weight='bold', pad=20)

# Automatically adjust the layout to prevent label overlap
plt.tight_layout()

# Display the plot
plt.show()