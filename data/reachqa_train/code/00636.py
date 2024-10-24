import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Define parks and hypothetical observation data (species count and sightings)
parks = ["Central Park", "Riverside Park", "Brooklyn Park", "Liberty Park", "Queens Botanical Garden"]

# Artificial data representing the number of bird species and total sightings
species_count = np.array([15, 18, 14, 20, 16])
sightings = np.array([200, 240, 180, 290, 210])

# Define a function to fit the data (quadratic model as a smooth curve)
def quadratic_model(x, a, b, c):
    return a * x**2 + b * x + c

# Fit the model to the data
params, covariance = curve_fit(quadratic_model, species_count, sightings)

# Generate a smooth line for the fitted curve
species_fit = np.linspace(min(species_count), max(species_count), 100)
sightings_fit = quadratic_model(species_fit, *params)

# Calculate average sightings per species for each park
avg_sightings_per_species = sightings / species_count

# Create a horizontal subplot layout (1x2)
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Subplot 1: Scatter plot with quadratic fit
axes[0].scatter(species_count, sightings, color='darkgreen', label='Observed Data', s=100, alpha=0.7)
axes[0].plot(species_fit, sightings_fit, color='forestgreen', linestyle='--', label='Fitted Curve', linewidth=2)
for i, park in enumerate(parks):
    axes[0].annotate(park, (species_count[i], sightings[i]), textcoords="offset points", xytext=(0, 10), ha='center')
axes[0].set_title("Urban Birdwatching Trends:\nDiversity and Sightings in City Parks", fontsize=14, fontweight='bold', pad=10)
axes[0].set_xlabel("Number of Bird Species", fontsize=12)
axes[0].set_ylabel("Total Sightings", fontsize=12)
axes[0].legend(loc='upper left', fontsize=10, frameon=True)
axes[0].grid(linestyle='--', alpha=0.5)

# Subplot 2: Bar chart of average sightings per species
axes[1].bar(parks, avg_sightings_per_species, color='steelblue', alpha=0.7)
axes[1].set_title("Average Sightings per Species\nin City Parks", fontsize=14, fontweight='bold', pad=10)
axes[1].set_xlabel("Parks", fontsize=12)
axes[1].set_ylabel("Avg Sightings per Species", fontsize=12)
for i, v in enumerate(avg_sightings_per_species):
    axes[1].text(i, v + 0.5, f"{v:.1f}", color='black', ha='center', fontweight='bold')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plots
plt.show()