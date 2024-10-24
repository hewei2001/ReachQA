import matplotlib.pyplot as plt

# Modes of transportation (expanded list)
transport_modes = [
    'Walking', 'Cycling', 'Public Transit', 'Carpooling', 
    'Private Vehicles', 'Electric Scooters', 'Ride Sharing', 
    'Telecommuting', 'Remote Work'
]

# Adjusted percentage of users preferring each mode (totaling 100% for each day)
weekday_data = [14, 10, 24, 8, 20, 4, 6, 8, 6]
weekend_data = [18, 13, 22, 5, 26, 3, 5, 5, 3]

# Define colors for each mode of transportation, ensuring good contrast
colors = [
    '#76C7C0', '#FFB6C1', '#8FBC8F', '#DEB887', 
    '#FFD700', '#FF69B4', '#ADD8E6', '#FFA07A', '#9370DB'
]

# Create a subplot grid for weekday and weekend preferences
fig, axs = plt.subplots(1, 2, figsize=(14, 8))

# Configuration for weekday pie chart
axs[0].pie(
    weekday_data,
    labels=transport_modes,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=[0.1 if mode == 'Public Transit' else 0.05 if mode == 'Private Vehicles' else 0 for mode in transport_modes],
    shadow=True
)
axs[0].set_title('Weekday Transportation Preferences', fontsize=14, weight='bold')

# Configuration for weekend pie chart
axs[1].pie(
    weekend_data,
    labels=transport_modes,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=[0.1 if mode == 'Private Vehicles' else 0.05 if mode == 'Public Transit' else 0 for mode in transport_modes],
    shadow=True
)
axs[1].set_title('Weekend Transportation Preferences', fontsize=14, weight='bold')

# Adjust text size and weight to ensure readability
for ax in axs:
    for text in ax.texts:
        text.set_fontsize(10)
        text.set_weight('bold')

# Add a shared legend outside the subplot grid
plt.legend(
    transport_modes, 
    title="Modes of Transportation", 
    loc="center left", 
    bbox_to_anchor=(1.05, 0.5), 
    fontsize=10
)

# Add a main title to the entire figure
fig.suptitle(
    'Metropolis 2025 Urban Mobility Survey:\nComplex Transportation Preferences by Time',
    fontsize=16, 
    weight='bold'
)

# Automatically adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Show the plot
plt.show()
