import numpy as np
import matplotlib.pyplot as plt

# Define a higher resolution of time segments for finer detail (e.g., every half-hour)
hours = np.linspace(0, 2 * np.pi, 48, endpoint=False)

# Generate data for a larger number of fish species with smooth variability
# Here, sinusoidal patterns are used with different amplitudes and phases to simulate activity
clownfish_activity = 5 + 10 * np.abs(np.sin(hours))
angelfish_activity = 2 + 8 * np.abs(np.cos(hours + np.pi / 6))
parrotfish_activity = 3 + 15 * np.abs(np.sin(hours + np.pi / 4))
butterflyfish_activity = 1 + 6 * np.abs(np.sin(hours - np.pi / 3))
lionfish_activity = 4 + 9 * np.abs(np.cos(hours - np.pi / 4))

# Set up the polar plot with increased figure size to handle complexity
fig, ax = plt.subplots(figsize=(12, 10), subplot_kw={'projection': 'polar'})

# Create stacked bar plots for multiple fish species
bars1 = ax.bar(hours, clownfish_activity, width=0.12, label='Clownfish', color='#FF6347', alpha=0.7)
bars2 = ax.bar(hours, angelfish_activity, width=0.12, label='Angelfish', color='#1E90FF', alpha=0.7, bottom=clownfish_activity)
combined_activity_1 = clownfish_activity + angelfish_activity
bars3 = ax.bar(hours, parrotfish_activity, width=0.12, label='Parrotfish', color='#32CD32', alpha=0.7, bottom=combined_activity_1)
combined_activity_2 = combined_activity_1 + parrotfish_activity
bars4 = ax.bar(hours, butterflyfish_activity, width=0.12, label='Butterflyfish', color='#FFD700', alpha=0.7, bottom=combined_activity_2)
combined_activity_3 = combined_activity_2 + butterflyfish_activity
bars5 = ax.bar(hours, lionfish_activity, width=0.12, label='Lionfish', color='#8A2BE2', alpha=0.7, bottom=combined_activity_3)

# Add titles with line breaks for clarity and adjust font size for readability
ax.set_title('Comparative Activity Patterns of Coral Reef Fish Species\nOver a 24-Hour Cycle with Half-Hour Resolution', 
             fontsize=16, fontweight='bold', pad=20)

# Remove radial (y) tick labels for aesthetic clarity
ax.set_yticklabels([])

# Define x-tick labels, increasing the density for half-hour intervals
hour_labels = ['12 AM', '12:30 AM', '1 AM', '1:30 AM', '2 AM', '2:30 AM', '3 AM', '3:30 AM', 
               '4 AM', '4:30 AM', '5 AM', '5:30 AM', '6 AM', '6:30 AM', '7 AM', '7:30 AM',
               '8 AM', '8:30 AM', '9 AM', '9:30 AM', '10 AM', '10:30 AM', '11 AM', '11:30 AM',
               '12 PM', '12:30 PM', '1 PM', '1:30 PM', '2 PM', '2:30 PM', '3 PM', '3:30 PM',
               '4 PM', '4:30 PM', '5 PM', '5:30 PM', '6 PM', '6:30 PM', '7 PM', '7:30 PM',
               '8 PM', '8:30 PM', '9 PM', '9:30 PM', '10 PM', '10:30 PM', '11 PM', '11:30 PM']
ax.set_xticks(hours)
ax.set_xticklabels(hour_labels, fontsize=8, rotation=45)

# Adjust legend to fit the increased complexity
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.15), fontsize=10)

# Automatically adjust the layout to ensure readability
plt.tight_layout()

# Display the chart
plt.show()