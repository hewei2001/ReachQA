import matplotlib.pyplot as plt
import numpy as np

# Define the decades and communication methods
decades = np.arange(1960, 2030, 10)
communication_methods = ['Letters', 'Landline Phones', 'Email', 'Mobile Phones', 'Social Media']

# Define communication data for each method across decades
letters = np.array([80, 65, 50, 30, 10, 5, 3])
landline_phones = np.array([20, 40, 60, 50, 20, 10, 5])
email = np.array([0, 0, 0, 20, 40, 30, 20])
mobile_phones = np.array([0, 0, 0, 0, 30, 45, 50])
social_media = np.array([0, 0, 0, 0, 0, 10, 22])

# Stack the data for plotting
communication_data = np.vstack([letters, landline_phones, email, mobile_phones, social_media])

# Set up the plot
plt.figure(figsize=(12, 7))

# Plot the stacked area chart
colors = ['#8B4513', '#2F4F4F', '#1E90FF', '#228B22', '#FFD700']
plt.stackplot(decades, communication_data, labels=communication_methods, colors=colors, alpha=0.7)

# Customize the plot
plt.title("Evolution of Communication Methods\nOver the Decades", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Decade", fontsize=12)
plt.ylabel("Share of Use (%)", fontsize=12)

# Add grid lines for better readability
plt.grid(linestyle='--', alpha=0.5)

# Rotate x-axis labels to avoid overlap and ensure clarity
plt.xticks(decades, rotation=45)
plt.yticks(np.arange(0, 101, 10))

# Add a legend for the communication methods
plt.legend(loc='upper left', fontsize=10, title="Communication Methods")

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()