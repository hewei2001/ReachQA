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

# Additional data for secondary y-axis: hypothetical mission budget (in million USD)
mission_budget = np.array([50, 55, 60, 65, 80, 100, 120, 150, 180, 210, 250])

# Set up the plot with dual y-axes
fig, ax1 = plt.subplots(figsize=(14, 8))
ax2 = ax1.twinx()

# Plot the primary line chart for instruments deployed
ax1.plot(years, instruments_deployed, marker='o', linestyle='-', color='tab:blue', linewidth=2, label='Instruments Deployed')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Number of Instruments Deployed', fontsize=12, color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Plot the secondary line chart for mission budget
ax2.plot(years, mission_budget, marker='s', linestyle='--', color='tab:green', linewidth=2, label='Mission Budget (Million USD)')
ax2.set_ylabel('Mission Budget (Million USD)', fontsize=12, color='tab:green')
ax2.tick_params(axis='y', labelcolor='tab:green')

# Annotate milestones with different markers
for year, milestone in milestones.items():
    idx = np.where(years == year)[0][0]
    ax1.annotate(milestone, 
                 xy=(year, instruments_deployed[idx]), 
                 xytext=(10, -30), 
                 textcoords='offset points',
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.3'),
                 fontsize=10,
                 color='darkred')
    ax1.scatter(year, instruments_deployed[idx], color='red', zorder=5)

# Add a title
ax1.set_title('Solar Voyager Mission Timeline\nInstruments Deployed and Budget Over the Years', 
              fontsize=16, fontweight='bold', pad=20)

# Add legends for both y-axes
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=10)

# Add shaded regions to highlight periods
ax1.axvspan(2033, 2035, alpha=0.1, color='purple', label='High Activity Period')
ax1.axvspan(2038, 2040, alpha=0.1, color='orange', label='Critical Milestones')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()