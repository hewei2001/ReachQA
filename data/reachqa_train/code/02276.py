import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define test phases and achieved speeds for each team
test_phases = np.array([1, 2, 3, 4, 5, 6, 7, 8])
alpha_speeds = np.array([150, 220, 280, 320, 400, 450, 480, 500])
beta_speeds = np.array([130, 200, 250, 310, 350, 420, 470, 490])
gamma_speeds = np.array([140, 210, 270, 330, 380, 440, 460, 480])

# Calculate the average speed for each team across the test phases
avg_speeds = {
    'Alpha': np.mean(alpha_speeds),
    'Beta': np.mean(beta_speeds),
    'Gamma': np.mean(gamma_speeds),
}

# Generate smooth curves using spline interpolation
smooth_x = np.linspace(test_phases.min(), test_phases.max(), 300)
alpha_smooth = make_interp_spline(test_phases, alpha_speeds)(smooth_x)
beta_smooth = make_interp_spline(test_phases, beta_speeds)(smooth_x)
gamma_smooth = make_interp_spline(test_phases, gamma_speeds)(smooth_x)

# Create the figure with two subplots
fig, ax = plt.subplots(1, 2, figsize=(18, 8))

# Plot 1: Line plot with scatter points
ax[0].scatter(test_phases, alpha_speeds, color='red', label='Team Alpha', s=100, alpha=0.7)
ax[0].scatter(test_phases, beta_speeds, color='green', label='Team Beta', s=100, alpha=0.7)
ax[0].scatter(test_phases, gamma_speeds, color='blue', label='Team Gamma', s=100, alpha=0.7)
ax[0].plot(smooth_x, alpha_smooth, color='red', linestyle='-', linewidth=2)
ax[0].plot(smooth_x, beta_smooth, color='green', linestyle='-', linewidth=2)
ax[0].plot(smooth_x, gamma_smooth, color='blue', linestyle='-', linewidth=2)

# Titles and labels for the first plot
ax[0].set_title('The Race for Speed:\nHyperloop Testing Phases', fontsize=14, fontweight='bold', pad=20)
ax[0].set_xlabel('Test Phase', fontsize=12)
ax[0].set_ylabel('Max Achieved Speed (km/h)', fontsize=12)
ax[0].set_xticks(test_phases)
ax[0].set_yticks(np.arange(100, 550, 50))
ax[0].legend(title='Hyperloop Teams', fontsize=10)
ax[0].grid(linestyle='--', alpha=0.7)

# Annotations for key milestones in the first plot
annotations = [
    (8, 500, 'Team Alpha: 500 km/h!'),
    (8, 490, 'Team Beta: 490 km/h'),
    (8, 480, 'Team Gamma: 480 km/h')
]
for (phase, speed, text) in annotations:
    ax[0].annotate(text, xy=(phase, speed), xytext=(phase + 0.5, speed + 10),
                   arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='gray'),
                   fontsize=9, bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightyellow', alpha=0.5))

# Plot 2: Bar plot showing the average speed for each team
ax[1].bar(avg_speeds.keys(), avg_speeds.values(), color=['red', 'green', 'blue'], alpha=0.7)
ax[1].set_title('Average Speed Across Test Phases', fontsize=14, fontweight='bold', pad=10)
ax[1].set_xlabel('Teams', fontsize=12)
ax[1].set_ylabel('Average Speed (km/h)', fontsize=12)
ax[1].set_yticks(np.arange(100, 550, 50))
ax[1].grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust the layout to prevent overlapping elements
plt.tight_layout()
plt.show()