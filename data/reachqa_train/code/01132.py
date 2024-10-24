import matplotlib.pyplot as plt
import numpy as np

# Define marketing channels and their engagement percentages
channels = ['Social Media', 'Email Marketing', 'Content Marketing', 'Pay-Per-Click', 'Influencer Collabs']
engagement_percentages = [40, 15, 25, 10, 10]

# Define expected growth rates for each channel
growth_rates = [5, 3, 4, 2, 6]

# Create a horizontal bar chart
fig, ax1 = plt.subplots(figsize=(12, 8))

# Colors for each channel
bar_colors = ['#4a90e2', '#50e3c2', '#f5a623', '#d0021b', '#9013fe']

# Plot the horizontal bar chart
bars = ax1.barh(channels, engagement_percentages, color=bar_colors, alpha=0.7, label='Engagement (%)')

# Plot the overlay line chart for growth rates
ax2 = ax1.twiny()  # Create a second x-axis on top
ax2.plot(growth_rates, channels, marker='o', color='black', linestyle='--', label='Expected Growth (%)')

# Adding labels and title
ax1.set_xlabel('Engagement Percentage (%)', fontsize=12)
ax2.set_xlabel('Expected Growth Rate (%)', fontsize=12)
ax1.set_title('TechSavvy Inc.: Digital Marketing Engagement and Expected Growth in 2023', fontsize=14, fontweight='bold', pad=15)

# Display percentage labels on bars
for bar in bars:
    width = bar.get_width()
    ax1.text(width + 1, bar.get_y() + bar.get_height()/2, f'{width}%', va='center', fontsize=10, color='black')

# Display growth rate labels on line plot
for i, rate in enumerate(growth_rates):
    ax2.text(rate + 0.2, i, f'{rate}%', va='center', fontsize=10, color='black')

# Invert y-axis to display the first element at the top
ax1.invert_yaxis()

# Add grid lines for the engagement percentage
ax1.xaxis.grid(True, linestyle='--', alpha=0.6)

# Set x-axis limits
ax1.set_xlim(0, 100)
ax2.set_xlim(0, max(growth_rates) + 2)

# Adjust layout to fit everything neatly
plt.tight_layout()

# Add legends
ax1.legend(loc='lower right', fontsize=10, frameon=False)
ax2.legend(loc='upper right', fontsize=10, frameon=False)

# Show plot
plt.show()