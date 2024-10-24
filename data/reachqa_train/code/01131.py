import matplotlib.pyplot as plt

# Define the marketing channels and their engagement percentages
channels = ['Social Media', 'Email Marketing', 'Content Marketing', 'Pay-Per-Click', 'Influencer Collabs']
engagement_percentages = [40, 15, 25, 10, 10]

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 6))

# Colors for each channel
colors = ['#4a90e2', '#50e3c2', '#f5a623', '#d0021b', '#9013fe']

# Plotting the data
bars = ax.barh(channels, engagement_percentages, color=colors)

# Adding labels and title
ax.set_xlabel('Engagement Percentage (%)', fontsize=12)
ax.set_title('TechSavvy Inc.:\nDigital Marketing Engagement in 2023', fontsize=14, fontweight='bold', pad=15)

# Display percentage labels on bars
for bar in bars:
    width = bar.get_width()
    ax.text(width + 2, bar.get_y() + bar.get_height()/2,
            f'{width}%', va='center', fontsize=10, color='black')

# Invert y-axis to display the first element at the top
ax.invert_yaxis()

# Set grid lines for readability
ax.xaxis.grid(True, linestyle='--', alpha=0.6)

# Set x-axis limit to 0-100 to represent percentages
ax.set_xlim(0, 100)

# Adjust layout to fit everything neatly
plt.tight_layout()

# Show plot
plt.show()