import matplotlib.pyplot as plt

# Define data for the original scatter plot
creatures = ['Dragon', 'Griffin', 'Phoenix', 'Pegasus', 'Hippogriff']
heights = [30, 15, 8, 10, 18]  # Heights in feet
wing_spans = [50, 25, 20, 22, 30]  # Wing spans in feet
colors = ['#FF6347', '#FFD700', '#1E90FF', '#32CD32', '#8A2BE2']
markers = ['o', 'v', '^', '<', '>']

# Define data for the additional bar plot
weights = [500, 250, 180, 300, 400]  # Weights in pounds

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Scatter plot: Height vs Wing Span
for i, creature in enumerate(creatures):
    ax1.scatter(heights[i], wing_spans[i], color=colors[i], marker=markers[i], label=creature, s=100)

ax1.set_title('Flying Fantasy Creatures:\nHeight vs. Wing Span', fontsize=14, fontweight='bold', pad=20)
ax1.set_xlabel('Height (ft)', fontsize=12)
ax1.set_ylabel('Wing Span (ft)', fontsize=12)
ax1.legend(title='Creatures', loc='upper left', fontsize=10, frameon=False)
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Bar plot: Creature Weight
bars = ax2.bar(creatures, weights, color=colors, edgecolor='black')
ax2.set_title('Weight of Flying Creatures', fontsize=14, fontweight='bold', pad=20)
ax2.set_ylabel('Weight (lbs)', fontsize=12)

# Annotate bar heights
for bar in bars:
    height = bar.get_height()
    ax2.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10)

# Adjust the layout
plt.tight_layout()

# Show the plots
plt.show()