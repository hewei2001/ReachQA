import matplotlib.pyplot as plt
import numpy as np

# Original scatter plot data
years_experience = np.array([1, 3, 5, 7, 10, 12, 15, 18, 20, 25, 30, 35, 40])
ai_adoption_rate = np.array([70, 65, 60, 55, 50, 52, 48, 45, 42, 40, 38, 35, 30])
number_of_tools = np.array([5, 4, 4, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1]) * 10

# Additional line plot data
ai_influence_index = np.array([5, 15, 28, 40, 60, 75, 90, 110, 130, 160, 200, 240, 280])

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 8))

# Scatter plot
scatter = axs[0].scatter(years_experience, ai_adoption_rate, s=number_of_tools, c='teal', alpha=0.7, edgecolors='w', linewidth=2)
axs[0].set_title("AI Adoption in Healthcare:\nExperience vs. Adoption Rate", fontsize=14, fontweight='bold')
axs[0].set_xlabel("Years of Experience", fontsize=12)
axs[0].set_ylabel("AI Adoption Rate (%)", fontsize=12)
axs[0].set_xticks(years_experience)
axs[0].tick_params(axis='x', rotation=45)
axs[0].set_yticks(np.arange(25, 80, 5))
axs[0].grid(True, linestyle='--', alpha=0.5)

# Annotate scatter plot
for i, (x, y) in enumerate(zip(years_experience, ai_adoption_rate)):
    axs[0].annotate(f'{number_of_tools[i]//10} tools', (x, y), textcoords="offset points", xytext=(0, -10), ha='center', fontsize=9)

axs[0].legend(['Size ~ Number of AI Tools Used'], loc='upper right', fontsize=9)

# Line plot
axs[1].plot(years_experience, ai_influence_index, color='purple', marker='o', linestyle='-')
axs[1].set_title("Cumulative AI Influence Index\nOver Time", fontsize=14, fontweight='bold')
axs[1].set_xlabel("Years of Experience", fontsize=12)
axs[1].set_ylabel("AI Influence Index", fontsize=12)
axs[1].set_xticks(years_experience)
axs[1].tick_params(axis='x', rotation=45)
axs[1].grid(True, linestyle='--', alpha=0.5)
axs[1].fill_between(years_experience, ai_influence_index, color='purple', alpha=0.1)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()