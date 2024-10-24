import matplotlib.pyplot as plt

# Define data for three cities
cities = ['Urbania', 'Metropolis', 'Greenfield']
park_sizes = [15, 22, 35, 45, 55, 25, 33, 40, 20, 30, 50, 60]
bird_species_count = {
    'Urbania': [12, 18, 26, 34],
    'Metropolis': [15, 19, 28, 36],
    'Greenfield': [10, 20, 30, 40]
}

# Extract corresponding data for each city
urbania_sizes = park_sizes[:4]
metropolis_sizes = park_sizes[4:8]
greenfield_sizes = park_sizes[8:]

# Create scatter plot
fig, ax = plt.subplots(figsize=(12, 8))

ax.scatter(urbania_sizes, bird_species_count['Urbania'], color='blue', s=100, label='Urbania', alpha=0.7, marker='o')
ax.scatter(metropolis_sizes, bird_species_count['Metropolis'], color='green', s=100, label='Metropolis', alpha=0.7, marker='s')
ax.scatter(greenfield_sizes, bird_species_count['Greenfield'], color='orange', s=100, label='Greenfield', alpha=0.7, marker='^')

# Set plot title and labels
ax.set_title("The Flight of Colors:\nBird Species Diversity in Urban Green Spaces", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel("Park Size (acres)", fontsize=14)
ax.set_ylabel("Number of Bird Species", fontsize=14)

# Customize grid and legend
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(title='Cities', loc='upper left', fontsize=12)

# Annotate a few data points for emphasis
annotations = ['U', 'M', 'G']
for j, (sizes, species_list, color, label_prefix) in enumerate(zip(
    [urbania_sizes, metropolis_sizes, greenfield_sizes], 
    bird_species_count.values(), 
    ['blue', 'green', 'orange'],
    annotations
)):
    for i, (size, species) in enumerate(zip(sizes, species_list)):
        ax.text(size, species + 0.5, f'{label_prefix}{i+1}', fontsize=10, ha='center', color=color)

# Adjust layout for clarity
plt.tight_layout()

# Display the plot
plt.show()