import matplotlib.pyplot as plt

# Define the data for the pie chart
continents = ['Africa', 'Antarctica', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']
initiatives_percentage = [15, 10, 25, 20, 18, 8, 4]

# Define colors for each continent
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2C2F0', '#FFB3E6', '#FFD700']

# Set up the figure
plt.figure(figsize=(12, 8))

# Create the pie chart
# Explode the largest sector (Asia) to emphasize it
explode = (0, 0, 0.1, 0, 0, 0, 0)
plt.pie(initiatives_percentage, labels=continents, autopct='%1.1f%%', startangle=120, colors=colors, shadow=True, explode=explode)

# Add the title with line breaks for better readability
plt.title('Global Exploration Initiatives by Continent\n(A Hypothetical Distribution)', fontsize=18, fontweight='bold', pad=20)

# Add a legend to the side of the pie chart
plt.legend(title="Continents", loc='center left', bbox_to_anchor=(1.1, 0.5), fontsize=12)

# Ensure that layout is adjusted to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()