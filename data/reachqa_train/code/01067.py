import matplotlib.pyplot as plt

# Data setup for sector pie chart
initiatives = [
    'Ocean Floor Mapping',
    'Marine Biodiversity Research',
    'Deep Sea Habitats Study',
    'Coral Reef Restoration',
    'Sustainable Fisheries Management',
    'Ocean Pollution Reduction'
]

# Funding distribution in percentage (must sum to 100)
funding_percentages = [25, 20, 15, 10, 18, 12]

# Color palette for the pie chart
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Explode the largest sector to highlight it
explode = (0.1, 0, 0, 0, 0, 0)

# Plotting the sector pie chart
fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))

# Plot pie chart
wedges, texts, autotexts = ax.pie(
    funding_percentages,
    explode=explode,
    labels=initiatives,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    textprops=dict(color="w")
)

# Add title
plt.title('Global Ocean Exploration Funding Distribution - 2023', size=15, color='navy', pad=20)

# Adjust label and percentage text
plt.setp(texts, size=9, weight="bold")
plt.setp(autotexts, size=10, weight="bold")

# Add legend outside the pie
ax.legend(
    wedges, initiatives,
    title="Initiatives",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1)
)

# Ensure plot is centered and well spaced
plt.tight_layout()

# Display the plot
plt.show()