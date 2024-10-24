import matplotlib.pyplot as plt

# Define years and corresponding biodiversity indices for different wildlife reserves
years = ['3050', '3051', '3052', '3053', '3054']

# Biodiversity indices for five wildlife reserves in different galaxies
alpha_reserve = [320, 350, 330, 310, 340]
beta_reserve = [290, 280, 300, 320, 310]
gamma_reserve = [310, 305, 295, 315, 300]
delta_reserve = [275, 290, 265, 250, 280]
epsilon_reserve = [260, 270, 275, 265, 285]

# Combine all reserves' data into a list for the box plot
biodiversity_data = [alpha_reserve, beta_reserve, gamma_reserve, delta_reserve, epsilon_reserve]

# Create the vertical box plot
fig, ax = plt.subplots(figsize=(10, 7))
box = ax.boxplot(biodiversity_data, notch=True, vert=True, patch_artist=True, labels=['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon'])

# Customize the appearance
colors = ['#FFA07A', '#20B2AA', '#87CEFA', '#FFB6C1', '#98FB98']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Set title and axis labels
ax.set_title("Interstellar Wildlife Reserves:\nBiodiversity Distribution Across Galaxies (Year 3050-3054)",
             fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel("Galactic Wildlife Reserves", fontsize=12)
ax.set_ylabel("Biodiversity Index", fontsize=12)

# Customize medians and other components for better visibility
plt.setp(box['whiskers'], color='gray', linestyle='--')
plt.setp(box['caps'], color='gray')
plt.setp(box['medians'], color='red', linewidth=2)

# Annotate the median biodiversity index for each reserve
for i, median in enumerate(box['medians']):
    median_value = median.get_ydata()[0]
    ax.text(i + 1, median_value + 2, f'{median_value:.0f}', ha='center', fontsize=10, fontweight='bold')

# Enable gridlines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout for better visualization
plt.tight_layout()

# Show the plot
plt.show()