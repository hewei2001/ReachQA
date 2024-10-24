import matplotlib.pyplot as plt

# Define the labels and data for the pie chart
energy_sources = ['Solar', 'Wind', 'Hydropower', 'Biomass', 'Geothermal']
production_percentages = [35, 30, 20, 10, 5]
colors = ['#FFD700', '#87CEEB', '#4682B4', '#9ACD32', '#FF6347']
explode = (0.1, 0, 0, 0, 0)  # Highlight the 'Solar' segment

# Create the pie chart
fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(
    production_percentages, 
    labels=energy_sources, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors,
    explode=explode,
    shadow=True
)

# Customizing text properties for better readability
plt.setp(autotexts, size=10, weight='bold', color='white')
plt.setp(texts, size=10)

# Set the title and customize the layout
ax.set_title('Global Renewable Energy\nProduction in 2023', fontsize=14, weight='bold')

# Add a legend, positioned to the right of the chart
ax.legend(wedges, energy_sources, title="Energy Source", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust the layout to prevent text overlap
plt.tight_layout()

# Show the chart
plt.show()