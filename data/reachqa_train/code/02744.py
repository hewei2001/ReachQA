import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Define categories and data
categories = ['Innovation', 'User Experience', 'Market Penetration', 'Customer Support', 'Security']
num_vars = len(categories)

# Data for each company
InnoTech = [9, 7, 6, 7, 8]
FutureWare = [7, 9, 7, 6, 7]
QuantumSoft = [6, 7, 9, 6, 8]
NexGenTech = [6, 8, 7, 9, 7]

# Combine data
data = np.array([InnoTech, FutureWare, QuantumSoft, NexGenTech])

# Compute angle for each axis
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Close the radar chart loop

# Data needs to be cyclic, hence we append the first point to the end
data = np.concatenate((data, data[:, [0]]), axis=1)

# Set up the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw one line per company and fill the area
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
for i, (company, company_data, color) in enumerate(zip(['InnoTech', 'FutureWare', 'QuantumSoft', 'NexGenTech'], data, colors)):
    ax.fill(angles, company_data, color=color, alpha=0.3, label=company)
    ax.plot(angles, company_data, color=color, linewidth=1.5)

# Add labels and title
plt.xticks(angles[:-1], categories, color='grey', size=10)
ax.set_title("Tech Giant Product Strengths in 2023", size=16, fontweight='bold', pad=20)

# Customize y-axis limits and grid
ax.set_rscale('linear')
ax.set_rlabel_position(0)
plt.yticks([2, 4, 6, 8, 10], ['2', '4', '6', '8', '10'], color='grey', size=9)
plt.ylim(0, 10)

# Add legend and customize it
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), title="Companies", fontsize=10)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()