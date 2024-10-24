import matplotlib.pyplot as plt
import numpy as np

# Training modules
modules = [
    'Zero Gravity\nManeuvering', 
    'Spacecraft\nSystems', 
    'Survival\nSkills', 
    'Research and\nExperimentation', 
    'Interplanetary\nCommunications'
]

# Data: hours spent by candidates on each module
hours_data = [
    [45, 55, 60, 50, 65, 48],  # Zero Gravity Maneuvering
    [70, 68, 72, 75, 71, 69],  # Spacecraft Systems
    [30, 34, 29, 35, 32, 31],  # Survival Skills
    [50, 52, 49, 55, 51, 53],  # Research and Experimentation
    [40, 42, 43, 45, 41, 44]   # Interplanetary Communications
]

# Derived data: average proficiency scores for each module (on a scale of 100)
proficiency_scores = [82, 90, 75, 85, 80]

# Initialize the plots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6), gridspec_kw={'width_ratios': [2, 1]})

# First subplot: Box plot
ax1 = axes[0]
boxprops = dict(facecolor='lightblue', color='black')
whiskerprops = dict(color='darkblue')
capprops = dict(color='black')
flierprops = dict(markerfacecolor='red', marker='o', markersize=6, linestyle='none')

ax1.boxplot(hours_data, vert=False, patch_artist=True, notch=True,
            boxprops=boxprops, whiskerprops=whiskerprops,
            capprops=capprops, flierprops=flierprops)

ax1.set_yticklabels(modules, fontsize=11, color='darkblue')
ax1.set_xlabel("Hours", fontsize=12, color='darkred')
ax1.set_title("Astronaut Training Program:\nHours Spent on Various Modules", fontsize=14, weight='bold')
ax1.grid(True, linestyle='--', linewidth=0.5, color='gray', axis='x')

# Second subplot: Bar chart for proficiency scores
ax2 = axes[1]
bars = ax2.barh(modules, proficiency_scores, color='lightgreen', edgecolor='black')
ax2.set_xlim(0, 100)
ax2.set_xlabel("Proficiency Score", fontsize=12, color='darkred')
ax2.set_title("Average Proficiency Scores", fontsize=13, weight='bold')

# Annotate the scores on the bars
for bar, score in zip(bars, proficiency_scores):
    ax2.text(score + 1, bar.get_y() + bar.get_height()/2, f'{score}', va='center', ha='left', fontsize=10, color='black')

# Tight layout to prevent text overlap
plt.tight_layout()

# Display the plots
plt.show()