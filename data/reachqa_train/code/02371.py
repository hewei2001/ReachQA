import matplotlib.pyplot as plt

# Countries and their renewable energy usage percentages
countries = ['Germany', 'China', 'USA', 'India', 'Brazil', 'Australia', 'Norway']
renewable_usage = [40, 30, 20, 25, 60, 35, 90]

# Define colors for each country using a custom palette
colors = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69']

# Explode the 'Norway' slice to highlight it more
explode = (0, 0, 0, 0, 0, 0, 0.1)  # Only 'Norway' is exploded

# Create the main figure
fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))

# Plot the pie chart
wedges, texts, autotexts = ax.pie(
    renewable_usage, labels=countries, autopct='%1.1f%%', startangle=140,
    colors=colors, explode=explode, shadow=True, wedgeprops=dict(edgecolor='w')
)

# Customize the appearance of the autotexts for better visibility
plt.setp(autotexts, size=10, weight="bold", color="black", 
         bbox=dict(boxstyle="round,pad=0.3", edgecolor='white', facecolor='lightgray'))

# Set a title with a focus on sustainability
ax.set_title("Renewable Energy Usage in Various Countries\nProjected for 2025", fontsize=14, fontweight='bold', pad=20)

# Add a legend to the right of the chart
ax.legend(wedges, countries, title="Countries", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Add an inner circle for a donut chart effect and annotate the central message
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)
plt.annotate('Pioneers of Sustainability', xy=(0, 0), fontsize=12, ha='center')

# Adjust layout to prevent overlapping of chart elements
plt.tight_layout()

# Display the plot
plt.show()