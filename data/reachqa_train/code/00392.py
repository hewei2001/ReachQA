import matplotlib.pyplot as plt

# Data for the pie chart
energy_sources = ['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Biomass', 'Ocean']
percentages = [35, 25, 20, 10, 5, 5]

# Colors for each segment of the pie chart
colors = ['gold', 'skyblue', 'lightgreen', 'salmon', 'purple', 'teal']

# Explode parameter to highlight a particular slice, such as Solar
explode = (0.1, 0, 0, 0, 0, 0)  # Only "explode" the first slice (Solar)

# Create a pie chart
plt.figure(figsize=(10, 7))
plt.pie(
    percentages,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode,
    shadow=True,
    wedgeprops={'edgecolor': 'black', 'linewidth': 1.5}
)

# Set title and description
plt.title('Global Renewable Energy Sources\nDistribution in 2050', fontsize=14, fontweight='bold', pad=20)
plt.annotate('Note: Projected data reflecting global energy goals.', (0, -1.1), fontsize=10, ha='center')

# Adding a legend outside the pie
plt.legend(
    energy_sources,
    title='Energy Sources',
    loc='center left',
    bbox_to_anchor=(1, 0.5)
)

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the plot
plt.show()