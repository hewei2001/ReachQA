import matplotlib.pyplot as plt
import numpy as np

# Define years and number of instruments deployed
years = np.array([2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040])
instruments_deployed = np.array([5, 8, 15, 25, 30, 40, 55, 65, 80, 95, 100])

# Define milestones with annotations
milestones = {
    2031: 'First Solar Pass',
    2034: 'Venus Orbit Insertion',
    2037: 'Mars Data Collected',
    2040: 'Jupiter Flyby'
}

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the line chart
ax.plot(years, instruments_deployed, marker='o', linestyle='-', color='tab:blue', linewidth=2, label='Instruments Deployed')

# Annotate milestones on the line
for year, milestone in milestones.items():
    ax.annotate(milestone, 
                xy=(year, instruments_deployed[np.where(years == year)[0][0]]), 
                xytext=(10, -20), 
                textcoords='offset points',
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.3'),
                fontsize=10,
                color='darkred')

# Add titles and labels
ax.set_title('Solar Voyager Mission Timeline\nInstruments Deployed and Key Milestones', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Number of Instruments Deployed', fontsize=12)

# Add a legend
ax.legend(loc='upper left', fontsize=10)

# Customize grid
ax.grid(True, linestyle='--', alpha=0.6)

# Adjust layout to fit annotations and avoid overlapping
plt.tight_layout()

# Display the plot
plt.show()