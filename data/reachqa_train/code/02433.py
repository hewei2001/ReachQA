import matplotlib.pyplot as plt
import squarify

# Expanded list of smartphone manufacturers and their estimated shipments in millions (including decimal values)
manufacturers = [
    "Apple", "Samsung", "Xiaomi", "Oppo", "Vivo",
    "Huawei", "OnePlus", "Motorola", "Nokia", "Sony",
    "LG", "HTC", "Lenovo", "Asus", "Realme", 
    "ZTE", "Alcatel", "Tecno", "Honor", "Google Pixel"
]
shipments = [
    230.5, 320.8, 150.3, 120.2, 100.1,
    80.5, 60.6, 50.4, 45.9, 40.3,
    35.7, 28.6, 27.8, 24.1, 22.5,
    20.3, 19.9, 17.5, 15.0, 12.5
]

# Define a gradient color palette based on shipment volume
colors = plt.cm.viridis([0.1 * i for i in range(len(shipments))])

# Calculate total shipment volume
total_shipments = sum(shipments)

# Create the treemap
plt.figure(figsize=(16, 10))
squarify.plot(
    sizes=shipments,
    label=[f"{manufacturer}\n{shipment}M ({shipment/total_shipments:.1%})" for manufacturer, shipment in zip(manufacturers, shipments)],
    color=colors,
    alpha=0.8,
    edgecolor="white",
    linewidth=2
)

# Customize the plot
plt.title("Global Market Share of Smartphone Manufacturers in 2023\n(With Total Shipments and Market Share Percentage)", fontsize=18, fontweight='bold', pad=20)
plt.axis('off')

# Use tight_layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()