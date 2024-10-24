import numpy as np
import matplotlib.pyplot as plt

# Define the parameters and their respective scores for each country
categories = ['Solar\nEnergy', 'Wind\nEnergy', 'Hydroelectric\nPower', 'Energy\nEfficiency', 'Carbon\nReduction']
num_vars = len(categories)

# Data scores for different countries
country_energy_data = {
    'Germany': [8, 9, 4, 8, 7],
    'France': [6, 7, 8, 7, 6],
    'Norway': [5, 4, 10, 6, 8],
    'Spain': [7, 6, 6, 7, 5],
    'Denmark': [7, 10, 3, 9, 8]
}

# Create a figure for the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Calculate the angle for each category
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop for the last angle

# Draw the radar chart with filled areas
for country, scores in country_energy_data.items():
    scores += scores[:1]  # Repeat the first value to close the radar chart loop
    ax.fill(angles, scores, alpha=0.25, label=country)
    ax.plot(angles, scores, linewidth=2)

# Customize the chart's appearance
plt.xticks(angles[:-1], categories, color='darkslategray', size=10)
ax.set_ylim(0, 10)
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=7)

# Title and legend settings
plt.title('Sustainable Energy Adoption\nin European Countries - 2023', size=16, color='forestgreen', y=1.1)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=9, title='Countries')

# Ensure everything is adjusted neatly
plt.tight_layout()

# Display the radar chart
plt.show()