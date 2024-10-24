import matplotlib.pyplot as plt
import squarify

# Market share data for different smartphone manufacturers
labels = ['Apple', 'Samsung', 'Xiaomi', 'Oppo', 'Vivo', 'Huawei', 'Others']
sizes = [30, 25, 15, 10, 8, 7, 5]  # Market share percentages
colors = ['#FF9999', '#66B2FF', '#FFCC99', '#99FF99', '#FF66B2', '#FFCC66', '#D1B3FF']

# Define figure size
plt.figure(figsize=(12, 8))

# Plot the tree map
squarify.plot(sizes=sizes, label=[f'{label} ({size}%)' for label, size in zip(labels, sizes)], 
              color=colors, alpha=0.8, text_kwargs={'fontsize': 10, 'weight': 'bold'})

# Title and styling
plt.title('Global Smartphone Market Share\nby Manufacturer - 2023', fontsize=16, fontweight='bold')
plt.axis('off')

# Adjust the layout to prevent overlapping text
plt.tight_layout()

# Display the plot
plt.show()