import matplotlib.pyplot as plt

# Data setup: Hypothetical number of different plant species in urban gardens
cities = ['New York', 'London', 'Tokyo', 'Sydney']
biodiversity_data = [
    [15, 18, 17, 20, 19, 22, 25, 18, 17, 21],  # New York
    [22, 25, 19, 23, 21, 26, 28, 22, 27, 24],  # London
    [16, 20, 18, 19, 21, 23, 20, 22, 18, 19],  # Tokyo
    [25, 28, 30, 27, 26, 29, 31, 30, 32, 28]   # Sydney
]

# Hypothetical average plant growth rates (% increase per year) in each city
growth_rates = [2.5, 3.0, 2.8, 3.2]  # Percent increase per year

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Box plot for biodiversity data
box = ax1.boxplot(
    biodiversity_data, vert=True, patch_artist=True, notch=True, labels=cities
)

colors = ['#8DD3C7', '#FFB3BA', '#BEBADA', '#FB8072']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

for whisker in box['whiskers']:
    whisker.set(color='gray', linewidth=1.5, linestyle='--')
    
for cap in box['caps']:
    cap.set(color='black', linewidth=1.5)
    
for median in box['medians']:
    median.set(color='firebrick', linewidth=2)
    
for flier in box['fliers']:
    flier.set(marker='o', color='#e7298a', alpha=0.5, markersize=5)

ax1.set_title('Biodiversity of Urban Gardens\nNumber of Plant Species Observed', fontsize=14, weight='bold')
ax1.set_xlabel('City', fontsize=12)
ax1.set_ylabel('Number of Plant Species', fontsize=12)
ax1.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
ax1.set_facecolor('#F5F5F5')

# Bar plot for plant growth rates
ax2.bar(cities, growth_rates, color=colors, alpha=0.7)
ax2.set_title('Average Annual Growth Rate\nof Plant Species by City', fontsize=14, weight='bold')
ax2.set_xlabel('City', fontsize=12)
ax2.set_ylabel('Growth Rate (%)', fontsize=12)
ax2.set_facecolor('#F5F5F5')
ax2.grid(True, axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Overall figure adjustments
plt.figtext(0.5, 0.02, 'Study highlights biodiversity and growth trends in urban environments', fontsize=10, ha='center')
plt.suptitle('Urban Biodiversity and Plant Growth Analysis', fontsize=16, weight='bold', y=1.02)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout to make space for titles and subtitles
plt.show()