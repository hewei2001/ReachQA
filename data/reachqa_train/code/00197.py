import matplotlib.pyplot as plt
import squarify

# Define data for research grant allocations (in millions of dollars)
technology_sectors = ['Artificial Intelligence', 'Quantum Computing', 'Renewable Energy', 'Biotechnology', 'Nanotechnology']
grant_allocations = [450, 300, 500, 350, 250]

# Calculate the total grant allocation for percentage calculations
total_allocation = sum(grant_allocations)

# Create labels with allocation values and percentages
labels = [f"{sector}\n${value}M\n({value / total_allocation * 100:.1f}%)"
          for sector, value in zip(technology_sectors, grant_allocations)]

# Color palette for each sector
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Plotting the treemap
fig, ax = plt.subplots(figsize=(12, 8))
squarify.plot(sizes=grant_allocations, label=labels, color=colors, alpha=0.8, ax=ax, text_kwargs={'fontsize': 10, 'weight': 'bold', 'wrap': True})

# Set title with clear description
plt.title('Distribution of Research Grants in Emerging Technologies:\nA Sectoral Analysis', fontsize=18, fontweight='bold')

# Remove axes for better visualization
plt.axis('off')

# Adjust layout for readability
plt.tight_layout()

# Display the plot
plt.show()