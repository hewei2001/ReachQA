import matplotlib.pyplot as plt
import numpy as np

# Define skill areas and the corresponding ratings for each explorer
labels = ['Navigation', 'First Aid', 'Shelter Building', 'Fire Craft', 'Food Procurement', 'Water Sourcing']
num_vars = len(labels)

# Data for each explorer
alex_skills = [8, 7, 6, 9, 5, 7]
jamie_skills = [5, 9, 8, 6, 7, 5]
morgan_skills = [6, 5, 7, 8, 9, 8]

# Append the first skill value to the end of each list to close the radar chart
alex_skills += alex_skills[:1]
jamie_skills += jamie_skills[:1]
morgan_skills += morgan_skills[:1]

# Compute angle for each skill
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Close the loop

# Set up the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each explorer's data with distinct styles
colors = ['#FF6347', '#4682B4', '#32CD32']
explorers = ['Alex', 'Jamie', 'Morgan']
data_sets = [alex_skills, jamie_skills, morgan_skills]

for data, color, explorer in zip(data_sets, colors, explorers):
    ax.fill(angles, data, color=color, alpha=0.25)
    ax.plot(angles, data, color=color, linewidth=2, label=explorer)

# Add labels and titles
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2', '4', '6', '8', '10'], color='gray', size=10)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=10)

# Add a title and legend
ax.set_title('Expedition Preparedness:\nA Radar View on Key Survival Skills', fontsize=14, pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=10)

# Enhance layout for clarity
plt.tight_layout()

# Show the plot
plt.show()