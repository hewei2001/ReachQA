import matplotlib.pyplot as plt
import numpy as np

# Define the decades and the corresponding adoption numbers (in thousands)
decades = ["2000s", "2010s", "2020s", "2030s", "2040s", "2050s", "2060s"]
adoption_numbers = [5, 20, 45, 120, 180, 300, 500]  # In thousands

# Expand the data into a form suitable for histogram plotting
expanded_data = []
for i, count in enumerate(adoption_numbers):
    expanded_data.extend([decades[i]] * count)

# Set up the plot
plt.figure(figsize=(12, 7))
plt.hist(expanded_data, bins=np.arange(len(decades) + 1) - 0.5, color='deepskyblue', edgecolor='black', rwidth=0.8)

# Set the titles and labels
plt.title("Futuristic Technology Adoption in Future City 2077\nA Decadal Overview from 2000 to 2060", fontsize=14, weight='bold')
plt.xlabel("Decade", fontsize=12)
plt.ylabel("Number of Adopters (Thousands)", fontsize=12)

# Set custom x-ticks
plt.xticks(ticks=np.arange(len(decades)), labels=decades)

# Add grid lines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the histogram
plt.show()