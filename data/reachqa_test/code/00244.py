import matplotlib.pyplot as plt
import squarify

# Define data for research topics and their distribution
research_topics = [
    "Artificial Intelligence\n25%", 
    "Quantum Computing\n15%", 
    "Bioengineering\n20%", 
    "Nanotechnology\n10%", 
    "Robotics\n10%", 
    "Renewable Energy\n20%"
]

projects_distribution = [25, 15, 20, 10, 10, 20]
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFB6C1', '#C0C0C0']

# Define additional data for the number of researchers in each field
researcher_counts = [120, 75, 100, 50, 50, 100]

# Create subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))
fig.suptitle("Exploring Frontiers:\nResearch Distribution and Resources in Advanced Science and Engineering", fontsize=16, fontweight='bold')

# Treemap subplot
squarify.plot(
    ax=axes[0], sizes=projects_distribution, label=research_topics, 
    color=colors, alpha=0.8, edgecolor="white", linewidth=2
)
axes[0].set_title("Research Distribution", fontsize=12)
axes[0].axis('off')  # Disable the axes for a cleaner look

# Bar chart subplot for researcher counts
axes[1].barh(research_topics, researcher_counts, color=colors, edgecolor='black', alpha=0.8)
axes[1].set_title("Researchers in Each Field", fontsize=12)
axes[1].set_xlabel("Number of Researchers")
axes[1].invert_yaxis()  # Invert the y-axis to match the order of the treemap

# Adjust layout to avoid overlap
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Display the plot
plt.show()