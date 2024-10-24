import matplotlib.pyplot as plt

# Define the data for each continent
continents = ['Europe', 'North America', 'South America', 'Asia', 'Africa', 'Oceania']
consumption_percentages = [35, 20, 15, 18, 8, 4]

# Assign distinct colors to each segment of the pie chart
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Create a figure and a single subplot
fig, ax = plt.subplots(figsize=(9, 9))

# Plot the pie chart
wedges, texts, autotexts = ax.pie(
    consumption_percentages,
    labels=continents,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops=dict(edgecolor='w'),
    explode=[0.1, 0, 0, 0, 0, 0],
    shadow=True
)

# Equal aspect ratio ensures the pie is drawn as a circle
ax.axis('equal')

# Customize text appearance
plt.setp(autotexts, size=10, weight='bold', color='black')
plt.setp(texts, size=11)

# Add title with line break for readability
plt.title(
    "Brewed Around the Globe:\nCoffee Consumption by Continent",
    fontsize=16, weight='bold', color='darkgreen', pad=20
)

# Add a legend outside the pie to describe each segment
ax.legend(
    wedges, continents,
    title="Continents",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1)
)

# Automatically adjust subplot parameters for a cleaner layout
plt.tight_layout()

# Display the pie chart
plt.show()