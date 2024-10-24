import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define cities and key technological domains
cities = ['Arcadia', 'Neonville', 'Solara']
domains = ['Infrastructure', 'Sustainability', 'Security', 'Connectivity', 'Healthcare']

# Technological focus index for each city (out of 100)
arcadia_data = [85, 75, 70, 90, 80]
neonville_data = [70, 90, 80, 85, 75]
solara_data = [80, 70, 85, 75, 90]

# Arrange data into a list
data = [arcadia_data, neonville_data, solara_data]

# Number of variables
N = len(domains)

# Compute angle for each axis
angles = np.linspace(0, 2 * pi, N, endpoint=False).tolist()
angles += angles[:1]  # complete the loop

# Initialize radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Function to plot each city
def plot_city(data, color, label):
    values = data + data[:1]
    ax.plot(angles, values, linewidth=2, linestyle='solid', color=color, label=label)
    ax.fill(angles, values, color=color, alpha=0.25)

# Plot each city's data with a unique color
plot_city(arcadia_data, 'b', 'Arcadia')
plot_city(neonville_data, 'g', 'Neonville')
plot_city(solara_data, 'r', 'Solara')

# Add labels to the chart
plt.xticks(angles[:-1], domains, color='grey', size=10)

# Set y-labels and grid
ax.yaxis.grid(True)
plt.yticks([20, 40, 60, 80, 100], ["20", "40", "60", "80", "100"], color="grey", size=8)
plt.ylim(0, 100)

# Set title and legend
plt.title("Technological Advancements\nin Futuristic Cities", size=15, color='darkblue', weight='bold', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), title='Cities')

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()