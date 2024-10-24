import matplotlib.pyplot as plt
import numpy as np

# Mission phases and resource allocation changes
phases = [
    "Initial Preparation", "Launch", "Mid-Course Correction", "Mars Orbit Insertion",
    "Landing", "Base Setup", "Scientific Operations", "Return Preparation",
    "Unexpected Challenge", "Final Return"
]

# Resource changes in 'Resource Units' for each phase
resource_changes = [1200, -300, -200, -500, -400, 1500, -700, -300, -250, 1000]
cumulative_resources = np.cumsum([0] + resource_changes[:-1])
colors = ['green' if x >= 0 else 'red' for x in resource_changes]

# Constructing a hypothetical mission success probability dataset
# Assuming it starts at 50% and fluctuates based on resource allocation and other factors
success_probability = [50, 60, 58, 55, 50, 70, 65, 60, 50, 75]  # percentages

# Initialize the figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))

# Plotting the waterfall chart
for i, (change, cum) in enumerate(zip(resource_changes, cumulative_resources)):
    ax1.bar(phases[i], change, bottom=cum, color=colors[i], edgecolor='grey', width=0.6)
    ax1.text(i, cum + change, f'{cum + change}', ha='center', va='bottom', fontsize=9, color='black')

ax1.set_title("Journey to Mars:\nResource Allocation Over the Mission Timeline", fontsize=14, fontweight='bold', pad=20)
ax1.set_ylabel("Resource Allocation (Resource Units)", fontsize=12)
ax1.set_ylim(0, 5000)
ax1.grid(axis='y', linestyle='--', alpha=0.6)
ax1.set_xticks(range(len(phases)))
ax1.set_xticklabels(phases, rotation=45, ha='right', fontsize=10)

# Drawing connecting lines for the waterfall chart
for i in range(1, len(cumulative_resources)):
    ax1.plot([i-1, i], [cumulative_resources[i-1] + resource_changes[i-1], cumulative_resources[i]], color='black', linewidth=1.5, linestyle='--', alpha=0.7)

# Plotting the line chart for success probability
ax2.plot(phases, success_probability, marker='o', linestyle='-', color='blue', linewidth=2)
for i, prob in enumerate(success_probability):
    ax2.text(i, prob + 1, f'{prob}%', ha='center', fontsize=9, color='blue')
ax2.set_title("Mission Success Probability Over Phases", fontsize=14, fontweight='bold', pad=20)
ax2.set_ylabel("Success Probability (%)", fontsize=12)
ax2.set_ylim(40, 80)
ax2.grid(axis='y', linestyle='--', alpha=0.6)
ax2.set_xticks(range(len(phases)))
ax2.set_xticklabels(phases, rotation=45, ha='right', fontsize=10)

# Adjust layout and display the plot
plt.tight_layout()
plt.show()