import matplotlib.pyplot as plt
import numpy as np

# Decades and corresponding efficiency scores
decades = np.array([1970, 1980, 1990, 2000, 2010, 2020])
efficiency_scores = np.array([2.5, 3.0, 4.2, 5.6, 7.3, 8.8])
std_devs = np.array([0.4, 0.5, 0.6, 0.7, 0.5, 0.4])

# Additional related data for the second plot (e.g., computational cost in millions)
computational_cost = np.array([8.0, 6.5, 5.5, 4.3, 3.0, 2.0])

# Create the subplots
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1: Error bar plot for AI efficiency
ax[0].errorbar(decades, efficiency_scores, yerr=std_devs, fmt='-o', color='darkorange',
               ecolor='lightblue', elinewidth=2, capsize=5, capthick=2, alpha=0.8)
ax[0].set_title("Evolution of AI Algorithm Efficiency\n1970-2020", fontsize=14, fontweight='bold', pad=20)
ax[0].set_xlabel("Decade", fontsize=12)
ax[0].set_ylabel("Efficiency Metric (Scale 1-10)", fontsize=12)
ax[0].grid(visible=True, linestyle='--', alpha=0.6)

# Annotate with milestones
milestones = ["Early Explorations", "Rule-Based Systems", "Neural Networks",
              "Early Deep Learning", "Rise of Big Data", "AI in Everyday Life"]
for i, (x, y) in enumerate(zip(decades, efficiency_scores)):
    ax[0].annotate(milestones[i], (x, y), textcoords="offset points", xytext=(-10, 10), ha='center',
                   fontsize=9, bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='wheat'))

ax[0].legend(["Efficiency Score"], loc='upper left', fontsize=10, frameon=False)

# Plot 2: Bar plot for Computational Cost
ax[1].bar(decades, computational_cost, color='lightseagreen', alpha=0.7)
ax[1].set_title("Decline in Computational Cost\nAssociated with AI Evolution", fontsize=14, fontweight='bold', pad=20)
ax[1].set_xlabel("Decade", fontsize=12)
ax[1].set_ylabel("Cost (Millions)", fontsize=12)
ax[1].grid(visible=True, linestyle='--', alpha=0.6)

# Annotating costs
for x, cost in zip(decades, computational_cost):
    ax[1].text(x, cost + 0.2, f"${cost:.1f}M", ha='center', va='bottom', fontsize=9, color='darkslategray')

# Adjust layout to prevent overlap and improve aesthetics
plt.tight_layout()

# Show the plot
plt.show()