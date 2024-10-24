import matplotlib.pyplot as plt
import numpy as np

# Data
countries = [
    "United States", "Germany", "Canada", "United Kingdom", "Australia",
    "Japan", "South Korea", "France", "China", "India"
]
education_percentages = [
    38.0, 31.0, 28.0, 29.0, 30.0,
    36.0, 34.0, 26.0, 20.0, 12.0
]

# Define colors for the bars
colors = plt.cm.viridis(np.linspace(0, 1, len(countries)))

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot horizontal bars
bars = ax.barh(countries, education_percentages, color=colors, edgecolor='black', height=0.6)

# Add title and labels
ax.set_title('Population with Bachelor\'s Degree or Higher\nacross Various Countries in 2022', fontsize=16, pad=20)
ax.set_xlabel('Percentage (%)', fontsize=12)
ax.set_ylabel('Country', fontsize=12)

# Add grid for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Annotate each bar with the percentage
for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.5, bar.get_y() + bar.get_height()/2,
            f'{width}%', va='center', ha='left', fontsize=10)

# Invert y-axis for better visual hierarchy
ax.invert_yaxis()

# Adjust tick parameters for better alignment and visibility
ax.tick_params(axis='y', which='major', labelsize=10)

# Automatically adjust the layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()