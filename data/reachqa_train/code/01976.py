import matplotlib.pyplot as plt
import numpy as np

# Define data for break times and corresponding efficiency scores
break_times = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55])
efficiency_scores = np.array([68, 72, 75, 77, 79, 78, 76, 74, 71, 70])

# Calculate polynomial fitting to smooth the data
coefficients = np.polyfit(break_times, efficiency_scores, 2)
polynomial = np.poly1d(coefficients)

# Generate a range of break times for plotting the smooth curve
break_times_smooth = np.linspace(break_times.min(), break_times.max(), 200)
efficiency_smooth = polynomial(break_times_smooth)

# Create a scatter plot
plt.figure(figsize=(12, 7))
plt.scatter(break_times, efficiency_scores, color='navy', label='Efficiency Data', s=100, alpha=0.8)

# Plot the smooth fitting curve
plt.plot(break_times_smooth, efficiency_smooth, color='tomato', label='Smooth Fit Curve', linewidth=2)

# Customize chart elements
plt.title('Influence of Break Duration on Employee Efficiency\nat OptimaTech', fontsize=16, fontweight='bold')
plt.xlabel('Break Time (minutes)', fontsize=14)
plt.ylabel('Efficiency Score', fontsize=14)
plt.legend(loc='upper right', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# Highlight the peak efficiency point
peak_efficiency_time = break_times[np.argmax(efficiency_scores)]
peak_efficiency_score = np.max(efficiency_scores)
plt.annotate(f'Peak Efficiency\n({peak_efficiency_time} mins, {peak_efficiency_score} score)',
             xy=(peak_efficiency_time, peak_efficiency_score),
             xytext=(peak_efficiency_time + 5, peak_efficiency_score - 5),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, color='black')

# Automatically adjust layout for better spacing
plt.tight_layout()

# Show the plot
plt.show()