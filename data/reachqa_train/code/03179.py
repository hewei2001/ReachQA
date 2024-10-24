import matplotlib.pyplot as plt
import numpy as np

# Expanded data for futuristic foods, adding sub-categories for more complexity
foods = [
    "Insect Protein Bars",
    "Lab-Grown Steak",
    "Algae Smoothies",
    "3D-Printed Pizza",
    "Fermented Plant-Based Yogurt",
    "Cultured Butter Alternatives",
    "Cell-based Fish",
    "Synthetic Coffee"
]

# Popularity index broken down into sub-categories (Taste, Nutritional Value, Affordability, Sustainability)
demand_data = {
    "Insect Protein Bars": [20, 25, 15, 25],
    "Lab-Grown Steak": [30, 20, 10, 15],
    "Algae Smoothies": [10, 20, 20, 15],
    "3D-Printed Pizza": [15, 25, 15, 15],
    "Fermented Plant-Based Yogurt": [20, 25, 20, 15],
    "Cultured Butter Alternatives": [15, 20, 20, 20],
    "Cell-based Fish": [25, 20, 15, 15],
    "Synthetic Coffee": [15, 20, 25, 15]
}

# Sub-category labels and colors
sub_categories = ["Taste", "Nutritional Value", "Affordability", "Sustainability"]
colors = ['#A569BD', '#48C9B0', '#F4D03F', '#F1948A']

# Create a horizontal stacked bar chart
fig, ax = plt.subplots(figsize=(14, 10))
bar_positions = np.arange(len(foods))
cumulative_data = np.zeros(len(foods))

# Plot each sub-category
for i, sub_category in enumerate(sub_categories):
    data_to_plot = [demand_data[food][i] for food in foods]
    bars = ax.barh(bar_positions, data_to_plot, left=cumulative_data, 
                   color=colors[i], edgecolor='black', height=0.6, label=sub_category)
    cumulative_data += data_to_plot

# Set title and axis labels
ax.set_title("Projected Popularity of Innovative Foods\nat the 2045 Global Culinary Innovation Expo", 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Popularity Index', fontsize=12, labelpad=10)
ax.set_ylabel('Futuristic Foods', fontsize=12, labelpad=10)
ax.set_yticks(bar_positions)
ax.set_yticklabels(foods, fontsize=11)
ax.invert_yaxis()  # Highest values on top

# Add a vertical grid for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.5)

# Adding data labels to each sub-category segment
for bar in ax.containers:
    ax.bar_label(bar, label_type='center', fontsize=9)

# Add a legend
ax.legend(title="Sub-categories", title_fontsize='13', fontsize='11', bbox_to_anchor=(1.05, 1), loc='upper left')

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the plot
plt.show()