import matplotlib.pyplot as plt

# Define energy sources and their respective usage in arbitrary units
energy_sources = ['Solar Fusion', 'Quantum Helium', 'Dark Matter', 'Gravitational Waves', 'Neutrino Streams']
usage = [35, 25, 20, 10, 10]

# Colors for each section of the pie chart
colors = ['gold', 'skyblue', 'purple', 'limegreen', 'lightcoral']

# Define an explosion effect to highlight the most significant sector (Solar Fusion)
explode = (0.1, 0, 0, 0, 0)  # Highlight 'Solar Fusion'

# Create a pie chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    usage, 
    explode=explode, 
    labels=energy_sources, 
    colors=colors, 
    autopct='%1.1f%%',
    startangle=140, 
    wedgeprops={'edgecolor': 'black'}
)

# Adjust text and annotations
for text in texts:
    text.set_fontsize(12)
    text.set_color('darkblue')
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

# Set the title and layout enhancements
plt.title('Energy Sources Distribution for Intergalactic Travel\nYear 2250', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()

# Add a legend for clarity
ax.legend(wedges, energy_sources, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Display the plot
plt.show()