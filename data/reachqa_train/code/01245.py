import matplotlib.pyplot as plt
import numpy as np

# Fictional data representing expedition durations (in years) for different mission types
sei_durations = [2.5, 3.0, 3.2, 3.5, 3.8, 4.0, 4.1, 4.5, 5.0, 5.2]  # Stellar Exploration Initiative
gra_durations = [1.5, 2.0, 2.1, 2.5, 2.8, 3.0, 3.5, 4.0]            # Galactic Research Alliance
cpc_durations = [4.0, 4.2, 4.5, 5.0, 5.5, 6.0, 6.2, 6.5, 7.0, 7.5]  # Cosmic Pioneers Corporation
afc_durations = [3.0, 3.3, 3.5, 3.7, 4.0, 4.2, 4.5, 4.7, 5.0]       # Astronomical Frontiers Council

# Compile the data into a list for plotting
data = [sei_durations, gra_durations, cpc_durations, afc_durations]
all_durations = sei_durations + gra_durations + cpc_durations + afc_durations

# Agency names
agencies = ['SEI', 'GRA', 'CPC', 'AFC']

# Plotting
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))

# Create a horizontal boxplot with customization
box = ax1.boxplot(data, vert=False, patch_artist=True, notch=True, labels=agencies, whis=1.5)

colors = ['#add8e6', '#90ee90', '#ffcccb', '#d3d3d3']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.6)

# Titles and labels
ax1.set_title('The Ethereal Voyage: \nInsight into Interstellar Expedition Durations', fontsize=14, fontweight='bold')
ax1.set_xlabel('Duration (Years)', fontsize=12)
ax1.set_ylabel('Space Agencies', fontsize=12)

# Add annotations to highlight findings
ax1.annotate('Longest Average Duration', xy=(6.5, 3), xytext=(7, 2.5),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')
ax1.annotate('Shortest Range', xy=(2.3, 1), xytext=(3, 0.5),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')

ax1.grid(linestyle='--', alpha=0.5)

# Create a histogram for all expedition durations
ax2.hist(all_durations, bins=10, color='#6a5acd', alpha=0.7, rwidth=0.85)
ax2.set_title('Distribution of Expedition Durations', fontsize=14, fontweight='bold')
ax2.set_xlabel('Duration (Years)', fontsize=12)
ax2.set_ylabel('Frequency', fontsize=12)

# Annotate important findings on histogram
ax2.annotate('Most Common Duration', xy=(4.0, 6), xytext=(5.5, 5),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')

plt.tight_layout()
plt.show()