import matplotlib.pyplot as plt

# Data representing the species distribution in Rainforest X
species = ['Mammals', 'Birds', 'Reptiles', 'Amphibians', 'Insects']
percentages = [20, 30, 10, 5, 35]

# Colors for each category
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(
    percentages, 
    labels=species, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    wedgeprops=dict(edgecolor='black'), 
    explode=(0.1, 0, 0, 0, 0.1), 
    shadow=True
)

# Set a title with line breaks for better readability
plt.title("Biodiversity in Rainforest X:\nSpecies Distribution", fontsize=16, fontweight='bold', pad=20)

# Adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()