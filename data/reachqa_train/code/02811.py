import matplotlib.pyplot as plt

# Define the renewable energy data
energy_types = ['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Biomass']
energy_shares = [22, 24, 35, 9, 10]

# Assign distinct colors to each energy type
colors = ['#ffcc00', '#66c2a5', '#8da0cb', '#e78ac3', '#a6d854']

# Create a pie chart
fig, ax = plt.subplots(figsize=(10, 7))

# Highlight the hydropower sector by slightly exploding it
explode = [0, 0, 0.1, 0, 0]

# Plot the pie chart
wedges, texts, autotexts = ax.pie(
    energy_shares,
    labels=energy_types,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    explode=explode,
    shadow=True
)

# Customize the label texts and autotexts for readability
plt.setp(texts, size=10, weight='bold', color='black')
plt.setp(autotexts, size=9, weight='bold', color='white')

# Add a comprehensive title with a line break for enhanced readability
plt.title(
    "Global Distribution of Renewable Energy Production by Type\n"
    "A Step Towards Sustainable Energy Future",
    fontsize=14,
    fontweight='bold',
    pad=20
)

# Add a legend to describe the energy types, located outside the pie chart
ax.legend(
    wedges, energy_types,
    title="Energy Types",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1)
)

# Ensure the pie chart maintains a circular shape
ax.axis('equal')

# Automatically adjust layout to prevent label overlap
plt.tight_layout()

# Display the plot
plt.show()