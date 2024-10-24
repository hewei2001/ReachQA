import matplotlib.pyplot as plt
import numpy as np

# Define the initiatives and their respective budget allocations
initiatives = [
    'Environmental Cleanup', 
    'Cultural Events', 
    'Social Welfare Programs', 
    'Educational Workshops', 
    'Health Campaigns', 
    'Infrastructure Development'
]

# Define the budget allocations as percentages
allocations = np.array([20, 15, 25, 10, 20, 10])

# Define colors for each sector
colors = ['#76C7C0', '#F28C28', '#76A1EA', '#F1C40F', '#9B59B6', '#2ECC71']

# Explode the 'Social Welfare Programs' sector for emphasis
explode = (0, 0, 0.1, 0, 0, 0)

# Create the pie chart
plt.figure(figsize=(10, 8))
plt.pie(
    allocations, 
    labels=initiatives, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors, 
    explode=explode,
    wedgeprops={'edgecolor': 'black', 'linewidth': 1}
)

# Add a title and adjust layout
plt.title('Annual Distribution of Community Engagement Initiatives\nin Urban Areas (2023)', fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()

# Add a legend to identify the initiatives
plt.legend(initiatives, title="Initiatives", loc='center left', bbox_to_anchor=(1, 0.5))

# Show the plot
plt.show()