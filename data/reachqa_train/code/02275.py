import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define test phases and achieved speeds for each team
test_phases = np.array([1, 2, 3, 4, 5, 6, 7, 8])
alpha_speeds = np.array([150, 220, 280, 320, 400, 450, 480, 500])
beta_speeds = np.array([130, 200, 250, 310, 350, 420, 470, 490])
gamma_speeds = np.array([140, 210, 270, 330, 380, 440, 460, 480])

# Generate smooth curves using spline interpolation
smooth_x = np.linspace(test_phases.min(), test_phases.max(), 300)
alpha_smooth = make_interp_spline(test_phases, alpha_speeds)(smooth_x)
beta_smooth = make_interp_spline(test_phases, beta_speeds)(smooth_x)
gamma_smooth = make_interp_spline(test_phases, gamma_speeds)(smooth_x)

# Create the scatter plot
plt.figure(figsize=(14, 8))
plt.scatter(test_phases, alpha_speeds, color='red', label='Team Alpha', s=100, alpha=0.7)
plt.scatter(test_phases, beta_speeds, color='green', label='Team Beta', s=100, alpha=0.7)
plt.scatter(test_phases, gamma_speeds, color='blue', label='Team Gamma', s=100, alpha=0.7)

# Plot smooth fitting curves
plt.plot(smooth_x, alpha_smooth, color='red', linestyle='-', linewidth=2)
plt.plot(smooth_x, beta_smooth, color='green', linestyle='-', linewidth=2)
plt.plot(smooth_x, gamma_smooth, color='blue', linestyle='-', linewidth=2)

# Adding titles and labels
plt.title('The Race for Speed:\nHyperloop Testing Phases', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Test Phase', fontsize=14)
plt.ylabel('Max Achieved Speed (km/h)', fontsize=14)
plt.xticks(test_phases)
plt.yticks(np.arange(100, 550, 50))

# Adding a legend
plt.legend(title='Hyperloop Teams', fontsize=12)

# Adding annotations for key milestones
annotations = [
    (8, 500, 'Team Alpha: 500 km/h!'),
    (8, 490, 'Team Beta: 490 km/h'),
    (8, 480, 'Team Gamma: 480 km/h')
]
for (phase, speed, text) in annotations:
    plt.annotate(text, xy=(phase, speed), xytext=(phase + 0.5, speed + 10),
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='gray'),
                 fontsize=10, bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightyellow', alpha=0.5))

# Display the plot with adjustments to prevent overlap
plt.grid(linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()