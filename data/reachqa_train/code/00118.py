import matplotlib.pyplot as plt
import numpy as np

# Define the tea types and their proportions in each region
regions = ["Northland", "Southscape", "Eastshore"]
tea_types = ["Black Tea", "Green Tea", "Herbal Tea", "White Tea", "Oolong Tea"]
northland_consumption = [40, 25, 15, 10, 10]
southscape_consumption = [20, 40, 20, 10, 10]
eastshore_consumption = [30, 20, 25, 15, 10]

# Organize the data by region
consumption_data = [northland_consumption, southscape_consumption, eastshore_consumption]

# Colors for the chart
colors = ['#e63946', '#a8dadc', '#1d3557', '#f1faee', '#457b9d']

# Create the ring chart
fig, ax = plt.subplots(1, 3, figsize=(15, 7), subplot_kw=dict(aspect="equal"))

for i, data in enumerate(consumption_data):
    wedges, texts, autotexts = ax[i].pie(
        data, colors=colors, wedgeprops=dict(width=0.4, edgecolor='w'), startangle=140,
        labels=tea_types, autopct='%1.1f%%', pctdistance=0.85, textprops=dict(color="w", fontsize=9)
    )
    for text in texts:
        text.set_color('black')
    ax[i].set_title(f'Tea Preferences in {regions[i]}', fontsize=12, pad=10)
    ax[i].set_xlabel(f'Total: {sum(data)}%', fontsize=10, color='gray')

# Add a global title to the figure
plt.suptitle("Regional Tea Consumption Preferences", fontsize=16, fontweight='bold', y=0.98)

# Adjust layout for better fit
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display the chart
plt.show()