import matplotlib.pyplot as plt
import numpy as np

# Define animal categories and the number of endangered species
categories = ['Mammals', 'Birds', 'Reptiles', 'Amphibians', 'Fish']
endangered_species = [1200, 1800, 650, 850, 1050]

# Conservation actions adopted for each category
conservation_actions = [
    "Habitat Restoration",
    "Captive Breeding",
    "Anti-Poaching Enforcement",
    "Disease Management",
    "Marine Protected Areas"
]

# Create the bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(categories, endangered_species, color=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700'])

# Annotate the bars with conservation actions
for bar, species, action in zip(bars, endangered_species, conservation_actions):
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 50, f'{species} ({action})', ha='center', va='bottom', fontsize=9)

# Customize the chart
ax.set_title('Conservation Efforts for Endangered Species in 2023', fontsize=14, weight='bold', wrap=True)
ax.set_xlabel('Animal Categories', fontsize=12)
ax.set_ylabel('Number of Endangered Species', fontsize=12)
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()