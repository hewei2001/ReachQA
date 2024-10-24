import matplotlib.pyplot as plt
import numpy as np

# Define years from 2015 to 2023
years = np.array(range(2015, 2024))

# Define market shares for each platform
netflix = np.array([50, 48, 45, 42, 40, 38, 35, 33, 30])
amazon_prime = np.array([20, 22, 23, 24, 25, 26, 27, 28, 29])
disney_plus = np.array([0, 0, 0, 0, 5, 10, 15, 18, 20])
hulu = np.array([10, 9, 8, 8, 7, 7, 7, 7, 7])
others = np.array([20, 21, 24, 26, 23, 19, 16, 14, 14])

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(10, 6))

ax.stackplot(years, netflix, amazon_prime, disney_plus, hulu, others, labels=[
    'Netflix', 'Amazon Prime Video', 'Disney+', 'Hulu', 'Others'],
    colors=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#C2C2C2'], alpha=0.8)

# Set titles and labels
ax.set_title('Market Share of Streaming Platforms\n(2015-2023)', fontsize=16)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Market Share (%)', fontsize=12)

# Rotate x-axis labels to avoid overlapping
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Add a legend outside of the plot to prevent occlusion
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title="Platforms")

# Automatically adjust layout for best fit
plt.tight_layout(rect=[0, 0, 0.85, 1])  # Leave space on the right for the legend

# Show plot
plt.show()