import matplotlib.pyplot as plt

# Define the data for global coffee consumption by continent
continents = ['Europe', 'North America', 'Asia', 'South America', 'Africa', 'Oceania']
consumption_percentages = [35, 25, 20, 10, 7, 3]  # In percentage

# Define colors for each continent
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Explode the slice for 'Europe' to emphasize its higher consumption
explode = (0.1, 0, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(9, 9))
wedges, texts, autotexts = ax.pie(
    consumption_percentages,
    labels=continents,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    pctdistance=0.85,
    explode=explode,
    shadow=True,
    wedgeprops=dict(width=0.3, edgecolor='w')
)

# Customize the text properties for better readability
plt.setp(autotexts, size=11, weight="bold", color="navy")
plt.setp(texts, size=11, color="darkblue")

# Set the title with a line break for readability
ax.set_title("Global Coffee Consumption\nby Continent (Fictional Data)", size=15, weight='bold', color='midnightblue')

# Enhance legend for better comprehension and positioning
plt.legend(
    wedges,
    continents,
    title="Continents",
    loc="center left",
    bbox_to_anchor=(1.1, 0.5),
    fontsize='11',
    title_fontsize='12',
    frameon=False
)

# Automatically adjust the layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()