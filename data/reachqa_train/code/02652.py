import matplotlib.pyplot as plt
import numpy as np

# Define the fictional dataset
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
hiking = [30, 20, 25, 10]     # Percentage of residents
swimming = [20, 40, 10, 5]
cycling = [25, 15, 20, 5]
gardening = [25, 25, 15, 5]

# Convert data to numpy arrays for easier manipulation
hiking = np.array(hiking)
swimming = np.array(swimming)
cycling = np.array(cycling)
gardening = np.array(gardening)

# Prepare data for stacking in area chart
activities = np.vstack([hiking, swimming, cycling, gardening])

# Plotting the area chart
plt.figure(figsize=(12, 7))
plt.stackplot(seasons, activities, labels=['Hiking', 'Swimming', 'Cycling', 'Gardening'],
              colors=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99'], alpha=0.8)

# Title and labels
plt.title("Recreational Activity Preferences\nin Sunnytown Throughout the Seasons", fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Season', fontsize=14)
plt.ylabel('Percentage of Population Engaging in Activity', fontsize=14)

# Legend
plt.legend(loc='upper left', fontsize=12, title='Activities')

# Customize grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Enhance layout for better spacing and to avoid text overlap
plt.tight_layout()

# Display the plot
plt.show()