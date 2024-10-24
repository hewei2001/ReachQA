import matplotlib.pyplot as plt
import numpy as np

# Define the categories for the radar chart
categories = ['Efficiency', 'Environmental Impact', 'Cost-Effectiveness', 'Accessibility', 'Technological Maturity']
num_vars = len(categories)

# Define the data for each energy source
solar = [7, 9, 6, 5, 8]
wind = [8, 9, 7, 6, 9]
hydro = [7, 8, 7, 4, 7]
nuclear = [8, 5, 7, 3, 9]
coal = [5, 2, 9, 7, 4]

# Define average scores for energy sources for additional plot
avg_scores = [np.mean(solar), np.mean(wind), np.mean(hydro), np.mean(nuclear), np.mean(coal)]

# Combine the data for easy iteration
energy_sources = [solar, wind, hydro, nuclear, coal]
labels = ['Solar', 'Wind', 'Hydro', 'Nuclear', 'Coal']

# Create an angle for each category in the plot
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Close the circle

# Setup the subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), subplot_kw=dict(polar=True))

# Plotting radar chart
for idx, data in enumerate(energy_sources):
    data += data[:1]
    ax1.fill(angles, data, alpha=0.25, label=labels[idx])
    ax1.plot(angles, data, linewidth=2)

ax1.set_xticks(angles[:-1])
ax1.set_xticklabels(categories, fontsize=11)
ax1.set_title("Sustainability Index of Energy Sources\nA Radar Analysis", size=14, ha='center')
ax1.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
ax1.set_yticklabels([])

# Adding a bar chart for average scores
bars = ax2.bar(labels, avg_scores, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])
ax2.set_title("Average Sustainability Score", size=14, ha='center')
ax2.set_ylim(0, 10)
ax2.set_ylabel('Average Score')
ax2.set_xticklabels(labels, rotation=45, ha='right')

# Annotate bar chart with values
for bar in bars:
    ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 0.5, f'{bar.get_height():.1f}', 
             ha='center', va='bottom', color='white', fontsize=10)

# Ensure layout doesn't overlap
plt.tight_layout()

# Display the combined chart
plt.show()