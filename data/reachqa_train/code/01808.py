import matplotlib.pyplot as plt
import numpy as np

# Define agencies and domains
agencies = ['NASA', 'ESA', 'CNSA', 'ISRO']
domains = ['Satellite\nTechnology', 'Manned\nMissions', 'Planetary\nScience', 
           'Propulsion\nSystems', 'International\nCollaborations']

# Competency scores for each agency
competency_scores = np.array([
    [9, 8, 10, 9, 7],  # NASA
    [8, 7, 9, 7, 8],   # ESA
    [9, 8, 7, 9, 6],   # CNSA
    [7, 6, 8, 7, 9]    # ISRO
])

# Number of variables
num_vars = len(domains)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Close the loop

# Create the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Adjust the radial limits
ax.set_ylim(0, 10)

# Plot each agency
for i, agency in enumerate(agencies):
    values = competency_scores[i].tolist()
    values += values[:1]  # Complete the loop
    
    ax.fill(angles, values, alpha=0.25, label=agency)
    ax.plot(angles, values, linewidth=2, linestyle='-')

# Add domain labels
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(domains, fontsize=10, ha='center')

# Enhance the appearance of the radar chart
ax.spines['polar'].set_visible(False)  # Hide the polar spine for a cleaner look
ax.grid(color='grey', linestyle='--', linewidth=0.5)

# Add title and legend
plt.title('The Symphony of Space Exploration:\nCompetency Profile of Leading Space Agencies in 2025',
          fontsize=14, fontweight='bold', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)

# Automatically adjust layout for better fit
plt.tight_layout()

# Display the radar chart
plt.show()