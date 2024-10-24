import matplotlib.pyplot as plt
import numpy as np

# Define epochs
epochs = ["Antiquity", "Middle Ages", "Renaissance", "Enlightenment", "Industrial Age", "Modern Era"]

# Influence values for each philosophical school over time
stoicism_influence = [70, 50, 20, 10, 5, 5]
rationalism_influence = [0, 10, 30, 70, 40, 30]
empiricism_influence = [0, 5, 20, 50, 70, 40]
existentialism_influence = [0, 0, 0, 10, 50, 80]
postmodernism_influence = [0, 0, 0, 0, 10, 60]

# Stack data for the area plot
influences = np.array([
    stoicism_influence,
    rationalism_influence,
    empiricism_influence,
    existentialism_influence,
    postmodernism_influence
])

# Related data for the new subplot: Technological advancements (example values)
tech_advancements = [10, 20, 40, 60, 80, 100]

# Set up the figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))

# Colors corresponding to each philosophical school
colors = ['#FFD700', '#8A2BE2', '#FF6347', '#20B2AA', '#FF4500']

# Create stacked area chart on the first subplot
ax1.stackplot(epochs, influences, labels=[
    'Stoicism', 'Rationalism', 'Empiricism', 'Existentialism', 'Postmodernism'],
    colors=colors, alpha=0.8)

ax1.set_title("Historical Dynamics of Philosophical Schools:\nInfluence Through the Ages", fontsize=16, weight='bold', pad=20)
ax1.set_xlabel("Epochs", fontsize=12)
ax1.set_ylabel("Influence Level", fontsize=12)
ax1.legend(loc='upper left', fontsize=10, title="Philosophical Schools")
ax1.grid(axis='y', linestyle='--', alpha=0.7)
plt.setp(ax1.get_xticklabels(), rotation=30, ha='right')

# Annotations for emphasis
for i, epoch in enumerate(epochs):
    total_influence = sum(influences[:, i])
    ax1.annotate('Peak', xy=(epoch, total_influence),
                 xytext=(0, 10), textcoords='offset points', ha='center', fontsize=8,
                 arrowprops=dict(arrowstyle='->', lw=0.8))

# Create a line plot for technological advancements on the second subplot
ax2.plot(epochs, tech_advancements, marker='o', color='navy', linewidth=2, label="Tech Advancements")
ax2.set_title("Technological Progress Across Epochs", fontsize=16, pad=20)
ax2.set_xlabel("Epochs", fontsize=12)
ax2.set_ylabel("Advancement Level", fontsize=12)
ax2.grid(axis='y', linestyle='--', alpha=0.7)
plt.setp(ax2.get_xticklabels(), rotation=30, ha='right')
ax2.legend(loc='upper left', fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()