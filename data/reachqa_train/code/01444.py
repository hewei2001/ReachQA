import matplotlib.pyplot as plt

# Define gaming consoles and their units sold (in millions)
consoles = [
    'Nintendo Entertainment System (NES)', 
    'Sega Master System', 
    'Atari 2600', 
    'Intellivision', 
    'ColecoVision', 
    'Commodore 64 Games System', 
    'TurboGrafx-16'
]

units_sold = [61.91, 13, 30, 3, 2, 1.5, 10]

# Create a color palette for the bars
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#955251', '#B565A7']

# Create the horizontal bar chart
plt.figure(figsize=(12, 8))
plt.barh(consoles, units_sold, color=colors, edgecolor='black', height=0.7)

# Add labels and title
plt.xlabel('Units Sold (Millions)', fontsize=12)
plt.title('Retro Gaming Console Popularity:\nA Nostalgic Journey Through the 1980s', fontsize=16, fontweight='bold', pad=20)

# Add value labels to each bar
for index, value in enumerate(units_sold):
    plt.text(value + 0.5, index, f"{value:.2f}", va='center', ha='left', fontsize=10, fontweight='bold')

# Customize y-axis labels for clarity
plt.yticks(fontsize=11, ha='right')

# Show grid for better readability
plt.grid(axis='x', linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()