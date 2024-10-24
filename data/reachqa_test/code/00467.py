import matplotlib.pyplot as plt
import numpy as np

# Years data
years = np.arange(2012, 2022)

# Data in thousands of users for each transportation mode over 10 years
public_transport = np.array([200, 220, 250, 280, 300, 320, 330, 340, 350, 360])
personal_vehicles = np.array([300, 290, 280, 270, 260, 250, 240, 230, 220, 210])
non_motorized = np.array([100, 110, 130, 150, 180, 200, 220, 240, 260, 280])

# Data for percentage share calculation
total_commuters = public_transport + personal_vehicles + non_motorized
public_transport_share = (public_transport / total_commuters) * 100
personal_vehicles_share = (personal_vehicles / total_commuters) * 100
non_motorized_share = (non_motorized / total_commuters) * 100

# Create figure and subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12))

# Stacked area plot
ax1.stackplot(years, public_transport, personal_vehicles, non_motorized, 
               labels=['Public Transport', 'Personal Vehicles', 'Non-Motorized'], 
               colors=['#1f77b4', '#ff7f0e', '#2ca02c'], alpha=0.8)

ax1.set_title('Growth in Urban Mobility:\nTransportation Modes Over the Last Decade', 
               fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Number of Commuters (in thousands)', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 1))
ax1.annotate('Peak Public Transport Use', xy=(2019, 340), xytext=(2017, 350),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)
ax1.annotate('Decline in Personal Vehicles', xy=(2021, 210), xytext=(2019, 230),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)

# Bar plot for percentage share
ax2.bar(years - 0.2, public_transport_share, width=0.2, label='Public Transport', color='#1f77b4')
ax2.bar(years, personal_vehicles_share, width=0.2, label='Personal Vehicles', color='#ff7f0e')
ax2.bar(years + 0.2, non_motorized_share, width=0.2, label='Non-Motorized', color='#2ca02c')

ax2.set_title('Percentage Share of Transportation Modes (2012 - 2021)', fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Percentage Share (%)', fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 1))

# Adjust layout to prevent overlap
plt.tight_layout()
plt.show()