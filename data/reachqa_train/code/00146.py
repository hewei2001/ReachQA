import matplotlib.pyplot as plt
import numpy as np

# Define extended categories
categories = [
    'Funding', 'Innovation', 'Team Skills', 
    'Market Opportunity', 'Legal Environment', 
    'Cost of Living', 'Networking Opportunities', 'Quality of Life'
]

# Extend the data for more cities
cities_data = {
    'Silicon Valley': [9, 8, 8, 9, 7, 6, 8, 9],
    'Tel Aviv': [7, 9, 8, 8, 6, 7, 8, 7],
    'Berlin': [6, 7, 7, 6, 8, 8, 6, 8],
    'New York': [8, 8, 7, 9, 6, 7, 9, 8],
    'London': [7, 8, 6, 7, 8, 7, 8, 7]
}

# Number of variables we're plotting
num_vars = len(categories)

# Compute angle for each axis and close the radar chart loop
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Start the plot
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Define colors for each city
colors = {
    'Silicon Valley': 'blue',
    'Tel Aviv': 'green',
    'Berlin': 'red',
    'New York': 'purple',
    'London': 'orange'
}

# Add each city's data to the radar chart
for city, data in cities_data.items():
    data += data[:1]  # Ensure the data closes the loop
    ax.fill(angles, data, color=colors[city], alpha=0.25, label=city)
    ax.plot(angles, data, color=colors[city], linewidth=2)

# Remove radial labels for a cleaner look
ax.set_yticklabels([])

# Define and style category labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10, ha='center')

# Add a descriptive multi-line title
plt.title('Comparative Analysis of Start-up Ecosystems\nAcross Major Global Cities', size=15, y=1.1)

# Add a legend with dynamic positioning
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Automatically adjust layout to prevent label overlap
plt.tight_layout()

# Display the radar chart
plt.show()