import matplotlib.pyplot as plt
import numpy as np

# Define the data: weeks taken by students in each academy to master spells
fireball = [15, 18, 21, 23, 19, 22, 25, 20, 24, 18, 21, 23, 19, 26, 22]
invisibility = [28, 32, 35, 31, 30, 33, 29, 34, 32, 30, 31, 36, 35, 33, 28]
healing = [10, 12, 15, 13, 11, 14, 12, 15, 13, 10, 12, 14, 11, 16, 15]

# New Data: average weekly practice hours
practice_hours = {
    'Fireball': [5, 6, 4, 6, 7, 5, 6, 5, 6, 5, 4, 7, 6, 5, 5],
    'Invisibility': [6, 7, 5, 6, 7, 6, 8, 6, 7, 6, 5, 7, 8, 6, 6],
    'Healing': [4, 5, 3, 4, 5, 4, 5, 3, 4, 4, 5, 5, 3, 6, 4]
}

# Bundle the data
boxplot_data = [fireball, invisibility, healing]

# Define spell names
spell_names = ['Fireball', 'Invisibility', 'Healing']

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# Box Plot
ax1 = axs[0]
boxprops = dict(facecolor='skyblue', color='navy', linewidth=1.5)
medianprops = dict(color='darkblue', linewidth=2)
whiskerprops = dict(color='navy', linewidth=1.5)
capprops = dict(color='navy', linewidth=1.5)
flierprops = dict(markerfacecolor='red', marker='o', markersize=7, linestyle='none')

bp = ax1.boxplot(boxplot_data, vert=False, patch_artist=True, notch=True,
                 boxprops=boxprops, medianprops=medianprops,
                 whiskerprops=whiskerprops, capprops=capprops, flierprops=flierprops)

colors = ['#6baed6', '#fc9272', '#74c476']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

ax1.set_yticklabels(spell_names, fontsize=12)
ax1.set_xlabel('Duration (Weeks)', fontsize=12)
ax1.set_title('Spell Mastery Duration\nA Comparative Study', fontsize=14, fontweight='bold', loc='left')
ax1.xaxis.grid(True, linestyle='--', alpha=0.7)

# Legend
handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
labels = ['Fireball Mastery', 'Invisibility Mastery', 'Healing Mastery']
ax1.legend(handles, labels, loc='upper right', edgecolor='black', fontsize=10, title='Spell Categories')

# Violin Plot for practice hours
ax2 = axs[1]
practice_data = [practice_hours['Fireball'], practice_hours['Invisibility'], practice_hours['Healing']]

vp = ax2.violinplot(practice_data, showmeans=False, showmedians=True)

for i, pc in enumerate(vp['bodies']):
    pc.set_facecolor(colors[i])
    pc.set_edgecolor('black')
    pc.set_alpha(0.7)

# Customize the violin plot appearance
vp['cmedians'].set_color('black')
vp['cmedians'].set_linewidth(2)

ax2.set_xticks(np.arange(1, len(spell_names) + 1))
ax2.set_xticklabels(spell_names, fontsize=12)
ax2.set_ylabel('Practice Hours per Week', fontsize=12)
ax2.set_title('Weekly Practice Hours Distribution\nfor Spell Mastery', fontsize=14, fontweight='bold', loc='left')

plt.tight_layout()
plt.show()