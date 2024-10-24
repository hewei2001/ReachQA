import matplotlib.pyplot as plt
import squarify

# Expanded data representing contributions to various digital technologies by specific countries
regions = [
    'USA - AI', 'USA - Blockchain', 'Canada - AI', 
    'Germany - AI', 'Germany - VR', 'France - Green Tech',
    'Japan - AI', 'China - VR', 'India - Blockchain',
    'Australia - VR', 'New Zealand - Green Tech',
    'Brazil - Green Tech', 'Chile - VR',
    'Nigeria - Blockchain', 'South Africa - AI'
]

# Corresponding contributions, ensuring they form a reasonable dataset sum
contributions = [
    20, 10, 15,  # USA and Canada
    18, 8, 9,    # Germany and France
    25, 22, 18,  # Japan, China, India
    10, 5,       # Australia and New Zealand
    7, 5,        # Brazil and Chile
    3, 10        # Nigeria and South Africa
]

# Enhanced color scheme for better differentiation
colors = [
    '#FF6347', '#FF4500', '#FFA07A',  # USA and Canada
    '#6495ED', '#1E90FF', '#00FA9A',  # Germany and France
    '#FFD700', '#FFA500', '#FF8C00',  # Japan, China, India
    '#4682B4', '#3CB371',  # Australia and New Zealand
    '#32CD32', '#66CDAA',  # Brazil and Chile
    '#6A5ACD', '#4B0082'   # Nigeria and South Africa
]

# Create the treemap with detailed data
plt.figure(figsize=(18, 10))
squarify.plot(
    sizes=contributions, 
    label=regions, 
    color=colors, 
    alpha=0.8, 
    edgecolor="white", 
    linewidth=2, 
    text_kwargs={'fontsize': 9, 'weight': 'bold'}
)

# Set title and ensure it's visually balanced across multiple lines
plt.title('Global Digital Innovation Hubs:\nPioneers of Technological Advancement in 2023', fontsize=18, weight='bold', pad=20)

# Remove axes to enhance clarity
plt.axis('off')

# Use tight_layout to adjust layout and prevent overlaps
plt.tight_layout()

# Display the plot
plt.show()