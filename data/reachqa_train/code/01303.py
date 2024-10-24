import matplotlib.pyplot as plt

# Device types and their corresponding internet usage shares in percentage
device_types = ['Mobile Phones', 'Laptops & Desktops', 'Tablets', 'Smart TVs', 'Wearables & Other Devices']
usage_percentages = [45, 30, 10, 8, 7]

# Color scheme for each device type
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Highlight the Mobile Phones slice by using explode
explode = (0.1, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    usage_percentages,
    explode=explode,
    labels=device_types,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    pctdistance=0.85,
    shadow=True
)

# Format percentage text inside the slices
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

# Draw a circle at the center to convert the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Ensure the pie is drawn as a circle by setting the aspect ratio
ax.axis('equal')

# Add title with line breaks for better readability
plt.title(
    "Digital Connections 2023:\nA Look at Global Internet Usage by Device Type",
    fontsize=16,
    fontweight='bold',
    pad=20
)

# Add a legend to the side of the pie chart
ax.legend(
    wedges,
    device_types,
    title="Device Types",
    loc='center left',
    bbox_to_anchor=(1, 0, 0.5, 1)
)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()