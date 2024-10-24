import matplotlib.pyplot as plt
import numpy as np

# Define spices and their corresponding flavor notes
spices = ['Cinnamon', 'Cardamom', 'Saffron', 'Star Anise', 'Clove']
flavor_notes = ['Sweet', 'Pungent', 'Bitter', 'Floral', 'Earthy']

# Intensity scores for each spice on the flavor notes scale
# Values denote the prominence of each flavor note
cinnamon_flavors = [8, 2, 3, 5, 4]
cardamom_flavors = [4, 7, 2, 6, 5]
saffron_flavors = [5, 3, 8, 7, 4]
star_anise_flavors = [6, 5, 3, 4, 7]
clove_flavors = [7, 6, 5, 3, 8]

# Combine data into a list of lists for plotting
flavor_data = [cinnamon_flavors, cardamom_flavors, saffron_flavors, star_anise_flavors, clove_flavors]

# Calculate number of categories and sector angles
num_notes = len(flavor_notes)
angles = np.linspace(0, 2 * np.pi, num_notes, endpoint=False).tolist()

# Function to plot each spice's flavors on a rose chart
def plot_spice_flavors(ax, data, label, color):
    # Loop data to close the plot
    data = np.concatenate((data, [data[0]]))
    angles_extended = angles + angles[:1]
    
    # Plot the data
    ax.fill(angles_extended, data, color=color, alpha=0.25, label=label)
    ax.plot(angles_extended, data, color=color, linewidth=2)

# Create the rose chart plot
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Plotting each spice with a unique color
colors = ['#D2691E', '#FFD700', '#FF4500', '#8A2BE2', '#5F9EA0']
for i, spice in enumerate(spices):
    plot_spice_flavors(ax, flavor_data[i], spice, colors[i])

# Customize the plot
ax.set_yticklabels([])  # Remove radial tick labels
ax.set_xticks(angles)
ax.set_xticklabels(flavor_notes, fontsize=12, fontweight='bold')

# Title and Legend
ax.set_title("Aromatic Heritage:\nFlavor Notes of Ancient Spices", size=16, weight='bold', pad=25)
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=10, title='Spices')

# Adjust layout for clarity and display the plot
plt.tight_layout()
plt.show()