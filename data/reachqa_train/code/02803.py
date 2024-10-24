import matplotlib.pyplot as plt
import squarify  # Importing the squarify library for tree maps

# Define the labels and their corresponding market share values
labels = [
    'Social Media\n(35%)', 'Messaging Apps\n(25%)', 'Email Services\n(15%)',
    'Video Conferencing\n(15%)', 'Professional Networking\n(10%)'
]
sizes = [35, 25, 15, 15, 10]  # Market share percentages

# Define colors for each category using a distinct palette
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']

# Create a new figure for the tree map
plt.figure(figsize=(10, 6))
plt.title('The Rise of Digital Communication Channels\nMarket Share Distribution', fontsize=16, fontweight='bold', pad=20)

# Plot the tree map
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8, text_kwargs={'fontsize': 12, 'weight': 'bold'})

# Remove axes for a cleaner look
plt.axis('off')

# Automatically adjust the layout to avoid overlaps
plt.tight_layout()

# Display the plot
plt.show()