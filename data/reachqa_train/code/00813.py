import matplotlib.pyplot as plt
import numpy as np

# Define the years and meditation practices
years = np.arange(2010, 2024)
meditation_practices = ['Mindfulness', 'Transcendental', 'Yoga Nidra']

# Data for each meditation practice in thousands of practitioners
mindfulness_practitioners = np.array([5, 8, 12, 18, 24, 30, 38, 45, 53, 61, 70, 80, 91, 103])
transcendental_practitioners = np.array([3, 5, 7, 10, 14, 18, 23, 28, 34, 41, 49, 58, 68, 79])
yoga_nidra_practitioners = np.array([2, 3, 5, 7, 10, 13, 17, 20, 24, 29, 35, 41, 48, 56])

# Stack data for plotting
practitioner_data = np.vstack([mindfulness_practitioners, transcendental_practitioners, yoga_nidra_practitioners])

# Calculate total practitioners for overlay line plot
total_practitioners = mindfulness_practitioners + transcendental_practitioners + yoga_nidra_practitioners

# Plotting the stacked area chart
fig, ax = plt.subplots(figsize=(12, 8))
colors = ['#6A5ACD', '#FF69B4', '#20B2AA']

# Plot the stackplot
ax.stackplot(years, practitioner_data, labels=meditation_practices, colors=colors, alpha=0.8)

# Overlay line plot for total practitioners
ax.plot(years, total_practitioners, color='black', linestyle='--', linewidth=2, label='Total Practitioners')

# Set titles and labels
ax.set_title('Evolution of Meditation Practices in Urban Communities\n2010-2023 with Total Practitioners Overlay', fontsize=15, weight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Practitioners (in thousands)', fontsize=12)
ax.legend(loc='upper left', fontsize=10)

# Enhance the grid
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add annotations for significant growth phases
ax.annotate('Mindfulness boom', xy=(2015, 18), xytext=(2012, 40),
            arrowprops=dict(facecolor='blue', arrowstyle='->', linewidth=1.5),
            fontsize=9, color='blue')

ax.annotate('Rise of Yoga Nidra', xy=(2020, 29), xytext=(2017, 50),
            arrowprops=dict(facecolor='green', arrowstyle='->', linewidth=1.5),
            fontsize=9, color='green')

ax.annotate('Overall Growth', xy=(2022, 190), xytext=(2018, 160),
            arrowprops=dict(facecolor='black', arrowstyle='->', linewidth=1.5),
            fontsize=9, color='black')

# Adjust the layout to avoid overlapping
plt.tight_layout()

# Display the chart
plt.show()