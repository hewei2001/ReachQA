import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib.patches as mpatches

# Define the time periods
eras = ['Ancient Era\n(5000 BC)', 'Medieval Era\n(1000 AD)', 
        'Industrial Revolution\n(1800)', 'Modern Era\n(2020)']

# Approximate dietary composition percentages for each era
proteins = [10, 15, 20, 25]
carbohydrates = [50, 40, 35, 30]
fats = [15, 20, 25, 30]
vegetables = [25, 25, 20, 15]

# Stack the data
data = np.array([proteins, carbohydrates, fats, vegetables])
x = np.arange(len(eras))

# Create figure and subplots
fig, ax = plt.subplots(1, 2, figsize=(16, 7), gridspec_kw={'width_ratios': [3, 1.5]})

# Color palette
colors = sns.color_palette("muted", n_colors=4)

# Plot the stacked area chart on the first subplot
ax[0].stackplot(x, data, labels=['Proteins', 'Carbohydrates', 'Fats', 'Vegetables'],
                colors=colors, alpha=0.8)

# Customize the plot
ax[0].set_title('The Evolution of Culinary Cultures\nThrough the Ages', fontsize=16, fontweight='bold', loc='center')
ax[0].set_xlabel('Time Period', fontsize=12)
ax[0].set_ylabel('Dietary Composition (%)', fontsize=12)
ax[0].set_xlim(0, len(eras) - 1)
ax[0].set_ylim(0, 100)
ax[0].set_xticks(x)
ax[0].set_xticklabels(eras, rotation=30, ha='right', fontsize=10)
ax[0].grid(True, linestyle='--', alpha=0.5)

# Add legend and annotations
legend_handles = [mpatches.Patch(color=colors[i], label=label) for i, label in enumerate(['Proteins', 'Carbohydrates', 'Fats', 'Vegetables'])]
ax[0].legend(handles=legend_handles, loc='upper left', bbox_to_anchor=(1, 1), fontsize=10, title="Food Components")

# Annotations to highlight trends
ax[0].annotate('Increased Proteins', xy=(3, 25), xytext=(2, 45),
               arrowprops=dict(facecolor='black', shrink=0.05), fontsize=9, color='black')
ax[0].annotate('Decreased Vegetables', xy=(3, 15), xytext=(2, 10),
               arrowprops=dict(facecolor='black', shrink=0.05), fontsize=9, color='black')

# Plotting individual component trends in the second subplot
components = [proteins, carbohydrates, fats, vegetables]
component_names = ['Proteins', 'Carbohydrates', 'Fats', 'Vegetables']

for i, component in enumerate(components):
    ax[1].plot(x, component, marker='o', linestyle='-', color=colors[i], label=component_names[i])

# Customize the subplot
ax[1].set_title('Detailed Component Trends', fontsize=14, fontweight='bold')
ax[1].set_xticks(x)
ax[1].set_xticklabels(eras, rotation=30, ha='right', fontsize=10)
ax[1].set_xlabel('Time Period', fontsize=12)
ax[1].set_ylabel('Percentage (%)', fontsize=12)
ax[1].set_ylim(0, 50)
ax[1].legend(loc='upper right', fontsize=10)
ax[1].grid(True, linestyle='--', alpha=0.5)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()