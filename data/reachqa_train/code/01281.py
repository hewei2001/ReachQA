import matplotlib.pyplot as plt
import numpy as np

# Define the countries and sustainable energy production data (GWh)
countries = ['Country A', 'Country B', 'Country C']
solar = [80, 50, 100]  # Solar energy in GWh
wind = [60, 90, 70]    # Wind energy in GWh
hydro = [40, 60, 80]   # Hydro energy in GWh

# Compute positions for the bars
x = np.arange(len(countries))

# Plotting the stacked bar chart
fig, ax = plt.subplots(figsize=(10, 7))

# Plot each energy source as a stacked bar
ax.bar(x, solar, label='Solar', color='#ffd700', alpha=0.85)
ax.bar(x, wind, bottom=solar, label='Wind', color='#00ced1', alpha=0.85)
ax.bar(x, hydro, bottom=np.array(solar) + np.array(wind), label='Hydro', color='#32cd32', alpha=0.85)

# Add titles and labels
ax.set_title('Innovations in Sustainable Energy by Country\nAnnual Production (2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Countries', fontsize=14)
ax.set_ylabel('Energy Production (GWh)', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(countries, fontsize=12)

# Add a legend to explain color coding
ax.legend(loc='upper left', fontsize=12)

# Annotate each stack with the total value
total_energy = np.array(solar) + np.array(wind) + np.array(hydro)
for i in range(len(countries)):
    ax.text(i, total_energy[i] + 5, f"{total_energy[i]} GWh", ha='center', fontsize=12, fontweight='bold')

# Add gridlines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent clipping
plt.tight_layout()

# Show the plot
plt.show()