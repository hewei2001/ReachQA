import matplotlib.pyplot as plt
import numpy as np

# Define months as the x-axis (1 to 12 representing January to December)
months = np.arange(1, 13)

# Simulate light intensity data using a sinusoidal pattern with arbitrary units
base_intensity = 100  # Base intensity level
seasonal_variation = 15 * np.sin(2 * np.pi * (months - 1) / 12)  # Seasonal change
atmospheric_effects = np.array([5, -3, 2, -1, 6, -2, 4, -4, 3, -1, 2, 0])  # Other effects
light_intensity = base_intensity + seasonal_variation + atmospheric_effects

# Create the line plot
plt.figure(figsize=(12, 7))
plt.plot(months, light_intensity, marker='o', linestyle='-', color='royalblue', linewidth=2, label='Zoltar-5 Light Intensity')

# Add annotations for selected key data points to avoid clutter
for i, intensity in enumerate(light_intensity):
    if i % 2 == 0:  # Annotate every other month for clarity
        plt.annotate(f'{intensity:.1f}', (months[i], intensity), textcoords="offset points", xytext=(-10, 10), ha='center')

# Set the title and labels with line breaks for better readability
plt.title("Simulated Light Intensity Variations\nfrom Zoltar-5 Over One Earth Year", fontsize=16, fontweight='bold')
plt.xlabel("Month", fontsize=12)
plt.ylabel("Light Intensity (Arbitrary Units)", fontsize=12)

# Customize the x-ticks to represent months
plt.xticks(months, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Add grid to improve readability
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Add legend to the plot
plt.legend(loc='upper right', fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()