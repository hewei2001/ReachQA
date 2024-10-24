import matplotlib.pyplot as plt
import numpy as np

# Define decades from 1970 to 2020
decades = np.array(['1970', '1980', '1990', '2000', '2010', '2020'])

# Population index data (arbitrary units)
coral_reefs = np.array([90, 85, 70, 50, 45, 55])
sharks_rays = np.array([70, 65, 60, 55, 60, 65])
marine_mammals = np.array([40, 50, 60, 75, 85, 80])
sea_turtles = np.array([20, 30, 45, 60, 70, 75])
pelagic_fish = np.array([100, 95, 90, 85, 80, 75])

# Stack the data for area plotting
biodiversity_data = np.vstack([coral_reefs, sharks_rays, marine_mammals, sea_turtles, pelagic_fish])

# Calculate the total biodiversity index over time
total_biodiversity = np.sum(biodiversity_data, axis=0)

# Set up the main plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plotting the stacked area chart
colors = ['#f39c12', '#3498db', '#e74c3c', '#2ecc71', '#9b59b6']
ax1.stackplot(decades, biodiversity_data, labels=[
    'Coral Reefs', 'Sharks & Rays', 'Marine Mammals', 'Sea Turtles', 'Pelagic Fish'],
    colors=colors, alpha=0.7)

# Adding markers to each data point
for idx, species in enumerate(biodiversity_data):
    ax1.plot(decades, species, marker='o', color=colors[idx], linestyle='-', linewidth=1.5)

# Set titles and labels
ax1.set_title('Oceanic Biodiversity Through the Decades:\nMarine Population Changes (1970-2020)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Decade', fontsize=14)
ax1.set_ylabel('Population Index (Arbitrary Units)', fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add legend
ax1.legend(loc='upper left', fontsize=11, title='Species Groups')

# Add grid lines for better readability
ax1.grid(alpha=0.3, linestyle='--', linewidth=0.7)

# Add some annotations to highlight trends
ax1.annotate('Coral Decline & Recovery', xy=('1990', 50), xytext=('1980', 150),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='#f39c12', backgroundcolor='white')
ax1.annotate('Conservation Success', xy=('2010', 275), xytext=('1990', 320),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='#2ecc71', backgroundcolor='white')

# Add a secondary plot for total biodiversity
ax2 = ax1.twinx()
ax2.plot(decades, total_biodiversity, 'k--', marker='s', label='Total Biodiversity Index', linewidth=2)
ax2.set_ylabel('Total Biodiversity Index', fontsize=14)
ax2.legend(loc='upper right', fontsize=11)

# Adjust layout to prevent overlapping elements
plt.tight_layout()

# Display the plot
plt.show()