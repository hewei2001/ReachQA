import matplotlib.pyplot as plt
import numpy as np

# Years and corresponding communication tool usage (in millions)
years = np.array([1900, 1920, 1940, 1960, 1980, 2000, 2020])
postal_mail = np.array([80, 120, 150, 160, 140, 100, 40])
telephone = np.array([0, 5, 50, 200, 600, 1200, 1500])
radio = np.array([0, 0, 30, 150, 300, 250, 50])
television = np.array([0, 0, 0, 20, 500, 1100, 1200])
internet = np.array([0, 0, 0, 0, 50, 800, 4000])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the data with appropriate styles
ax.plot(years, postal_mail, label='Postal Mail', marker='o', color='#ff7f0e', linewidth=2, linestyle='-')
ax.plot(years, telephone, label='Telephone', marker='^', color='#1f77b4', linewidth=2, linestyle='--')
ax.plot(years, radio, label='Radio', marker='s', color='#2ca02c', linewidth=2, linestyle='-.')
ax.plot(years, television, label='Television', marker='D', color='#d62728', linewidth=2, linestyle=':')
ax.plot(years, internet, label='Internet', marker='x', color='#9467bd', linewidth=2, linestyle='-')

# Annotate data points
for i, year in enumerate(years):
    ax.annotate(f'{postal_mail[i]}', (year, postal_mail[i]), textcoords="offset points", xytext=(0,10), ha='center', color='#ff7f0e')
    ax.annotate(f'{telephone[i]}', (year, telephone[i]), textcoords="offset points", xytext=(0,10), ha='center', color='#1f77b4')
    ax.annotate(f'{radio[i]}', (year, radio[i]), textcoords="offset points", xytext=(0,10), ha='center', color='#2ca02c')
    ax.annotate(f'{television[i]}', (year, television[i]), textcoords="offset points", xytext=(0,10), ha='center', color='#d62728')
    ax.annotate(f'{internet[i]}', (year, internet[i]), textcoords="offset points", xytext=(0,10), ha='center', color='#9467bd')

# Set title and labels
ax.set_title('The Evolution of Communication Tools\nFrom 1900 to 2020', fontsize=18, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Users (in millions)', fontsize=14)

# Add grid and legend
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax.legend(title='Communication Tool', loc='upper left', fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()