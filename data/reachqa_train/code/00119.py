import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

# Define the tea types and their proportions in each region
regions = ["Northland", "Southscape", "Eastshore"]
tea_types = ["Black Tea", "Green Tea", "Herbal Tea", "White Tea", "Oolong Tea"]
northland_consumption = [40, 25, 15, 10, 10]
southscape_consumption = [20, 40, 20, 10, 10]
eastshore_consumption = [30, 20, 25, 15, 10]

# Organize the data by region
consumption_data = [northland_consumption, southscape_consumption, eastshore_consumption]

# Define a gradient color map for more sophisticated color representation
colors = cm.viridis(np.linspace(0, 1, len(tea_types)))

# Create the figure with 3 pie charts plus one aggregate subplot
fig, ax = plt.subplots(2, 2, figsize=(15, 12), subplot_kw=dict(aspect="equal"))
ax = ax.flatten()

# Plot individual regional preferences
for i, data in enumerate(consumption_data):
    wedges, texts, autotexts = ax[i].pie(
        data, colors=colors, wedgeprops=dict(width=0.4, edgecolor='w', alpha=0.9), startangle=140,
        labels=tea_types, autopct='%1.1f%%', pctdistance=0.85, textprops=dict(color="black", fontsize=9, weight='bold')
    )
    ax[i].set_title(f'Tea Preferences in {regions[i]}', fontsize=14, pad=20)

# Combine all data to a single pie chart to compare aggregate preferences
total_data = np.sum(consumption_data, axis=0)
wedges, texts, autotexts = ax[3].pie(
    total_data, colors=colors, wedgeprops=dict(width=0.4, edgecolor='w', alpha=0.9), startangle=140,
    labels=tea_types, autopct='%1.1f%%', pctdistance=0.85, textprops=dict(color="black", fontsize=9, weight='bold')
)
ax[3].set_title("Aggregate Tea Consumption Across Regions", fontsize=14, pad=20)

# Adjust layout for better fit and add a global title
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.suptitle("Regional and Aggregate Tea Consumption Preferences", fontsize=18, fontweight='bold', y=0.98)

# Add a unified legend for clarity
fig.legend(wedges, tea_types, title="Tea Types", loc='center right', bbox_to_anchor=(1.1, 0.5))

# Show the chart
plt.show()