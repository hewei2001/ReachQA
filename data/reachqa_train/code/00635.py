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

# Plot the data
plt.figure(figsize=(10, 6))
plt.scatter(species_count, sightings, color='darkgreen', label='Observed Data', s=100, alpha=0.7)
plt.plot(species_fit, sightings_fit, color='forestgreen', linestyle='--', label='Fitted Curve', linewidth=2)

# Annotate parks on the scatter points
for i, park in enumerate(parks):
    plt.annotate(park, (species_count[i], sightings[i]), textcoords="offset points", xytext=(0, 10), ha='center')

# Customize the plot
plt.title("Urban Birdwatching Trends:\nDiversity and Sightings in City Parks", fontsize=14, fontweight='bold', pad=10)
plt.xlabel("Number of Bird Species", fontsize=12)
plt.ylabel("Total Sightings", fontsize=12)
plt.legend(loc='upper left', fontsize=10, frameon=True)
plt.grid(linestyle='--', alpha=0.5)

# Adjust the layout
plt.tight_layout()

# Show the plot
plt.show()