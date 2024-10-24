import matplotlib.pyplot as plt
import squarify

# Define continents and eco-friendly fashion brands
continents = ['North America', 'Europe', 'Asia', 'South America', 'Africa', 'Oceania']
brands = ['GreenThreads', 'EcoStyle', 'NatureWear', 'SustainableFashion', 'RecycleChic']

# Market share of each brand across continents (in percentage points)
data = {
    'North America': [25, 20, 15, 25, 15],
    'Europe': [30, 15, 20, 25, 10],
    'Asia': [10, 30, 30, 15, 15],
    'South America': [20, 25, 25, 20, 10],
    'Africa': [25, 20, 25, 10, 20],
    'Oceania': [15, 25, 20, 30, 10]
}

# Prepare data for the tree map
labels = []
sizes = []
colors = ['#69b3a2', '#40858a', '#b2e061', '#3f956b', '#f9dc5c']  # Consistent color palette per brand

for continent in continents:
    for brand, size in zip(brands, data[continent]):
        labels.append(f"{continent}\n{brand}\n{size}%")
        sizes.append(size)

# Create the figure and axis
plt.figure(figsize=(14, 8))
squarify.plot(sizes=sizes, label=labels, color=colors * len(continents), alpha=0.7, pad=True, edgecolor='white')

# Add a title and adjust the font size
plt.title("Eco-Friendly Fashion Brand Distribution Across Continents", fontsize=18, pad=20)

# Removing axes for a cleaner look
plt.axis('off')

# Automatically adjust layout to ensure labels and elements fit well
plt.tight_layout()

# Display the plot
plt.show()