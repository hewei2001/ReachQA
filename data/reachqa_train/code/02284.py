import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.array(range(1990, 2021))

# Emphasis scores for each philosophy
stoicism = np.array([10, 12, 13, 15, 16, 18, 21, 24, 27, 30, 33, 35, 37, 40, 42, 45, 48, 52, 55, 58, 61, 63, 65, 68, 70, 73, 75, 77, 80, 83, 85])
confucianism = np.array([20, 21, 23, 25, 26, 29, 32, 35, 37, 39, 42, 45, 47, 50, 53, 55, 58, 60, 63, 66, 68, 71, 73, 75, 77, 80, 82, 84, 87, 90, 92])
taoism = np.array([15, 16, 17, 19, 21, 23, 25, 28, 31, 33, 35, 38, 40, 43, 46, 48, 51, 53, 56, 59, 61, 63, 66, 68, 70, 72, 75, 77, 80, 82, 84])
epicureanism = np.array([5, 7, 8, 9, 11, 13, 16, 18, 21, 23, 26, 28, 30, 33, 36, 39, 41, 43, 46, 49, 51, 54, 56, 59, 62, 64, 67, 69, 72, 74, 77])
platonism = np.array([25, 27, 29, 31, 33, 35, 38, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70, 73, 75, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98])

# Plotting
plt.figure(figsize=(14, 8))

# Plot each philosophy's emphasis score
plt.plot(years, stoicism, marker='o', label='Stoicism', linestyle='-', linewidth=2, color='teal')
plt.plot(years, confucianism, marker='s', label='Confucianism', linestyle='--', linewidth=2, color='gold')
plt.plot(years, taoism, marker='^', label='Taoism', linestyle='-.', linewidth=2, color='purple')
plt.plot(years, epicureanism, marker='x', label='Epicureanism', linestyle=':', linewidth=2, color='crimson')
plt.plot(years, platonism, marker='d', label='Platonism', linestyle='-', linewidth=2, color='navy')

# Customize the chart
plt.title('Revival of Ancient Philosophies:\nA Modern Interpretation (1990-2020)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Emphasis Score', fontsize=14)
plt.xticks(np.arange(1990, 2021, 5))
plt.yticks(np.arange(0, 101, 10))
plt.grid(True, linestyle='--', alpha=0.6)

# Add a legend
plt.legend(loc='upper left', fontsize=12)

# Ensure layout is not cut off
plt.tight_layout()

# Display the plot
plt.show()