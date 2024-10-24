import matplotlib.pyplot as plt
import numpy as np

# Define data for the pie chart
energy_sources = ['Solar', 'Wind', 'Hydroelectric', 'Biomass', 'Geothermal']
contributions_2023 = [30, 25, 20, 15, 10]  # Total adds up to 100%
colors = ['#FFD700', '#87CEEB', '#32CD32', '#A0522D', '#FF4500']
explode = (0.1, 0, 0, 0, 0)  # Explode the Solar segment

# Define data for the bar chart subplot
years = [2021, 2022, 2023]
contributions = {
    'Solar': [25, 28, 30],
    'Wind': [22, 24, 25],
    'Hydroelectric': [20, 20, 20],
    'Biomass': [18, 16, 15],
    'Geothermal': [15, 12, 10],
}

# Create a figure with 2 subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 8))

# Create the pie chart in the first subplot
wedges, texts, autotexts = axs[0].pie(
    contributions_2023, labels=energy_sources, autopct='%1.1f%%', startangle=140,
    colors=colors, explode=explode, shadow=True, wedgeprops=dict(edgecolor='white'))

plt.setp(autotexts, size=12, weight="bold", color='white')
plt.setp(texts, size=14)
axs[0].set_title('Global Renewable Energy\nContribution in 2023', fontsize=16, weight='bold', pad=20)
axs[0].axis('equal')  # Ensures the pie chart is a circle

# Create a bar chart in the second subplot
width = 0.15  # Bar width
x = np.arange(len(years))  # Label locations
for idx, (source, values) in enumerate(contributions.items()):
    axs[1].bar(x + idx * width, values, width, label=source, color=colors[idx])

axs[1].set_xlabel('Year', fontsize=12, weight='bold')
axs[1].set_ylabel('Contribution Percentage', fontsize=12, weight='bold')
axs[1].set_title('Renewable Energy Contributions Over Years', fontsize=16, weight='bold', pad=20)
axs[1].set_xticks(x + width * (len(energy_sources) - 1) / 2)
axs[1].set_xticklabels(years)
axs[1].legend(title="Energy Sources", bbox_to_anchor=(1, 1), loc='upper left', fontsize=10)

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()