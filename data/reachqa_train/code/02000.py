import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2010, 2026)

# Artificial data for AI academic interest over the years
machine_learning = [5, 8, 12, 18, 24, 32, 41, 51, 60, 70, 81, 92, 105, 119, 134, 150]
natural_language_processing = [2, 3, 4, 5, 8, 10, 13, 18, 24, 30, 38, 46, 55, 65, 76, 88]
robotics = [3, 4, 6, 8, 11, 15, 19, 24, 30, 36, 42, 49, 57, 65, 74, 84]
computer_vision = [1, 2, 3, 5, 7, 10, 14, 19, 25, 32, 40, 49, 59, 70, 82, 95]
ai_ethics = [0, 0, 1, 2, 4, 6, 9, 13, 18, 24, 31, 39, 48, 58, 69, 81]

# Combine datasets for stackplot
ai_domains = np.array([machine_learning, natural_language_processing, robotics, computer_vision, ai_ethics])

# Create a figure
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the stacked area chart
ax.stackplot(years, ai_domains, labels=['Machine Learning', 'NLP', 'Robotics', 'Computer Vision', 'AI Ethics'],
             colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], alpha=0.8)

# Title and labels
ax.set_title("Evolution of AI Domains in Academia\n(2010-2025)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Number of Programs and Projects", fontsize=14)

# X-axis configuration
ax.set_xticks(years[::2])
ax.set_xticklabels(years[::2], rotation=45)

# Add grid lines and legend
ax.grid(alpha=0.3, linestyle='--')
ax.legend(loc='upper left', fontsize=12, title='AI Domains')

# Use tight layout to prevent overlapping
plt.tight_layout()

# Show plot
plt.show()