import matplotlib.pyplot as plt
import squarify

# Adjusted Sales data for better proportionality
categories = [
    'Electronics', 'Mobile Phones', 'Laptops', 
    'Fashion', 'Clothing', 'Accessories', 
    'Home & Kitchen', 'Furniture', 'Kitchen Appliances'
]
sales = [400, 120, 80, 300, 180, 120, 250, 150, 100]  # Enhanced to reflect more distinct proportions
colors = [
    '#FF9999', '#FF6666', '#FF3333',  # Electronics shades
    '#FFCC99', '#FF9933', '#FF6600',  # Fashion shades
    '#99CCFF', '#66B2FF', '#3399FF'   # Home & Kitchen shades
]

# Create the plot
plt.figure(figsize=(12, 8))
squarify.plot(
    sizes=sales, 
    label=categories, 
    color=colors, 
    alpha=0.8, 
    edgecolor="white", 
    linewidth=2, 
    text_kwargs={'fontsize': 10, 'weight': 'bold', 'color': 'darkblue'}
)

# Title with a line break for clarity
plt.title("2023 E-commerce Sales Distribution\nby Product Categories", fontsize=16, fontweight='bold', pad=20)
plt.axis('off')  # Remove axes for a cleaner look

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()