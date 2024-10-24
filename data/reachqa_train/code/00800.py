import matplotlib.pyplot as plt
import numpy as np

# Decades from the 1920s to the 2020s
decades = np.arange(1920, 2030, 10)

# Communication modality percentage shares over the decades
postal_mail = np.array([90, 80, 70, 60, 50, 40, 20, 10, 5, 3, 1])
telephony = np.array([5, 15, 25, 40, 50, 50, 40, 30, 20, 15, 10])
radio = np.array([2, 3, 10, 20, 15, 10, 5, 3, 2, 1, 1])
television = np.array([0, 1, 5, 10, 30, 40, 40, 35, 30, 25, 20])
internet = np.array([0, 0, 0, 0, 5, 10, 25, 40, 60, 70, 75])
digital_messaging = np.array([0, 0, 0, 0, 0, 0, 10, 20, 30, 35, 40])

# Plotting the stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))

# Stackplot with distinct colors and transparency
ax.stackplot(
    decades, postal_mail, telephony, radio, television, internet, digital_messaging,
    labels=['Postal Mail', 'Telephony', 'Radio', 'Television', 'Internet', 'Digital Messaging'],
    colors=['#d73027', '#4575b4', '#fee08b', '#91cf60', '#1a9850', '#762a83'],
    alpha=0.85
)

# Titles and labels
ax.set_title(
    'Evolution of Communication Modalities\nThrough the Decades (1920s-2020s)',
    fontsize=16, fontweight='bold', pad=20
)
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Percentage Share (%)', fontsize=12)

# Setting x-ticks with custom labels
ax.set_xticks(decades)
ax.set_xticklabels([f'{year}s' for year in decades], rotation=45, ha='right')

# Grid for readability
ax.grid(True, linestyle='--', alpha=0.5)

# Legend positioned outside the plot
ax.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 1))

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()