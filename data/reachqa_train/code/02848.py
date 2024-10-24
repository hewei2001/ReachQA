import matplotlib.pyplot as plt

# Define energy sources and their allocations
energy_sources = ['Solar Power', 'Wind Energy', 'Hydro Power', 'Geothermal Energy', 'Biomass', 'Wave Energy']
allocations = [30, 25, 20, 10, 10, 5]  # in percentage

# Define a color palette for each energy source
colors = ['#FFD700', '#32CD32', '#1E90FF', '#FF8C00', '#8B4513', '#4682B4']

# Create the ring chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(aspect="equal"))

# Plot the data with specific wedge properties to form a ring
wedges, texts, autotexts = ax.pie(
    allocations,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    textprops=dict(size=12, weight='bold')
)

# Enhance the chart with a central label to utilize inner space
ax.text(0, 0, 'Neoterra\n2125', horizontalalignment='center', verticalalignment='center',
        fontsize=18, fontweight='bold', color='grey')

# Set the title with a multi-line approach for clarity
ax.set_title("Renewable Energy Resource Allocation\nin Neoterra, 2125",
             fontsize=16, fontweight='bold', pad=30)

# Optimize layout to prevent text overlap
plt.tight_layout()

# Show the plot
plt.show()