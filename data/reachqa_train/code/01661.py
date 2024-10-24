import matplotlib.pyplot as plt

# Define the data for the galactic citizenship distribution
citizenship_labels = [
    'Full Citizens', 
    'Temporary Residents', 
    'Probationary Citizens', 
    'Non-Aligned Beings', 
    'Galactic Nomads', 
    'Exiled or Outlawed'
]
citizenship_sizes = [45, 20, 15, 10, 5, 5]

# Define colors for each segment, ensuring good contrast
colors = ['#8ecae6', '#219ebc', '#023047', '#ffb703', '#fb8500', '#d62828']

# Explode the first slice (Full Citizens) slightly to emphasize it
explode = (0.1, 0, 0, 0, 0, 0)

# Create a pie chart
plt.figure(figsize=(12, 8))
plt.pie(citizenship_sizes, explode=explode, labels=citizenship_labels, colors=colors, 
        autopct='%1.1f%%', startangle=140, wedgeprops=dict(edgecolor='w', linewidth=1.5), shadow=True)

# Add a title with thematic emphasis
plt.title('Galactic Citizenship Distribution in the\nGrand Galactic Federation (Year 3085)', 
          fontsize=16, weight='bold', pad=20)

# Display the legend outside the pie chart
plt.legend(citizenship_labels, title="Citizenship Status", bbox_to_anchor=(1.05, 1), loc='upper left')

# Automatically adjust the layout to fit elements within the figure
plt.tight_layout()

# Show the plot
plt.show()