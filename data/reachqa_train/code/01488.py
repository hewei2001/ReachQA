import matplotlib.pyplot as plt
import numpy as np

# Decades from 1500s to 1590s
decades = np.arange(1500, 1600, 10)

# Popularity Index (from 0 to 100) for each fashion element
ruff_collars = [10, 15, 25, 35, 50, 60, 75, 85, 90, 95]
puffed_sleeves = [5, 20, 40, 55, 65, 70, 65, 50, 35, 25]
brocade_fabrics = [20, 30, 35, 45, 55, 65, 75, 80, 85, 90]

# Create a plot
fig, ax = plt.subplots(figsize=(12, 7))

# Color map for gradient lines
colors = ['#1f78b4', '#e31a1c', '#ff7f00']

# Plot lines with gradient color effect
ax.plot(decades, ruff_collars, marker='o', linestyle='-', color=colors[0], linewidth=2.5, label='Ruff Collars')
ax.fill_between(decades, ruff_collars, color=colors[0], alpha=0.1)

ax.plot(decades, puffed_sleeves, marker='s', linestyle='--', color=colors[1], linewidth=2.5, label='Puffed Sleeves')
ax.fill_between(decades, puffed_sleeves, color=colors[1], alpha=0.1)

ax.plot(decades, brocade_fabrics, marker='^', linestyle=':', color=colors[2], linewidth=2.5, label='Brocade Fabrics')
ax.fill_between(decades, brocade_fabrics, color=colors[2], alpha=0.1)

# Add vertical dotted lines
for decade in decades:
    ax.axvline(x=decade, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

# Add data annotations with arrows
for i, (decade, rc, ps, bf) in enumerate(zip(decades, ruff_collars, puffed_sleeves, brocade_fabrics)):
    ax.annotate(str(rc), (decade, rc), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=8, color=colors[0])
    ax.annotate(str(ps), (decade, ps), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=8, color=colors[1])
    ax.annotate(str(bf), (decade, bf), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=8, color=colors[2])

# Customize plot
ax.set_title('Renaissance Fashion Trends\nThrough the Decades: 1500s to 1590s', fontsize=16, fontweight='bold', y=1.05)
ax.set_xlabel('Decades', fontsize=14)
ax.set_ylabel('Popularity Index', fontsize=14)
ax.set_xticks(decades)
ax.set_yticks(np.arange(0, 101, 10))
ax.grid(which='major', axis='both', linestyle='--', linewidth=0.75, alpha=0.6)

# Add legend
ax.legend(title='Fashion Elements', loc='upper left', fontsize=12)

# Adjust layout
fig.tight_layout()

# Show plot
plt.show()