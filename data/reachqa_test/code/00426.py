import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Set Seaborn style for the plot
sns.set(style='darkgrid')

# Define the weeks
weeks = np.arange(1, 9)

# Adjusted average heights of plants (in cm) under different light conditions
sunlight_heights = np.array([5, 10, 17, 24, 30, 35, 39, 42])
led_heights = np.array([4, 9, 15, 22, 27, 32, 36, 39])
fluorescent_heights = np.array([3, 8, 14, 20, 25, 29, 32, 34])

# Adjusted standard deviations for clearer error bands
sunlight_error = np.array([0.5, 0.6, 0.8, 1.0, 1.2, 1.3, 1.5, 1.7])
led_error = np.array([0.4, 0.5, 0.7, 0.9, 1.1, 1.2, 1.4, 1.6])
fluorescent_error = np.array([0.3, 0.4, 0.6, 0.8, 1.0, 1.1, 1.3, 1.4])

# Initialize the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot each light condition with error bands
ax.fill_between(weeks, sunlight_heights - sunlight_error, sunlight_heights + sunlight_error, color='#FFD700', alpha=0.2)
ax.plot(weeks, sunlight_heights, 'o-', label='Sunlight', color='#FFD700', linewidth=2, markersize=6)

ax.fill_between(weeks, led_heights - led_error, led_heights + led_error, color='#1E90FF', alpha=0.2)
ax.plot(weeks, led_heights, 's--', label='LED Light', color='#1E90FF', linewidth=2, markersize=6)

ax.fill_between(weeks, fluorescent_heights - fluorescent_error, fluorescent_heights + fluorescent_error, color='#32CD32', alpha=0.2)
ax.plot(weeks, fluorescent_heights, '^-.', label='Fluorescent Light', color='#32CD32', linewidth=2, markersize=6)

# Annotate the maximum growth points
ax.annotate('Max: 42 cm', xy=(8, 42), xytext=(6, 44),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=12, color='black')
ax.annotate('Max: 39 cm', xy=(8, 39), xytext=(6, 37),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=12, color='black')
ax.annotate('Max: 34 cm', xy=(8, 34), xytext=(6, 32),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=12, color='black')

# Set labels and title
ax.set_xlabel('Weeks', fontsize=14)
ax.set_ylabel('Average Plant Height (cm)', fontsize=14)
ax.set_title('Plant Growth under Different Light Conditions\n(8-Week Study)', fontsize=16, fontweight='bold')

# Add legend
ax.legend(title="Light Conditions", fontsize=12, title_fontsize=14)

# Customize ticks
ax.set_xticks(weeks)
ax.set_yticks(range(0, 50, 5))

# Add grid for better readability
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()