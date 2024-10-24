import matplotlib.pyplot as plt
import numpy as np

# Seasons
seasons = ['Spring', 'Summer', 'Autumn', 'Winter']

# Population sizes for each butterfly species per season
golden_monarch = [150, 300, 250, 200]
azure_wing = [200, 150, 300, 100]
crimson_admiral = [100, 250, 150, 250]

# Prepare data for the stacked area chart
species_data = np.array([golden_monarch, azure_wing, crimson_admiral])

# Plot the stacked area chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(seasons, species_data, labels=['Golden Monarch', 'Azure Wing', 'Crimson Admiral'],
             colors=['gold', 'skyblue', 'crimson'], alpha=0.8)

# Customizing the chart
ax.set_title("Migration Patterns of Butterfly Species\nin the Enchanted Forest", fontsize=16, pad=20)
ax.set_xlabel("Seasons", fontsize=12)
ax.set_ylabel("Population Size", fontsize=12)
ax.legend(title='Butterfly Species', loc='upper left', bbox_to_anchor=(1, 1))

# Annotate significant changes
ax.annotate('Peak Population', xy=('Summer', 300), xytext=('Summer', 350),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Adding grid lines for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Rotate x-axis labels to avoid overlap
plt.xticks(rotation=45)

# Adjust layout for a neat look
plt.tight_layout()

# Show plot
plt.show()