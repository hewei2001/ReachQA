import matplotlib.pyplot as plt
import numpy as np

# Define decades from 1890 to 2020
decades = np.array(['1890', '1910', '1930', '1950', '1970', '1990', '2010', '2020'])

# Faintest magnitude detectable (lower numbers are fainter, so we will decrease values)
faintest_magnitude = np.array([10, 12, 14, 16, 18, 20, 24, 28])

# Set up the main plot
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the line chart
ax.plot(decades, faintest_magnitude, marker='o', color='b', linestyle='-', linewidth=2, label='Faintest Magnitude Detected')

# Set titles and labels
ax.set_title('Advancements in Telescope Sensitivity (1890-2020):\nExploring Deeper into the Cosmos', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Decade', fontsize=14)
ax.set_ylabel('Faintest Magnitude Detected', fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add legend
ax.legend(loc='lower right', fontsize=11)

# Add grid lines for better readability
ax.grid(alpha=0.3, linestyle='--', linewidth=0.7)

# Add some annotations to highlight key technological advancements
annotations = [
    ('Invention of Radio Telescopes', '1950', 16, 'left'),
    ('Introduction of CCDs', '1990', 20, 'right'),
    ('Launch of the Hubble Space Telescope', '2010', 24, 'right'),
]

for note, x_loc, y_loc, align in annotations:
    ax.annotate(
        note, 
        xy=(x_loc, y_loc), 
        xytext=(x_loc, y_loc + 2),
        ha=align,
        fontsize=10, 
        color='darkred',
        arrowprops=dict(facecolor='darkred', arrowstyle='->')
    )

# Annotate each data point with its magnitude
for i, txt in enumerate(faintest_magnitude):
    ax.annotate(f'{txt}', (decades[i], faintest_magnitude[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

# Adjust layout to prevent overlapping elements
plt.tight_layout()

# Display the plot
plt.show()