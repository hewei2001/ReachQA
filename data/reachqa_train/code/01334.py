import matplotlib.pyplot as plt

# Data: Proportion of renewable energy sources in 2023
energy_sources = ['Solar Energy', 'Wind Energy', 'Hydropower', 'Biomass', 'Geothermal']
percentages = [35, 30, 20, 10, 5]

# Color palette for the pie chart
colors = ['#f4a261', '#2a9d8f', '#264653', '#e9c46a', '#e76f51']

# Explode the Solar and Wind sectors slightly for emphasis
explode = (0.1, 0.1, 0, 0, 0)

# Create the pie chart
plt.figure(figsize=(10, 7))
wedges, texts, autotexts = plt.pie(percentages, labels=energy_sources, autopct='%1.1f%%',
                                   startangle=90, colors=colors, pctdistance=0.85,
                                   wedgeprops=dict(edgecolor='w'), explode=explode)

# Enhance the aesthetics of the chart
plt.setp(autotexts, size=10, weight="bold", color="white")
for text in texts:
    text.set_fontsize(12)

# Add a center circle for a doughnut chart look
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
plt.gca().add_artist(centre_circle)

# Set title
plt.title('Global Renewable Energy Mix in 2023', fontsize=15, fontweight='bold', pad=20)

# Add a legend
plt.legend(wedges, energy_sources, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()