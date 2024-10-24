import matplotlib.pyplot as plt
import squarify

# Define the sectors and their respective budget allocations in billions of dollars
sectors = [
    'Healthcare\n$220B', 'Education\n$150B', 
    'Infrastructure\n$180B', 'Defense\n$250B', 
    'Technology\n$100B', 'Environmental\nProtection\n$100B'
]
budget_allocation = [220, 150, 180, 250, 100, 100]

# Define colors for each sector
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700', '#FF6F61']

# Healthcare sector breakdown (subset data for new plot)
healthcare_categories = ['Hospitals\n$100B', 'Research\n$60B', 'Insurance\n$40B', 'Public Health\n$20B']
healthcare_allocation = [100, 60, 40, 20]
healthcare_colors = ['#FFC0CB', '#FF69B4', '#FF1493', '#DB7093']

# Create a figure with subplots
fig, axes = plt.subplots(1, 2, figsize=(18, 8))

# Plot the treemap on the first subplot
squarify.plot(ax=axes[0], sizes=budget_allocation, label=sectors, color=colors, alpha=.8,
              edgecolor="white", linewidth=2, text_kwargs={'fontsize': 10, 'weight': 'bold'})
axes[0].set_title('Econlandia Government Annual Budget Distribution\n(in Billions)', fontsize=14, fontweight='bold', pad=20)
axes[0].axis('off')  # Hide axes for a cleaner look

# Plot the pie chart on the second subplot
axes[1].pie(healthcare_allocation, labels=healthcare_categories, colors=healthcare_colors,
            startangle=140, autopct='%1.1f%%', pctdistance=0.85, textprops={'fontsize': 10, 'weight': 'bold'})
# Draw a circle at the center to turn pie into a donut
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)
axes[1].set_title('Detailed Breakdown of Healthcare Budget', fontsize=14, fontweight='bold', pad=20)

# Adjust the layout to ensure all elements are well-positioned
plt.tight_layout()

# Display the chart
plt.show()