import matplotlib.pyplot as plt
import squarify

# Data: Projected market share of emerging technologies in 2025 (in percentage)
tech_labels = [
    'Quantum Computing\n20%', 
    'Augmented Reality\n15%', 
    'Blockchain\n18%', 
    'IoT\n10%', 
    '5G Infrastructure\n12%', 
    'Artificial Intelligence\n25%', 
    'Autonomous Vehicles\n5%', 
    'Cybersecurity Solutions\n8%', 
    'Biotechnology\n6%', 
    'Edge Computing\n4%'
]
market_shares = [20, 15, 18, 10, 12, 25, 5, 8, 6, 4]

# Colors for each technology
colors = [
    '#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', 
    '#955251', '#B565A7', '#009B77', '#DD4124', '#45B8AC'
]

# Create a figure for the treemap
plt.figure(figsize=(12, 8))

# Use squarify to plot the treemap with given sizes and labels
squarify.plot(sizes=market_shares, label=tech_labels, color=colors, alpha=0.85, 
              bar_kwargs=dict(linewidth=2, edgecolor="#fff"))

# Set the title and configure the layout
plt.title('Projected Market Share of Emerging Technologies\nin 2025', fontsize=16, fontweight='bold', pad=20)
plt.axis('off')

# Adjust the layout for better appearance and visibility
plt.tight_layout()

# Display the treemap
plt.show()