import matplotlib.pyplot as plt
import squarify
import matplotlib.cm as cm
import numpy as np

# Define the market share data for various snack brands within their categories
data = {
    'Chips': [
        {'name': 'CrunchyDelight', 'value': 20},
        {'name': 'Crispwave', 'value': 15},
        {'name': 'SaltSnap', 'value': 10}
    ],
    'Chocolates': [
        {'name': 'ChocoLux', 'value': 18},
        {'name': 'SweetSurge', 'value': 12},
        {'name': 'CocoaDreams', 'value': 10}
    ],
    'Cookies': [
        {'name': 'CookieCrisps', 'value': 12},
        {'name': 'BiscuitBlast', 'value': 8},
        {'name': 'OatSnaps', 'value': 5}
    ]
}

# Flatten the data structure for plotting
labels = []
values = []
categories = []
colors = cm.Paired(np.arange(len(data['Chips']) + len(data['Chocolates']) + len(data['Cookies'])))

# Prepare data for plotting
for category, items in data.items():
    for item in items:
        labels.append(f"{item['name']}\n({category} - {item['value']}%)")
        values.append(item['value'])
        categories.append(category)

# Start plotting the treemap using squarify
plt.figure(figsize=(14, 10))
squarify.plot(
    sizes=values, 
    label=labels, 
    color=colors, 
    alpha=.8, 
    edgecolor="black", 
    linewidth=1.5, 
    text_kwargs={'fontsize': 10, 'weight': 'bold'}
)

# Title and layout adjustments
plt.title("Market Share Analysis of Snack Brands\nin Future City Malls - 2050", fontsize=18, fontweight='bold', pad=20)
plt.axis('off')

# Customize the legend
handles = [plt.Rectangle((0, 0), 1, 1, color=colors[i], ec="black") for i in range(len(data))]
plt.legend(handles, data.keys(), loc='upper left', bbox_to_anchor=(1, 1), title="Categories", fontsize=10, title_fontsize=12)

plt.tight_layout(rect=[0, 0, 0.85, 1])  # Adjust layout to accommodate legend

# Display the plot
plt.show()