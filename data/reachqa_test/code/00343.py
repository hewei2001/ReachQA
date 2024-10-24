import matplotlib.pyplot as plt
import numpy as np

# Years from 2012 to 2022
years = np.arange(2012, 2023)

# Percentage of people using electric vehicles
ev_adoption = np.array([1, 1.5, 2, 3, 4, 5.5, 8, 10, 14, 18, 23])

# Percentage of people using bicycles
bike_adoption = np.array([5, 5.5, 6, 7, 8.5, 9.5, 11, 12.5, 13.5, 15, 16.5])

# Percentage of people using public transport
# Simulated data for public transport adoption
public_transport_adoption = np.array([25, 24.5, 24, 23, 22.5, 22, 21.5, 21, 20.5, 20, 19.5])

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the data for electric vehicles
ax1.plot(years, ev_adoption, label='Electric Vehicles', color='teal', linewidth=2, marker='o')

# Plot the data for bicycles
ax1.plot(years, bike_adoption, label='Bicycles', color='orange', linewidth=2, marker='s')

# Add a secondary y-axis for the bar plot
ax2 = ax1.twinx()

# Plot the data for public transport as a bar chart
bars = ax2.bar(years, public_transport_adoption, width=0.4, label='Public Transport',
               color='skyblue', alpha=0.6, align='edge')

# Add annotations for electric vehicles
for i, year in enumerate(years):
    if year in [2014, 2017, 2022]:
        ax1.annotate(f'{ev_adoption[i]}%', 
                     (year, ev_adoption[i]),
                     textcoords="offset points",
                     xytext=(0, 10),
                     ha='center',
                     fontsize=10,
                     color='teal')

# Add annotations for bicycles
for i, year in enumerate(years):
    if year in [2015, 2020]:
        ax1.annotate(f'{bike_adoption[i]}%', 
                     (year, bike_adoption[i]),
                     textcoords="offset points",
                     xytext=(0, -15),
                     ha='center',
                     fontsize=10,
                     color='orange')

# Add annotations for public transport
for bar in bars:
    ax2.annotate(f'{bar.get_height()}%', 
                 (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                 textcoords="offset points",
                 xytext=(0, 5),
                 ha='center',
                 fontsize=10,
                 color='skyblue')

# Add labels and title
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Percentage of Commuters using EV and Bicycles (%)', fontsize=12)
ax2.set_ylabel('Percentage using Public Transport (%)', fontsize=12)
ax1.set_title('Eco-Friendly Transportation Trends (2012-2022)\nAdoption of Electric Vehicles, Bicycles, and Public Transport', 
              fontsize=16, fontweight='bold', pad=20)

# Add legends
ax1.legend(loc='upper left', fontsize=11)
ax2.legend(loc='upper right', fontsize=11)

# Add grid to primary axis
ax1.grid(True, linestyle='--', alpha=0.5)

# Adjust x and y limits
ax1.set_xlim(2011, 2023)
ax1.set_ylim(0, 25)
ax2.set_ylim(0, 30)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()