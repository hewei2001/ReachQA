import matplotlib.pyplot as plt

# Define the energy sources and their respective percentages
energy_sources = ["Solar", "Wind", "Hydroelectric", "Geothermal", "Biomass"]
percentages = [23, 28, 30, 10, 9]  # Hypothetical percentage distribution

# Colors for each segment
colors = ['#FDB813', '#0096FF', '#76C3B2', '#FF6F61', '#A1C935']

# Create the plot
fig, ax = plt.subplots(figsize=(10, 7))

# Plotting a donut pie chart with some segments exploded for emphasis
explode = (0.05, 0.05, 0, 0, 0)  # Slightly pull out Solar and Wind segments for emphasis
wedges, texts, autotexts = ax.pie(percentages, labels=energy_sources, autopct='%1.1f%%',
                                  startangle=140, colors=colors, pctdistance=0.85,
                                  wedgeprops=dict(width=0.3), explode=explode, shadow=True)

# Styling text
plt.setp(autotexts, size=10, weight="bold", color='white')
plt.setp(texts, size=12)

# Title of the chart
ax.set_title("Global Renewable Energy Sources in 2023:\nEmbracing a Sustainable Future", fontsize=16, fontweight='bold', pad=20)

# Adding a legend
ax.legend(wedges, energy_sources, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()