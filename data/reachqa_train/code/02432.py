import matplotlib.pyplot as plt
import squarify

# Define the smartphone manufacturers and their estimated shipments in millions
manufacturers = [
    "Apple", "Samsung", "Xiaomi", "Oppo", "Vivo", 
    "Huawei", "OnePlus", "Motorola", "Nokia", "Sony"
]
shipments = [
    230, 320, 150, 120, 100, 
    80, 60, 50, 45, 40
]

# Define colors for each segment, ensuring distinctness for each manufacturer
colors = [
    "#FF9999", "#66B3FF", "#99FF99", "#FFCC99", "#FFD700",
    "#FF6F61", "#008080", "#DFFF00", "#FF00FF", "#FF6347"
]

# Create the treemap
plt.figure(figsize=(14, 8))
squarify.plot(
    sizes=shipments,
    label=[f"{manufacturer}\n{shipment}M" for manufacturer, shipment in zip(manufacturers, shipments)],
    color=colors,
    alpha=0.8,
    edgecolor="white",
    linewidth=2
)

# Customize the plot
plt.title("Global Market Share\nSmartphone Manufacturers in 2023", fontsize=16, fontweight='bold', pad=20)
plt.axis('off')  # Hide the axis

# Adjust layout to prevent text overlap and improve spacing
plt.tight_layout()

# Display the plot
plt.show()