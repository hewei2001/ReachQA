import matplotlib.pyplot as plt

# Define the species and their diet compositions
species = ['Azure Parrot', 'Golden Tamarin', 'Violet Fox']
diet_labels = ['Fruits', 'Insects', 'Leaves', 'Nectar']

# Diet data representing percentage compositions
azure_parrot_diet = [50, 20, 15, 15]
golden_tamarin_diet = [40, 30, 20, 10]
violet_fox_diet = [25, 40, 30, 5]

diet_data = [azure_parrot_diet, golden_tamarin_diet, violet_fox_diet]

# Colors for each segment
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']

# Create figure and subplots
fig, axs = plt.subplots(1, 3, figsize=(18, 6), subplot_kw=dict(aspect="equal"))

# Plot each ring chart
for i, ax in enumerate(axs):
    wedges, texts, autotexts = ax.pie(
        diet_data[i], 
        colors=colors, 
        labels=diet_labels, 
        autopct='%1.1f%%', 
        startangle=140, 
        pctdistance=0.85, 
        wedgeprops=dict(width=0.3, edgecolor='w'),
        textprops=dict(color="black")
    )
    
    # Add a central label to enhance the ring effect
    ax.text(0, 0, species[i], ha='center', va='center', fontsize=12, fontweight='bold')

    # Ensure equal aspect ratio to make the circle round
    ax.axis('equal')
    ax.set_title(f'{species[i]} Diet', fontsize=14, weight='bold', pad=10)

# Add the main title for all charts
plt.suptitle(
    'Diet Composition of Endangered Wildlife Species\nin Mystical Forest Reserve', 
    fontsize=16, 
    weight='bold'
)

# Add a legend below the plots
fig.legend(wedges, diet_labels, loc='lower center', ncol=4, bbox_to_anchor=(0.5, -0.05), fontsize=12)

# Automatically adjust the layout to prevent overlaps
plt.tight_layout(rect=[0, 0.1, 1, 0.9])

# Display the plot
plt.show()