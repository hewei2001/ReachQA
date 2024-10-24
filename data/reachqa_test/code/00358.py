import matplotlib.pyplot as plt
import numpy as np

# Data construction
industries = ['Finance', 'Healthcare', 'Manufacturing', 'Retail', 'Technology', 'Education', 'Energy', 'Transportation']
years = list(range(2014, 2022))  # years from 2014 to 2021
ai_adoption_rates = np.array([
    [80, 75, 90, 85, 78, 92, 88, 95],
    [60, 65, 70, 72, 68, 75, 80, 82],
    [40, 45, 50, 52, 48, 55, 60, 62],
    [30, 35, 40, 42, 38, 45, 50, 52],
    [95, 98, 99, 97, 96, 99, 100, 98],
    [20, 25, 30, 32, 28, 35, 40, 42],
    [50, 55, 60, 62, 58, 65, 70, 72],
    [35, 40, 45, 47, 43, 50, 55, 57]
])

# Create figure and axis
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Plot heatmap
im = ax1.imshow(ai_adoption_rates, cmap='viridis', interpolation='nearest', aspect='auto')

# Set title and labels
ax1.set_title("Embracing the Future:\nAI Adoption Rates Across Industries (2014-2021)")
ax1.set_xlabel("Years")
ax1.set_ylabel("Industries")

# Set x-axis tick labels
ax1.set_xticks(np.arange(len(years)))
ax1.set_xticklabels([str(year) for year in years], rotation=45, ha='right')

# Set y-axis tick labels
ax1.set_yticks(np.arange(len(industries)))
ax1.set_yticklabels(industries, rotation=0, ha='right')

# Create color bar
cbar = fig.colorbar(im, ax=ax1, shrink=0.5)
cbar.set_label('AI Adoption Rate (%)', rotation=90, labelpad=15)

# Plot bar chart
ax2.bar(industries, np.mean(ai_adoption_rates, axis=1), color='skyblue')
ax2.set_title("Average AI Adoption Rate by Industry")
ax2.set_xlabel("Industries")
ax2.set_ylabel("Average AI Adoption Rate (%)")

# Adjust layout to avoid occlusion
plt.tight_layout(rect=[0, 0, 1, 0.9])

# Show plot
plt.show()