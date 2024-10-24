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

# Plotting the bar chart with data annotation
fig, ax = plt.subplots(figsize=(12, 6))

# Width of a single bar
width = 0.25

# Indices for placement of bars
x_indexes = np.arange(len(methods))

# Plot each species' preferences
ax.bar(x_indexes - width, zogthari_prefs, width=width, label='Zogthari', color='#7fc97f')
ax.bar(x_indexes, xylordian_prefs, width=width, label='Xylordians', color='#beaed4')
ax.bar(x_indexes + width, plutonese_prefs, width=width, label='Plutonese', color='#fdc086')

# Title and labels
ax.set_title('Alien Encounters: Preferred Contact Methods\nin Intergalactic Trade', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Communication Methods', fontsize=12)
ax.set_ylabel('Preference Level (Units)', fontsize=12)
ax.set_xticks(x_indexes)
ax.set_xticklabels(methods, fontsize=10)
ax.legend(title='Alien Species')

# Adding data annotation
for i, v in enumerate(zogthari_prefs):
    ax.text(i - width, v + 2, str(v), ha='center', va='bottom', fontsize=9)
for i, v in enumerate(xylordian_prefs):
    ax.text(i, v + 2, str(v), ha='center', va='bottom', fontsize=9)
for i, v in enumerate(plutonese_prefs):
    ax.text(i + width, v + 2, str(v), ha='center', va='bottom', fontsize=9)

# Customize grid
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()