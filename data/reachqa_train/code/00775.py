import matplotlib.pyplot as plt
import numpy as np

# Decades considered for the study
decades = np.array(['1980s', '1990s', '2000s', '2010s', '2020s'])

# Simulated data for educational technology adoption (in arbitrary units)
personal_computers = np.array([10, 30, 70, 85, 90])
interactive_whiteboards = np.array([0, 10, 50, 75, 80])
online_learning_platforms = np.array([0, 5, 25, 60, 90])
ai_personalized_learning = np.array([0, 0, 0, 20, 60])

# Related data for the second plot (e.g., projected impact score)
impact_scores = {
    'Personal Computers': np.array([5, 15, 35, 60, 80]),
    'Interactive Whiteboards': np.array([0, 5, 30, 55, 70]),
    'Online Learning Platforms': np.array([0, 2, 20, 50, 85]),
    'AI-driven Personalized Learning': np.array([0, 0, 0, 15, 50])
}

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 8))
fig.suptitle('Evolution and Projected Impact of Educational Technology\nFrom the 1980s to the 2020s', fontsize=16, fontweight='bold', color='darkblue', y=1.02)

# First subplot: Line Plot
axs[0].plot(decades, personal_computers, marker='o', linestyle='-', linewidth=2, color='blue', label='Personal Computers')
axs[0].plot(decades, interactive_whiteboards, marker='s', linestyle='-', linewidth=2, color='green', label='Interactive Whiteboards')
axs[0].plot(decades, online_learning_platforms, marker='^', linestyle='-', linewidth=2, color='orange', label='Online Learning Platforms')
axs[0].plot(decades, ai_personalized_learning, marker='d', linestyle='-', linewidth=2, color='red', label='AI-driven Personalized Learning')

axs[0].set_title('Adoption Levels', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Decades', fontsize=12)
axs[0].set_ylabel('Adoption Level (Arbitrary Units)', fontsize=12)
axs[0].legend(loc='upper left', fontsize=10, frameon=False)
axs[0].grid(True, linestyle='--', color='gray', alpha=0.7)

# Annotations for the first subplot
for i, txt in enumerate(personal_computers):
    axs[0].annotate(txt, (decades[i], personal_computers[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
for i, txt in enumerate(interactive_whiteboards):
    axs[0].annotate(txt, (decades[i], interactive_whiteboards[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
for i, txt in enumerate(online_learning_platforms):
    axs[0].annotate(txt, (decades[i], online_learning_platforms[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
for i, txt in enumerate(ai_personalized_learning):
    axs[0].annotate(txt, (decades[i], ai_personalized_learning[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

# Second subplot: Bar Chart
bar_width = 0.2
x = np.arange(len(decades))

axs[1].bar(x - 1.5*bar_width, impact_scores['Personal Computers'], width=bar_width, label='Personal Computers', color='blue')
axs[1].bar(x - 0.5*bar_width, impact_scores['Interactive Whiteboards'], width=bar_width, label='Interactive Whiteboards', color='green')
axs[1].bar(x + 0.5*bar_width, impact_scores['Online Learning Platforms'], width=bar_width, label='Online Learning Platforms', color='orange')
axs[1].bar(x + 1.5*bar_width, impact_scores['AI-driven Personalized Learning'], width=bar_width, label='AI-driven Personalized Learning', color='red')

axs[1].set_title('Projected Impact Scores', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Decades', fontsize=12)
axs[1].set_ylabel('Impact Score (Arbitrary Units)', fontsize=12)
axs[1].set_xticks(x)
axs[1].set_xticklabels(decades)
axs[1].legend(loc='upper left', fontsize=10, frameon=False)
axs[1].grid(True, linestyle='--', color='gray', alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()