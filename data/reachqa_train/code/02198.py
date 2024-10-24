import matplotlib.pyplot as plt

# Define the labels and their corresponding data
energy_sources = ['Solar', 'Wind', 'Hydropower', 'Biomass', 'Geothermal', 'Others']
percentages = [30, 25, 20, 15, 5, 5]

# Define colors for each segment of the pie chart
colors = ['#FFD700', '#87CEEB', '#32CD32', '#D2691E', '#FF6347', '#B0C4DE']

# Define the explode parameter to highlight the 'Solar' slice
explode = (0.1, 0, 0, 0, 0, 0)

# Create a pie chart
plt.figure(figsize=(10, 8))
plt.pie(percentages, labels=energy_sources, autopct='%1.1f%%', startangle=90, 
        colors=colors, explode=explode, wedgeprops={'edgecolor': 'black'}, shadow=True)

# Adding a title and enhancing layout
plt.title('Global Distribution of Renewable Energy Sources\nin 2023', fontsize=14, fontweight='bold', pad=20)

# Add a legend to provide more insights
plt.legend(title="Energy Sources", loc='upper left', bbox_to_anchor=(1, 0.6), fontsize=10)

# Ensure the pie chart is a circle and not an oval
plt.axis('equal')

# Automatically adjust subplot parameters to give specified padding.
plt.tight_layout()

# Show the plot
plt.show()