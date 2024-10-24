import matplotlib.pyplot as plt

# Data representing the percentage market share of renewable energy types
labels = ['Solar', 'Wind', 'Hydroelectric', 'Biomass', 'Geothermal']
sizes = [35, 25, 20, 15, 5]
colors = ['#ffcc00', '#66b3ff', '#99ff99', '#ff9999', '#c2c2f0']
explode = (0.1, 0, 0, 0, 0)  # "Explode" the Solar slice

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')

# Adding a title with line breaks for better presentation
plt.title("Global Market Share of Renewable Energy Sources (2023)\nFocusing on Sustainable Energy Expansion",
          fontsize=14, fontweight='bold', pad=20)

# Adding a legend outside the pie chart
plt.legend(labels, title="Energy Types", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()