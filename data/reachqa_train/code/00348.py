import matplotlib.pyplot as plt

# Celestial bodies and their budget allocations
destinations = ['Mars', 'Europa', 'Titan', 'Asteroid Belt', 'Venus', 'Enceladus', 'Moon']
budget_allocation = [35, 20, 15, 10, 10, 5, 5]  # in percentage

# Colors inspired by celestial body characteristics
colors = ['#FF5733', '#3498DB', '#9B59B6', '#E67E22', '#F39C12', '#85C1E9', '#F7DC6F']

# Explode the largest slice (Mars) to highlight it
explode = (0.1, 0, 0, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    budget_allocation,
    explode=explode,
    labels=destinations,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    shadow=True,
    wedgeprops=dict(edgecolor='w')
)

# Style the autotexts for better visibility
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

# Set aspect ratio to ensure pie is drawn as a circle
ax.axis('equal')

# Title with contextual information
plt.title("Budget Distribution for\nGalactic Exploration Missions (2030-2040)", fontsize=14, fontweight='bold')

# Legend configuration for clarification
legend_labels = [f"{destination}: {allocation}%" for destination, allocation in zip(destinations, budget_allocation)]
ax.legend(legend_labels, title="Mission Budget Allocation", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=10)

# Tight layout for better spacing and preventing overlap
plt.tight_layout()

# Display the plot
plt.show()