import matplotlib.pyplot as plt
import numpy as np

# Original listening hours data
beethoven_data = [55, 60, 58, 57, 61, 59, 65, 68, 60, 62, 65, 63, 70, 72, 66, 65, 68, 70, 75, 76]
mozart_data = [50, 52, 54, 55, 56, 58, 60, 65, 60, 63, 64, 68, 66, 70, 71, 69, 72, 74, 76, 78]
bach_data = [40, 43, 50, 45, 48, 46, 49, 55, 53, 56, 58, 62, 64, 67, 70, 72, 74, 73, 76, 78]
tchaikovsky_data = [45, 47, 46, 50, 54, 49, 53, 55, 58, 56, 60, 62, 65, 63, 67, 69, 70, 72, 71, 74]
brahms_data = [30, 35, 37, 38, 40, 45, 48, 50, 55, 60, 62, 65, 67, 70, 71, 73, 75, 77, 80, 82]

# Modified data for the violin plot
beethoven_mod_data = np.array(beethoven_data) * 1.1
mozart_mod_data = np.array(mozart_data) * 0.9
bach_mod_data = np.array(bach_data) * 1.05
tchaikovsky_mod_data = np.array(tchaikovsky_data) * 1.15
brahms_mod_data = np.array(brahms_data) * 0.95

# Subplot arrangement
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 8))

# Boxplot on the first subplot
boxplot_data = [beethoven_data, mozart_data, bach_data, tchaikovsky_data, brahms_data]
colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightsalmon', 'lightpink']

bplot = axes[0].boxplot(boxplot_data, vert=False, patch_artist=True, notch=True,
                        boxprops=dict(facecolor='w', color='black', linewidth=1.5),
                        whiskerprops=dict(color='black', linewidth=1.5),
                        capprops=dict(color='black', linewidth=1.5),
                        flierprops=dict(marker='o', color='red', alpha=0.5),
                        medianprops=dict(color='darkorange', linewidth=2))

for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

axes[0].set_title('Classical Listening\nBoxplot Analysis (1920-2020)', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Listening Hours per Year', fontsize=12)
axes[0].set_yticks(range(1, len(boxplot_data) + 1))
axes[0].set_yticklabels(["Beethoven", "Mozart", "Bach", "Tchaikovsky", "Brahms"], fontsize=12)
axes[0].grid(axis='x', linestyle='--', alpha=0.7)

# Violin plot on the second subplot
violinplot_data = [beethoven_mod_data, mozart_mod_data, bach_mod_data, tchaikovsky_mod_data, brahms_mod_data]

vplot = axes[1].violinplot(violinplot_data, vert=False, showmeans=False, showextrema=True, showmedians=True)
for i, pc in enumerate(vplot['bodies']):
    pc.set_facecolor(colors[i])
    pc.set_alpha(0.7)

axes[1].set_title('Classical Listening\nViolin Plot Variation', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Listening Hours per Year (Adjusted)', fontsize=12)
axes[1].set_yticks(range(1, len(violinplot_data) + 1))
axes[1].set_yticklabels(["Beethoven", "Mozart", "Bach", "Tchaikovsky", "Brahms"], fontsize=12)
axes[1].grid(axis='x', linestyle='--', alpha=0.7)

# Main title for both plots
plt.suptitle('Century of Classical Listening:\nComparative Analysis of Composer Popularity', fontsize=16, fontweight='bold', y=1.05)

# Adjust layout
plt.tight_layout()
plt.show()