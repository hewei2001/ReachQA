import numpy as np
import matplotlib.pyplot as plt

# Define the time range for decades
decades = np.arange(1970, 2030, 10)

# Fictional data on music genre popularity (in percentage)
rock = [40, 35, 25, 15, 10, 5]
disco = [20, 25, 10, 5, 0, 0]
pop = [10, 15, 25, 30, 35, 40]
hip_hop = [0, 0, 10, 20, 25, 30]
electronic = [5, 10, 15, 20, 20, 15]
indie = [0, 0, 5, 10, 10, 10]

# Stack the data to plot
stacked_data = np.vstack([rock, disco, pop, hip_hop, electronic, indie])

# Hypothetical data: Popularity of music streaming services (% of population)
streaming_services = [0, 0, 5, 20, 50, 70]

# Initialize the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Create the stacked area chart
ax1.stackplot(decades, stacked_data, labels=['Rock', 'Disco', 'Pop', 'Hip Hop', 'Electronic', 'Indie'],
              colors=['#d62728', '#ff7f0e', '#1f77b4', '#9467bd', '#2ca02c', '#8c564b'], alpha=0.7)

# Customize the primary y-axis
ax1.set_xlabel("Decade", fontsize=14)
ax1.set_ylabel("Popularity (%)", fontsize=14)
ax1.set_title("Shifting Melodies: Music Genre Popularity and the Rise of Streaming\nfrom the 1970s to 2020s", 
              fontsize=16, fontweight='bold', pad=20)
ax1.set_xticks(decades)
ax1.grid(axis='y', linestyle='--', alpha=0.5)

# Add annotation to highlight notable genre transition
ax1.annotate('Rise of Hip Hop', xy=(2000, 20), xytext=(1980, 60),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

# Create secondary y-axis for the overlay plot
ax2 = ax1.twinx()
ax2.plot(decades, streaming_services, label='Streaming Services', color='black', linestyle='--', marker='o')
ax2.set_ylabel("Streaming Users (%)", fontsize=14)

# Add legends for both plots
ax1.legend(loc='upper left', fontsize=12, title='Music Genres', bbox_to_anchor=(0, 1))
ax2.legend(loc='upper left', fontsize=12, bbox_to_anchor=(0.8, 1))

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the plot
plt.show()