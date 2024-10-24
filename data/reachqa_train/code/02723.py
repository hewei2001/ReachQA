import matplotlib.pyplot as plt
import numpy as np

# Defining the study hours data for each discipline
engineering_hours = [20, 22, 19, 24, 18, 21, 23, 20, 22, 19, 24, 18, 21, 20, 23, 25, 19, 22, 24, 21]
arts_hours = [15, 17, 14, 16, 18, 13, 17, 16, 15, 14, 16, 19, 15, 17, 18, 14, 16, 17, 13, 19]
sciences_hours = [25, 27, 26, 23, 28, 24, 25, 27, 26, 23, 24, 28, 24, 25, 27, 26, 28, 23, 24, 25]
business_hours = [18, 20, 19, 21, 22, 17, 20, 21, 19, 22, 18, 20, 21, 23, 17, 19, 22, 21, 20, 18]
humanities_hours = [16, 18, 17, 15, 19, 14, 18, 17, 15, 16, 19, 18, 14, 15, 17, 16, 19, 18, 14, 15]

# Additional data for mean and standard deviation for a line plot
disciplines = ['Engineering', 'Arts', 'Sciences', 'Business', 'Humanities']
mean_hours = [np.mean(engineering_hours), np.mean(arts_hours), np.mean(sciences_hours), np.mean(business_hours), np.mean(humanities_hours)]
std_hours = [np.std(engineering_hours), np.std(arts_hours), np.std(sciences_hours), np.std(business_hours), np.std(humanities_hours)]

# Setting up the plot with 1x2 layout
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Box plot in the first subplot
box = ax1.boxplot([engineering_hours, arts_hours, sciences_hours, business_hours, humanities_hours],
                  patch_artist=True, labels=disciplines, notch=True, vert=True)

colors = ['#E63946', '#F1A208', '#4A4E69', '#9A8C98', '#C9ADA7']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

for whisker, cap, median in zip(box['whiskers'], box['caps'], box['medians']):
    whisker.set(color='gray', linewidth=1.5, linestyle='--')
    cap.set(color='gray', linewidth=1.5)
    median.set(color='black', linewidth=2)

ax1.set_xlabel('Disciplines', fontsize=12)
ax1.set_ylabel('Study Hours per Week', fontsize=12)
ax1.set_title('Study Hour Distribution Across Disciplines:\nA Box Plot Analysis', fontsize=14, fontweight='bold', pad=20)
ax1.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Line plot in the second subplot
ax2.errorbar(disciplines, mean_hours, yerr=std_hours, fmt='o-', color='blue', ecolor='red', capsize=5, linewidth=2, label='Mean ± Std Dev')

ax2.set_xlabel('Disciplines', fontsize=12)
ax2.set_ylabel('Average Study Hours per Week', fontsize=12)
ax2.set_title('Average Study Hours with Standard Deviation', fontsize=14, fontweight='bold', pad=20)
ax2.legend(loc='upper left')
ax2.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()