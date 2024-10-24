import matplotlib.pyplot as plt
import numpy as np

# Alien species
species = ['Zogthari', 'Xylordians', 'Plutonese']

# Communication methods
methods = ['Quantum\nMessage', 'Wormhole\nDispatch', 'Galactic\nFax', 'Telepathy\nTransmission', 'Star\nRelay']

# Preference data (in arbitrary units)
zogthari_prefs = [75, 50, 20, 30, 55]
xylordian_prefs = [45, 60, 10, 70, 40]
plutonese_prefs = [60, 40, 65, 25, 35]

# Reliability data for secondary y-axis
method_reliability = [0.8, 0.9, 0.7, 0.85, 0.95]

# Create figure and axis
fig, ax1 = plt.subplots(figsize=(14, 7))

# Create secondary y-axis
ax2 = ax1.twinx()

# Indices for placement of bars
x_indexes = np.arange(len(methods))
width = 0.25

# Bar plot with gradient colors
for idx, prefs in enumerate([zogthari_prefs, xylordian_prefs, plutonese_prefs]):
    colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(prefs)))
    ax1.bar(x_indexes + (idx - 1) * width, prefs, width=width, label=species[idx], color=colors)

# Add annotations with custom markers
markers = ['*', 'o', 's']
for i, species_prefs in enumerate([zogthari_prefs, xylordian_prefs, plutonese_prefs]):
    for j, v in enumerate(species_prefs):
        ax1.text(j + (i - 1) * width, v + 2, f'{v}{markers[i]}', ha='center', va='bottom', fontsize=9)

# Plot reliability on secondary y-axis
ax2.plot(x_indexes, method_reliability, color='black', linestyle='--', marker='D', markersize=8, label='Reliability')

# Customize axes
ax1.set_title('Alien Encounters: Preferred Contact Methods\nand Reliability in Intergalactic Trade',
              fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Communication Methods', fontsize=12)
ax1.set_ylabel('Preference Level (Units)', fontsize=12)
ax2.set_ylabel('Reliability', fontsize=12)

ax1.set_xticks(x_indexes)
ax1.set_xticklabels(methods, fontsize=10, rotation=45, ha='right')
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Combine legends
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(handles1 + handles2, labels1 + labels2, loc='upper right', fontsize=10)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()