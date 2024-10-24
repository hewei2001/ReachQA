import matplotlib.pyplot as plt
import numpy as np

# Decades considered for the study
decades = np.array(['1980s', '1990s', '2000s', '2010s', '2020s'])

# Simulated data for educational technology adoption (in arbitrary units)
personal_computers = np.array([10, 30, 70, 85, 90])
interactive_whiteboards = np.array([0, 10, 50, 75, 80])
online_learning_platforms = np.array([0, 5, 25, 60, 90])
ai_personalized_learning = np.array([0, 0, 0, 20, 60])

# Create the plot
plt.figure(figsize=(12, 8))

plt.plot(decades, personal_computers, marker='o', linestyle='-', linewidth=2, color='blue', label='Personal Computers')
plt.plot(decades, interactive_whiteboards, marker='s', linestyle='-', linewidth=2, color='green', label='Interactive Whiteboards')
plt.plot(decades, online_learning_platforms, marker='^', linestyle='-', linewidth=2, color='orange', label='Online Learning Platforms')
plt.plot(decades, ai_personalized_learning, marker='d', linestyle='-', linewidth=2, color='red', label='AI-driven Personalized Learning')

# Add title and labels
plt.title('Evolution of Educational Technology\nFrom the 1980s to the 2020s', fontsize=16, fontweight='bold', color='darkblue', pad=20)
plt.xlabel('Decades', fontsize=12)
plt.ylabel('Adoption Level (Arbitrary Units)', fontsize=12)

# Customize the legend
plt.legend(loc='upper left', fontsize=10, frameon=False)

# Enhance the x-axis for better visibility
plt.xticks(decades, fontsize=11)

# Add grid lines for better readability
plt.grid(True, linestyle='--', color='gray', alpha=0.7)

# Add annotations for each technology to highlight trends
for i, txt in enumerate(personal_computers):
    plt.annotate(txt, (decades[i], personal_computers[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
for i, txt in enumerate(interactive_whiteboards):
    plt.annotate(txt, (decades[i], interactive_whiteboards[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
for i, txt in enumerate(online_learning_platforms):
    plt.annotate(txt, (decades[i], online_learning_platforms[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
for i, txt in enumerate(ai_personalized_learning):
    plt.annotate(txt, (decades[i], ai_personalized_learning[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()