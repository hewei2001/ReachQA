import matplotlib.pyplot as plt

# Define the energy sources and their corresponding percentages
energy_sources = ['Solar', 'Wind', 'Hydroelectric', 'Biomass', 'Geothermal']
percentages = [35, 25, 20, 10, 10]

# Define custom colors for each energy source
colors = ['#FFD700', '#87CEEB', '#32CD32', '#8B4513', '#FF6347']

# Highlight the 'Solar' sector by exploding it slightly
explode = (0.1, 0, 0, 0, 0)

# Create a pie chart
plt.figure(figsize=(10, 7))
wedges, texts, autotexts = plt.pie(percentages, labels=energy_sources, autopct='%1.1f%%', startangle=90, colors=colors,
                                   explode=explode, wedgeprops={'edgecolor': 'black'})

# Adjust text size and style for readability
for text in texts:
    text.set_fontsize(10)
for autotext in autotexts:
    autotext.set_fontsize(8)
    autotext.set_color('black')
    autotext.set_weight('bold')

# Add a title to the pie chart, splitting it into two lines
plt.title("Diverse Energy Sources Distribution in Eco-Friendly City\n2023 Analysis", fontsize=14, fontweight='bold', pad=20)

# Add a legend to the chart outside of the pie
plt.legend(wedges, energy_sources, title="Energy Sources", loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()