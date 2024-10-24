import matplotlib.pyplot as plt

# Expanded data for a more complex chart
spice_data = {
    'India': {'Aromatic': {'Turmeric': 30, 'Cumin': 25, 'Coriander': 20, 'Mustard Seed': 15, 'Cardamom': 10}},
    'Mexico': {'Hot': {'Chili': 25, 'Cumin': 25, 'Oregano': 20, 'Garlic': 15, 'Cinnamon': 15}},
    'Italy': {'Herbs': {'Basil': 40, 'Oregano': 30, 'Rosemary': 15, 'Thyme': 10, 'Garlic': 5}},
    'Morocco': {'Exotic': {'Saffron': 35, 'Cinnamon': 25, 'Cumin': 20, 'Paprika': 10, 'Ginger': 10}},
    'China': {'Fragrant': {'Star Anise': 30, 'Sichuan Pepper': 20, 'Ginger': 20, 'Garlic': 15, 'Clove': 15}}
}

# Select regions to visualize
selected_regions = ['India', 'Mexico']

fig, axes = plt.subplots(1, len(selected_regions), figsize=(12, 8))
colors = {
    'India': ['#F4A460', '#FFD700', '#DAA520', '#8B4513', '#D2691E'],
    'Mexico': ['#FF6347', '#E9967A', '#8B0000', '#FF4500', '#FF6347']
}

for i, region in enumerate(selected_regions):
    category = list(spice_data[region].keys())[0]
    spices, usage_percentage = zip(*spice_data[region][category].items())
    
    wedges, texts, autotexts = axes[i].pie(
        usage_percentage,
        labels=spices,
        autopct='%1.1f%%',
        startangle=140,
        colors=colors[region],
        wedgeprops={'edgecolor': 'black'},
        explode=[0.1] + [0] * (len(spices) - 1)
    )
    
    axes[i].set_title(f"{region}'s Spice Usage\n({category} Spices)", fontsize=14, fontweight='bold')
    for text in texts:
        text.set_fontsize(10)
    for autotext in autotexts:
        autotext.set_fontsize(8)
        autotext.set_weight('bold')
    
    axes[i].legend(
        wedges, spices, title="Spices", loc="center left", bbox_to_anchor=(1, 0.4, 0.5, 1)
    )

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()
