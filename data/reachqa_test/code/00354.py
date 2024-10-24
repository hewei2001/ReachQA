import matplotlib.pyplot as plt
import numpy as np

# Data
fields = ['Physics', 'Chemistry', 'Biology', 'Computer Science', 'Engineering', 'Mathematics']
gov_grants = [20, 25, 15, 30, 40, 20]
private_investments = [10, 15, 20, 25, 30, 10]
internal_funding = [30, 20, 40, 20, 15, 30]

# Create a new figure
fig, ax = plt.subplots(figsize=(10, 6))

# Define the colors for each funding source
colors = ['#FFC080', '#FFA07A', '#FF69B4']

# Calculate the x coordinates for each field
x = np.arange(len(fields))

# Plot each funding source
bottom = np.zeros(len(fields))
labels = ['Government Grants', 'Private Investments', 'Internal University Funding']
for i, (funding, label) in enumerate(zip([gov_grants, private_investments, internal_funding], labels)):
    ax.bar(x, funding, bottom=bottom, color=colors[i], label=label)
    bottom += funding

# Set the title
ax.set_title("Research Funding Allocation by Field\n"
             "Government Grants, Private Investments, and\n"
             "Internal University Funding")

# Set the x-axis labels
ax.set_xticks(x)
ax.set_xticklabels(fields, rotation=45, ha="right", fontsize=10)

# Set the y-axis label
ax.set_ylabel("Percentage of Research Funding", fontsize=12)

# Add a legend
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.05), fontsize=10)

# Add a grid
ax.grid(axis='y', linestyle='--', alpha=0.5)

# Add some annotations
for i, field in enumerate(fields):
    ax.text(i, gov_grants[i], str(gov_grants[i]) + '%', ha="center", va="bottom", fontsize=9)
    ax.text(i, gov_grants[i] + private_investments[i], str(private_investments[i]) + '%', ha="center", va="bottom", fontsize=9)
    ax.text(i, gov_grants[i] + private_investments[i] + internal_funding[i], str(internal_funding[i]) + '%', ha="center", va="bottom", fontsize=9)

# Automatically adjust the image layout
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Show the plot
plt.show()