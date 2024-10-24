import matplotlib.pyplot as plt
import numpy as np

# Define energy sources and their respective usage in arbitrary units
energy_sources = ['Solar Fusion', 'Quantum Helium', 'Dark Matter', 'Gravitational Waves', 'Neutrino Streams']
usage = [35, 25, 20, 10, 10]

# Define an explosion effect to highlight the most significant sector (Solar Fusion)
explode = (0.1, 0, 0, 0, 0)

# New data for the additional plot: fictional Annual Growth Rate for each energy source
growth_rate = [5.5, 3.8, 4.2, 2.0, 1.5]

# Create a figure with 1 row and 2 columns of subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# Pie Chart
wedges, texts, autotexts = axs[0].pie(
    usage, 
    explode=explode, 
    labels=energy_sources, 
    autopct='%1.1f%%',
    startangle=140, 
    wedgeprops={'edgecolor': 'black'},
    colors=['gold', 'skyblue', 'purple', 'limegreen', 'lightcoral']
)

# Adjust text size and color
for text in texts:
    text.set_fontsize(12)
    text.set_color('darkblue')
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

axs[0].set_title('Energy Sources Distribution\nfor Intergalactic Travel Year 2250', fontsize=14, fontweight='bold', pad=10)

# Bar Chart
colors_bar = ['goldenrod', 'deepskyblue', 'mediumpurple', 'mediumseagreen', 'indianred']
axs[1].bar(energy_sources, growth_rate, color=colors_bar, edgecolor='black')
axs[1].set_title('Annual Growth Rate of Energy Sources', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Energy Sources')
axs[1].set_ylabel('Growth Rate (%)')
axs[1].grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Annotate the bar chart
for i, rate in enumerate(growth_rate):
    axs[1].annotate(f'{rate}%', xy=(i, rate), xytext=(0, 3), textcoords='offset points', ha='center', fontsize=10, color='black')

# Adjust layout to avoid overlapping
plt.tight_layout()

# Add legends
axs[0].legend(wedges, energy_sources, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
axs[1].legend(['Growth Rate (%)'], loc='upper right')

# Display the plot
plt.show()